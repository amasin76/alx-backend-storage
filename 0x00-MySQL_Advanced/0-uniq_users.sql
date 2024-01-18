-- Task: Create a table users with unique email

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(50),
    PRIMARY KEY(id)
);
