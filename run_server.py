from waitress import serve
from toin.wsgi import application
from whitenoise import WhiteNoise

application = WhiteNoise(application, root="staticfiles/")
application.add_files("media/", prefix="media/")

if __name__ == "__main__":
    serve(application, host="0.0.0.0", port=8000)
