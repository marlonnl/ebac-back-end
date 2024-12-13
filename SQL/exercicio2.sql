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

--- INSERÇÃO DE DADOS

-- inserindo clientes
INSERT INTO customers (name, email, document, phone, address)
VALUES 
('Marlonn', 'marlonn@email.com', '123456', '99999999', 'rua a'),
('Maria', 'maria@email.com', '234567', '98888888', 'rua b'),
('Pedro', 'pedro@email.com', '345678', '97777777', 'rua c'),
('Paula', 'paula@email.com', '456789', '96666666', 'rua d'),
('Carlo', 'carlo@email.com', '567890', '95555555', 'rua e'),
('Julia', 'julia@email.com', '678901', '94444444', 'rua f');

-- inserindo produtos
INSERT INTO products (name, description, price)
VALUES
('Garfo', 'utensílio de cozinha', 5),
('Colher', 'utensílio de cozinha', 4),
('Camiseta', 'roupa 100% algodão', 60),
('Calça', 'jeans de qualidade', 200),
('Óculos', 'armação sem a lente', 500);

-- inserindo valores no stock
INSERT INTO stock (product_id, quantity)
VALUES
(1, 10),
(2, 11),
(3, 12),
(4, 13),
(5, 14);