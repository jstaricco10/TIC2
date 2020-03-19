#include <stdio.h>


#define IN 1  //dentro de una palabra
#define OUT 0 // fuera de una palabra
#define maxLargoLinea 50



int
main(){
	int c, i,j;
	char lineaEnCuestion[maxLargoLinea];
	i = j = 0 ;
	for (j = 0; j< maxLargoLinea; j++){
		lineaEnCuestion[j]= ' ';
	}

	while((c = getchar()) != EOF){
		while (c != '\n' && c!= EOF){
		lineaEnCuestion[i] = c;
		c = getchar();
		i++;
		}
		int temp = reverse(lineaEnCuestion,i);
		i = 0;
		for (j = 0; j< maxLargoLinea; j++){
		lineaEnCuestion[j]= ' ';
		}
	}

	//Test funcionamiento
	// char juanmahola[11];

	// juanmahola [0] = 'a';
	// juanmahola [1] = 'l';
	// juanmahola [2] = 'o';
	// juanmahola [3] = 'h';
	// juanmahola [4] = ' ';
	// juanmahola [5] = 'a';
	// juanmahola [6] = 'm';
	// juanmahola [7] = 'n';
	// juanmahola [8] = 'a';
	// juanmahola [9] = 'u';
	// juanmahola [10] = 'j';


	
	//int func = reverse(juanmahola,sizeof(juanmahola)/sizeof(char));
	return 0;
}



int reverse(char aRevertir[],int tamano){
	int i, j;

	// int tamano = sizeof(aRevertir)/sizeof(char);
	//printf("%d\n", tamano );
	char revertido [tamano];
	int lugar = tamano-1;
	

	for(i = 0; i < tamano ; i++){
		revertido[i] = aRevertir[lugar-i];
	}

	for(j = 0; j < tamano ; j++){
		putchar(revertido[j]);
	}
	printf("\n");
	return 0;
}


