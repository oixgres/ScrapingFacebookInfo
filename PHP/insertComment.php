<?php

require_once 'connection.php';
require_once 'generalFunctions.php';

$id = $_POST['idComment'];
$idPost = $_POST['idPost'];
$user = $_POST['name'];
$text = $_POST['content'];

if(getFirstQueryElement($conn, 'comentario', 'id_comentario', 'id_comentario', $id))
{
  $query = "UPDATE comentario SET texto='$text' WHERE id_comentario='$id' AND id_post='$idPost'";
  $res = array('res' => "El comentario ".$id. " ha sido actualizado");
}
else
{
  $query = "INSERT INTO comentario (id_comentario, id_post, persona, texto) VALUES ('$id','$idPost','$user','$text')";
  $res = array('res' => "El comentario ".$id. " ha sido creado");
}

if(mysqli_query($conn, $query))
  echo json_encode($res);
else
  echo json_encode(array(
    'res' => 'ERROR',
    'error' => "ERROR AL AGREGAR COMENTARIO DEL USUARIO".$user."POST ".$idPost
  ));

mysqli_close($conn);
?>