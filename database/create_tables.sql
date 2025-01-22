CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(255),
    employee_id INT,
    ship_country VARCHAR(255)
);

CREATE TABLE order_details (
    order_id INT REFERENCES orders(order_id),
    product_id INT,
    quantity INT,
    unit_price DECIMAL,
    discount FLOAT
);
