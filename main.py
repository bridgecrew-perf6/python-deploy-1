import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Se indiano consegue deployar, nois tb"

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()