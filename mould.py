from flask import Flask, render_template

mould = Flask(__name__)

@mould.route("/")
def index():
    return render_template("index.html")

@mould.route("/result/", methods=["POST"])
def result():
    return render_template("result.html")

if __name__ == "__main__":
    mould.debug = True
    mould.run()
