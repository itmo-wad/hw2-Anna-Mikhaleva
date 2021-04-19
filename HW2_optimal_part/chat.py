from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def session():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        #fullname = request.form.get("fullname")
        answers = {'Hello': 'Hi', 'How are you?': 'Fine, Thanks', 'Do you like ITMO?': 'Yes, and you?',
                   'Yes': 'Great!', 'What is your name?': 'My name is AnyaBot', 'Can you play football?': 'No. And you?',
                   'No': "It's a pity", "Goodbye": "Bye!", "What kind of weather do you like?": "Sunny",
                   "I like you": "I like you too"}
        if message in answers:
            answer = answers[message]
            return render_template("cabinet.html", message= message, answer=answer)
        else:
            return render_template("cabinet.html", message = message, answer="I don't understand you")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)