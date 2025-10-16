# 🚀 Render Deployment Guide - Quick Reference

Your Django application is **fully configured for Render deployment**. Here's the fastest path to production:

## 📖 Documentation Map

| Document                    | Purpose                                        | Read Time |
| --------------------------- | ---------------------------------------------- | --------- |
| **EMAIL_CONFIG_SUMMARY.md** | ⭐ Start here! Overview of email configuration | 3 min     |
| **DEPLOYMENT_CHECKLIST.md** | Step-by-step checklist for Render setup        | 5 min     |
| **RENDER_DEPLOYMENT.md**    | Complete guide with all options                | 10 min    |
| **SECURITY_CONFIG.md**      | Security setup explanation                     | 5 min     |
| **.env.example**            | Template for local development                 | 1 min     |

## ⚡ 5-Minute Deploy

### 1. Generate a Secure Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 2. Set Up Render Web Service

-   Go to [render.com](https://render.com)
-   Create Web Service from GitHub repo
-   Build: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
-   Start: `gunicorn toin.wsgi:application`

### 3. Add Minimal Environment Variables

```
DEBUG=False
SECRET_KEY=<paste-generated-key-above>
ALLOWED_HOSTS=your-domain.onrender.com
DATABASE_URL=<copy-from-PostgreSQL-instance>
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=true
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

> **Gmail users**: Get your App Password from https://myaccount.google.com/apppasswords

### 4. Deploy

-   Push to `main` branch
-   Render auto-deploys
-   Visit your domain
-   Test "Keep in touch" form

**Done!** ✅

---

## 📋 Complete Checklist Version

If you prefer step-by-step with all details, follow **DEPLOYMENT_CHECKLIST.md**

---

## 🆘 Quick Troubleshooting

**Email not working?**

-   Check email credentials in Render dashboard
-   For Gmail: Use App Password, not regular password
-   Check Render logs for errors

**Website won't load?**

-   Verify `DATABASE_URL` is set
-   Check build command output in Render logs
-   Ensure `DEBUG=False`

**500 errors?**

-   Check Render logs: `Render Dashboard → Your Service → Logs`
-   Usually missing environment variable

---

## 📚 Full Documentation

For comprehensive guides with all options, see:

-   **RENDER_DEPLOYMENT.md** - Email provider options, security, troubleshooting
-   **SECURITY_CONFIG.md** - SSL, CSRF, SECRET_KEY details
-   **EMAIL_CONFIG_SUMMARY.md** - Email configuration overview

---

## 🎯 What's Already Configured

✅ Email backend (console + SMTP)  
✅ Database (PostgreSQL support)  
✅ Static files (WhiteNoise)  
✅ Security headers (HSTS, XSS, etc.)  
✅ CSRF protection  
✅ Blog publishing system  
✅ Contact form with async email  
✅ Admin CV management

---

## 🔄 Development vs Production

### Local Development

```bash
cp .env.example .env
# Edit .env with test values
python manage.py runserver
# Emails print to console by default
```

### Production (Render)

```
Environment variables → Auto-configuration
SMTP credentials → Real emails sent
DEBUG=False → Full security enabled
```

---

## 💡 Next Steps

1. **Read** EMAIL_CONFIG_SUMMARY.md (3 min)
2. **Follow** DEPLOYMENT_CHECKLIST.md (step-by-step)
3. **Deploy** to Render (push to main)
4. **Test** contact form (fill out form on site)
5. **Verify** email received ✅

---

**Questions?** See RENDER_DEPLOYMENT.md or [Render Docs](https://render.com/docs/deploy-django)

**Status**: ✅ Ready to deploy!
