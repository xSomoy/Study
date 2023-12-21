# works theoritically but Sololearn Doesn't Accept
url = input()
if 'v' in url:
    link, id = url.split('v=')
    print (id)
else:
    link,id = url.split('.be/')
    print (id)