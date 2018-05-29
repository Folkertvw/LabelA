# LabelA Assesment
De volgende queries zijn gerbuikt om de databse op te zetten:
* CREATE TABLE Brand(Brand_ID int PRIMARY KEY, Brand varchar(255));
* CREATE TABLE Model(Model_ID int, Model varchar(255), PRIMARY KEY(Model_ID));
* CREATE TABLE Car(Car_ID int UNIQUE, Model_ID int UNIQUE REFERENCES Model(Model_ID), Brand_ID int REFERENCES Brand(Brand_ID),  PRIMARY KEY(Car_ID, Model_ID));
* CREATE TABLE Battery(Battery_ID int, Car_ID int REFERENCES Car(Car_ID), battery_name varchar(255), battery_price decimal, PRIMARY KEY(Battery_ID, Car_ID));
* CREATE TABLE Tyre(Tyre_ID int, Car_ID int REFERENCES Car(Car_ID), tyre_name varchar(255), tyre_price decimal, PRIMARY KEY(Tyre_ID, Car_ID));
* CREATE TABLE Brake(Brake_ID int, Car_ID int REFERENCES Car(Car_ID), brake_name varchar(255), brake_price decimal, PRIMARY KEY(Brake_ID, Car_ID));

---

* INSERT INTO Brand(brand_id, brand) values(1, 'Mercedes');
* INSERT INTO Brand(brand_id, brand) values(2, 'Porsche');
* INSERT INTO Model(model_id, model) values(1, 'C-klasse');
* INSERT INTO Car(Car_ID, Model_ID, Brand_ID) values(1,1,1);
* INSERT INTO Battery(battery_id, car_id, battery_name, battery_price) values(1, 1, 'Varta', 49.99);
* INSERT INTO Tyre(tyre_id, car_id, tyre_name, tyre_price) values(1, 1, 'Michelin', 399.99);
* INSERT INTO Brake(brake_id, car_id, brake_name, brake_price) values(1, 1, 'Brembo', 499.99);
* INSERT INTO Model(model_id, model) values(2, 'E-klasse');
* INSERT INTO Car(Car_ID, Model_ID, Brand_ID) values(2,2,1);
* INSERT INTO Battery(battery_id, car_id, battery_name, battery_price) values(1, 2, 'Varta', 49.99);
* INSERT INTO Tyre(tyre_id, car_id, tyre_name, tyre_price) values(2, 1, 'Falken', 499.99);
* INSERT INTO Tyre(tyre_id, car_id, tyre_name, tyre_price) values(1, 2, 'FalkenV2', 499.99);
* INSERT INTO tyre(tyre_id, car_id, tyre_name, tyre_price) values(2, 2, 'Falken', 499.99);
* INSERT INTO Brake(brake_id, car_id, brake_name, brake_price) values(2, 1, 'StopTech', 499.99);
---

* SELECT model.model_id, model.model, tyre_name, tyre_id FROM model JOIN car ON(model.model_id = car.model_id) JOIN tyre ON(car.car_id = tyre.car_id)