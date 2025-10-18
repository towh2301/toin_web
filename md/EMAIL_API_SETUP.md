# Email via HTTP API (No SMTP)

Render chặn SMTP nên dự án dùng HTTP API qua django-anymail. Hỗ trợ SendGrid hoặc Resend. Bạn có thể test local bằng .env và lệnh quản trị.

1. Cài dependency

-   Đã khai báo trong requirements.txt: `django-anymail[requests]==11.2`

2. Biến môi trường (.env)
   Tạo hoặc cập nhật file `.env` ở thư mục gốc:

```
# Bắt buộc
DEFAULT_FROM_EMAIL=noreply@your-domain.com

# Chọn 1 trong 2 provider
# --- SendGrid ---
EMAIL_PROVIDER=sendgrid
SENDGRID_API_KEY=SG.xxxxxx

# --- Resend ---
# EMAIL_PROVIDER=resend
# RESEND_API_KEY=re_xxxxxx

# Tùy chọn debug
ANYMAIL_DEBUG=true

# Dùng cho lệnh test
TEST_EMAIL_TO=you@example.com
```

Lưu ý: Với SendGrid/Resend, bạn nên cấu hình domain gửi (SPF/DKIM) theo hướng dẫn của provider để email không vào spam.

3. Cấu hình trong settings
   `toin/settings.py` đã tự động:

-   Chọn backend theo `EMAIL_PROVIDER` (sendgrid/resend)
-   Mặc định dùng console backend khi chạy DEBUG mà không set provider
-   Vẫn giữ fallback SMTP (không khuyến nghị trên Render)

4. Test local
   Chạy lệnh sau để gửi thử email:

```
python manage.py send_test_email --html
```

Hoặc chỉ định địa chỉ nhận:

```
python manage.py send_test_email --to someone@example.com
```

Nếu bạn chưa cài thư viện, cài requirements trước:

```
pip install -r requirements.txt
```

5. Cấu hình trên Render

-   Thêm các Environment Variables tương tự .env vào Render Dashboard → Service → Settings → Environment
-   Không cần mở cổng SMTP; outbound HTTPS là đủ
-   Deploy lại service

6. Tích hợp vào luồng gửi hiện có
   Mã hiện tại dùng `django.core.mail.EmailMessage` và `send_mail`. Khi AnyMail được cấu hình, hai API này sẽ tự động gửi qua HTTP (SendGrid/Resend) mà không cần đổi code.

7. Khắc phục sự cố

-   Kiểm tra log Render và bật `ANYMAIL_DEBUG=true`
-   Xác minh `DEFAULT_FROM_EMAIL` khớp domain đã xác minh
-   Kiểm tra quota/tài khoản của provider
-   Nếu vẫn lỗi, đổi provider khác (Resend thường đơn giản khi khởi đầu)
