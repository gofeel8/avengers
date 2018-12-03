<?php
	$sql = 'select * from avengers_comment where co_no=co_order and board=' . $bNo;
	$result = $conn->query($sql);

?>
<div id="comments">

		<?php
			while($row = $result->fetch_assoc()) {
		?>
		<ul >

					<li>
        	<form action="./delete_update.php" method="post">
          <input type="hidden" name="co_no" value="<?php echo $row['co_no']?>">
          <input type="hidden" name="back" value="<?php echo $bNo?>">
					<address>
				</address>
					<header>
							<figure class="avatar"><img src="images/avatar.png" alt=""></figure>
							<address class="">

								By <a><?php echo $row['co_id']?></a>
							</address>
						<time datetime=<?php echo $row['writedate']?>><?php echo $row['writedate']?></time>

					</header>

        <div class="comcont"><?php echo $row['co_content']?></div>
				<?php
				  if(isset($_SESSION['username'])&&$_SESSION['username'] == $row['co_id']){
				 ?>
            <button type="submit" class="float-right btn text-white btn-danger"style="float: right;">삭제</button>
						<?php
						}
						 ?>
        </form>

			</li>
		</ul>
		<?php } ?>

</div>





<?php
  if(isset($_SESSION['username'])){
 ?>
 <div class="writecomment">
<h2>댓글 쓰기</h2>
<form action="comment_update.php" method="post">
  	<input type="hidden" name="board" value="<?php echo $bNo?>">
	<table>
		<tbody>
			<tr>
        <th ><label for="bID">작성자: </label></th>
        <td >
          <?php
          echo "<h4>".$_SESSION['username']."</h4>";

                          ?>
          <input type="hidden" name="coId" value="<?php echo $_SESSION['username']; ?>">
        </tr>

				           <div class="block clear">
				<tr>

					<th ><label for="coContent">내용:</label></th>
					<td><input type="text" name="coContent" id="name" value="" size="80" required></td>

					<!-- <td><textarea name="coContent" id="coContent"></textarea></td> -->

				</tr>
		</tbody>
	</table>
	<div class="btnSet">
		<input type="submit" class="btnSubmit btn" value="댓글작성">
	</div>
</form>

</div>
<?php
}
else {
	echo "로그인해야 댓글을 작성할 수 있습니다.";
}
 ?>
