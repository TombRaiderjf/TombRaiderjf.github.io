<?php
header('Access-Control-Allow-Origin:http://tl.cyg.changyou.com');

$id = $_POST['id'];
$number = $_POST['number'];
$image = $_POST['image'];
$servername = "localhost";//MySQL默认为localhost，端口号3306
$username = "root";
$password = "hc7783au";
$dbname = "captcha";

$connect = new mysqli($servername, $username, $password, $dbname);

if($connect->connect_error)
{
    $err = TRUE;
    die("连接失败：". $connect->connect_error);
}

$sql = "INSERT INTO image (id, number) VALUES (".$id.", '".$number."')";

if (mysqli_query($connect, $sql)) {
    // echo "success to add data ". ;
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($connect);
}

$connect->close();

# 存图片

$img_decode = base64_decode($image);
$file_name = "./captcha/".$id.".jpg";
if(file_put_contents($file_name, $img_decode))
{
    echo "success to store image!";
}
else{
    echo "fail to store image!";
}

?>