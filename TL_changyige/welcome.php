<?php


$chonglou = $_POST["chonglou"];
$sex = $_POST["sex"]; 
$price = $_POST["price"];
$menpai = $_POST["menpai"];
$rank = $_POST["rank"];
$score_equipment = $_POST["score_equipment"];
$score_diamond = $_POST["score_diamond"];
$blood = $_POST["blood"];
$wuyi_level = $_POST["wuyi_level"];


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
if ($sex != "-1")
    $sql = $sql." where sex=".$sex;
if ($chonglou != "-1")
    $sql = $sql." chonglou=".$chonglou;

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
            'wuyi_level'=>$row["wuyi_level"]
        ); 
        // if ($sex == "-1" or (int)$sex == $data['sex'] ) {
            //if ($chonglou == "-1" or (int)$chonglou == $data['chonglou']){
                if ((int)$price >= $data['price']){
                    if ((int)$score_equipment >= $data['score_equipment']){
                        if ((int)$score_diamond <= $data['score_diamond']){
                            if ((int)$blood <= $data['blood']){
                                if((int)$wuyi_level <= $data['wuyi_level'])

                                    array_push($res, $data);
                            }
                                
                        }
                    }
                }
            //}
        // }
        $count = $count + 1;
    }
    die(json_encode($res));
}
else {
    echo "0 结果";
}
$connect->close();


?>