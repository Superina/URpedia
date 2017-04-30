<html>
<head>
<style>

table, th, td {
    border: 1px solid black;
}
</style>
</head>
    
    

<body>

<table>
    <tr>
        <th>field</th>
        <th>subfield_of</th>
    </tr>

<?php


$server  = mysql_connect("localhost","jshang5","iEXDfQqe");
$db      = mysql_select_db("jshang5",$server);
$query   = mysql_query("select * from Field");
while ($row = mysql_fetch_array($query)){

  echo "<tr>";
?>

  <td><form id="article" method="post" action="mainscreen2.php" >
        <input type="submit" name="Article" value="<?php echo $row['field'] ?>">
      </form>
  </td>
<?php
  echo "<td>".$row["subfield_of"]."</td>";
}



// $query1  = mysql_query("select field from Field where field='Algebra'");
// $query2  = mysql_query("select field from Field where field='Analysis'");
// $query3  = mysql_query("select field from Field where field='Chemistry'");
// $query4  = mysql_query("select field from Field where field='Complex Analysis'");
// $query5  = mysql_query("select field from Field where field='Computer Science'");
// $query6  = mysql_query("select field from Field where field='Data Science'");
// $query7  = mysql_query("select field from Field where field='Database Systems'");
// $query8  = mysql_query("select field from Field where field='Mathematics'");
// $query9  = mysql_query("select field from Field where field='Physics'");
// $query10 = mysql_query("select field from Field where field='Real Analysis'");
// $query11 = mysql_query("select field from Field where field='Theoretical Physics'");
// $query12 = mysql_query("select field from Field where field='Unspecified'");


// $row1 = mysql_fetch_array($query1);
// $row2 = mysql_fetch_array($query2);
// $row3 = mysql_fetch_array($query3);
// $row4 = mysql_fetch_array($query4);
// $row5 = mysql_fetch_array($query5);
// $row6 = mysql_fetch_array($query6);
// $row7 = mysql_fetch_array($query7);
// $row8 = mysql_fetch_array($query8);
// $row9 = mysql_fetch_array($query9);
// $row10 = mysql_fetch_array($query10);
// $row11 = mysql_fetch_array($query11);
// $row12 = mysql_fetch_array($query12);






?>




           
           

</table>
</body>
</html>