## CREATE TABLE -lauseet 

```
 CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL,
    role VARCHAR(144) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE application (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	sum INTEGER(144) NOT NULL, 
	definition VARCHAR(1000) NOT NULL,
    approved BOOLEAN NOT NULL,
	PRIMARY KEY (id),
    foreign key(account_id) references account (id)
);

CREATE TABLE stipend (
	id integer, 
	date_created datetime, 
	date_modified datetime, 
	name VARCHAR(144) NOT NULL, 
	sum INTEGER(144) NOT NULL, 
	definition VARCHAR(1000) NOT NULL,
	receiver INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	foreign key(account_id) references account (id)
);

CREATE TABLE association (
	foreign key(account_id) references account (id), 
	foreign key (stipend_id) references stipend (id)
);

```