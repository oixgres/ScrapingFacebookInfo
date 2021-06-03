<?php 

require_once 'connection.php';
require_once 'generalFunctions.php';


$id = $_POST['idPost'];
$user = $_POST['persona'];

// if(getFirstQueryElement($conn, 'visto', 'id_post', 'id_post', $id) && getFirstQueryElement($conn, 'visto', 'persona', 'persona', $user))
if(getFirstQueryElement_multiCoincidencies($conn, 'visto', 'id_visto', "id_post='$id' AND persona='$user'"))
{
  $res = array('res' => "Ya existia registro de que el usuario ".$user." vio el post ".$id);
  echo json_encode($res);
}
else
{
  $query = "INSERT INTO visto (id_post, persona) VALUES ('$id', '$user')";
  $res = array('res' => "El usuario ".$user." vio el post ".$id);

  if(mysqli_query($conn, $query))
    echo json_encode($res);
  else
    echo json_encode(array(
      'res' => 'ERROR',
      'error' => 'ERROR AL AGREGAR VISTO'
    ));
}

mysqli_close($conn);
?>