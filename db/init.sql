create database people;
use people;

CREATE TABLE famous_people (
   id INT NOT NULL AUTO_INCREMENT, '
   name VARCHAR(255) NOT NULL,
   field VARCHAR(255) NOT NULL,
   country VARCHAR(255) NOT NULL, '
   PRIMARY KEY (id)
);

INSERT INTO famous_people
  (name, field, country)
VALUES
  ("Abraham Lincoln", "president", "United States"),
  ("Bill Gates", "businessman", "United States"),
  ("Albert Einstein", "scientist", "Germany"),
  ("Queen Victoria", "monarch", "Great Britain"),
  ("Charles Darwin", "scientist", "Great Britain"),
  ("Leonardo da Vinci", "painter", "Italy"),
  ("Vincent van Gogh", "painter", "Netherlands"),
  ("George Orwell", "author", "Great Britain"),
  ("Oscar Wilde", "author", "Great Britain");
