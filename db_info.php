<?php


$conn = new mysqli('dblab.jbnu.ac.kr', 's201315164', 'tkdvlf132!', 's201315164');

if ($conn->connect_error) {
  die('데이터베이스 연결에 문제가 있습니다.\n관리자에게 문의 바랍니다.');
}

$conn->set_charset('utf8');
?>
