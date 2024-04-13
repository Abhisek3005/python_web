from flask import Flask, render_template,jsonify

app  = Flask(__name__)
JOBS =[
  {
    "id":1,
    "tittle":'Data Analyst',
    "location":"Bengaluru",
    "salary":"Rs.10,00,000"},
  {
  "id":2,
  "tittle":"Frontend Engineer",
  "location":"Remote",
  "salary":"Rs.10,00,05"},

  {
    "id":3,
    "tittle":"Backend Engineer",
    "location":"France",
    "salary":"$2000"
  },
  {"id":4,
  "tittle":"CyberSecurity Analyst",
  "location":"Hyderabad",
  "salary":"Rs.20,00,000"
  
  }]

@app.route("/")
def hello_world():
  return render_template("home.html",jobs = JOBS)
@app.route("/api/jobs")
def get_job():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  print("I am inside the if now")
  app.run(host="0.0.0.0",debug=True)

             
             