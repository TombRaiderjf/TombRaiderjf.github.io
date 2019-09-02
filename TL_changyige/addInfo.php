<?php
// 处理提交的发布信息请求
header('Access-Control-Allow-Origin:http://tombraiderjf.com');
// echo  '-1';
$id = $_POST['id'];
$method = $_POST['method'];
$contact = $_POST['contact'];
// echo $id;
// $output = system("python addInfo.py {$id} {$method} {$contact}");
$output = shell_exec("python addInfo.py 201908201331248636 1 21314542");
echo "-1";
// echo $output;
// $array = explode(',', $output);
// echo $array;

?>