\c postgres;

CREATE TABLE Flat (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    image_url VARCHAR(255)
);
