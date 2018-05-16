from wtforms import Form, validators, StringField, SelectField, IntegerField
import sympy as sp
import numpy as np


def checkSynSympy(form, field):
    """Form validation that checks syntax for sympy"""
    x = form.var.data
    t = field.data
    namespace = sp.__dict__.copy()  # copies the sympy namespace
    namespace.update({x: sp.symbols(x)})
    try:
        eval(t, namespace)
    except:
        raise validators.ValidationError('Incorrect Syntax!')


def checkSynNumpy(form, field):
    """Form validation that checks syntax for numpy"""
    x = field.data
    try:
        eval(x, np.__dict__)
    except:
        raise validators.ValidationError('Incorrect Syntax!')


class InputForm(Form):
    var = StringField(label="Name of independent variable:", default="x",
                      validators=[validators.InputRequired()])
    formula = StringField(label="Expression in independent variable:", default="sin(x)",
                          validators=[validators.InputRequired(), checkSynSympy])
    xmin = StringField(label="Minimum X value in the plot:", default="0",
                       validators=[validators.InputRequired(), checkSynNumpy])
    xmax = StringField(label="Maximum X value in the plot:", default="2*pi",
                       validators=[validators.InputRequired(), checkSynNumpy])
    ymin = StringField(label="Minimum Y value in the plot:", default="-2",
                       validators=[validators.InputRequired(), checkSynNumpy])
    ymax = StringField(label="Maximum Y value in the plot:", default="2",
                       validators=[validators.InputRequired(), checkSynNumpy])
    x0 = StringField(label="Point for series expansion:", default="0",
                     validators=[validators.InputRequired(), checkSynSympy])
    N = IntegerField(label="Polynomial degree of series-approximation:", default="3",
                     validators=[validators.InputRequired()])
    legend = SelectField(label="Location of legend in the plot:", choices=[('0', 'best'), ('1', 'upper right'),
                                                                           ('2', 'upper left'), ('3', 'lower left'),
                                                                           ('4', 'lower right'), ('5', 'right'),
                                                                           ('6', 'center left'), ('7', 'center right'),
                                                                           ('8', 'lower center'), ('9', 'upper center'),
                                                                           ('10', 'center')],
                         validators=[validators.InputRequired()])
    erase = SelectField(label="Erase all curves?", choices=[('yes', "Yes"),
                                                            ('no', 'No')],
                        validators=[validators.InputRequired()])
