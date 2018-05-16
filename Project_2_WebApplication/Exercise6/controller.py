from compute import add, mul
from model import AddForm, MulForm
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/twoprograms', methods=['GET', 'POST'])
def index():
    form = {}
    result = {}
    form['add'] = AddForm(request.form)
    form['mul'] = MulForm(request.form)
    if request.method == 'POST' and form['mul'].validate() and request.form['btn'] == 'Multiply':
        result['mul'] = mul(form['mul'].p.data, form['mul'].q.data)
    elif request.method == 'POST' and form['add'].validate() and request.form['btn'] == 'Add':
        result['add'] = add(form['add'].a.data, form['add'].b.data)
    else:
        result = None
    return render_template('view.html', form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)