from flask import Blueprint, render_template, request, redirect, url_for
from .models import Company, Item, Purchase, Sales, db
from datetime import datetime


# Create a blueprint for routes
app_routes = Blueprint('app_routes', __name__)

# Show the homepage with cash balance and items
@app_routes.route('/')
def index():
    company = Company.query.first()
    items = Item.query.all()
    return render_template('index.html', company=company, items=items)

# Add a new item
@app_routes.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_id = request.form['item_id']
        item_name = request.form['item_name']
        new_item = Item(item_id=item_id, item_name=item_name)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('app_routes.index'))
    return render_template('items.html')

# Add a new purchase
@app_routes.route('/add_purchase', methods=['GET', 'POST'])
def add_purchase():
    if request.method == 'POST':
        item_id = request.form['item_id']
        qty = int(request.form['qty'])
        rate = float(request.form['rate'])
        item = Item.query.filter_by(item_id=item_id).first()
        amount = rate * qty
        purchase = Purchase(purchase_id=f"purchase_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
                            item_id=item_id, qty=qty, rate=rate, amount=amount)
        item.qty += qty  # Update item quantity
        company = Company.query.first()
        company.cash_balance -= amount  # Update company cash balance
        db.session.add(purchase)
        db.session.commit()
        return redirect(url_for('app_routes.index'))
    items = Item.query.all()
    return render_template('purchases.html', items=items)

# Add a new sale
@app_routes.route('/add_sale', methods=['GET', 'POST'])
def add_sale():
    if request.method == 'POST':
        item_id = request.form['item_id']
        qty = int(request.form['qty'])
        rate = float(request.form['rate'])
        item = Item.query.filter_by(item_id=item_id).first()
        amount = rate * qty
        if item.qty >= qty:
            sale = Sales(sales_id=f"sale_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
                         item_id=item_id, qty=qty, rate=rate, amount=amount)
            item.qty -= qty  # Update item quantity
            company = Company.query.first()
            company.cash_balance += amount  # Update company cash balance
            db.session.add(sale)
            db.session.commit()
            return redirect(url_for('app_routes.index'))
        else:
            return "Not enough stock to sell"
    items = Item.query.all()
    return render_template('sales.html', items=items)
