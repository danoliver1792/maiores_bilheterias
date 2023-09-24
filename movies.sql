CREATE DATABASE movies;

USE movies;

CREATE TABLE filmes (
	id INT AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(255) NOT NULL,
	bilheteria INT NOT NULL
);

-- após o erro que tive no terminal
ALTER TABLE filmes MODIFY bilheteria DECIMAL(20, 0);