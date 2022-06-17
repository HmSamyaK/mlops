import flask

app = flask.Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello Jethalal</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")