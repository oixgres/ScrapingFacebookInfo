<?php

function getFirstQueryElement($conn, $table, $item, $coincidence, $keyCoincidence){
  $query="SELECT $item FROM $table WHERE $coincidence=$keyCoincidence";

  $res = mysqli_query($conn, $query);
  $res = mysqli_fetch_array($res);
  return $res[0];
}
?>