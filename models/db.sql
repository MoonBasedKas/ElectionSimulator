create database votes;

use votes;

create table voteTable (id int NOT NULL AUTO_INCREMENT, canidate varchar(255), origin varchar(255), votes bigint, primary key(id));

create table voteTablePT (id int NOT NULL AUTO_INCREMENT, canidate varchar(255), origin varchar(255), votes bigint, primary key(id));