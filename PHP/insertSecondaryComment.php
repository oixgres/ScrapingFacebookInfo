<?php

require_once 'connection.php';

$idRespuesta = $_POST['fromId'];
$idPost = $_POST['postId'];
$user = $_POST['name'];
$text = $_POST['content'];
$idComentario =$_POST['toId'];
$persona_destino = $_POST['toName']


$query = "INSERT INTO respuesta (id_respuesta,id_comentario, persona,texto,persona_destino,id_post) 
        VALUES ('$idRespuesta','$idComentario','$user','$text',$persona_destino,,$idPost)";
if(mysqli_query($conn, $query)){
    echo mysqli_insert_id($conn)
}else{
    echo:"error : no se pudo crear respuesta"
}

mysqli_close($conn);

echo $text;
?>