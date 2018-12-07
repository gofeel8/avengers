<?php
session_start(); //세션시작에 실패하면 false 반환   에러시 무시: @sesison_start(); 또는 output_buffering=on인지 확인
?>

<!doctype html>
<html lang="en" dir="ltr">
<head>
<title>어벤져수</title>
<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="./css/style.css">
  <link href="css/bootstrap.min.css" rel="stylesheet">
<script src="http://maps.googleapis.com/maps/api/js?key=AIzaSyAuS-Y2hBFUahR8P21QbAADrJmBRJpkfqo"></script>
</head>

<body>
  <div id="grid2">
<a href="index.php">
<img src="./images/logo.png"  height="200px" width="500px" class="center">
</a>
  </div>

<div id="grid">
  <div id="login">

  <ul class="list-group">
    <li class="list-group-item"><a href="index.php"> 메인페이지</a></li>
    <li class="list-group-item"><a href="board.php"> 공지사항</a></li>
    <li class="list-group-item"><a href="menu.php">메뉴1</a></li>
    <li class="list-group-item"><a href="menu.php">메뉴2</a></li>
    <li class="list-group-item"><a href="menu.php">메뉴3</a></li>
    <li class="list-group-item"><a href='menu.php'>메뉴4</a></li>
  </ul>
  <div>
    <?php
    if(!isset($_SESSION['username']))
    {

     echo '<form  method="post" action="login.php" > <!--post로 login.php로 로그인정보 보냄-->
                 <div class="form-group">
               <label for="ID">ID : </label> <br/>
               <input type="text" class="form-control" id="ID" name="id" placeholder="ID를입력해주세요" /><br />

               </div>
               <label for="PASSWORD"> PASSWORD :</label> <br/>
               <input type="password"  class="form-control"  class="form-control" name="password" placeholder="비밀번호를입력해주세요"  /> <br />
               <input type="submit" value="로그인"  class="btn btn-info"/>
               <input type="button" name ="버튼" value="회원가입" class="btn btn-info" onclick="location.href=\'join.php\'";>
              </form>';

    }
    else
    {
      echo "<h3>".$_SESSION['username'].'님</h3><br>';
      echo '<input type="button" name ="button" value="로그아웃" class="btn btn-info" onclick="window.location.href=\'logout.php\'">';           //로그아웃 페이지 링크.

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
