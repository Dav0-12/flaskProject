from flask import Flask

app = Flask(__name__)


def convert_c_to_f(celsius):
    """Convert from Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<temp>')
def celsius_to_fahrenheit(temp):
    try:
        temp = float(temp)
        return (f"<h1>Temperature Conversion</h1>"
                f"Celsius Input: {temp} <br> <br>"
                f"Fahrenheit Output: {convert_c_to_f(temp)}")
    except ValueError:
        return 'Enter a valid number in URL'


if __name__ == '__main__':
    app.run()
