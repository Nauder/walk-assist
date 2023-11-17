CREATE DATABASE tcs_db;
CREATE ROLE tcs_role;
GRANT ALL PRIVILEGES ON DATABASE tcs_db TO tcs_role;

-- Run inside tcs_db
GRANT ALL PRIVILEGES ON SCHEMA public TO tcs_role;
CREATE ROLE tcs_user WITH LOGIN PASSWORD '123123';
GRANT tcs_role TO tcs_user;
INSERT INTO usuario VALUES (default, 1, 'admin@mail.com', '202cb962ac59075b964b07152d234b70', 'admin', 1);
