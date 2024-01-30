from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Dhaka, Bangladesh",
        "salary": "120000"
    },
    {
        "id": 2,
        "title": "DevOps Engineer",
        "location": "Dhaka, Bangladesh",
        "salary": "130000"
    },
    {
        "id": 3,
        "title": "Fontend Developer",
        "location": "Dhaka, Bangladesh",
        #"salary": "100000"
    },
    {
        "id": 4,
        "title": "Backend Developer",
        "location": "Dhaka, Bangladesh",
        "salary": "110000"
    },
]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Amit")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
