--Specify to use storedata database
USE storedata;

-- Creating the Table
CREATE TABLE sales (
	id INT(5) PRIMARY KEY,
    store_code VARCHAR(5),
    total_sale DECIMAL(9,2),
    transaction_date DATE
);



