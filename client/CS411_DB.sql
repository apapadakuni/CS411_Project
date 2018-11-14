CREATE DATABASE CS411_DB;
USE CS411_DB;
DROP TABLE User_Accounts CASCADE;
DROP TABLE User_Profile CASCADE;
DROP TABLE User_Schedule CASCADE;


# Create User Login Credentials
CREATE TABLE User_Accounts (UID INT(8) NOT NULL AUTO_INCREMENT, Email VARCHAR(100) NOT NULL, Password VARCHAR(128) NOT NULL, Status VARCHAR(20) DEFAULT NULL, Type VARCHAR(20) DEFAULT NULL, CreateDate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, LastModified timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(UID),UNIQUE(Email),INDEX name (UID,Email,CreateDate,LastModified));

#Create User Profiles
CREATE TABLE User_Profile (PID INT(8) NOT NULL AUTO_INCREMENT, UID INT(8) NOT NULL, UserName VARCHAR(100) NOT NULL, Weight FLOAT(8) NOT NULL, Height FLOAT(8) NOT NULL, Age INT(8) NOT NULL, Progress VARCHAR(200), CreateDate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, LastModified timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(PID), FOREIGN KEY(UID) REFERENCES User_Accounts(UID), INDEX name (PID,CreateDate,LastModified));

#Create User Events Schedules
CREATE TABLE User_Schedule (SID INT(8) NOT NULL AUTO_INCREMENT, UID INT(8) NOT NULL, Days VARCHAR(100) NOT NULL, Event_Name VARCHAR(100) NOT NULL, Start_time VARCHAR(100) NOT NULL, End_time VARCHAR(100) NOT NULL, Location VARCHAR(100) NOT NULL, Goal_mile FLOAT(8), Goal_Cal FLOAT(8), CreateDate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, LastModified timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(SID),FOREIGN KEY(UID) REFERENCES User_Accounts(UID), INDEX name (SID,CreateDate,LastModified));
