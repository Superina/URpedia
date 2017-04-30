<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js" type="text/javascript"></script>
        <style type="text/css">
            tr.header
  {
    font-weight:bold;
  }
            tr.alt
            {
	      background-color: #777777;
            }
        </style>
        <script type="text/javascript">
	      $(document).ready(function(){
		  $('.striped tr:even').addClass('alt');
		});
        </script>
        <title></title>
    </head>
    <body>



<?php

$server = mysql_connect("localhost","cperkin5","=8QYd#2T");
$db =  mysql_select_db("cperkin5",$server);

$maxID = mysql_query("SELECT MAX(id) FROM Article");
$rowID = mysql_fetch_row($maxID);
$id = $rowID[0]+1;

$title = $_POST['title'];
$creator = $_COOKIE["username"];
$editing_level = (int)$_POST['editing_level'];
$category = $_POST['category'];
$body = $_POST['body'];
$last_edited = date('Y-m-d');


$server = mysql_connect("localhost","cperkin5","=8QYd#2T");
$db =  mysql_select_db("cperkin5",$server);
$query = mysql_query("INSERT INTO Article (id,title,last_edited,editing_level,creator,belongs_to,content) 
    VALUES ('$id','$title','$last_edited','$editing_level','$creator','$category','$body')");
mysql_query($query) or die("Error:".mysql_error());
//$numberChange = mysqli_affected_rows($query);

/*if ($outcome===true) {
    print "sucess!";
}

else {
    echo 'There is an error'. $error ."<br />\n";

}*/

?>
</body>
</html>