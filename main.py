from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about-us")
def about():
    return render_template('about-us.html')

@app.route("/events")
def events():
    return render_template('events.html')

if __name__ == '__main__':
    app.run(debug=True)
