#include <stdio.h>

#define IN 1  //dentro de una palabra
#define OUT 0 // fuera de una palabra


int
main(){
	char hola[] = {'a','l','o','h'};

	// no se revierte porque esta en una fucion , tendriamos
	// que usar un puntero
	// hola = reverse(hola);
		int i;
	int tamano = sizeof(hola);
	char revertido [tamano];
	int lugar = tamano-1;

	for(i = 0; i < tamano ; i++){
		revertido[i] = hola[lugar-i];
	}

	for(i = 0; i < tamano ; i++){
		printf("%c ", revertido[i] );
	}
	printf("\n");


	return 0;
}



// char*
// reverse(char* aRevertir){
// 	int i;
// 	int tamano = sizeof(aRevertir);
// 	char revertido [tamano];
// 	int lugar = tamano-1;

// 	for(i = 0; i < tamano ; i++){
// 		revertido[i] = aRevertir[lugar-i];
// 	}

// 	for(i = 0; i < tamano ; i++){
// 		putchar(revertido[i]);
// 		printf("\n");
// 	}
// 	return revertido;
// }

