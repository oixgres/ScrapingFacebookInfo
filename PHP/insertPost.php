<?php
require_once 'connection.php';

$id = $_POST['id'];
$url = $_POST['url'];
$user = $_POST['user'];
$text = $_POST['text'];

$query = "INSERT INTO post(id_post, url, persona, texto) VALUES ('".$id."', '".$url."', '".$user."', '".$text."')";

mysqli_query($conn, $query);

mysqli_close($conn);

echo $text;
?>