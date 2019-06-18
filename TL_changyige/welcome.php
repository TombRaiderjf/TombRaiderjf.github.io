<?php
$array['age'] = array();
$array['name'] = $_POST['name'];
$array['age'] = $_POST['age'];
$array['height'] = $_POST['height'];
die(json_encode($array));
?>