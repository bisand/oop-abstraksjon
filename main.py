from crypt import methods
from flask import Flask, redirect, render_template, request
from models.Car import Car
from models.Vehicle import Vehicle
from models.Media import Media
from models.Book import Book
from models.DVD import DVD
from models.Magazine import Magazine

app = Flask(__name__)

database = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/media", methods=["GET"])
def media():
    res = []
    for data in database:
        res.append(data.__dict__)
    return render_template("media.html", media=res)


@app.route("/media", methods=["POST"])
def new_media():
    title = request.form["title"]
    author = request.form["author"]
    director = request.form["director"]
    # editor = request.form["editor"]
    issue_number = request.form["issue_number"]

    media = Media(title)
    if author is not "":
        media = Book(title, author)
    if director is not "":
        media = DVD(title, director)
    if issue_number is not "":
        media = Magazine(title, issue_number)

    database.append(media)

    print(media.__dict__)
    return redirect("/media")


app.run()
