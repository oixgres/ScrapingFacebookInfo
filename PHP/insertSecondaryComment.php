<?php

require_once 'connection.php';
require_once 'generalFunctions.php';

$idRespuesta = $_POST['fromId'];
$idPost = $_POST['postId'];
$user = $_POST['name'];
$text = $_POST['content'];
$idComentario =$_POST['toId'];
$persona_destino = $_POST['toName'];

if(getFirstQueryElement($conn, 'respuesta', 'id_respuesta', 'id_respuesta', $idRespuesta))
{
  $query = "UPDATE respuesta SET texto='$text', persona_destinada='$persona_destino' WHERE id_respuesta='$idRespuesta' AND id_post='$idPost'";
  $res = array('res' => "La respuesta ".$idRespuesta." ha sido actualizada");
}
else
{
  $query = "INSERT INTO respuesta (id_respuesta,id_comentario, persona,texto,persona_destinada,id_post) VALUES ('$idRespuesta','$idComentario','$user','$text','$persona_destino','$idPost')";
  $res = array('res' => "La respuesta ".$idRespuesta." ha sido creada");
}

if(mysqli_query($conn, $query))
  echo json_encode($res);
else
  echo json_encode(array(
    'res' => 'ERROR',
    'error' => 'ERROR AL AGREGAR RESPUESTA'
  ));


mysqli_close($conn);
?>