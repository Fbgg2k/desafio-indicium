CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,  -- SERIAL para auto increment
    order_date DATE NOT NULL,
    customer_id VARCHAR(50) NOT NULL,
    employee_id INT NOT NULL,
    ship_country VARCHAR(100) NOT NULL
);

CREATE TABLE order_details (
    order_detail_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(10, 2) NOT NULL,
    discount REAL DEFAULT 0.0
);

CREATE INDEX idx_order_id ON order_details(order_id);
