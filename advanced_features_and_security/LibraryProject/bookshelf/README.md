Disabled DEBUG in production.
Added CSRF tokens in forms.
Avoided raw SQL to prevent SQL injection.
Enabled browser protections with settings.
Added CSP middleware to block risky scripts.


## Security Configuration Summary

-  HTTPS Enforced with `SECURE_SSL_REDIRECT = True`
-  HSTS (Strict Transport Security) enabled for 1 year with preload and subdomains
-  Cookies secured with `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`
-  Clickjacking prevented using `X_FRAME_OPTIONS = "DENY"`
-  Browser XSS filter and content sniffing protections enabled
-  SSL configured via Let's Encrypt and Nginx reverse proxy