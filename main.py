from flask import Flask, render_template
import pandas as pd

# Points default template and static folders to target folders
app = Flask(__name__)

# "/" is root webpage
@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about_page(station, date):
    # df = pd.read_csv("")
    # temperature = df.station(date)
    # return render_template("about.html")
    temperature = 23
    return {"station": station, "date": date, "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True)