import ntplib
from web import create_app


if __name__ == '__main__':
    app = create_app(debug=False)
    app.run(host='0.0.0.0', port=5001)
