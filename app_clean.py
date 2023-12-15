# import flask class , render html jasontify
from flask import Flask, render_template, jsonify
from sqlalchemy.engine.interfaces import DBAPIType

#since we create database.py we can invoke it as a module
from database import engine
from sqlalchemy import text

app = Flask(__name__)  # create object app of the class


def load_jobs_from_db():
  # open database name as conn and do anything you want
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = result.all()
    jobs_dict = [row._asdict() for row in jobs]
    # cast alchemy class list to python dictionary
    print("jobs_alchemy is ", type(jobs), " jobs_dict is ", type(jobs_dict))
    return jobs_dict


# datadynamic using jason
@app.route('/api/jobs')
# www.poprla.com(DNS)/...  << หลัง / คือ route , @ คือเครื่องหมายที่ใช้ function พิเศษ library นั้นๆได้ หลัง '/' ด้านบน def function to return "helloworld"
@app.route('/')
def home():
  job_list = load_jobs_from_db()  # here what we query from db
  # render this html file, python list sent to renders via html
  return render_template("home.html", jobs=job_list, companyname="IDK")
  #return 'Hello, this is a basic Flask webpage!'


# 0.0.0.0 คือ ให้เป็น public ip ที่สามารถเข้าไปในเว็บไต์ได้ debug=True เพื่อให้ code เปลี่ยนแปลง อัพเดทบนหน้าเว็บทันที
print("__name is ", __name__)
if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
