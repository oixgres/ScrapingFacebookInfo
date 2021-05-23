<?php 

$host = 'localhost';
$user = 'conisoft_fb';
$pass = 'Fengoigres1094346';
$db = 'conisoft_facebook_scraper';

$conn = mysqli_connect($host, $user, $pass, $db);

mysqli_set_charset($conn, "utf8mb4");
?>