from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    updateNum = db.Column(db.Integer)
    date = db.Column(db.Integer)
    url = db.Column(db.String(200))
    deaths = db.Column(db.Integer)
    imported = db.Column(db.Integer)
    community = db.Column(db.Integer)
    tested = db.Column(db.Integer)
    contact = db.Column(db.Integer)

    def toDict(self):
        return {
            "id": self.id,
            "updateNum": self.updateNum,
            "date": self.date,
            "url": self.url,
            "deaths": self.deaths,
            "imported": self.imported,
            "community": self.community,
            "tested": self.tested,
            "contact":self.contact
        }