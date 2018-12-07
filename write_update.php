<?php
date_default_timezone_set('Asia/Seoul');

  require_once("./db_info.php");
 	if(isset($_POST['bno'])) {
	$bNo = $_POST['bno'];
	}

  if(empty($bNo)) {
  $date = date('Y-m-d H:i:s');
	$bID = $_POST['user'];
  }
  $bTitle = $_POST['title'];
  $bContent = $_POST['comment'];


  if(isset($bNo)) {
  		$sql = "UPDATE board set title='".$bTitle."',comment='".$bContent."' WHERE id=" .$bNo;
  		$msgState = '수정';

  }
  else {


  $sql = "INSERT INTO avengers_board(user,title,comment,writedate,see,category) values('".$bID."', '".$bTitle."','".$bContent."','".$date."',0,1)";
  $msgState = '등록';
}
  $result=mysqli_query($conn,$sql);
	if($result) {
    $msg = '정상적으로 글이 ' . $msgState . '되었습니다.';


		$replaceURL = './board.php' ;
	} else {
		$msg = '글을 ' . $msgState . '하지 못했습니다.';
?>
		<script>
			alert("<?php echo $msg?>");
			history.back();
		</script>
<?php
exit;
	}

?>
<script>
	alert("<?php echo $msg?>");
	location.replace("<?php echo $replaceURL?>");
</script>
