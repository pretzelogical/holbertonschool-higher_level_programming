-- creates database hbtn_0d_2 and user user_od_2
CREATE DATABASE hbtn_0d_2;
CREATE USER user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 TO user_0d_2@localhost;
