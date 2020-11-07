DROP TABLE IF EXISTS citys;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  continent VARCHAR(255)
);

CREATE TABLE citys (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  visited BOOLEAN,
  country_id INT REFERENCES countries(id)
);