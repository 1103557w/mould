from flask import Flask, render_template, flash
from forms import CalculatorForm

mould = Flask(__name__)

@mould.route("/")
def index():
    form = CalculatorForm()
    return render_template("index.html", form=form)

@mould.route("/result/", methods=["POST"])
def result(request):
    form = CalculatorForm(request.form)

    print(form.data)

if __name__ == "__main__":
    mould.debug = True
    mould.run()
