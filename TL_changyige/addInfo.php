<?php
// 处理提交的发布信息请求
header('Access-Control-Allow-Origin:http://tombraiderjf.com');
$output = exec("python addInfo.py {$_POST['id']} {$_POST['method']} {$_POST['contact']}", $out, $res);
if($res == 0){
    echo 'success';
}
else{
    echo 'error';
}

?>