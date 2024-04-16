CREATE TABLE region (
    code CHAR(3) PRIMARY KEY,
    name VARCHAR(100) NOT null UNIQUE,
    iso_2_code CHAR(2) NOT null UNIQUE
);

CREATE TABLE country (
    code CHAR(3) PRIMARY KEY,
    name VARCHAR(100) NOT null UNIQUE,
    iso_2_code CHAR(2) NOT null UNIQUE,
    longitude DOUBLE PRECISION,
    latitude DOUBLE PRECISION,
    region_code CHAR(3) NOT NULL,
    CONSTRAINT unique_longitude_latitude UNIQUE (longitude, latitude),
    FOREIGN KEY (region_code) REFERENCES region(code)
);

CREATE TABLE source (
    id SERIAL PRIMARY KEY,
    code CHAR(3) NOT null UNIQUE,
    name VARCHAR(100) NOT null UNIQUE,
    last_updated date NOT NULL
);

CREATE TABLE indicator (
    code VARCHAR(50) PRIMARY KEY,
    name VARCHAR(250) NOT null,
    source_note VARCHAR(5000),
    source_organization VARCHAR(5000),
    source_id int NOT NULL,
    FOREIGN KEY (source_id) REFERENCES source(id)
);

CREATE TABLE topic (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT null UNIQUE,
    source_note VARCHAR(2000)
);

CREATE table indicator_x_region (
	id serial PRIMARY KEY,
	indicator_code varchar(20)  not null,
	region_code char(3) not null,
	year int not null,
	value numeric not null,
	FOREIGN KEY (indicator_code) REFERENCES indicator(code),
    FOREIGN KEY (region_code) REFERENCES region(code),
    CONSTRAINT year_after_1900 CHECK (year > 1900)
    --CONSTRAINT unique_record UNIQUE (indicator_code, region_code, year) --
);

CREATE TABLE indicator_x_country (
	id SERIAL PRIMARY KEY,
    year int NOT NULL,
    value numeric NOT NULL,
    indicator_code VARCHAR(20) NOT NULL,
    country_code CHAR(3) NOT NULL,
    FOREIGN KEY (indicator_code) REFERENCES indicator(code),
    FOREIGN KEY (country_code) REFERENCES country(code),
    CONSTRAINT year_after_1900 CHECK (year > 1900)
    --CONSTRAINT unique_record UNIQUE (indicator_code, country_code, year) --
);

CREATE TABLE indicator_x_topic (
	id SERIAL PRIMARY KEY,
    indicator_code VARCHAR(20) NOT NULL,
    topic_id int NOT NULL,
    FOREIGN KEY (indicator_code) REFERENCES indicator(code),
    FOREIGN KEY (topic_id) REFERENCES topic(id)
    --CONSTRAINT unique_record UNIQUE (indicator_code, topic_id) --
);