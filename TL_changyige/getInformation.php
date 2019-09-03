<?php
header('Access-Control-Allow-Origin: http://tombraiderjf.com');

$servername = "localhost";//MySQL默认为localhost，端口号3306
$username = "root";
$password = "hc7783au";
$dbname = "tl";

$connect = new mysqli($servername, $username, $password, $dbname);

$err = FALSE;

if($connect->connect_error)
{
    $err = TRUE;
    die("连接失败：". $connect->connect_error);
}

$sql = "SELECT * FROM information";


$result = $connect->query($sql);


if ($result->num_rows > 0) {
    // 输出数据 
    $res = array();
    $count = 0;
    while ($row = $result->fetch_assoc()){
        $data = array(
            'id'=>$row["id"], 
            'server'=>$row['server'],
            'sex'=>$row["sex"],
            'chonglou'=>$row["chonglou"],
            'price'=>$row["price"],
            'menpai'=>$row["menpai"],
            'rank'=>$row["rank"],
            'score_equipment'=>$row["score_equipment"],
            'score_diamond'=>$row["score_diamond"],
            'max_attack'=>$row["max_attack"],
            'max_attribute'=>$row["max_attribute"],
            'shending'=>$row["shending"],
            'blood'=>$row["blood"],
            'wuyi_level'=>$row["wuyi_level"],
            'clothes'=>$row["clothes"],
            'ride'=>$row["ride"],
            'contact'=>$row["contact"],
            'method'=>$row["method"]
        ); 
        array_push($res, $data);
        $count = $count + 1;
    }
    die(json_encode($res));
}
else {
    echo "-1";
}
$connect->close();


?>