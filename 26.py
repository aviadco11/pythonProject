from flask import Flask, request

app = Flask("something")


@app.route('/what', methods=['GET'])
def hello():
    resu = 1 / 0
    with open("namesyqwedfoibasdflhbasdf.txt") as f:
        result = f.read()
        return result


@app.route('/whatismyname', methods=['POST'])
def blabla():
    result = 1 + 1
    if request.method == 'POST':
        return "saved new cars"


@app.route('/')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001, debug=True)