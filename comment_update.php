<?php
date_default_timezone_set('Asia/Seoul');

require_once("./db_info.php");
  $date = date('Y-m-d H:i:s');
	$board = $_POST['board'];
	$coId = $_POST['coId'];
	$coContent = $_POST['coContent'];
	$sql = 'insert into avengers_comment values(null, ' .$board . ', null, "' . $coContent . '", "' . $coId . '","'.$date.'")';

	$result = $conn->query($sql);
	$coNo = $conn->insert_id;



	$sql = 'update avengers_comment set co_order = co_no where co_no = ' . $coNo;



	$result = $conn->query($sql);

	if($result) {

?>

	<script>

		// alert('댓글이 정상적으로 작성되었습니다.');

    history.back();
	</script>

<?php

	}
  else{
    ?>
    <script>

      alert('오류.');

          history.back();

    </script>

<?php
  }

?>
