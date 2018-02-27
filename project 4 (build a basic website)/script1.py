from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "homepage is here"

@app.route('/about/')
def about():
    return "About moji's company!!!"

if __name__ == "__main__":
    app.run(debug=True)
