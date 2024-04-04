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

6. Run the flask app by:
	python app.py
# Make sure the app.config in line 10 of app.py aligns with your own database credientials #

7. Open a web browser and type in the url:
	localhost:5000

8. Here you should be able to see all the data from the mock data sheet as well as create, update, and delete specific sales data

9. To utilize the GET endpoint to show all sales within a specifc date range: http://localhost:5000/get_sales_data?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
	http://localhost:5000/get_sales_data?start_date=2023-01-01&end_date=2023-05-05
# I used the dates in the url above to test this #

10. To utilize the POST endpoint to add a new row to the dataset, in the terminal I ran:
	curl -X POST -H "Content-Type: application/json" -d '{"id": 1001, "store_code": "TX001", "total_sales": 100.00, "transaction_date": "2023-01-20"}' http://localhost:5000/add_sale


-Samuel Pham

Upload and share repository (imelendez@cbac.com)
# git init - git add . (add everything in directory) - git commit -m "init app"