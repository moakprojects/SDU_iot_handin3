<?php

var_dump($_REQUEST);

$servername = "#####";
$username = "#####";
$password = "#####";

try {
    $conn = new PDO("mysql:host=$servername;dbname=#####", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully";
    }
catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }
	
if($_REQUEST) {
	var_dump($_REQUEST);
	$time = $_REQUEST['time'];
	$temp = $_REQUEST['temp'];
	$light0 = $_REQUEST['light0'];
	$light1 = $_REQUEST['light1'];
	$volt = $_REQUEST['volt'];
	print($temp);
	
	
	try {
		$sql = "INSERT INTO logs3 (time, temp, lightblue, lightred, volt) VALUES ($time, $temp, $light0, $light1, $volt)";
		$conn->exec($sql);
		echo "New record created successfully";
    }
	catch(PDOException $e)
    {
		echo $sql . "<br>" . $e->getMessage();
    }

	$conn = null;
}


?>
