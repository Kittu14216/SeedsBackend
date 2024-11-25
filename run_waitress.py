from waitress import serve
from chilliblossombackend.wsgi import application  # Update with your project name

if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=8000)
