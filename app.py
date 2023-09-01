from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    who = "asdfasdfasd"
    return render_template('index.html', who=who)

@app.route('/hello')
def again():
    return "hello again, bros"

@app.route('/question', methods=["POST", "GET"])
def question():
    if request.method == "POST":
        pass
    if request.method == "GET":
        pass
    return ""

if __name__ == "__main__":
    app.run(debug=True)