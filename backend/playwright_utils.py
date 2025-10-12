from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_PROFILE_DIR = Path("edge-profile")
DEFAULT_STATE_FILE = Path("playwright-state.json")


@dataclass
class PlaywrightConfig:
    channel: str | None
    user_data_dir: Path
    headless: bool
    storage_state_path: Path
    storage_state_exists: bool
    browser_args: list[str]


@dataclass
class ManagedContext:
    context: Any

    def __getattr__(self, item: str) -> Any:
        return getattr(self.context, item)

    def close(self) -> None:
        self.context.close()


def load_config() -> PlaywrightConfig:
    raw_channel = os.getenv("PLAYWRIGHT_BROWSER_CHANNEL", "chromium").strip()
    channel = raw_channel or None
    user_data_dir = Path(
        os.getenv("PLAYWRIGHT_USER_DATA_DIR", DEFAULT_PROFILE_DIR.as_posix())
    ).expanduser().resolve()
    headless = os.getenv("PLAYWRIGHT_HEADLESS", "true").lower() in {"1", "true", "yes"}
    storage_state_env = os.getenv("PLAYWRIGHT_STORAGE_STATE")
    storage_state_path = (
        Path(storage_state_env).expanduser()
        if storage_state_env
        else DEFAULT_STATE_FILE
    ).resolve()
    storage_state_exists = storage_state_path.exists()

    browser_args = ["--no-sandbox"]
    extra_args = [
        arg.strip()
        for arg in os.getenv("PLAYWRIGHT_EXTRA_ARGS", "").split(",")
        if arg.strip()
    ]
    browser_args.extend(extra_args)

    return PlaywrightConfig(
        channel=channel,
        user_data_dir=user_data_dir,
        headless=headless,
        storage_state_path=storage_state_path,
        storage_state_exists=storage_state_exists,
        browser_args=browser_args,
    )


def launch_context(
    pw,
    *,
    headless_override: bool | None = None,
    use_storage_state: bool | None = None,
) -> ManagedContext:
    config = load_config()
    headless = config.headless if headless_override is None else headless_override
    should_use_state = config.storage_state_exists
    if use_storage_state is not None:
        should_use_state = use_storage_state and config.storage_state_exists

    profile_dir = config.user_data_dir
    profile_dir.mkdir(parents=True, exist_ok=True)

    browser_args = list(config.browser_args)
    if headless and "--disable-gpu" not in browser_args:
        browser_args.append("--disable-gpu")

    kwargs = {
        "user_data_dir": str(profile_dir),
        "headless": headless,
        "args": browser_args,
    }
    if config.channel and config.channel.lower() != "chromium":
        kwargs["channel"] = config.channel

    try:
        context = pw.chromium.launch_persistent_context(**kwargs)
    except Exception:
        if "channel" in kwargs:
            kwargs.pop("channel")
            context = pw.chromium.launch_persistent_context(**kwargs)
        else:
            raise

    if should_use_state:
        try:
            state_data = json.loads(config.storage_state_path.read_text(encoding="utf-8"))
            cookies = state_data.get("cookies") or []
            if cookies:
                context.add_cookies(cookies)
        except FileNotFoundError:
            pass
        except Exception:
            pass

    return ManagedContext(context=context)
