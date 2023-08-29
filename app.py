from flask import Flask, render_template, flash
from forms import CalculatorForm, DumbForm

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@app.route("/", methods=["POST", "GET"])
def index():
    form1 = CalculatorForm(prefix="form1")
    form2 = DumbForm(prefix="form2")
    if form1.calculate.data and form1.validate():
        # TODO ensure rooms_affected <= rooms
        rooms = form1.total_rooms.data
        rooms_affected = form1.rooms_affected.data
        mould_months = form1.mould_months.data
        rent = form1.rent.data
        severity = float(form1.severity.data)
        result_number = mould_months * (rooms_affected / rooms) * severity * rent
        result_str = f"£{result_number:.2f}"
        return render_template("index.html", form1=form1, form2=form2, result=result_str)
    if form2.submit.data:
        if form2.validate():
            return render_template("index.html", form1=form1, form2=form2, result="HEY")
    return render_template("index.html", form1=form1, form2=form2)

# @mould.route("/result/", methods=["POST"])
# def result(request):
#     form = CalculatorForm(request.form)
#
#     print(form.data)

if __name__ == "__main__":
    app.debug = True
    app.run()
