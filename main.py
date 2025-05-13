from flask import Flask, render_template, request

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

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    reason = request.form['reason']
    message = request.form['message']

    with open('feedback.txt', 'a') as f:
        f.write(f"Name: {name}\nEmail: {email}\nReason: {reason}\nMessage: {message}\n---\n")

    return render_template('thankyou.html')

@app.route('/feedbacks')
def feedbacks():
    try:
        with open('feedback.txt', 'r') as f:
            data = f.read()
    except FileNotFoundError:
        data = "No feedback yet."
    
    return render_template('feedback.html', feedback_data=data)

@app.route('/delete-feedbacks', methods=['POST'])
def delete_feedbacks():
    open('feedback.txt', 'w').close()
    return render_template('feedback.html', feedback_data="All feedback deleted.")

if __name__ == '__main__':
    app.run(debug=True)
