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

$err = FALSE;

if($connect->connect_error)
{
    $err = TRUE;
    die("连接失败：". $connect->connect_error);
}

$sql = "SELECT id, score_equipment FROM goods";
$result = $connect->query($sql);


if ($result->num_rows > 0) {
    // 输出数据 
    $res = array();
    $count = 0;
    while ($row = $result->fetch_assoc()){
        // echo "列名1: " . $row["id"]. " 列名2: " . $row["score_equipment"]."<br>";
        $data = array(
            'id'=>$row["id"], 
            'sex'=>$row["sex"],
            'price'=>$row["price"],
            'menpai'=>$row["menpai"],
            'rank'=>$row["rank"],
            'score_equipment'=>$row["score_equipment"],
            'score_diamond'=>$row["score_diamond"],
            'blood'=>$row["blood"],
            'wuyi_level'=>$row["wuyi_level"]
        );     
        array_push($res, $data);
        $count = $count + 1;
    }
    die(json_encode($res));
}
else {
    echo "0 结果";
}
$connect->close();


?>