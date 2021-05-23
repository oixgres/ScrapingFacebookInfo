<?php 
require_once 'connection.php';

$id = $_POST['idPost'];
$type = $_POST['tipo'];
$user = $_POST['persona'];

$query = "INSERT INTO reaccion (tipo, persona, id_post) VALUES ('$type', '$user', '$id')";
mysqli_query($conn, $query);

mysqli_close($conn);

echo $user." ".$type;

?>