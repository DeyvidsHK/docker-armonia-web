<?php
session_start();
session_destroy();
header("Location: tienda.php");
exit;
?>
