from flask import Flask, render_template, flash
from forms import CalculatorForm

mould = Flask(__name__)

mould.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@mould.route("/", methods=["POST", "GET"])
def index():
    form = CalculatorForm()
    if form.validate_on_submit():
        # print(form.data)
        mould.logger.warning("hey")
        print("hey")
        flash("HEY")
        return render_template("index.html", form=form, result=12)
    return render_template("index.html", form=form)

# @mould.route("/result/", methods=["POST"])
# def result(request):
#     form = CalculatorForm(request.form)
#
#     print(form.data)

if __name__ == "__main__":
    mould.debug = True
    mould.run()
