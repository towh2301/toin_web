# Error Page Protection & Configuration

## Overview

Your Django application now has branded error pages with custom 404 and 500 error handlers. These pages maintain the site's branding by including the header and footer.

## What Was Configured

### 1. **Error Templates Created**

#### `templates/404.html`

-   **Purpose**: Handles all "Page Not Found" (404) errors
-   **Features**:
    -   Includes site header with navigation and logo
    -   Includes site footer
    -   Styled error message with icon
    -   "Go Home" and "Go Back" action buttons
    -   Multilingual support (EN/VI/JP)
    -   Responsive design matching site branding
    -   Gradient background (purple/blue tones)

#### `templates/500.html`

-   **Purpose**: Handles all "Server Error" (500) errors
-   **Features**:
    -   Includes site header and footer
    -   Professional error message
    -   Action buttons for navigation
    -   Multilingual support
    -   Responsive design
    -   Distinct gradient background (pink/red tones) to differentiate from 404

### 2. **Error Handler Views**

Added two new views in `pages/views.py`:

```python
def page_not_found(request, exception=None):
    """Handle 404 Page Not Found errors."""
    return render(request, "404.html", status=404)

def server_error(request):
    """Handle 500 Server Error."""
    return render(request, "500.html", status=500)
```

### 3. **Settings Configuration**

Added handlers to `toin/settings.py`:

```python
# Error Page Handlers
handler404 = "pages.views.page_not_found"  # 404 - Page not found
handler500 = "pages.views.server_error"    # 500 - Server error
```

## How It Works

### 404 Error (Page Not Found)

-   **Trigger**: User visits a non-existent URL (e.g., `/en/nonexistent-page/`)
-   **Response**: Custom 404 page with:
    -   Site header with logo and navigation
    -   "404" error code
    -   Error message in user's language
    -   Buttons to go home or back
    -   Site footer
    -   HTTP status: 404

### 500 Error (Server Error)

-   **Trigger**: Unhandled exception during request processing
-   **Response**: Custom 500 page with:
    -   Site header and footer
    -   "500" error code
    -   Apology message
    -   Navigation options
    -   HTTP status: 500

## Testing Error Pages

### Test 404 Error (Locally)

1. **Start development server**:

    ```bash
    python manage.py runserver
    ```

2. **Visit non-existent URL**:

    - Navigate to: `http://127.0.0.1:8000/en/this-does-not-exist/`
    - You should see the custom 404 page

3. **Test multilingual support**:

    - Try different language prefixes: `/vi/fake-page/`, `/jp/fake-page/`

4. **Test buttons**:
    - Click "Go Home" → Should navigate to home page
    - Click "Go Back" → Should use browser back button

### Test 500 Error (Manual Testing in Production)

For safety, 500 errors are only shown when:

-   **Production (`DEBUG=False`)**: Custom 500 page is rendered
-   **Development (`DEBUG=True`)**: Django debug page is shown instead

To test locally:

1. Temporarily set `DEBUG=False` in `.env`
2. Intentionally raise an exception in a view
3. Access that view to trigger 500 page
4. Restore `DEBUG=True`

## Important Settings

### For Local Development (`DEBUG=True`)

**Django Debug Page is shown instead of custom 500 page**

-   This is intentional - you get detailed error info for debugging
-   Custom 500 template is only used in production

### For Production (`DEBUG=False`)

**Custom error pages are displayed**

-   404 errors show branded page
-   500 errors show branded page
-   Detailed errors are logged, not shown to user (security best practice)

## Security Considerations

✅ **Error messages don't leak sensitive info**

-   No internal server details in 404 page
-   No exception traces in 500 page

✅ **Custom pages maintain consistency**

-   Same header/footer as rest of site
-   Users won't see generic Django error pages

✅ **Proper HTTP status codes**

-   404 errors return HTTP 404 status
-   500 errors return HTTP 500 status

✅ **Multilingual support**

-   Error pages respect site language setting
-   Messages translated for EN/VI/JP

## Customization

### To Customize Error Pages

1. **Edit `templates/404.html`** for 404 errors
2. **Edit `templates/500.html`** for 500 errors

### To Change Button Actions

In error templates, modify the button links:

```html
<a href="{% url 'pages:index' %}" class="btn-home"> Go to Home </a>
```

### To Change Gradient Colors

Edit the style section in templates:

```css
.error-page {
	background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

## URL Routing Protection

While Django handles 404s automatically, you can also:

### Protect Specific Routes

Create a view to handle invalid routes:

```python
def invalid_view(request):
    raise Http404("This resource does not exist")
```

### Redirect Old URLs

Add redirects in `pages/urls.py`:

```python
from django.views.generic import RedirectView

urlpatterns = [
    path("old-path/", RedirectView.as_view(url="pages:index", permanent=True)),
]
```

### Validate URL Parameters

In views, validate ID parameters:

```python
def blog_detail(request, post_id):
    post = Post.objects.filter(id=post_id, is_published=True).first()
    if not post:
        raise Http404("Post not found")
    return render(request, "pages/blog_detail.html", {"post": post})
```

## Example Scenarios

### Scenario 1: User Typos URL

1. User types: `http://domain.com/en/blomg/`
2. Django can't find matching URL pattern
3. 404 handler is called
4. Custom 404 page displays
5. User sees professional error page with navigation options

### Scenario 2: Database Query Error

1. View tries to access database
2. Unexpected error occurs
3. 500 handler is called
4. Custom 500 page displays
5. Error is logged (not shown to user in production)
6. User sees helpful message with home/back options

### Scenario 3: Deleted Resource

1. URL was valid but resource was deleted
2. View returns Http404 explicitly
3. 404 page displays
4. User can navigate home

## Files Modified/Created

**Created:**

-   ✅ `templates/404.html` - Custom 404 error page template
-   ✅ `templates/500.html` - Custom 500 error page template

**Modified:**

-   ✅ `toin/settings.py` - Added handler404 and handler500
-   ✅ `pages/views.py` - Added page_not_found() and server_error() views

## Next Steps

1. **Test locally** - Visit non-existent URL to see 404 page
2. **Verify on production** - After deploying to Render, test error pages
3. **Monitor errors** - Check server logs for actual errors
4. **Customize as needed** - Adjust colors, text, or layout to match branding

## References

-   [Django Error Views](https://docs.djangoproject.com/en/5.2/ref/urls/#django.views.defaults.page_not_found)
-   [Django Exception Handling](https://docs.djangoproject.com/en/5.2/topics/http/exceptions/)
-   [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

**Status**: ✅ Route protection with branded error pages configured and ready for deployment!
