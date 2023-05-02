CREATE DATABASE first;
use first;
GRANT ALL on first to root@localhost;

CREATE TABLE covid (
  RegNo int(5),
  Fname varchar(10)  NULL,
  Lname varchar(10) null,
  VacStatus char(3)  null
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert into covid values
    (12345,'Shreyash','Sarade','Yes'),
    (11223,'Kiran','Thigale','No');