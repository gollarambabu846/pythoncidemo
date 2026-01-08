# app.py
def add(a, b):
    return a + b

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    result = add(2, 3)
    return f"Hello, Jenkins CI! Addition: {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
