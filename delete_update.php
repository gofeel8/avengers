<?php

	require_once("./db_info.php");

	if(isset($_POST['bno'])) {
		$bNo = $_POST['bno'];
	}
	if(isset($_POST['co_no'])) {
		$co_no = $_POST['co_no'];
	}
if(isset($bNo)) {
		$sql = 'delete from avengers_board where id = ' . $bNo;

}

if(isset($co_no)) {
		$sql = "DELETE from avengers_comment where co_no =".$co_no;
}

if(isset($crawl_co_no)) {
		$sql = "DELETE from avengers_crawling_comment where co_no =".$co_no;
}


$result=mysqli_query($conn,$sql);

if($result) {

	$msg = '정상적으로 글이 삭제되었습니다.';
	if(isset($co_no)){
	$replaceURL = './view.php?bno='. $_POST['back'];
		}
	else {
			$replaceURL = './board.php';
	}
} else {

	$msg = '글을 삭제하지 못했습니다.';

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
