from flask import Flask
from flask import request

shiva = Flask(__name__)


@shiva.route(("/test1"))
def test1():
    return "<h1>shivaji is a good boy </h1>" 

@shiva.route("/good_morning")
def good_morning():
    return "<h1> hello good morning india</h1>"

@shiva.route("/good_night")
def good_night():
    return "<h1> hello good night we will meet u in hell and heaven</h1>"

@shiva.route("/test2")
def test2():
    a = 66 +88 * 5
    return "<h1> hello good morning india</h1> {}".format(a) 

@shiva.route("/test3")
def test3():
    data = request.args.get("x")
    return "<h1> This is going is bombacious </h1> {}".format(data)   


if __name__ == "__main__":
    shiva.run(host = "0.0.0.0")