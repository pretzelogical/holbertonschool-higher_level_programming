-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE states(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name varchar(256) NOT NULL;
)