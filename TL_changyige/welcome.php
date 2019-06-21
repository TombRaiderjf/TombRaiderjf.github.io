<?php

$servername = "localhost";//MySQL默认为localhost，端口号3306
$username = "root";
$password = "hc7783au";
$dbname = "tl";

$connect = new mysqli($servername, $username, $password, $dbname);

if($connect->connect_error)
{
    die("连接失败：". $connect->connect_error);
}

$sql = "SELECT id, score_equipment FROM goods";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出数据
    while($row = $result->fetch_assoc()) {
        echo "列名1: " . $row["列名1"]. " 列名2: " . $row["列名2"]."<br>";
    }
} else {
    echo "0 结果";
}
$connect->close();


$array['sex'] = array();
$array['chonglou'] = $_POST['chonglou'];
$array['sex'] = $_POST['sex'];
die(json_encode($array));
?>