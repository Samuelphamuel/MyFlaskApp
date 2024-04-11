Transfering excel mock data to MySQL Workbench
In order to import the excel data into MySQL Workbench, I had to change the formatting of the total sale
and date format to match the format needed for MySQL (no $ or commas, and YYYY-MM-DD format). I also
converted it to a .csv file.

How To Run
1. Open terminal into CBAProject folder

2. Make sure to have virtual evironments installed by:
	pip install virtualenv

3. Create a virtual environment by:
	python -m venv venv

4. Activate the virtual environment by:
	.\env\Scripts\activate OR venv/Scripts/activate for Windows

5. Install dependencies in environment by:
	pip install -r requirements.txt

6. To run the function to connect to the MySQL database and return data:
	python db_utils.py
# In db_utils.py you can adjust the SQL query on line 32 to print the result in the terminal #
	query = "SELECT * FROM sales WHERE id = 5;" # This is the SQL query I used #

7. Run the flask app by:
	python app.py
# Make sure the app.config in line 10 of app.py and lines 7-10 in db_utils.py aligns with your own database credientials #

8. Open a web browser and type in the url:
	localhost:5000

9. Here you should be able to see all the data from the mock data sheet as well as create, update, and delete specific sales data

10. To utilize the GET endpoint to show all sales within a specifc date range: http://localhost:5000/get_sales_data?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
	http://localhost:5000/get_sales_data?start_date=2023-01-01&end_date=2023-05-05
# I used the dates in the url above to test this #

11. To utilize the POST endpoint to add a new row to the dataset, while I run the flask app in my gitbash terminal and in cmd I run:
	curl -X POST -H "Content-Type: application/json" -d '{"id": 1001, "store_code": "TX001", "total_sales": 100.00, "transaction_date": "2023-01-20"}' http://localhost:5000/add_row


-Samuel Pham

Upload and share repository (imelendez@cbac.com)