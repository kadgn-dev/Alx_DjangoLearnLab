# --------------------------------------------------
# SECURITY SETTINGS (ALX REQUIREMENT)
# --------------------------------------------------

# Browser protections
SECURE_BROWSER_XSS_FILTER = True               # XSS filter
SECURE_CONTENT_TYPE_NOSNIFF = True            # Prevent MIME sniffing

# Clickjacking
X_FRAME_OPTIONS = "DENY"

# Secure cookies
CSRF_COOKIE_SECURE = True                     # CSRF cookie over HTTPS only
SESSION_COOKIE_SECURE = True                  # Session cookie over HTTPS only
CSRF_COOKIE_HTTPONLY = True                   # JS cannot access CSRF cookie

# HSTS: Tell browsers to always use HTTPS
SECURE_HSTS_SECONDS = 31536000                # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Redirect all HTTP to HTTPS
SECURE_SSL_REDIRECT = True                    # Only works when HTTPS is active

# Required when Django sits behind a reverse proxy / load balancer
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
