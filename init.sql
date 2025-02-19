-- Create the table
CREATE TABLE files (
    uid VARCHAR(36) PRIMARY KEY NOT NULL UNIQUE,
    original_name VARCHAR(255) NOT NULL,
    extension VARCHAR(10) NOT NULL,
    size INTEGER NOT NULL,
    format VARCHAR(50) NOT NULL
);