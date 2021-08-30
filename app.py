from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/evenodd/<int:n>')
def even_odd(n):
    print(f"Enter a number: ")
    if (n % 2) == 0:
        result = {
            "Number": n,
            "Even": True
        }
    else:
        result = {
            "Number": n,
            "Odd": False
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
