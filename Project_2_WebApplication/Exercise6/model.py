from wtforms import Form, FloatField


class AddForm(Form):
    """ A class for the Add program"""
    a = FloatField(label='a value', default=0)
    b = FloatField(label='b value', default=0)

class MulForm(Form):
    """ A class for the multiply program"""
    p = FloatField(label='p value', default=1)
    q = FloatField(label='q value', default=1)