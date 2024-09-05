from flask import Flask, render_template

app = Flask(__name__, template_folder="app/templates")


@app.route("/")
def home():
    context = {"name": f"World"}
    return render_template("home.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
