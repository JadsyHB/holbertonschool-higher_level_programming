-- Module 0: create table users

CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email NOT NULL UNIQUE VARCHAR(255),
       name VARCHAR(255)
);
