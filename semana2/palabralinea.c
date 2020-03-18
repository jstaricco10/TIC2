#include <stdio.h>

#define IN 1   // en una palabra
#define OUT 0  // fuera de una palabra



// contar lines, palabras, y caracteres de un input


int
main(){
	int c,nl,nw,nc, state;

	state = OUT;
	nl = nw = nc = 0;
	while ((c = getchar()) != EOF){
		++nc;
		if (c == '\n')
			++nl;
		if (c == ' ' || c == '\n' || c == '\t')
			state = OUT;
		else if (state == OUT){
			state = IN;
			++nw;
		}
	}
	printf(" lineas: %d palabras: %d caracteres: %d\n", nl,nw,nc );
}