#include <stdio.h>
#include <stdlib.h>

#define NAME 80
void main(){
    char ch, name[NAME];
    int i;
    system("clear");
    printf("Hello! Please type you name: ");
    for(i=0;(ch=getchar())!= '\n'; ++i){
        name[i]=ch;
    }
    name[i] = '\0';
    printf("\n%s %s %s", "Nice to meet you", name,".");
    system("sleep 1"); // sleep alternative
    printf("\nYour name spelled backward is ");
   for (--i; i>=0; --i){
       putchar(name[i]);
   }
   printf("\n\nHave a nice day...\n");
   system("sleep 5");
}

// Mushphyqur Rahman Tanveer
