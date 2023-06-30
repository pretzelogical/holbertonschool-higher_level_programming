-- creates the database hbtn_0d_usa
-- and the table cities
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    FOREIGN KEY(`state_id`) REFERENCES states(`id`)
);
