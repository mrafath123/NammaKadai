from datetime import datetime
from . import db

# Company Model
class Company(db.Model):
    __tablename__ = 'company'
    company_name = db.Column(db.String(100), primary_key=True)
    cash_balance = db.Column(db.Float)

# Item Model
class Item(db.Model):
    __tablename__ = 'item'
    item_id = db.Column(db.String(50), primary_key=True)
    item_name = db.Column(db.String(100))
    qty = db.Column(db.Integer, default=0)

# Purchase Model
class Purchase(db.Model):
    __tablename__ = 'purchase'
    purchase_id = db.Column(db.String(50), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    item_id = db.Column(db.String(50), db.ForeignKey('item.item_id'))
    qty = db.Column(db.Integer)
    rate = db.Column(db.Float)
    amount = db.Column(db.Float)
    item = db.relationship('Item', backref=db.backref('purchases', lazy=True))

# Sales Model
class Sales(db.Model):
    __tablename__ = 'sales'
    sales_id = db.Column(db.String(50), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    item_id = db.Column(db.String(50), db.ForeignKey('item.item_id'))
    qty = db.Column(db.Integer)
    rate = db.Column(db.Float)
    amount = db.Column(db.Float)
    item = db.relationship('Item', backref=db.backref('sales', lazy=True))

# Initialize some data (optional) - To be used when the app starts
def init_data():
    company = Company.query.first()
    if not company:
        company = Company(company_name="Namma Kadai", cash_balance=1000.0)
        db.session.add(company)
        db.session.commit()

    items = [
        {'item_id': 'pen', 'item_name': 'Pen'},
        {'item_id': 'pencil', 'item_name': 'Pencil'},
        {'item_id': 'eraser', 'item_name': 'Eraser'},
        {'item_id': 'sharpener', 'item_name': 'Sharpener'},
        {'item_id': 'geometry_box', 'item_name': 'Geometry Box'}
    ]
    for item in items:
        if not Item.query.filter_by(item_id=item['item_id']).first():
            new_item = Item(item_id=item['item_id'], item_name=item['item_name'])
            db.session.add(new_item)
    db.session.commit()
