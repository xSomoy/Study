let foo = 8;
let bar= 1;
let a = 1;
let b = 1;
let blob = '';
let blob1 = '';
let p1 = '#';
let p2 = ' ';

while ( bar <= foo){
    while (a <= foo) {
        if (a % 2 == 0) blob =  blob + p1;
        else blob = blob + p2;
        ++a;
    }
    while (b <= foo) {
        if (b % 2 == 0) blob1 =  blob1 + p2;
        else blob1 = blob1 + p1;
        ++b;
    }
    if ( bar % 2 == 0) console.log(blob1);
    else console.log(blob);

    ++bar;
}

