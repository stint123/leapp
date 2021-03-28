from main import app
from models import db, Records
import json

db.create_all(app=app)

with open('data.json') as json_file:
    data = json.load(json_file)

for row in data:
    record = Records(updateNum= row['updateNum'], date= row['date'], url= row['url'], 
    deaths= row['cases']['deaths'], imported= row['cases']['imported'], community= row['cases']['community'], 
    tested= row['tested'], contact= row['cases']['contact'])

    db.session.add(record)

db.session.commit()
print('database initialized!')