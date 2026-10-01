from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    napis_w_BE = "Jesteśmy w szablonie - treść z pliku .py"
    return render_template("index.html", napis_do_FE = napis_w_BE)

if __name__ == "__main__":
    app.run(debug=True)


