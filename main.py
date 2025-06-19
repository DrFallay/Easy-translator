from flask import Flask, render_template, request
import os
from side import translate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated = ""
    if request.method == "POST":
        input_text = request.form["text"]
        target_lang = request.form["lang"]
        translated = translate(input_text, target_lang)

    return render_template("index.html", translated=translated)

if __name__ == "__main__":
    app.run(debug=True)