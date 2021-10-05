<?php
require_once 'connection.php';
require_once 'generalFunctions.php';

$id_post = $_POST['id_post'];
$id_group = $_POST['id_group'];
$url = $_POST['url'];
$user = $_POST['user'];
$text = $_POST['text'];

if(getFirstQueryElement($conn, 'post', 'id_post', 'id_post', $id_post))
{
  $query = "UPDATE post SET url='$url', persona='$user', texto='$text' WHERE id_post='$id_post'";
  $res = array('res' => "El post ".$id_post. " ha sido actualizado");
}
else
{
  $query = "INSERT INTO post(id_post, url, persona, texto) VALUES ('".$id_post."', '".$url."', '".$user."', '".$text."')";
  $res = array('res' => "El post ".$id_post." ha sido creado");
}

if(mysqli_query($conn, $query))
  echo json_encode($res);
else
  echo json_encode(array(
    'res' => 'ERROR',
    'error' => "ERROR AL AGREGAR POST ".$id_post
  ));

mysqli_close($conn);
?>