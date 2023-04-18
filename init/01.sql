CREATE DATABASE IF NOT EXISTS test_db;

USE test_db;

CREATE TABLE games(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price DECIMAL(9,2) NOT NULL
);

INSERT INTO games(name, description, price)
VALUES 
    ("Counter Strike", "Shooter", 64.99),
    ("Assassins Creed I", "Altair history", 32.99);
