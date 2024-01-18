-- Task: Create a table users with country enumeration

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(50),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY(id)
);
