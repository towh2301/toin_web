# Render Deployment Guide

This guide covers deploying the TOIN Django application to [Render.com](https://render.com).

## Quick Start

1. **Connect your GitHub repository** to Render
2. **Create a new Web Service** on Render
3. **Set the build and start commands** (see below)
4. **Add environment variables** (see Configuration section)
5. **Deploy!**

---

## Environment Variables

Configure these in your Render dashboard under **Environment** (or in a `.env` file for local testing):

### Core Django Settings

```
DEBUG=False
SECRET_KEY=your-secret-key-here-change-in-production
ALLOWED_HOSTS=yourdomain.com,yourdomain.onrender.com
```

### Database

```
DATABASE_URL=postgresql://user:password@host:port/database
```

> **Note:** Render provides PostgreSQL automatically. Copy the `DATABASE_URL` from your PostgreSQL instance.

### Email Configuration

Choose **one** of the following email backends:

#### Option 1: Gmail SMTP (Recommended for Small Projects)

```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=true
EMAIL_USE_SSL=false
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

**Setup Instructions:**

1. Enable 2-factor authentication on your Gmail account
2. Generate an [App Password](https://myaccount.google.com/apppasswords)
3. Use the app password in `EMAIL_HOST_PASSWORD` (not your regular Gmail password)

#### Option 2: SendGrid (Recommended for Production)

```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=true
EMAIL_USE_SSL=false
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
```

**Setup Instructions:**

1. Sign up for [SendGrid](https://sendgrid.com)
2. Create an API key in Settings → API Keys
3. Set `EMAIL_HOST_USER` to `apikey` (literal string)
4. Set `EMAIL_HOST_PASSWORD` to your API key

#### Option 3: Other SMTP Providers

For services like Mailgun, AWS SES, or Postmark, use their SMTP settings:

```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.your-provider.com
EMAIL_PORT=587  # or 465 for SSL
EMAIL_USE_TLS=true  # or false if using SSL
EMAIL_USE_SSL=false  # or true if using SSL
EMAIL_HOST_USER=your-smtp-username
EMAIL_HOST_PASSWORD=your-smtp-password
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
```

### Static Files & Security

```
SECURE_SSL_REDIRECT=True
SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTO,https
USE_X_FORWARDED_HOST=True
CSRF_TRUSTED_ORIGINS=https://yourdomain.onrender.com,https://yourdomain.com
```

### Optional: Force SMTP in Development

To test SMTP even when `DEBUG=True`:

```
FORCE_SMTP=true
```

---

## Build & Start Commands

In your Render dashboard, set:

**Build Command:**

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

**Start Command:**

```bash
gunicorn toin.wsgi:application
```

> The build command will:
>
> 1. Install Python dependencies
> 2. Collect static files for WhiteNoise
> 3. Run all pending database migrations

---

## How Email Works in This App

### Development Mode (`DEBUG=True`)

-   **Without SMTP credentials**: Uses Django console backend (prints to console)
-   **With SMTP credentials + `FORCE_SMTP=true`**: Uses configured SMTP (for testing)

### Production Mode (`DEBUG=False`)

-   **Always uses SMTP** (configured by environment variables)
-   **Falls back to console** if credentials are missing (prints warning)
-   **Handles failures gracefully** (won't crash your app if email fails)

### Email Endpoints

The app sends emails from two places:

1. **Keep in Touch Form** (`/en/keep-in-touch/`)

    - Sends to: `DEFAULT_FROM_EMAIL`
    - Confirmation to: User's email address
    - Async sending (doesn't block requests)

2. **Contact/HR Messages** (Admin actions, CV submissions)
    - Sends to: Recipients specified in views
    - Uses: `DEFAULT_FROM_EMAIL` as sender

---

## Troubleshooting

### "Missing email credentials" Warning

**Error in logs:**

```
⚠️ WARNING: Missing email credentials — using console backend instead.
```

**Solution:** Add email environment variables (see Email Configuration section above).

### "Failed to send email" in Production

**Possible causes:**

-   Invalid SMTP credentials
-   Firewall blocking port 587 or 465
-   Sender email doesn't match SMTP account

**Debug steps:**

1. Verify credentials in Render dashboard
2. Test with Gmail's app password (easiest to start)
3. Check Render logs: `render.com/services/your-service/logs`

### Email Not Sending Asynchronously

**Note:** The app uses threading for async email, which works fine on Render but may not work well across server restarts. For production, consider using:

-   Celery + Redis (more complex setup)
-   Huey (simpler alternative to Celery)
-   Render background workers

For now, threading is sufficient for most use cases.

---

## Complete Environment Variables Example

```
DEBUG=False
SECRET_KEY=django-insecure-change-me-in-production
ALLOWED_HOSTS=toin-vn.onrender.com,toin-vn.com
DATABASE_URL=postgresql://user:password@host:port/database

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=true
EMAIL_USE_SSL=false
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com

SECURE_SSL_REDIRECT=True
SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTO,https
USE_X_FORWARDED_HOST=True
CSRF_TRUSTED_ORIGINS=https://toin-vn.onrender.com,https://toin-vn.com
```

---

## Deployment Steps

1. **Push to GitHub**

    ```bash
    git add .
    git commit -m "Prepare for Render deployment"
    git push origin main
    ```

2. **Create Web Service on Render**

    - Dashboard → New → Web Service
    - Select your GitHub repo
    - Name: `toin-vn`
    - Runtime: `Python 3`
    - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
    - Start Command: `gunicorn toin.wsgi:application`

3. **Add Environment Variables**

    - Go to Environment section
    - Add all variables from "Complete Environment Variables Example" above

4. **Deploy**

    - Click "Create Web Service"
    - Render will automatically deploy when pushed to `main`

5. **Verify**
    - Check Render logs for errors
    - Visit your deployed URL: `https://toin-vn.onrender.com`
    - Test email sending: Fill out "Keep in touch" form

---

## Additional Resources

-   [Render Django Documentation](https://render.com/docs/deploy-django)
-   [Gmail App Passwords](https://support.google.com/accounts/answer/185833)
-   [SendGrid SMTP Setup](https://docs.sendgrid.com/ui/account-and-settings/smtp)
-   [Django Email Documentation](https://docs.djangoproject.com/en/5.2/topics/email/)

---

## Notes

-   **Render free tier** has limitations (spins down after 15 minutes of inactivity)
-   **PostgreSQL** is included with Render Web Services (SQLite won't work in production)
-   **Static files** are automatically served by WhiteNoise
-   **Media files** should be stored in Render Disk or external storage (S3, etc.)

For a production setup with persistent media storage, consider adding [Render Disk](https://render.com/docs/disks) or integrating with AWS S3.
