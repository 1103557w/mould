from wtforms import Form, IntegerField, RadioField, FloatField, SelectField
from wtforms.validators import InputRequired, NumberRange


# class CalculatorForm(Form):
#     severity_choices = [("70%", .7), ("75%", 0.75), ("80%", 0.8), ("85%", 0.85), ("90%", 0.9), ("95%", 0.95), ("100%", 1)]
#     total_rooms = IntegerField(label="Total Number of Rooms: ", validators=[InputRequired(), NumberRange(1, 40)])
#     rooms_affected = IntegerField(label="Number of Rooms Effected: ", validators=[InputRequired(), NumberRange(1, 40)])
#     mould_months = IntegerField(label="Number of Months Mould Experienced: ", validators=[InputRequired(), NumberRange(1, 40)])
#     rent = FloatField(label="Rent Per Month in Pounds: ", validators=[InputRequired(), NumberRange(10, 10_000)])
#     severity = SelectField(label="Severity (See explanation): ", choices=severity_choices)
class CalculatorForm(Form):
    pass
