<?php

$servername = "localhost";//MySQL默认为localhost，端口号3306
$username = "root";
$password = "hc7783au";
$dbname = "tl";


// $array['sex'] = array();
// $array['chonglou'] = $_POST['chonglou'];
// $array['sex'] = $_POST['sex'];
// die(json_encode($array));

$connect = new mysqli($servername, $username, $password, $dbname);

// if($connect->connect_error)
// {
//     echo "连接失败！";
//     die("连接失败：". $connect->connect_error);
// }
// else{
//     echo "连接成功！";
// }

$sql = "SELECT id, score_equipment FROM goods";
$result = $connect->query($sql);


if ($result->num_rows > 0) {
    // 输出数据
    
    while($row = $result->fetch_assoc()) {
        // echo "列名1: " . $row["id"]. " 列名2: " . $row["score_equipment"]."<br>";
        $data = array('id'=>$row["id"], 'score_equipment'=>$row["score_equipment"]);
        die(json_encode($data));
        break;
    }
} else {
    echo "0 结果";
}
$connect->close();


?>