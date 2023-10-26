<?php
$to = "+8801674608620@sms.alltelwireless.com";
$from = "bKash";
$message = "This is a text message\nNew line...";
$headers = "From: $from\n";
mail($to, '', $message, $headers);
?>