import scrape_mars

from flask_pymongo import PyMongo

from flask import Flask, render_template, request



app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_data"
mongo = PyMongo(app)

@app.route("/")
def index():

    mars_data = mongo.mars_db.data.find_one()

    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():

    mars_data = scrape_mars.scrape()

    mongo.mars_db.data.update({}, mars_data, upsert=True)
    return 'Working?'

if __name__ == "__main__":
    app.run(debug=False)