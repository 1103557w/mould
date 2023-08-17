from flask import Flask, render_template, flash
from forms import CalculatorForm

mould = Flask(__name__)

@mould.route("/")
def index():
    return render_template("index.html")

@mould.route("/result/", methods=["POST"])
def result(request):
    form = CalculatorForm(request.post)
    if request.method == "POST" and form.validate():
        total_rooms = form.total_rooms.data
        rooms_affected = form.rooms_affected.data
        mould_months = form.rooms_affected.data
        rent = form.rent.data
        severity = form.severity.data
        result = ((total_rooms * severity  * rent) / rooms_affected) * mould_months
        flash(result)
        return render_template("index.html")
    return render_template("result.html")

if __name__ == "__main__":
    mould.debug = True
    mould.run()
