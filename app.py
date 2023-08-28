from flask import Flask, render_template, flash
from forms import CalculatorForm


# {': 12, : 2, : 2, '
# rent': 132.0, 'severity': '0.7', 'csrf_token': 'IjY1ZDhkMGQzOTI5ZjMyMmIzYjA1NmQ4YWQyOGNkYWViMjdmYTE5ZmUi.ZOzJIg.7Dgh7KrtjgAkBmTZ55qm05OvwNU'}
mould = Flask(__name__)

mould.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@mould.route("/", methods=["POST", "GET"])
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
    mould.debug = True
    mould.run()
