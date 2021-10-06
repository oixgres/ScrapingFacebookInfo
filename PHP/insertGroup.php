<?php 
require_once 'connection.php';
require_once 'generalFunctions.php';

$url = $_POST['url'];
$name = $_POST['name'];

$id = $_POST['id'];

if(!getFirstQueryElement($conn, 'grupo', 'id_grupo' ,'id_grupo', $id))
{
    $query = "INSERT INTO grupo (id_grupo,url, nombre) VALUES ('$id','$url', '$name')";
    $res = array('res' => "El grupo ".$name." ha sido creado" );

    if(mysqli_query($conn, $query))
      echo json_encode($res);
    else
        echo json_encode(array(
            'res'=>'ERROR',
            'error'=>"ERROR AL AGREGAR GRUPO ".$id."" 
        ));
}
else
  echo json_encode(array(
    'res' => "El grupo ".$name." ya habia sido ingresado"
  ));
mysqli_close($conn)

?>