<?php
require_once 'connection.php';
require_once 'generalFunctions.php';

$id = $_POST['id'];
$url = $_POST['url'];
$user = $_POST['user'];
$text = $_POST['text'];

if(getFirstQueryElement($conn, 'post', 'id_post', 'id_post', $id))
{
  $query = "UPDATE post SET url='$url', persona='$user', texto='$text' WHERE id_post='$id'";
  $res = array('res' => "El post ".$id. " ha sido actualizado");
}
else
{
  $query = "INSERT INTO post(id_post, url, persona, texto) VALUES ('".$id."', '".$url."', '".$user."', '".$text."')";
  $res = array('res' => "El post ".$id." ha sido creado");
}

if(mysqli_query($conn, $query))
  echo json_encode($res);
else
  echo json_encode(array(
    'res' => 'ERROR',
    'error' => "ERROR AL AGREGAR POST ".$id
  ));

mysqli_close($conn);
?>