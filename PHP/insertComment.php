<?php

require_once 'connection.php';

mysqli_set_charset($conn, "utf8mb4");

$id = $_POST['idComment'];
$idPost = $_POST['idPost'];
$user = $_POST['name'];
$text = $_POST['content'];

$query = "INSERT INTO comentario (id_comentario, id_post, persona, texto) VALUES ('$id','$idPost','$user','$text')";
mysqli_query($conn, $query);

mysqli_close($conn);

echo $text;
?>