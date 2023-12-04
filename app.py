from flask import Flask   # import flask class

app = Flask(__name__)      # create object app of the class

@app.route('/')           # www.poprla.com(DNS)/...  << หลัง / คือ route , @ คือเครื่องหมายที่ใช้ function พิเศษ library นั้นๆได้ 
# หลัง '/' ด้านบน def function to return "helloworld" 
def home():               
    return 'Hello, this is a basic Flask webpage!'
print("__name is ", __name__)
if __name__ == '__main__':
  app.run('0.0.0.0', debug=True) # 0.0.0.0 คือ ให้เป็น public ip ที่สามารถเข้าไปในเว็บไต์ได้ debug=True เพื่อให้ code เปลี่ยนแปลง อัพเดทบนหน้าเว็บทันที
  
