from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Jira?_?__?_?'


if __name__ == '__main__':
    app.run(debug=True)


