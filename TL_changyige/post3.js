$(document).ready(function(){

    function valid(str) { 
        return /^\w+$/.test(str); 
    }

    $("#submit").click(function(){
        var id = $("#id").val();
        
        var method = $("#method").val();
        
        var contact = $("#contact").val();
        
        if (id == '' || contact == ''){
            alert("不能为空！");
            return;
        }
        if (!valid(contact)){
            alert("联系方式输入格式错误！");
            return;
        }
        console.log(id, method, contact);
        if (!$("#agree").is(":checked")){
            alert("请勾选许可！");
            return;
        }
        var postData = {'id': id, 'method': method, 'contact': contact};
        $.ajax({
            url: "http://47.102.140.114/TL_changyige/addInfo.php",
            data: postData,//传输的数据
            type:'post',//数据传送的方式post
            dataType:'text',//数据传输的格式是json
            success: function(response){
                console.log(response);
                if(response == "success"){
                    alert("提交成功！");
                }
                else{
                    alert("提交失败，请检查商品号是否正确或重复！");
                }
            },
            error: function(response){
                console.log(response);
            }
        });
    });
    
});