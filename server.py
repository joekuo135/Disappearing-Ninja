from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjaFamily():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def ninjaColor(color):
    return render_template('ninjaColor.html', color=color)

app.run(debug=True)