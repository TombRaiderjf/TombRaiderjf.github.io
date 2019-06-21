<?php
$array['sex'] = array();
$array['chonglou'] = $_POST['chonglou'];
$array['sex'] = $_POST['sex'];
die(json_encode($array));
?>