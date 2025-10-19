import os, ssl, certifi, requests
from urllib.parse import urljoin

BASE = "https://jhu.instructure.com"  # make sure yours matches
URL = urljoin(BASE, "/api/v1/courses")

print("Python:", ssl.OPENSSL_VERSION)
print("certifi.where():", certifi.where())
print("REQUESTS_CA_BUNDLE:", os.environ.get("REQUESTS_CA_BUNDLE"))
print("SSL_CERT_FILE:", os.environ.get("SSL_CERT_FILE"))
print("HTTP(S)_PROXY:", os.environ.get("HTTP_PROXY"), os.environ.get("HTTPS_PROXY"))
print("NO_PROXY:", os.environ.get("NO_PROXY"))

# 1a) Probe bare host (what you said succeeds)
r0 = requests.get(BASE, timeout=10)
print("BASE status:", r0.status_code, "via", r0.request.url)

# 1b) Probe API endpoint (no auth) – should 401/403 but NOT SSL fail
try:
    r1 = requests.get(URL, timeout=10)
    print("API (no auth) status:", r1.status_code)
except Exception as e:
    print("API (no auth) error:", repr(e))

# 1c) Same call but force system CA bundle (if you use enterprise CA)
verify_path = os.environ.get("REQUESTS_CA_BUNDLE") or os.environ.get("SSL_CERT_FILE") or certifi.where()
try:
    r2 = requests.get(URL, timeout=10, verify=verify_path)
    print("API with verify_path status:", r2.status_code, "verify_path:", verify_path)
except Exception as e:
    print("API with verify_path error:", repr(e))

# 1d) Same call but without inheriting env proxies (to detect proxy difference)
with requests.Session() as s:
    s.trust_env = False
    try:
        r3 = s.get(URL, timeout=10, verify=verify_path)
        print("API (trust_env=False) status:", r3.status_code)
    except Exception as e:
        print("API (trust_env=False) error:", repr(e))
