$(document).ready(function(){
    $("#check").click(function(){
        var sex = $('input:radio[name="sex"]:checked').val();
        var chonglou = $('input:radio[name="chonglou"]:checked').val();
        var postData = {"sex": sex, "chonglou": chonglou};
        console.log($('input:radio:checked').val());
        $.ajax({
            url:'http://47.102.140.114/TL_changyige/welcome.php',//目的php文件
            data: postData,//传输的数据
            type:'post',//数据传送的方式post
            dataType:'json',//数据传输的格式是json
            success:function(response){
            //数据给后端php文件并成功返回
                console.log(response);//打印返回的值
            } ,
            error:function(response){
            //数据给后端后返回错误
                console.log(response);//打印返回的信息
            }
        })
    })
});