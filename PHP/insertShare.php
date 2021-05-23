<?php 
require_once 'connection.php';

$id = $_POST['idPost'];
$user = $_POST['persona'];

$query = "INSERT INTO compartir (id_post, persona) VALUES ('$id', '$user')";
mysqli_query($conn, $query);

mysqli_close($conn);

echo $user;
?>