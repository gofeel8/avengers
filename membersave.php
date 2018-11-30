<html>
   <meta charset="utf-8">
<?php
	require_once("./db_info.php");
 $id=$_POST['id'];
 $password=($_POST['pwd']);
 $name=$_POST['name'];


// var_dump($id);
// var_dump($password);
// var_dump($name);
// var_dump($position);
if($id==NULL ||$password==NULL ||$name==NULL){
  echo "빈 칸을 모두 채워주세요<br>";
  echo "<a href=join.php>뒤로가기</a>";
  exit();
}

$check="SELECT * from avengers_member WHERE id ='$id'";
$result=$conn->query($check);
if($result->num_rows==1){
  // echo "<script>alert(\"ID가 중복됩니다\"); window.location.replace(\"index.php\");</script>";
  echo "중복된 id";
  echo "<a href=join.php>뒤로가기</a>";
exit();
}
 $sql = "insert into avengers_member (id, pwd, name)";             // (입력받음)insert into 테이블명 (column-list)
 $sql = $sql. "values('$id','$password','$name')";         // calues(column-list에 넣을 value-list)
 if($conn->query($sql)){                                                              //만약 sql로 잘 들어갔으면
  echo 'success inserting <p/>';
    // echo "<script>alert(\"가입성공\"); window.location.replace(\"index.php\");</script>";                                                     //success inserting 으로 표시
  echo $name.'님 가입 되셨습니다.<p/>';                                   // id님 안녕하세요.
 }else{                                                                                //아니면
  echo 'fail to insert sql';                                                            //fail to insert sql로 표시
 }
mysqli_close($conn);


?>
<input type="button" value="로그인하러가기" onclick="location='index.php'">
</html>
