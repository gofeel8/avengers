<?php
session_start();
require_once("./db_info.php");
  $bNo = $_GET['bno'];
	if(!empty($bNo)) {
		$sql = 'UPDATE avengers_crawling set see = see + 1 where id = ' . $bNo;
    $result=mysqli_query($conn,$sql);
		if(empty($result)) {
			?>
			<script>
				alert('오류가 발생했습니다.');
				history.back();
			</script>
			<?php
		}
	}
  $sql ='SELECT title,com,day,info,img,page,see from avengers_crawling where id = ' . $bNo;
  $result=mysqli_query($conn,$sql);
  $row=mysqli_fetch_array($result);
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>공모전</title>
<link rel="stylesheet" href="./css/style.css">
<link href="css/layout.css" rel="stylesheet" type="text/css" media="all">
<link href="css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="./css/board.css" />

</head>

<body>
  <div id="grid2">
<a href="index.php">
<img src="images/logo.png"  height="200px" width="500" class="center">
</a>
  </div>

<div id="grid">
  <div id="login">
    <ul class="list-group">
      <li class="list-group-item"><a href="index.php"> 메인페이지</a></li>
      <li class="list-group-item"><a href="board.php"> 공지사항</a></li>
      <li class="list-group-item"><a href="crawling.php">공모전</a></li>
    </ul>
  <div id="jb-sidebar-right">
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

<article class="boardArticle">
<h3>공지사항</h3>
<div id="boardView">
  <h3 id="boardTitle"><?php echo $row['title']?></h3>

  <div class="poster-holder">
<a href="<?php echo $row['img']; ?>">
    <img src="<?php echo $row['img']; ?>" alt="공모전">
</a>
<table class="type-5">
  <colgroup>
  <col style="width:100px;">
  <col style>
  </colgroup>

  <tbody>
    <tr>
      <th scope="row">
        작성자</th>
      <td>관리자</td>
    </tr>
    <tr>
      <th scope="row">
        조회수</th>
      <td><?php echo $row['see']?></td>
    </tr>
    <tr>
      <th scope="row">
        주최</th>
      <td><?php echo $row['com']?></td>
    </tr>
    <tr>
      <th scope="row">
        기간</th>
      <td><?php echo $row['day']?></td>
    </tr>
    <tr>
      <th scope="row">
        홈페이지</th>
      <td>
      <a href="<?php echo $row['page']?>"><?php echo $row['page']?></a></td>
    </tr>
  </tbody>
</table>
</div>


<br><br>
<div id="boardInfo">
<?php echo $row['info'] ?>
</div>
<div id="boardContent"><?php echo $row['comment']?></div>
<?php
  if(isset($_SESSION['username'])&&$_SESSION['username'] == $row['user']){
 ?>
<div  style="float: right;">
  <form action="./write.php" method="get"class="inlineform">
    <input type="hidden" name="bno" value="<?php echo $bNo;?>">
    <button type="submit" class="btnSubmit btn">수정</button>
  </form>
  &nbsp;
<form action="./delete_update.php" method="post" class="inlineform">
  <input type="hidden" name="bno" value="<?php echo $bNo;?>">
  <button type="submit" class="float-right btn text-white btn-danger">삭제</button>
</form>
</div>

<?php
}
 ?>
<div id="boardComment">
  <?php require_once('./comment.php')?>
</div>
</div>
</div>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script src="js/bootstrap.js"></script>
</article>


</body>
</html>
