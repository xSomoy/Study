# works theoritically but Sololearn Doesn't Accept
foo=input()
bar=0
for i in foo:
    if (i == '$'):
        cash=foo[bar]
    elif( i == 'T'):
        gru=foo[bar]
    else:
        bar=bar+1
print (cash)
print (gru)
