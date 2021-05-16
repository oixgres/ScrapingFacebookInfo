<?php

require_once 'connection.php';

$id = $_POST['idComment'];
$idPost = $_POST['idPost'];
$user = $_POST['name'];
$text = $_POST['content'];

$query = "INSERT INTO Comentarios (idComentarios, Post_idPost, Persona, Texto) VALUES ('$id','$idPost','$user','$text')";
mysqli_query($conn, $query);

mysqli_close($conn);
?>