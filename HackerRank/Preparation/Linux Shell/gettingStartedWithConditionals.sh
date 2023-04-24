read -n1 ans    
if [ "$ans" == 'y' ] || [ "$ans" == 'Y' ]
then
    echo 'YES'
elif [ "$ans" == 'n' ] || [ "$ans" == 'N' ]
then
    echo 'NO'
fi

