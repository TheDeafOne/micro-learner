from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir="/home/woodbkb2/git/micro-learner/backend/edge-profile",
        headless=False,   # keep headed while debugging
        args=[
            "--profile-directory=Default",  # <-- key part
            "--no-sandbox",
            "--disable-gpu"
        ],
    )
    page = ctx.new_page()
    page.goto("https://jh.hosted.panopto.com/", wait_until='domcontentloaded')
    input("Press Enter to close...")
    ctx.close()
