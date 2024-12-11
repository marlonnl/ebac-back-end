-- criação da DB
create database store;
\c store

-- id, name, email, document, phone, address
create table customers (
	customer_id SERIAL PRIMARY KEY,
	name varchar(255) NOT NULL,
	email varchar(255) UNIQUE NOT NULL,
	document varchar(15) UNIQUE NOT NULL,
	phone varchar(15) NOT NULL,
	address varchar(255)
);

-- id, name, description, price
create table products (
	product_id SERIAL PRIMARY KEY,
	name varchar(255),
	description varchar(255),
	price numeric CHECK (price > 0)
);

-- stock
-- product_id, stock (??)
create table stock (
	product_id integer REFERENCES products (product_id),
	quantity integer CHECK (quantity > 0)
);