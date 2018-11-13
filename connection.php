<?php

class Db {

    private static $instance = NULL;

    private function __construct() {
        
    }

    private function __clone() {
        
    }

    public static function getInstance() {
        $host = 'localhost';
        $db = 'EPIC';
        $user = ' ';
        $pass = ' ';
        $charset = 'utf8';

        $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
        if (!isset(self::$instance)) {
            $opt = [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES => false,
            ];

            self::$instance = new PDO($dsn, $user, $pass, $opt);
        }
        return self::$instance;
    }
}

function fetchdata($query) {
    $db = Db::getInstance();
    $stmt = $db->prepare($query);
    if ($stmt->execute()) {
        $result = $stmt->fetch();
        return $result;
    } else
        return False;
}

function fetchdataAll($query) {
    $db = Db::getInstance();
    $stmt = $db->prepare($query);
    if ($stmt->execute()) {
        $result = $stmt->fetchAll();
        return $result;
    } else
        return False;
}

function returnlast($table) {
    $query = "SELECT * FROM " . $table . " ORDER BY lastmodified DESC LIMIT 1";
    $result = fetchdata($query);
    return $result;
}

function returnlastbycondition($table,$where) {
    $query = "SELECT * FROM " . $table . " WHERE ". $where." ORDER BY lastmodified DESC LIMIT 1";
    $result = fetchdata($query);
    return $result;
} 

function do_query($query) {
    $db = Db::getInstance();
    $stmt = $db->prepare($query);
    if ($stmt->execute())
        return True;
    else
        return False;
}

function do_query_return_last($query) {
    $db = Db::getInstance();
    $stmt = $db->prepare($query);
    if ($stmt->execute())
        return $db->lastInsertId();
    else
        return False;
}


function get_DATA($table) {
    $query = "SELECT * FROM " . $table;
    $result = fetchdataALL($query);
    return $result;
}

function get_id_name($table, $id, $name) {
    $query = "SELECT " . $id . ", " . $name . " FROM " . $table;
    $result = fetchdataALL($query);
    return $result;
}

function update_DATA($table, $valuelist, $where) {
    $valuelist["LastModified"] = date('Y-m-d H:i:s');
    $setlist = "";
    $valuelist = str_replace('"', '\"', $valuelist);
    $valuelist = str_replace("'", "\'", $valuelist);
    foreach ($valuelist as $key => $value) {
        $setlist = $setlist . $key . " = " . "'$value', ";
    }
    $setlist = substr($setlist, 0, -2);
    $query = "UPDATE " . $table . " SET " . $setlist . " WHERE " . $where . "";
    return (do_query($query));
}

function search_DATA($table, $where) {
    $query = "SELECT * FROM " . $table . " WHERE " . $where . "";
    $result = fetchdata($query);
    return $result;
}

function search_DATAs($table, $where) {
    if ($where) {
        $query = "SELECT * FROM " . $table . " WHERE " . $where . "";
        $result = fetchdataAll($query);
        return $result;
    } else {
        $query = "SELECT * FROM " . $table . "";
        $result = fetchdataAll($query);
        return $result;
    }
}

function insert_DATA_return_last($table, $valuelist) {
    $valuelist["CreateDate"] = date('Y-m-d H:i:s');
    $valuelist["LastModified"] = date('Y-m-d H:i:s');
    $valuelist = str_replace('"', '\"', $valuelist);
    $valuelist = str_replace("'", "\'", $valuelist);
    $namelist = "(";
    $values = "(";
    foreach ($valuelist as $key => $value) {
        $namelist = $namelist . $key . ", ";
        if(is_array($value)){
            $value =json_encode($value);
        }
        $values = $values . "'$value', ";
    }
    $namelist = substr($namelist, 0, -2); // delete last ","
    $namelist = $namelist . ")";
    $values = substr($values, 0, -2);
    $values = $values . ")";
    $query = "INSERT INTO " . $table . " " . $namelist . " VALUES " . $values . "";
    return (do_query_return_last($query));
}


function insert_DATA($table, $valuelist) {
    $valuelist["CreateDate"] = date('Y-m-d H:i:s');
    $valuelist["LastModified"] = date('Y-m-d H:i:s');
    $valuelist = str_replace('"', '\"', $valuelist);
    $valuelist = str_replace("'", "\'", $valuelist);
    $namelist = "(";
    $values = "(";
    foreach ($valuelist as $key => $value) {
        $namelist = $namelist . $key . ", ";
        if(is_array($value)){
            $value =json_encode($value);
        }
        $values = $values . "'$value', ";
    }
    $namelist = substr($namelist, 0, -2); // delete last ","
    $namelist = $namelist . ")";
    $values = substr($values, 0, -2);
    $values = $values . ")";
    $query = "INSERT INTO " . $table . " " . $namelist . " VALUES " . $values . "";
    return (do_query($query));
}

function delete_DATA($table, $where) {
    $query = "DELETE FROM " . $table . " WHERE " . $where . "";
    return (do_query($query));
}

function getColumnNames($table) {//contains bug
    $query = "Show Columns FROM " . $table . "";
    try {
        $output = fetchdataall($query);
        $output = array_slice($output, 1, -2);
        $list = [];
        foreach ($output as $val) {
            $list["" . $val["Field"] . ""] = "";
        }
        return $list;
    } catch (PDOException $pe) {
        trigger_error('Could not connect to MySQL database. ' . $pe->getMessage(), E_USER_ERROR);
    }
}

function preparekeyvalpare($table, $id, $name) {
    $row = get_id_name($table, $id, $name);
    $result = [];
    foreach ($row as $value) {
        $result[$value[$id]] = $value[$name];
    }
    return $result;
}

function preparesingledict($table, $keyindex, $valueindex) {
    $query = "SELECT " . $keyindex . ", " . $valueindex . " FROM " . $table;
    $data = fetchdataAll($query);
    $DICT = [];
    foreach ($data as $val) {
        $DICT["" . $val[$keyindex] . ""] = $val[$valueindex];
    }
    return $DICT;
}

?>