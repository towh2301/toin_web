# Render Deployment Checklist

Use this checklist to ensure your application is ready for deployment to Render.

## Pre-Deployment

-   [ ] All code changes committed to GitHub
-   [ ] `requirements.txt` is up to date (run `pip freeze > requirements.txt` if needed)
-   [ ] Local testing completed (`python manage.py runserver`)
-   [ ] Django system checks pass (`python manage.py check`)
-   [ ] All migrations are created (`python manage.py makemigrations`)
-   [ ] All migrations are applied locally (`python manage.py migrate`)

## Render Configuration

### Web Service Setup

-   [ ] GitHub repository connected to Render
-   [ ] Web Service created (name: `toin-vn` or your preferred name)
-   [ ] Build Command set to:
    ```bash
    pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
    ```
-   [ ] Start Command set to:
    ```bash
    gunicorn toin.wsgi:application
    ```

### Environment Variables

**Core Django:**

-   [ ] `DEBUG=False`
-   [ ] `SECRET_KEY` set to a strong random key (use `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
-   [ ] `ALLOWED_HOSTS` includes your Render domain (e.g., `toin-vn.onrender.com`)

**Database:**

-   [ ] PostgreSQL instance created in Render
-   [ ] `DATABASE_URL` copied from PostgreSQL instance details

**Email Configuration:**

-   [ ] Email provider chosen (Gmail, SendGrid, etc.)
-   [ ] `EMAIL_HOST` set correctly
-   [ ] `EMAIL_PORT` set correctly (usually 587 for TLS, 465 for SSL)
-   [ ] `EMAIL_USE_TLS` and `EMAIL_USE_SSL` configured appropriately
-   [ ] `EMAIL_HOST_USER` set (e.g., your email or `apikey` for SendGrid)
-   [ ] `EMAIL_HOST_PASSWORD` set (Gmail app password or SendGrid API key)
-   [ ] `DEFAULT_FROM_EMAIL` set to sender email address

**Security (Production):**

-   [ ] `SECURE_SSL_REDIRECT=True`
-   [ ] `SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTO,https`
-   [ ] `USE_X_FORWARDED_HOST=True`
-   [ ] `CSRF_TRUSTED_ORIGINS` includes your domain (e.g., `https://toin-vn.onrender.com,https://toin-vn.com`)

## Email Provider Setup

### If Using Gmail

-   [ ] Gmail account has 2-factor authentication enabled
-   [ ] App Password generated (https://myaccount.google.com/apppasswords)
-   [ ] App Password used in `EMAIL_HOST_PASSWORD` (not regular Gmail password)

### If Using SendGrid

-   [ ] SendGrid account created (https://sendgrid.com)
-   [ ] API key generated in Settings → API Keys
-   [ ] `EMAIL_HOST_USER` set to `apikey` (literal string)
-   [ ] `EMAIL_HOST_PASSWORD` set to the API key

### If Using Other Provider (Mailgun, AWS SES, etc.)

-   [ ] SMTP credentials obtained from provider
-   [ ] All fields correctly filled in settings

## Deployment

-   [ ] Environment variables saved in Render dashboard
-   [ ] Ready to deploy? Click "Create Web Service" or push to `main` branch
-   [ ] Deployment logs checked for errors (View Logs in Render dashboard)
-   [ ] No "Missing email credentials" warnings in logs

## Post-Deployment Testing

-   [ ] Website loads successfully: `https://toin-vn.onrender.com`
-   [ ] No 500 errors in production
-   [ ] Render logs show no warnings or errors
-   [ ] Fill out "Keep in touch" contact form and verify email sent
-   [ ] Admin page accessible: `https://toin-vn.onrender.com/admin`
-   [ ] Blog page displays published posts only

## Troubleshooting

**If deployment fails:**

1. Check Render logs: Render Dashboard → Your Service → Logs
2. Verify all environment variables are set
3. Ensure `requirements.txt` includes all dependencies
4. Test locally first: `python manage.py collectstatic --noinput`

**If email isn't sending:**

1. Verify `DEBUG=False` in Render
2. Check email credentials in Render Environment
3. Test with console backend first (`DEBUG=True` temporarily)
4. Check Render logs for SMTP errors
5. Verify sender email matches configured account

**If database migrations fail:**

1. Ensure `DATABASE_URL` is correctly set
2. Check database is running in Render
3. Run migrations manually in Render shell (if supported)

## Additional Resources

-   [Render Django Deployment Guide](RENDER_DEPLOYMENT.md) (included in repo)
-   [Render Documentation](https://render.com/docs)
-   [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)

---

**Notes:**

-   Render automatically redeploys when you push to `main` branch
-   First deployment may take 5-10 minutes
-   Free tier spins down after 15 minutes of inactivity (wake up time: ~30 seconds)
-   PostgreSQL instance must be running for web service to work
