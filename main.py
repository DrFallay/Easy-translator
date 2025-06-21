from flask import Flask, render_template, request, session
import os
#from livereload import Server
from side import translate

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def index():
    translated = ""
    
    # Initialize history if it doesn't exist
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        input_text = request.form["text"]
        target_lang = request.form["lang"]
        translated = translate(input_text, target_lang)

        # Add to history
        session["history"].append({
            "original": input_text,
            "translated": translated,
            "lang": target_lang
        })
        session.modified = True  # Make sure Flask saves the session

    return render_template("index.html", translated=translated, history=session["history"])


if __name__ == "__main__":
    #server = Server(app.wsgi_app)
    #server.serve(debug=True)
    app.run(debug=True)
