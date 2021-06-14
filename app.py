from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars=mongo.db.all_data.find_one()
    # Return template and data
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars=mongo.db.all_data
    mars_info = scrape_mars.scrape()
    mars.update({}, mars_info, upsert = True)
    return redirect("/", code = 302)


if __name__ == "__main__":
    app.run(debug=True)