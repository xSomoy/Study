<?php
$to = "somoyyt@gmail.com";
$subject = "Local Host Mail Test";
$message = "Send Mail Successfully";
$headers = "From:John Deadman";  
if ( mail($to,$subject,$message,$headers,)) {
    echo " Affermative";
}
else {
    echo"Negetive";
}
?>