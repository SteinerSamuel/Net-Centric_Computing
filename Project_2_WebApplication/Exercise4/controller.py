from model import InputForm
from flask import Flask, render_template, request
import compute
import sys

app = Flask(__name__)

# checks to see if the bootstrap version of the template is to be used and if a template that does not
try:
    template_name = sys.argv[1]
except IndexError:
    template_name = 'view_plane'

if template_name == 'view_bootstrap':
    from flask_bootstrap import Bootstrap
    Bootstrap(app)
else:
    template_name = 'view_plane'


# decorates the function with app.route setting the route of the application to /vib1
@app.route('/vib1', methods=['GET', 'POST'])
def index():
    #  When a POST request is made it grabs the data from the form and sends it to compute.
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result, tex = compute.visualize_series(form.formula.data, form.var.data, form.N.data, form.xmin.data,
                                               form.xmax.data, form.ymin.data, form.ymax.data, form.legend.data,
                                               form.x0.data, form.erase.data)
    else:
        result = None
        tex = None
    # returns the rendered template using form and the results from the compute file
    return render_template(template_name + '.html',
                           form=form, result=result, tex=tex)


if __name__ == '__main__':
    app.run(debug=True)
