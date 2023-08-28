from flask import Flask, render_template, flash
from forms import CalculatorForm


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@app.route("/", methods=["POST", "GET"])
def index():
    form = CalculatorForm()
    if form.validate_on_submit():
        # TODO ensure rooms_affected <= rooms
        rooms = form.total_rooms.data
        rooms_affected = form.rooms_affected.data
        mould_months = form.mould_months.data
        rent = form.rent.data
        severity = float(form.severity.data)
        result_number = mould_months * (rooms_affected / rooms) * severity * rent
        result_str = f"£{result_number:.2f}"
        return render_template("index.html", form=form, result=result_str)
    return render_template("index.html", form=form)

# @mould.route("/result/", methods=["POST"])
# def result(request):
#     form = CalculatorForm(request.form)
#
#     print(form.data)

if __name__ == "__main__":
    app.debug = True
    app.run()
