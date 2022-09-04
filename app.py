from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route("/")
def login():
    return "테스트 성공"
    # return render_template()

if __name__ == "__main__":
    app.run(debug=True)