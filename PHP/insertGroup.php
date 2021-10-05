<?php 
require_once 'connection.php';
require_once 'generalFunctions.php';

$url = $_POST['url'];
$name = $_POST['name'];

$id = $_POST['id'];

if(!getFirstQueryElement($conn, 'group', 'id_group' ,'id_group', $id))
{
    $query = "INSERT INTO group (url, nombre) VALUES ('$url', '$name')";
    $res = array('msg' => "El grupo ".$name." ha sido creado" );
}

if(mysqli_query($conn, $query))
    echo json_encode($res);
else
    echo json_encode(array(
        'res'=>'ERROR',
        'error'=>'ERROR AL AGREGAR GRUPO'
    ));

mysqli_close($conn)

?>