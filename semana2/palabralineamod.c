#include <stdio.h>

#define IN 1   // en una palabra
#define OUT 0  // fuera de una palabra

#define nl '\n'


// agarro la input y la imprimo una palabra por linea


int
main(){
	int c,state;

	state = OUT;
	while ((c = getchar()) != EOF){
		if (c != ' ' && c != '\n' && c != '\t'){
			state = IN;
			putchar(c);
		}	
		else {
			state = OUT;
			printf("\n");
		}
	}
}