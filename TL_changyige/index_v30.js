$(document).ready(function(){

    $("#back2top").click(function(){
        $('body,html').animate({scrollTop: $("#header").offset().top},800);
    });

    ride_dict = {'a': "沧澜羽翼" , 'b': "金羽", 'c':"梦灵仙驹", 'd':"青翼战龙", 'e': "添福锦鳞", 'f':"水碧飞鸢", 'g':"绒雪神牛", 'h':"黑天马", 'i':"紫电", 'j':"月白龙马", 'k':"四喜送鲤台", 'l':"绝云焱龙", 'm':"熔岩魔犀", 'n':"绛紫飞鸢", 'o':"梦幻仙驹", 'p':"霸世羽龙"}

    attribute_dict = {"0": "image/冰.bmp", "1": "image/火.bmp", "2": "image/玄.bmp", "3": "image/毒.bmp"};
    menpai_dict = {"0": "少林","1":"明教", "2":"丐帮", "3": "武当", "4":"峨嵋", "5": "星宿", "6":"天龙", "7": "天山", "8": "逍遥", "9": "慕容", "10": "唐门", "11": "鬼谷"};
    sex_dict = {"0": "女", "1": "男"};
    tl_link = "http://tl.cyg.changyou.com/goods/char_detail?serial_num=";
    //表头
    tableColumns = [
        {
            field: "menpai",
            title: "门派",
            formatter: function(value, row, index) {
                return menpai_dict[value];
            }       
        },
        {
            field: "sex",
            title: "性别",
            formatter: function(value, row, index){
                return sex_dict[value];
            }             
        },
        {
            field: "rank",
            title: "等级",
            sortable: true 
        },
        {
            field: "score_equipment",
            title: "装备评分",
            sortable: true         
        },
        {
            field: "score_diamond",
            title: "宝石评分",
            sortable: true        
        },
        {
            field: "max_attack",
            title: "属性",
            sortable: true,  
            formatter: function(value, row, index){
                return "<img width=19px src=" + attribute_dict[row.max_attribute] + ">&nbsp;" + value;
            }  
        },
        {
            field: "blood",
            title: "血量",
            sortable: true
        },
        {
            field: "wuyi_level",
            title: "武意",
            sortable: true
        },
        {
            field: "price",
            title: "价格",
            sortable: true
        },
        {
            field: "ride",
            title: "坐骑",
            formatter: function(value, row, index){
                if (value == '0'){
                    return "无";
                }
                else{
                    res = "";
                    for(var i=0; i<value.length; i++)
                    {
                        res += ("<img src='image/坐骑/" + ride_dict[value[i]] + ".jpg' width=19px style='padding-right: 1px;' title='" + ride_dict[value[i]] + "'>");
                    }
                    return res;
                }
            }
        },
        {
            field: "id",
            title: "链接",
            formatter: function(value, row, index){
                return "<a target='_blank' href='" + tl_link + value + "'>购买</a>";
            }
        }
    ];


    //动态加载表格之前，先销毁表格
    $('#table').bootstrapTable('destroy');
    $("#table").bootstrapTable({ //表格初始化
        striped: true,
        showHeader : true,
        showColumns : true,
        columns: tableColumns,
        data: {},
        pagination: true,
        pageNumber: 1,
        pageSize: 25, 
        rowStyle: function (row, index) {
            //这里有5个取值代表5种颜色['active', 'success', 'info', 'warning', 'danger'];
            var strclass = "";
            if (row.chonglou == "1") {
                strclass = 'danger';
            }
            else {
                strclass = 'active';
            }
            return { classes: strclass }
        },
    });

    $("#check").click(function(){ 
        //确认post数据
        var menpai = [];
        $('input[name="menpai"]:checked').each(function(){//遍历每一个名字为menpai的复选框，其中选中的执行函数    
            menpai.push($(this).val());//将选中的值添加到数组menpai中    
        });
        if (menpai.length == 0)
            menpai.push("-1");
        else if (menpai.length > 1 && menpai[0] == "-1")
            menpai.shift();
        var sex = $('input:radio[name="sex"]:checked').val();
        var chonglou = $('input:radio[name="chonglou"]:checked').val();
        var price = $('input:radio[name="price"]:checked').val();
        var rank = $('input:radio[name="rank"]:checked').val();
        var score_equipment = $('input:radio[name="score_equipment"]:checked').val();
        var score_diamond = $('input:radio[name="score_diamond"]:checked').val();
        var blood = $('input:radio[name="blood"]:checked').val();
        var wuyi_level = $('input:radio[name="wuyi_level"]:checked').val();
        var ride = $('input:radio[name="ride"]:checked').val();
        var condition = $('input:radio[name="condition"]:checked').val();
        var postData = {
            "sex": sex, 
            "chonglou": chonglou, 
            "price": price, 
            "menpai": menpai,
            "rank": rank, 
            "score_equipment": score_equipment, 
            "score_diamond": score_diamond,
            "blood": blood,
            "wuyi_level": wuyi_level,
            "ride": ride,
            "condition": condition
        };

        console.log(postData);
        
        $.ajax({
            url:'http://47.102.140.114/TL_changyige/welcome_v2.php',//目的php文件
            data: postData,//传输的数据
            type:'post',//数据传送的方式post
            dataType:'json',//数据传输的格式是json
            success:function(response){
            //数据给后端php文件并成功返回
                console.log(response);//打印返回的值
                //处理服务器回传的数据

                //bootstrap-table 方法更新表格数据
                $('#table').bootstrapTable('destroy');
                $("#table").bootstrapTable({ //表格初始化
                    striped: true,
                    showHeader : true,
                    showColumns : true,
                    columns: tableColumns,
                    data: response,
                    pagination: true,
                    pageNumber: 1,
                    pageSize: 25, 
                    rowStyle: function (row, index) {
                        //这里有5个取值代表5种颜色['active', 'success', 'info', 'warning', 'danger'];
                        var strclass = "";
                        if (row.chonglou == "1") {
                            strclass = 'danger';
                        }
                        else {
                            strclass = 'active';
                        }
                        return { classes: strclass }
                    },
                });
            },
            error:function(response){
            //数据给后端后返回错误
                console.log(response);//打印返回的信息
            }
        })
    })
});