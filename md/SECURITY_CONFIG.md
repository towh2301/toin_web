# Production Security Configuration

This document explains the deployment security configuration for Render.

## ✅ What's Configured

Your `toin/settings.py` is ready for production with proper security settings:

```python
# Enabled in settings.py:
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
SECURE_SSL_REDIRECT = not DEBUG  # Set to True when DEBUG=False
```

## ⚠️ Pre-Deployment Warnings (Expected)

Running `python manage.py check --deploy` shows these warnings locally:

1. **SECURE_SSL_REDIRECT not True** → ✅ Fixed by setting `DEBUG=False` in Render
2. **SECRET_KEY unsafe** → ✅ Set secure `SECRET_KEY` in Render environment
3. **SESSION_COOKIE_SECURE not set** → ✅ Add `SESSION_COOKIE_SECURE=True` in Render (optional)
4. **CSRF_COOKIE_SECURE not set** → ✅ Add `CSRF_COOKIE_SECURE=True` in Render (optional)
5. **DEBUG=True in deployment** → ✅ Set `DEBUG=False` in Render

**These are NOT errors - just warnings that go away in production!**

## 🚀 Render Environment Variables for Security

Add these to your Render dashboard:

### Required for Production Safety

```
DEBUG=False
SECRET_KEY=<use-output-of-command-below>
```

**To generate a secure SECRET_KEY:**

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Optional but Recommended

```
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## 📋 Complete Render Environment Setup

See **DEPLOYMENT_CHECKLIST.md** for the full list of required environment variables.

Key sections:

-   Core Django (DEBUG, SECRET_KEY, ALLOWED_HOSTS)
-   Database (DATABASE_URL)
-   Email (EMAIL\_\* variables)
-   Security (SSL, CSRF, HSTS)

## 🔒 Security Checklist

Before deploying to Render:

-   [ ] `DEBUG=False` in production environment
-   [ ] `SECRET_KEY` is long, random, and different from development
-   [ ] `ALLOWED_HOSTS` includes your Render domain
-   [ ] `SECURE_PROXY_SSL_HEADER` configured (done in settings.py)
-   [ ] `CSRF_TRUSTED_ORIGINS` includes your domain
-   [ ] Database credentials not exposed in code
-   [ ] Email credentials in environment variables, not in code
-   [ ] `.env` file in `.gitignore` (never commit secrets)

## 🌐 HTTPS/SSL on Render

**Render automatically provides:**

-   ✅ Free SSL certificates
-   ✅ HTTPS by default on your domain
-   ✅ Automatic HTTP → HTTPS redirect

**Your code handles:**

-   ✅ `SECURE_SSL_REDIRECT` (when DEBUG=False)
-   ✅ `SECURE_PROXY_SSL_HEADER` (trusts Render's proxy)
-   ✅ `X_FRAME_OPTIONS = "DENY"` (prevents clickjacking)

## 🚨 Common Issues

### "CSRF verification failed" on Render?

**Solution:** Ensure `CSRF_TRUSTED_ORIGINS` includes your Render domain:

```
CSRF_TRUSTED_ORIGINS=https://toin-vn.onrender.com,https://toin-vn.com
```

### "Mixed Content" warning?

**Solution:** This happens if assets are served over HTTP. Render automatic redirects should handle this, but ensure:

-   `DEBUG=False`
-   `SECURE_SSL_REDIRECT=True` (automatic when DEBUG=False)
-   Static files collected: `python manage.py collectstatic --noinput`

### SSL certificate not found?

**Solution:** Render takes 5-15 minutes to issue SSL. Check:

1. Your domain is in `ALLOWED_HOSTS`
2. Wait 15 minutes for SSL to provision
3. Check Render dashboard for SSL status

## 📚 References

-   [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
-   [Render Django Security](https://render.com/docs/deploy-django)
-   [OWASP Security Headers](https://owasp.org/www-project-secure-headers/)

## ✨ Pro Tips

1. **Never use default Django secret key** → Generate a new one with command above
2. **Use Render environment variables** → Not .env files in production
3. **Enable HTTP → HTTPS redirect** → `DEBUG=False` enables it automatically
4. **Regular updates** → Keep Django and dependencies up to date
5. **Monitor logs** → Check Render logs regularly for security warnings

---

**Status**: ✅ Security configuration ready for Render deployment!

Proceed with DEPLOYMENT_CHECKLIST.md when ready to deploy.
