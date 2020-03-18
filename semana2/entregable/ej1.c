#include <stdio.h>

#define IN 1  //dentro de una palabra
#define OUT 0 // fuera de una palabra



// histograma horizontal de el largo de palabras

int
main(){
	int c, state, largos[10] ,largoPalabra, i, j;
	state = OUT;
	for (i = 0; i < 10	; i++) largos[i] = 0;

	largoPalabra = i = j = 0;	

	while ((c = getchar()) != EOF){
		
		if (c == ' ' || c == '\t' || c == '\n')
        state = OUT;
    	else 
    	state = IN;
    	
    	if (state == IN)
    		largoPalabra++;
    	
    	else if (largoPalabra > 0) {	
    		
    			if (largoPalabra <11)
    			largos[largoPalabra-1]++;
    	
    			largoPalabra = 0;
    			state = IN;
    		}
    	
	}


	// Impresion horizontal
	for (i = 0; i <10;i++)
    	{
     	printf("%d: ",i+1);
     	for (j = 0; j < largos[i]; j++)
        putchar('X');
    	putchar('\n');
    } 






	return 0;
}