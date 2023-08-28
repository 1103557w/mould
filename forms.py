from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, FloatField, SelectField
from wtforms.validators import InputRequired, NumberRange


class CalculatorForm(FlaskForm):
    severity_choices = [(.7, "70%"), (0.75, "75%"), (0.8, "80%"), (0.85, "85%"), (0.9, "90%"), (0.95, "95%"), (1, "100%")]
    total_rooms = IntegerField(label="Total Number of Rooms: ", validators=[InputRequired(), NumberRange(1, 40)])
    rooms_affected = IntegerField(label="Number of Rooms Affected: ", validators=[InputRequired(), NumberRange(1, 40)])
    mould_months = IntegerField(label="Number of Months Mould Experienced: ", validators=[InputRequired(), NumberRange(1, 40)])
    rent = FloatField(label="Rent Per Month in Pounds: ", validators=[InputRequired(), NumberRange(10, 10_000)])
    severity = SelectField(label="Severity (See explanation): ", choices=severity_choices)
