<html>
<head>
    <meta charset="utf-8">
    <title>乘法表</title>
    <script type="text/javascript">
    function getvalue(){
    var n=document.getElementById("a1").value;
    if (n>0&&n<10) {
    document.write("<table style=background-color:#ffff99;width:200px;height:200px;'>");//这里需要一个table标签，样式表可以直接写标签后面
    for (var i=1;i<=n;i++) {
    document.write('<tr>');
    for (var j=1;j<=i;j++){
    document.write('<td style="border:#CC0000 1px solid;width:20px;height:20px;">'+i+'*'+j+'='+i*j+'</td>'); 
    }
    document.write('</tr>');
    }
    document.write('</table>');
    } 
    else alert("请输入1-9之间的数字！")
    }
    </script>
    <style>
    </style>
</head>
<body>
    <input type="text" id="a1" placeholder="请输入数字1-9">
    <input type="button" value="生成乘法表" onclick="getvalue()">
</body>
</html>
