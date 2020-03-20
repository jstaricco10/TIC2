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
    printf("\nHistograma horizontal de palabras por longitud. \n\n");
	for (i = 0; i <10;i++)
    	{
     	printf("%d: ",i+1);
     	for (j = 0; j < largos[i]; j++)
        putchar('X');
    	putchar('\n');
    } 

    // Impresion vertical 
    printf("\nHistograma vertical de palabras por longitud. \n\n");
    int masCant = 0;
    for (i = 0; i<11; i++)
        if(largos[i] > masCant)
            masCant = largos[i];
    for (i = masCant ; i > 0; i--){
        printf("%2s  ", ">" );
        for (j = 0; j < 11 ; j++){
            if (largos[j] >= i)
                printf("%2s ","X");
            else
                printf("%2s "," ");
        }
        printf("\n");        
    }
    for (i=0 ; i < 11;i++)
        printf("====");
    printf("\n");
    printf("%2s  ", " ");
    for (int i = 0; i < 10; ++i)
    {
        printf("%2d ",i+1);
    }







	return 0;
}