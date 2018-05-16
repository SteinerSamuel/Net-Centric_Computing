from capture import capture_image
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/webcam', methods=['GET', 'POST'])
def index():
    print('test')
    if request.method == 'POST':
        result = capture_image()
    else:
        result = None
    return render_template('view.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)