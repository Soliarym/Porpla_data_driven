import sqlalchemy
from sqlalchemy import create_engine, text
import os
database_connection_text = os.environ['db_connection']

print("___ start database.py : sqlalchemy version is ", sqlalchemy.__version__)
# connected to databse mysql workbench with planetscale, using sqlalchemy , ssl conection
engine = create_engine(database_connection_text,
                       connect_args={"ssl": {
                           "ssl_cert": "/etc/ssl/cert.pem"
                       }})
print("___ end database.py   : database is connected")


def load_jobs_from_db():
  # open database name as conn and do anything you want
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = result.all()
    jobs_dict = [row._asdict() for row in jobs]
    # cast alchemy class list to python dictionary
    print("jobs_alchemy is ", type(jobs), " jobs_dict is ", type(jobs_dict))
    return jobs_dict

def load_one_jobs_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
       text(f"SELECT * FROM jobs WHERE id={id}")
      )
    rows = result.all()
    jobs_dict = [row._asdict() for row in rows]
    if len(jobs_dict) == 0:
      return None
    else:
      return jobs_dict[0]




def increase_salary_db():
  jobs_dict = load_jobs_from_db()
  for job in jobs_dict:
    if job['id'] == 2:
      job['salary'] = job['salary'] + 1000
    else:
      job['salary'] += 1

  # Save the changes to the database
  with engine.connect() as conn:
    for job in jobs_dict:
      update_query = text(
          "UPDATE jobs SET salary = :salary WHERE id = :job_id")
      conn.execute(update_query, {
          'salary': job['salary'],
          'job_id': job['id']
      })


# open database name as conn and do anything you want
# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))
#   jobs = result.all()
#   print("__type jobs ", type(jobs))
#   print("__type result ", type(result))
#   jobs_dict = [row._asdict() for row in jobs]
#   # cast alchemy class list to python dictionary
#   print( "jobs_alchemy is ", type(jobs), " jobs_dict is ", type(jobs_dict) )

# for job in jobs_dict:
#   if job['title'] == 'Data Scientist':
#       print(" CURRENT salary is ", job['salary'])
#       job['salary'] = 700
#       print(" LATERR salary is ", job['salary'])

# Update the database with the modified job data
# with engine.connect() as conn:
#     for job in jobs_dict:
#         update_query = text("UPDATE jobs SET salary = :salary WHERE id = :job_id")
#         conn.execute(update_query, {'salary': job['salary'], 'job_id': job['id']})
