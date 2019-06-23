$(document).ready(function(){
    var menpai_dict = {"0": "少林","1":"明教", "2":"丐帮", "3": "武当", "4":"峨嵋", "5": "星宿", "6":"天龙", "7": "天山", "8": "逍遥", "9": "慕容", "10": "唐门", "11": "鬼谷"};
    sex_dict = ["女", "男"];
    $("#check").click(function(){
        var menpai = [];
        $('input[name="menpai"]:checked').each(function(){//遍历每一个名字为menpai的复选框，其中选中的执行函数    
            menpai.push($(this).val());//将选中的值添加到数组menpai中    
        });
        var sex = $('input:radio[name="sex"]:checked').val();
        var chonglou = $('input:radio[name="chonglou"]:checked').val();
        var price = $('input:radio[name="price"]:checked').val();
        var rank = $('input:radio[name="rank"]:checked').val();
        var score_equipment = $('input:radio[name="score_equipment"]:checked').val();
        var score_diamond = $('input:radio[name="score_diamond"]:checked').val();
        var blood = $('input:radio[name="blood"]:checked').val();
        var wuyi_level = 100;
        var postData = {
            "sex": sex, 
            "chonglou": chonglou, 
            "price": price, 
            "menpai": menpai,
            "rank": rank, 
            "score_equipment": score_equipment, 
            "score_diamond": score_diamond,
            "blood": blood,
            "wuyi_level": wuyi_level
        };

        console.log(postData);
        
        $.ajax({
            url:'http://47.102.140.114/TL_changyige/welcome.php',//目的php文件
            data: postData,//传输的数据
            type:'post',//数据传送的方式post
            dataType:'json',//数据传输的格式是json
            success:function(response){
            //数据给后端php文件并成功返回
                console.log(response);//打印返回的值
                var tempHtml = "";
                for(var i = 0; i< response.length; i++)
                {
                    tempHtml += "<tr>";
                    tempHtml += ("<td>" + menpai_dict[response[i]["menpai"]] + "</td>");
                    tempHtml += ("<td>" + sex_dict[response[i]["sex"]] + "</td>");
                    tempHtml += ("<td>" + response[i]["score_equipment"] + "</td>");
                    tempHtml += ("<td>" + response[i]["diamond_equipment"] + "</td>");
                    tempHtml += "<td>10000</td>";
                    tempHtml += ("<td>" + response[i]["blood"] + "</td>");
                    tempHtml += ("<td>" + response[i]["wuyi_level"] + "</td>");
                    tempHtml += ("<td>" + response[i]["price"] + "</td>")
                    var url = "http://tl.cyg.changyou.com/goods/char_detail?serial_num=" + response[i]["id"];
                    tempHtml += ("<td><a href=" + url + "></a></td>");
                    tempHtml += "</tr>";
                }
                $("#table tbody").append(tempHtml);
            },
            error:function(response){
            //数据给后端后返回错误
                console.log(response);//打印返回的信息
            }
        })
    })
});