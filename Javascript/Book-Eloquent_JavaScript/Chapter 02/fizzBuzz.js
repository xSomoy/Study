let foo = 1;
while ( foo <= 100 ) {
    if (foo % 3 == 0 && foo % 5 == 0) console.log("FizzBuzz")
    else {
        if (foo % 3 == 0) console.log ("Fizz");
        else if (foo % 5 == 0) console.log("Buzz");
        else console.log(foo);
    }
    ++foo;
}