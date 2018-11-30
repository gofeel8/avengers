<?php
// include"session.php";   //session.php파일을 포함
session_start(); //세션시작에 실패하면 false 반환   에러시 무시: @sesison_start(); 또는 output_buffering=on인지 확인
	require_once("./db_info.php");

?>

<!doctype html>
<html lang="en" dir="ltr">
<head>
<title>어벤져스</title>
<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="./css/style.css">
  <link href="css/bootstrap.min.css" rel="stylesheet">
<script src="http://maps.googleapis.com/maps/api/js?key=AIzaSyAuS-Y2hBFUahR8P21QbAADrJmBRJpkfqo"></script>


</head>

<body>
  <div id="grid2">
<a href="login.php">
<img src="./images/logo.png"  height="200px" width="500px" class="center">
</a>
  </div>

<div id="grid">
  <div id="login">

  <ul class="list-group">
		<li class="list-group-item"><a href="index.php"> 메인페이지</a></li>
    <li class="list-group-item"><a href="board.php"> 공지사항</a></li>
    <li class="list-group-item"><a href="map.php">메뉴1</a></li>
    <li class="list-group-item"><a href="map.php"> 메뉴2</a></li>
    <li class="list-group-item"><a href="map.php"> 메뉴3</a></li>
    <li class="list-group-item"><a href='menu.php'>메뉴4</a></li>

  </ul>
  <div>

    <?php

    $memberId = $_POST['id'];
    $memberPw = $_POST['password'];
    $sql = "SELECT * FROM avengers_member WHERE id = '$memberId' AND pwd = '$memberPw'"; //my sqli 연결의 끈을 생성시키고, 쿼리를 실행
      //고른다 모든것 member테이블로부터 id와 pwd가 일치하는 것을
    $res = $conn->query($sql); //실행결과는 $res에 저장
    $row = $res->fetch_array(MYSQLI_ASSOC); // 넘어온 결과를 한 행씩 패치해서 $row라는 배열에 담는다.
if(!isset($_SESSION['username']))
{
  if ($row != null) {                                                 //만약 배열에 존재한다면

    $_SESSION['username'] = $row['name'];                           // 세션을 만들어준다.
    echo "<h3>".$_SESSION['username'].'님</h3><br>';
    // echo '<a href="logout.php" >로그아웃 하기</a>';           //로그아웃 페이지 링크.
    echo '<input type="button" name ="button" value="로그아웃" class="btn btn-info" onclick="window.location.href=\'logout.php\'">';           //로그아웃 페이지 링크.
    // <input type=\"button\" name =\"버튼\" value=\"로그아웃\" class=\"btn btn-info\" onclick=\"location.href=\'logo.php\'\";>

  }

  else if($row == null){

    echo "<script>alert(\"id or pw error\"); window.location.replace(\"index.php\");</script>";
    // header('Location:index.php');

  }
}
else
{
  echo "<h3>".$_SESSION['username'].'님</h3><br>';
  echo '<input type="button" name ="button" value="로그아웃" class="btn btn-info" onclick="window.location.href=\'logout.php\'">';           //로그아웃 페이지 링크.

  // echo '<a href="logout.php" >로그아웃 하기</a>';           //로그아웃 페이지 링크.
  // echo " <input type=\"button\" name =\"버튼\" value=\"로그아웃\" class=\"btn btn-info\" onclick=window.location.replace(\"index.php\");>";           //로그아웃 페이지 링크.

}

    ?>

  </div>
</div>
<div id="article">
<h2>메인페이지입니다</h2>

	</div>
  </div>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
 <script src="js/bootstrap.js"></script>
  </body>
  </html>
