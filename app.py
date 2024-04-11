# import modules
from flask import Flask, jsonify, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db_utils import execute_sql_query
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pa$$w0rd@localhost/storedata' # database user:password@localhost/database credentials
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define class Sales
class Sales(db.Model):
    __tablename__ = 'sales'

    # Table columns
    id = db.Column(db.Integer, primary_key=True)
    store_code = db.Column(db.String(5), nullable=False)
    total_sale = db.Column(db.DECIMAL(9,2), nullable=False)
    transaction_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Sales %r>' % self.id

# Index route to display all data from database
@app.route('/')
def index():
    sales_data = Sales.query.all()
    return render_template('index.html', sales=sales_data)

# Create route and function for POST request for creating new data in sales
@app.route('/create', methods=['POST'])
def create_sale():
    if request.method == 'POST':
        id = int(request.form['id'])
        store_code = request.form['store_code'],
        total_sale = round(float(request.form['total_sale']), 2)
        transaction_date = date.fromisoformat(request.form['transaction_date'])

        new_sale = Sales(
        id = id,
        store_code = store_code,
        total_sale = total_sale,
        transaction_date = transaction_date
        )
        try:
            db.session.add(new_sale)
            db.session.commit()
            return redirect('/')
        except:
            return 'Something went wrong'

    # Return to index.html with new created sale and order all sales ID
    else:
        sales = Todo.query.order_by(Todo.id).all()
        return render_template('index.html', sales=sales)

# Create route and function for PUT request for updating data
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_sale(id):
    sale = Sales.query.get_or_404(id) # Attempt to get that sale or 404 bad request

    if request.method == 'POST':
        sale.store_code = request.form['store_code']
        sale.total_sale = round(float(request.form['total_sale']), 2)
        sale.transaction_date = date.fromisoformat(request.form['transaction_date'])

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('update.html', sale=sale) # Pass sale object to update.html

# Create route and function for DELETE request for deleting data by ID
@app.route('/delete/<int:id>', methods=['GET'])
def delete_sale(id):
    sale_to_delete = Sales.query.get_or_404(id) # Attempt to get that sale or 404 bad request

    if sale_to_delete:
        db.session.delete(sale_to_delete)
        db.session.commit()
    return redirect(url_for('index'))

# Route to execute SQL queries
@app.route('/sql_query', methods=['POST'])
def sql_query():
    query = request.json['query']
    result = execute_sql_query(query)
    return jsonify(result)

# GET endpoint to get data based on date range
@app.route('/get_sales_data', methods=['GET'])
def get_sales_data():

    # Start and end date paremeters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 404

    sales_data = Sales.query.filter(Sales.transaction_date.between(start_date, end_date)).all()

    # JSON dictionary
    json_data = [{
        'id': sale.id,
        'store_code': sale.store_code,
        'total_sale': float(sale.total_sale),
        'transaction_date': str(sale.transaction_date for sale in sales_data)} for sale in sales_data]

    # List
    list_data = [[sale.id,
        sale.store_code,
        float(sale.total_sale),
        str(sale.transaction_date)] for sale in sales_data]

    # Pandas Data Frame
    df = pd.DataFrame(list_data, columns=['id', 'store_code', 'total_sale', 'transaction_date'])

    return jsonify({'json_data': json_data,
                    'list_data': list_data,
                    'dataframe': df.to_dict(orient= 'records')
    })

# POST endpoint to add new row to MySQL database
@app.route('/add_row', methods=['POST'])
def add_row():
    if request.method == 'POST':
        data = request.json()

        # Extract parameters from request
        new_sale = Sales(
            id = data['id'],
            store_code = data['store_code'],
            total_sales = data['total_sales'],
            transaction_date = data['transaction_date']
        )

        db.session.add(new_sale)
        db.session.commit()
        return jsonify({'message': 'Sale added successfully to database.'})
    else:
        return jsonify({'message': 'Error adding sale.'})


# To run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

