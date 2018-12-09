<?php
session_start();
	require_once("./db_info.php");
	/* 페이징 시작 */
	$paging='';
  	//페이지 get 변수가 있다면 받아오고, 없다면 1페이지를 보여준다.
$subString='';
$searchColumn ='';
  	if(isset($_GET['page'])) {
  		$page = $_GET['page'];
  	} else {
  		$page = 1;
  	}
		/* 검색 시작 */
		if(isset($_GET['searchColumn'])) {
			$searchColumn = $_GET['searchColumn'];
			$subString .= '&amp;searchColumn=' . $searchColumn;
		}
		if(isset($_GET['searchText'])) {
			$searchText = $_GET['searchText'];
			$subString .= '&amp;searchText=' . $searchText;
		}
		if(isset($searchColumn) && isset($searchText)) {
			$searchSql = ' where ' . $searchColumn . ' like "%' . $searchText . '%"';
		} else {
			$searchSql = '';
		}
		/* 검색 끝 */
		$sql = "SELECT count(*) as cnt from avengers_board".$searchSql;
		$result=mysqli_query($conn,$sql);
		// $row = mysqli_query($con, $sql)

    $row=mysqli_fetch_array($result);
  	$allPost = $row['cnt']; //전체 게시글의 수

		if(empty($allPost)) {
	$emptyData = '<tr><td class="textCenter" colspan="5">글이 존재하지 않습니다.</td></tr>';
	// $paging = '<ul>';
	$paging .= '<li>1</li>';
	// $paging .= '</ul>';
	}
	 else {
  	$onePage = 15; // 한 페이지에 보여줄 게시글의 수.
  	$allPage = ceil($allPost / $onePage); //전체 페이지의 수
  	if($page < 1 || ($allPage && $page > $allPage)) {
  ?>
  		<script>
  			alert("존재하지 않는 페이지입니다.");
  			history.back();
  		</script>
  <?php
  		exit;
  	}
  	$oneSection = 10; //한번에 보여줄 총 페이지 개수(1 ~ 10, 11 ~ 20 ...)
  	$currentSection = ceil($page / $oneSection); //현재 섹션
  	$allSection = ceil($allPage / $oneSection); //전체 섹션의 수
  	$firstPage = ($currentSection * $oneSection) - ($oneSection - 1); //현재 섹션의 처음 페이지
  	if($currentSection == $allSection) {
  		$lastPage = $allPage; //현재 섹션이 마지막 섹션이라면 $allPage가 마지막 페이지가 된다.
  	} else {
  		$lastPage = $currentSection * $oneSection; //현재 섹션의 마지막 페이지
  	}
  	$prevPage = (($currentSection - 1) * $oneSection); //이전 페이지, 11~20일 때 이전을 누르면 10 페이지로 이동.
  	$nextPage = (($currentSection + 1) * $oneSection) - ($oneSection - 1); //다음 페이지, 11~20일 때 다음을 누르면 21 페이지로 이동.
  	// $paging = '<ul>'; // 페이징을 저장할 변수
  	//첫 페이지가 아니라면 처음 버튼을 생성
  	// if($page != 1) {
						// $paging .= '<li><a href="./board.php?page=1' . $subString . '">처음</a></li>';
  	// }
  	//첫 섹션이 아니라면 이전 버튼을 생성
  	if($currentSection != 1) {
			$paging .= '<li ><a href="./board.php?page=' . $prevPage . $subString . '">이전</a></li>';
  	}
  	for($i = $firstPage; $i <= $lastPage; $i++) {
  		if($i == $page) {
  			$paging .= '<li ><a href="./board.php?page=' . $i . $subString . '">' . $i . '</a></li>';
  		}
			else {
  					$paging .= '<li><a href="./board.php?page=' . $i . $subString . '">' . $i . '</a></li>';
  		}
  	}
  	//마지막 섹션이 아니라면 다음 버튼을 생성
  	if($currentSection != $allSection) {
  		$paging .= '<li><a href="./board.php?page=' . $nextPage . $subString . '">다음</a></li>';
  	}
  	//마지막 페이지가 아니라면 끝 버튼을 생성
  	// if($page != $allPage) {
			// $paging .= '<li ><a href="./board.php?page=' . $allPage . $subString . '">끝</a></li>';
  	// }
  	// $paging .= '</ul>';
    /* 페이징 끝 */
  	$currentLimit = ($onePage * $page) - $onePage; //몇 번째의 글부터 가져오는지
  	$sqlLimit = ' limit ' . $currentLimit . ', ' . $onePage; //limit sql 구문
  	// $sql = 'select * from board order by id desc' . $sqlLimit; //원하는 개수만큼 가져온다. (0번째부터 20번째까지
		$sql = 'SELECT * from avengers_board'.$searchSql.' order by id desc'.$sqlLimit;
	  $result=mysqli_query($conn,$sql);
}
?>



<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>자유게시판</title>
<link rel="stylesheet" href="./css/style.css">
  <link href="css/bootstrap.min.css" rel="stylesheet">

</head>

<body>
  <div id="grid2">
<a href="index.php">
<img src="./images/logo.png"  height="200px" width="500" class="center">
</a>
  </div>

<div id="grid">
  <div id="login">
		<ul class="list-group">
			<li class="list-group-item"><a href="index.php"> 공모전</a></li>
	    <li class="list-group-item"><a href="board.php"> 자유게시판</a></li>
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

    <div class="container">

<table class="table table-hover">
	<caption class="readHide">자유게시판</caption>

  <thead>
    <tr>

      <th width="50%">제목</th>
      <th>작성자</th>
      <th>날짜</th>
      <th>조회수</th>
    </tr>
  </thead>
  <tbody>
		<?php
					if(isset($emptyData)) {
						echo $emptyData;
					} else {

	      							while($row=mysqli_fetch_array($result))
	      							{

	      								$datetime = explode(' ', $row['writedate']);

	      								$date = $datetime[0];

	      								// $time = $datetime[1];

	      								// if($date == Date('Y-m-d'))

	      									// $row['b_date'] = $time;

	      								// else

	      									$row['writedate'] = $date;

	      						?>
					<tr>


						<td class="title"><a href="./view.php?bno=<?php echo $row['id']?>"><?php echo $row['title']?></a></td>

						<td class="author"><?php echo $row['user']?></td>

						<td class="date"><?php echo $row['writedate']?></td>

						<td class="hit"><?php echo $row['see']?></td>

					</tr>

						<?php

							}
						}
						?>
  </tbody>
</table>
<?php
if(isset($_SESSION['username'])){
 ?>
<a href="./write.php" class="btn btn-default pull-right">글쓰기</a>
<?php
}
 ?>
<div class="text-center">
  <ul class="pagination">

		<?php echo $paging ?>
  </ul>

</div>

</div>

<div class="searchBox" align="center">

	<form action="./board.php" method="get">

		<select name="searchColumn">

			<option <?php echo $searchColumn=='title'?'selected="selected"':null?> value="title">제목</option>

			<option <?php echo $searchColumn=='comment'?'selected="selected"':null?> value="comment">내용</option>

			<option <?php echo $searchColumn=='user'?'selected="selected"':null?> value="user">작성자</option>

		</select>

		<input type="text" name="searchText" value="<?php echo isset($searchText)?$searchText:null?>">

		<button type="submit" class="btn">검색</button>

	</form>

</div>



    </div>
  </div>





  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
 <script src="js/bootstrap.js"></script>
  </body>
  </html>
