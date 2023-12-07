# import flask class , render html jasontify
from flask import Flask, render_template, jsonify
app = Flask(__name__)  # create object app of the class

# python dictionary normally same format as database
JOBS = [ 
      {
        'id': 1,
        'title': 'Python Developer',
        'location': 'New York',
        'salary': '$100,000'
      },  
      {
         'id': 2,
         'title': 'Data Scientist',
         'location': 'San Francisco',
         'salary': '$120,000'
      },
      {    
         'id': 3,  
         'title': 'Machine Learning Engineer',
         'location': 'San Francisco',
         'salary': '$90,000'
      },
      {
         'id': 4,
         'title': 'Dev Op',
         'location': 'San Francisco',

      }
]

# datadynamic using jason 
@app.route('/api/jobs')  
# convert to python dict to jason
def list_jobs():
    return jsonify(JOBS)

# www.poprla.com(DNS)/...  << หลัง / คือ route , @ คือเครื่องหมายที่ใช้ function พิเศษ library นั้นๆได้ หลัง '/' ด้านบน def function to return "helloworld"
@app.route('/')  



def home():
  # render this html file, python list sent to renders via html
  return render_template("home.html", jobs = JOBS, companyname = "IDK")  
  #return 'Hello, this is a basic Flask webpage!'


# 0.0.0.0 คือ ให้เป็น public ip ที่สามารถเข้าไปในเว็บไต์ได้ debug=True เพื่อให้ code เปลี่ยนแปลง อัพเดทบนหน้าเว็บทันที
print("__name is ", __name__)
if __name__ == '__main__':
  app.run(
      '0.0.0.0', debug=True
  )  
