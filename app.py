# import flask class , render html jasontify
from flask import Flask, render_template, jsonify, redirect, url_for
# from sqlalchemy.engine.interfaces import DBAPIType
from sqlalchemy import text
#since we create database.py we can invoke it as a module
from database import load_jobs_from_db, increase_salary_db

app = Flask(__name__)  # create object app of the class
job_list = load_jobs_from_db()


# datadynamic using jason
@app.route('/jobs')
def list_jobs():  # convert jason return as json webpage
  return jsonify(job_list)


# www.porprla.com(DNS)/...  << หลัง / คือ route , @ คือเครื่องหมายที่ใช้ function พิเศษ library นั้นๆได้ หลัง '/' ด้านบน def function to return "helloworld"
@app.route('/')
def home():
  job_list = load_jobs_from_db()
  # render this html file, python list sent to renders via html
  return render_template("home.html", jobs=job_list, companyname="IDK")
  #return 'Hello, this is a basic Flask webpage!'


#after click apply
@app.route('/apply', methods=['POST'])
def apply():
  increase_salary_db()
  return redirect(url_for('home'))


# 0.0.0.0 คือ ให้เป็น public ip ที่สามารถเข้าไปในเว็บไต์ได้ debug=True เพื่อให้ code เปลี่ยนแปลง อัพเดทบนหน้าเว็บทันที
print("__name is ", __name__)
if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
