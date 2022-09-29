<!DOCTYPE html> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Biological database</title>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>  
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />  
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  
    <link rel="stylesheet" href="style5.css" />  
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>  
    
</head>

<body>
<div class="w3-top">
  <div class="w3-bar w3-deep-purple w3-card w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" href="javascript:void(0);" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
    <a href="dbname.html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white" text-decoration="none">Home</a>
    <a href="table.php" class="w3-bar-item w3-button w3-padding-large w3-white">Database</a>
    <a href="columns.html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">About</a>
  </div>

  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium w3-large">
    <a href="dbname.html" class="w3-bar-item w3-button w3-padding-large">About Databases</a>
    <a href="columns.html" class="w3-bar-item w3-button w3-padding-large">About Columns</a>
    <a href="table.php" class="w3-bar-item w3-button w3-padding-large">Database</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 4</a>
  </div>
</div>
<header class="w3-container w3-purple w3-center" style="padding: 70px 50px 16px">
  <h2 class="w3-margin w3-xxlarge">AntiJournal</h2>
  <p class="w3-xlarge">Database for Antigens</p>
</header>
<?php
 $dbhost = "localhost";
 $dbuser = "root";
 $dbpass = "";
 $db = "antigen_db";
 $conn = new mysqli($dbhost, $dbuser, $dbpass,$db,4000) ;
 
 if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
  session_start();
?>

<div class="searchdiv">
  <br>
<h2>Filter</h2> 
<form id="search_form" name="search_form1" method="POST" action="table.php" >
<div class="flex-container">
        <div class="column">
        
           <span class="input_h" >UniProt ID</span> <input type="text" name="UniProt_ID" value=""/> <br>
           <span class="input_h"> Name  </span><input type="text" name="Entry_Name" value=""/> <br>
           <span class="input_h"> Status</span> <input type="text" name="status" value=""/> <br>
           <span class="input_h"> Protein Name </span><input type="text" name="Protein_Name" value=""/> <br>


</div>
<div class="column bg-alt ">
           <span class="input_h" >Gene Name</span><input type="text" name="Gene_Name" value=""/><br>
           <span class="input_h" >Organism</span> <input type="text" name="Organism" value=""/><br>
           <span class="input_h" >Sequence Length</span><input type="text" name="Seq_Length" value=""/> <br>
           </div>
    </div>
 <div class="container">
  
 <br><br>
 <div class="row">
 <div class="col d-flex justify-content-center w3-padding-24">
            <br> <input type="submit" name="search" value="Search" class="search_button">
 </div>
</div>
<br><br>
<div class="row">
 <div class="col d-flex justify-content-center w3-padding">
            <input type="reset" name="reset" value="Reset" class="reset_button">
 </div>
</div>
</div>
</div>

</form><br>
</div>

<div class="center  table justify-content-center">
<?php
if (isset($_POST['search'])) {
  $search_term_id = !empty($_POST['UniProt_ID']) ? mysqli_real_escape_string($conn,$_POST['UniProt_ID']) : 'no_entry';
  $search_term_name = !empty($_POST['Entry_Name']) ? mysqli_real_escape_string($conn,$_POST['Entry_Name']) : 'no_entry';
  $search_term_status = !empty($_POST['status']) ? mysqli_real_escape_string($conn,$_POST['status']) : 'no_entry';
  $search_term_pname = !empty($_POST['Protein_Name']) ? mysqli_real_escape_string($conn,$_POST['Protein_Name']) : 'no_entry';
  $search_term_gname = !empty($_POST['Gene_Name']) ? mysqli_real_escape_string($conn,$_POST['Gene_Name']) : 'no_entry';
  $search_term_organism = !empty($_POST['Organism']) ? mysqli_real_escape_string($conn,$_POST['Organism']) : 'no_entry';
  $search_term_seqlen = !empty($_POST['Seq_Length']) ? mysqli_real_escape_string($conn,$_POST['Seq_Length']) : 'no_entry';

  $sql = "SELECT `UniProt_ID`, `Entry_Name`, `Status`,`Protein_Name` , `Gene_Name`, `Organism`, `Seq_Length` , `UniProt_Link` FROM mytable
   as TableC  WHERE
  
  (TableC.`UniProt_ID` like '%{$search_term_id}%' OR '$search_term_id'='no_entry') 
  AND (TableC.`Entry_Name` like '%{$search_term_name}%' OR '$search_term_name'='no_entry' )  
  AND (TableC.`Status` like '{$search_term_status}%' OR '$search_term_status'='no_entry') 
  AND (TableC.`Protein_Name` like '%{$search_term_pname}%' OR '$search_term_pname'='no_entry' )  
  AND (TableC.`Gene_Name` like '%{$search_term_gname}%' OR '$search_term_gname'='no_entry' )  
  AND (TableC.`Organism` like '%{$search_term_organism}%' OR '$search_term_organism'='no_entry' )  
  AND (TableC.`Seq_Length` like '%{$search_term_seqlen}%' OR '$search_term_seqlen'='no_entry')";
  $result = $conn->query($sql);
}

  



if($result){
if ($result->num_rows != 0) {
  echo 'No. of results:'. $result->num_rows;
  echo "<table class='table' ><tr><th> UniProt ID </th><th> Name </th>&nbsp&nbsp<th>Status</th><th>Protein Name</th><th>Gene Name</th><th>Organism</th><th>Sequence Length</th><th>UniProtLink</th></tr>";
  // output data of each row
  while($row = $result->fetch_assoc()) {

    echo "<tr><td>&nbsp&nbsp".$row["UniProt_ID"]."</td>&nbsp&nbsp&nbsp<td>&nbsp&nbsp".$row["Entry_Name"]."</td>&nbsp&nbsp&nbsp<td>".$row["Status"]."</td><td>&nbsp&nbsp&nbsp&nbsp".$row["Protein_Name"]."</td>
      <td>&nbsp&nbsp&nbsp&nbsp".$row["Gene_Name"]."<td>&nbsp&nbsp&nbsp&nbsp".$row["Organism"]."</td><td>&nbsp&nbsp&nbsp&nbsp".$row["Seq_Length"]."</td>
    <td>&nbsp&nbsp&nbsp&nbsp".$row["UniProt_Link"]."</td></tr>";
  }

  echo "</table>";
} else {
  echo "0 results";
}
}
else{
    echo ("Error description: " . mysqli_error($conn));
}
 
$conn->close();
?> 
</div>
</body>
</html>
