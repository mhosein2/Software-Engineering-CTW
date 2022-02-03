import flask
app = flask.Flask(__name__)


@app.route("/")
def index():
    favShows = ["The Walking Dead", "Daredevil", "Cobra Kai", "The Witcher", "The Wheels of Time"]
    return flask.render_template("index.html", len = len(favShows), favShows = favShows, name="Michael")

app.run(debug=True)