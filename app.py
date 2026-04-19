from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def age():
    result = ""

    if request.method == "POST":
        age = int(request.form["age"])

        if age >= 18:
            result = "Siz kattasiz 🧑"
        else:
            result = "Siz kichiksiz 🧒"

    return render_template("age.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
