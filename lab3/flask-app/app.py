from flask import Flask

app = Flask(__name__)

def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i**2
    return result

@app.route('/')
def hello():
    return "hello!, result is " + str(sum_of_squares(1_000_000))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6969)

