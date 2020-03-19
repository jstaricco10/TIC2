#include <stdio.h>


#define IN 1  //dentro de una palabra
#define OUT 0 // fuera de una palabra
#define maxLargoLinea 50

int
main(){
	int c,i,j;
	char lineaEnCuestion[maxLargoLinea];
	char saco[5];
	i = j = 0 ;
	for (j = 0; j< maxLargoLinea; j++){
		lineaEnCuestion[j]= ' ';
	}

	saco [0] = 'a';
	saco [1] = 'e';
	saco [2] = 'i';
	saco [3] = 'o';
	saco [4] = 'u';

	while((c = getchar()) != EOF){
		while (c != '\n' && c!= EOF){
		lineaEnCuestion[i] = c;
		c = getchar();
		i++;
		}
		int temp = squeeze(lineaEnCuestion,saco, i);
		i = 0;
		for (j = 0; j< maxLargoLinea; j++){
		lineaEnCuestion[j]= ' ';
		}
	}


	//putchar('\0'); sirve perri

	return 0;
}

int 
squeeze(char aReducir[], char loQueSaco[], int tamano){
 // tamano del a reducir
 // en esta funcion debo hacer la impresion post operaciones
	int i, j;
	char reducido[tamano];

	int lugar = 0; // variable para descarte, mueve i cuando es vocal

	for(i = 0; i < tamano ; i++){
		for (j = 0; j < 5 ; j++){
			if (aReducir[i] == loQueSaco[j]){
				reducido[i] = '\0';
				aReducir[i] = '\0';
			}
			else if (aReducir != '\0') 
				reducido [i] = aReducir[i];
		}
	}

	for(j = 0; j < tamano ; j++){
		putchar(reducido[j]);
	}
	printf("\n");

	return 0;
}

