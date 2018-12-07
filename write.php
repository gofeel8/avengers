<?php
session_start();

	require_once("./db_info.php");

  	if(isset($_GET['bno'])) {
  		$bNo = $_GET['bno'];
  		$sql = 'SELECT title, comment, user from avengers_board where id = ' . $bNo;
  $result=mysqli_query($conn,$sql);
  $row=mysqli_fetch_array($result);
  	}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<title>공지사항</title>
  <link rel="stylesheet" href="./css/style.css">
  <link href="css/bootstrap.min.css" rel="stylesheet">

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
		    <li class="list-group-item"><a href="menu.php">메뉴1</a></li>
		    <li class="list-group-item"><a href="menu.php">메뉴2</a></li>
		    <li class="list-group-item"><a href="menu.php">메뉴3</a></li>
		    <li class="list-group-item"><a href='menu.php'>메뉴4</a></li>
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
		<h3>공지사항 글쓰기</h3>
		<div id="boardWrite">
			<form action="./write_update.php" method="post">
        <?php

      				if(isset($bNo)) {

      					echo '<input type="hidden" name="bno" value="' . $bNo . '">';

      				}
      				?>
        <table id="boardWrite">
					<caption class="readHide">글쓰기</caption>
					<tbody>
						<tr>
							<th scope="row"><label for="bID">아이디</label></th>
							<td class="id">
                <?php

              	echo $_SESSION['username'];

                              	// echo $row['user'];
                                ?>
                <!-- <input type="text" name="user" id="bID"></td> -->
                <input type="hidden" name="user" value="<?php echo $_SESSION['username']; ?>">
          	</tr>
						<tr>
							<th scope="row"><label for="bTitle">제목</label></th>
							<td class="title"><input type="text" name="title" style="width:100%;" id="bTitle"value="<?php echo isset($row['title'])?$row['title']:null?>"></td>
						</tr>
						<tr>
							<th scope="row"><label for="bContent">내용</label></th>
							<td class="content"><textarea name="comment" rows="10" cols="100" id="bContent"><?php echo isset($row['comment'])?$row['comment']:null?></textarea></td>
						</tr>
					</tbody>
				</table>
				<div class="btnSet">
					<button type="submit"  class="btnSubmit btn">
	<?php echo isset($bNo)?'수정':'작성'?>
          </button>
					<a href="board.php" class="btn btn-default">취소</a>
				</div>
			</form>
		</div>
  </div>
  </div>
	</article>




</body>
</html>
