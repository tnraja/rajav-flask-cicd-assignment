from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to Flask CI/CD Demo!</h1>'

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
