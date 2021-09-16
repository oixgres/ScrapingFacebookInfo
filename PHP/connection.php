<?php 

$host = 'localhost';
$user = '*****';
$pass = '******';
$db = '******';

$conn = mysqli_connect($host, $user, $pass, $db);

mysqli_set_charset($conn, "utf8mb4");
?>