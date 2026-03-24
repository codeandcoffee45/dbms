from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mechanics')
def mechanics():
    return render_template('mechanics.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/payments')
def payments():
    return render_template('payments.html')

if __name__ == '__main__':
    app.run(debug=True)