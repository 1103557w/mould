from flask import Flask, render_template, flash
from forms import CalculatorForm

mould = Flask(__name__)

@mould.route("/")
def index():
    return render_template("index.html")

@mould.route("/result/", methods=["POST"])
def result(request):
    form = CalculatorForm(request.form)

    form_data = {}
    for field_name, field in form._fields.items():
        form_data[field_name] = field.data
    print(form_data)

if __name__ == "__main__":
    mould.debug = True
    mould.run()
