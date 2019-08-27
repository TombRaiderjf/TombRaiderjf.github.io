<?php
header('Access-Control-Allow-Origin:http://tombraiderjf.com');

$chonglou = $_POST["chonglou"];
$sex = $_POST["sex"]; 
$price = $_POST["price"];
$menpai = $_POST["menpai"];
$rank = $_POST["rank"];
$score_equipment = $_POST["score_equipment"];
$score_diamond = $_POST["score_diamond"];
$blood = $_POST["blood"];
$wuyi_level = $_POST["wuyi_level"];
$clothes = $_POST["clothes"];
$ride = $_POST["ride"];
$condition = $_POST["condition"];

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

$sql = "SELECT * FROM goods";
if ($condition == "0"){
    $sql = $sql." where sale=0";
}
else{
    $sql = $sql." where sale=1";
}

$temp = 0;

if ($ride != "-1"){
    if ($temp == 0){
        $sql = $sql." where ";
        $temp = 1;
    }
    else
        $sql = $sql." and ";
    if ($ride == "1"){
        $sql = $sql."ride<>'0'";
    }
    else{
        $sql = $sql."ride='0'";
    }
}


if ($clothes != "-1"){
    if ($temp == 0){
        $sql = $sql." where ";
        $temp = 1;
    }
    else
        $sql = $sql." and ";
    if ($clothes == "1"){
        $sql = $sql."clothes<>'0'";
    }
    else{
        $sql = $sql."clothes='0'";
    }
}

if ($score_diamond != "0"){
    if ($temp == 0){
        $sql = $sql." where ";
        $temp = 1;
    }
    else
        $sql = $sql." and ";
    $sql = $sql."score_diamond>=".$score_diamond;
}
if ($score_equipment != "10000000"){
    if ($temp == 0){
        $sql = $sql." where ";
        $temp = 1;
    }
    else
        $sql = $sql." and ";
    $sql = $sql."score_equipment<=".$score_equipment;
}
if ($price != "1000000"){
    if ($temp == 0){
        $sql = $sql." where ";
        $temp = 1;
    }
    else
        $sql = $sql." and ";
    $sql = $sql."price<=".$price;
}
if ($blood != "0"){
    if ($temp == 0){
        $sql = $sql." where ";
        $temp = 1;
    }
    else
        $sql = $sql." and ";
    $sql = $sql."blood>=".$blood;
}
if ($wuyi_level != "0"){
    if ($temp == 0){
        $sql = $sql." where ";
        $temp = 1;
    }
    else
        $sql = $sql." and ";
    $sql = $sql."wuyi_level>=".$wuyi_level;
}
if ($sex != "-1"){
    if ($temp == 0){
        $sql = $sql." where ";
        $temp = 1;
    }
    else
        $sql = $sql." and ";
    $sql = $sql."sex=".$sex;
}
if ($chonglou != "-1"){
    if ($temp == 0){
        $sql = $sql." where ";
        $temp = 1;
    }
    else
        $sql = $sql." and ";
    $sql = $sql."chonglou=".$chonglou;
}
$result = $connect->query($sql);


if ($result->num_rows > 0) {
    // 输出数据 
    $res = array();
    $count = 0;
    while ($row = $result->fetch_assoc()){
        $data = array(
            'id'=>$row["id"], 
            'sex'=>$row["sex"],
            'chonglou'=>$row["chonglou"],
            'price'=>$row["price"],
            'menpai'=>$row["menpai"],
            'rank'=>$row["rank"],
            'score_equipment'=>$row["score_equipment"],
            'score_diamond'=>$row["score_diamond"],
            'max_attack'=>$row["max_attack"],
            'max_attribute'=>$row["max_attribute"],
            'blood'=>$row["blood"],
            'wuyi_level'=>$row["wuyi_level"],
            'clothes'=>$row["clothes"],
            'ride'=>$row["ride"]
        ); 
        if ($rank == "0")
        {
            if ($data['rank']>89)
                continue;
        }
        else if($rank == "1"){
            if($data['rank']<90 or $data['rank']>99)
                continue;
        }
        else if($rank == "2"){
            if($data['rank']<100 or $data['rank']>109)
                continue;
        }
        else if($rank == "3"){
            if($data['rank']<110)
                continue;
        }
        if ($menpai[0] != "-1"){
            $flag = 0;
            foreach($menpai as $value)
                if($value == $data['menpai'])
                    $flag = 1;
            if ($flag == 0)
                continue; 
        }
        array_push($res, $data);
        $count = $count + 1;
    }
    die(json_encode($res));
}
else {
    echo array();
}
$connect->close();


?>