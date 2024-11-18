from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test():
    a=5+6
    return "this is my test function{}".format(a)


if __name__=="__main__":
    app.run(host="0.0.0.0")