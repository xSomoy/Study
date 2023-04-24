nslookup myip.opendns.com resolver1.opendns.com > tmpFile 
set /p myvar= < tmpFile 
echo %myvar%
set /p id=Enter ID: 

