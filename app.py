# import flask class , render html jasontify
from flask import Flask, render_template, jsonify, redirect, url_for, request
# from sqlalchemy.engine.interfaces import DBAPIType
from sqlalchemy import text
#since we create database.py we can invoke it as a module
from database import load_jobs_from_db, increase_salary_db, load_one_jobs_from_db, add_application_to_db

app = Flask(__name__)  # create object app of the class
job_list = load_jobs_from_db()


# datadynamic using jason
@app.route('/api/jobs')
def list_jobs():  # convert jason return as json webpage
  return jsonify(job_list)


#add recruitment page each jobs
@app.route("/jobs/<id>")
def showjobs(id):
  job_list = load_one_jobs_from_db(id)
  if not job_list:
    return "Not Found", 404
  return render_template("jobpage.html", job=job_list, companyname="IDK")
  # return jsonify(job_list)


# www.porprla.com(DNS)/...  << หลัง / คือ route , @ คือเครื่องหมายที่ใช้ function พิเศษ library นั้นๆได้ หลัง '/' ด้านบน def function to return "helloworld"
@app.route('/')
def home():
  job_list = load_jobs_from_db()
  # render this html file, python list sent to renders via html
  return render_template("home.html", jobs=job_list, companyname="IDK")
  #return 'Hello, this is a basic Flask webpage!'


#after click increase money
# @app.route('/apply', methods=['POST'])
@app.route('/plusmoney', methods=['POST'])
def apply():
  increase_salary_db()
  return redirect(url_for('home'))


#after click submit form for register]
@app.route('/jobs/apply_to_jobs', methods=['POST'])
def apply_to_jobs():
  # request from alsk after fill in form we get those data from here
  data = request.form
  job_id = request.form['job_id']
  add_application_to_db(int(job_id), data)
  # Construct a dictionary to jsonify the data
  # data = {
  #     'job_id'    : job_id,
  #     'name'      : name,
  #     'email'     : email,
  #     'linkedin'  : linkedin,
  #     'phone'     : phone,
  #     'education' : education
  # }
  return render_template("app_submitted.html",
                         application=data,
                         jobs=job_list,
                         jobname=job_list[int(job_id)-1]
)



# 0.0.0.0 คือ ให้เป็น public ip ที่สามารถเข้าไปในเว็บไต์ได้ debug=True เพื่อให้ code เปลี่ยนแปลง อัพเดทบนหน้าเว็บทันที
print("__name is ", __name__)
if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
