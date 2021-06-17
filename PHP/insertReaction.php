<?php 
require_once 'connection.php';
require_once 'generalFunctions.php';


$id = $_POST['idPost'];
$type = $_POST['tipo'];
$user = $_POST['persona'];

if(getFirstQueryElement_multiCoincidencies($conn, 'reaccion', 'id_reaccion', "id_post='$id' AND persona='$user'"))
{
  $query = "UPDATE reaccion SET tipo='$type' WHERE persona='$user' AND id_post='$id'";
  $res = array('res' => "La reaccion del usuario ".$user." en el post ".$id." ha sido actualizada");

}
else
{
  $query = "INSERT INTO reaccion (tipo, persona, id_post) VALUES ('$type', '$user', '$id')";
  $res = array('res' => "La reaccion del usuario ".$user." en el post ".$id." ha sido creada");
}

if(mysqli_query($conn, $query))
  echo json_encode($res);
else
echo json_encode(array(
  'res' => 'ERROR',
  'error' => "ERROR AL AGREGAR REACCION DEL USUARIO ".$user." DEL POST ".$id
));

mysqli_close($conn);

?>