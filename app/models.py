from app import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# class Ticket(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
#     user_id = db.Column(db.Integer, nullable=False)
#     status = db.Column(db.String(20), default='waiting')

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    # date = db.Column(db.String(30), nullable=True)  # You can later convert this to DateTime if needed
    status = db.Column(db.String(20), default='waiting')
