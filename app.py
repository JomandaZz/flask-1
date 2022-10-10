from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/shop')
def shop():
    return render_template("shop.html")


@app.route('/cabinet')
def cabinet():
    return render_template("cabinet.html")


@app.route('/hunter')
def hunter():
    return render_template("hunter.html")


@app.route('/bows')
def bows():
    return render_template("bows.html")


@app.route('/bullets')
def bullets():
    return render_template("bullets.html")


@app.route('/old')
def old():
    return render_template("old.html")


@app.route('/pistols')
def pistols():
    return render_template("pistols.html")


@app.route('/rifles')
def rifles():
    return render_template("rifles.html")


if __name__ == "__main__":
    app.run(debug=True)
