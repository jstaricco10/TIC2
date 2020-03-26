#include <stdio.h>


extern void my_strcpy(char *s1, char *s2);

extern void mytolower(char *s1);

extern char* my_strcat(char *dest, char *src);

int
main(){
	//int x;
	//int *ip; // puntero a enteros
	//ip = &x; // el puntero pasa a apuntar a x
	//ip ++ aumenta la direccion del puntero
	//(*ip)++ aumenta a lo que apunta el puntero


	//char hola[] = "hola" ;
	//char copia[] = "jola";
	

	char holapunt[] = "hola";
	char juamnapunt[] = "HOLA";

	char *puntero;

	
	//Prueba de strlen:
	// int largo  = my_strlen(holapunt);
	// printf("%d\n", largo);

	//Se puede imprimir con:
	// printf("%s\n",holapunt );

	//Prueba de strcpy:

	// my_strcpy(juamnapunt,holapunt);
	// printf("%s\n",juamnapunt);



	//Prueba de strcmp:

	// int comp =my_strcmp(holapunt,juamnapunt);
	// printf("%d\n",comp );

	//Prueba de strcasecmp:
	// int compcase;
	// compcase =my_strcasecmp(holapunt,juamnapunt);
	// printf("%d\n",compcase );


	//Prueba strcat
	char* resultado = my_strcat(holapunt,juamnapunt);
	printf("%s\n",resultado );


	return 0;
}

int my_strlen(char *s){
	int largo = 0;

	while( *s!= '\0'){
		s++;
		largo++;
	}
	return largo;
}

void my_strcpy(char *s1, char *s2){
	// copiamos el s2 en el 1
	// while(*s2 != '\0' && *s1 != '\0' ){
	// 	*s1 = *s2;	
	// 	s1++;
	// 	s2++;
	// }

	while((*s2++ = *s1++) != '\0')
		;

}


int my_strcmp(char *s1, char *s2){
	int resta;
	resta = 0;
	while(*s1 != '\0' && *s2 != '\0' && resta == 0){
		resta = *s1 - *s2;
		s1++;
		s2++;
	}

	return resta;
}

int my_strcasecmp(char *s1, char *s2){
	int resta;
	resta = 0;
	while(*s1 != '\0' && *s2 != '\0' && resta == 0){

		if ((*s1 >= 65) && (*s1 <= 90))
		{
		//mytolower(*s1);
			*s1 = *s1 + 32;
		}
		if ((*s2 >= 65) && (*s2 <= 90))
		{
			*s2 = *s2 + 32;	
		//mytolower(*s2);
		}
		resta = *s1 - *s2;
		s1++;
		s2++;
	}

	return resta;
}

char* my_strcat(char *dest, char *src){
	char *res;
	char *temp = res;
	//int lugar;
	while(*dest != '\0'){
		*temp = *dest;
		temp++;
		dest++;
	}	
	while(*src != '\0'){
		*temp = *src;
		temp++;
		src++;
	}
	*temp = '\0'; 
	return (char *) res;

}

// char* my_strcat(char *s1, char *s2)
// {


//     char *p1 = (char *)s1;
//     char *p2 = (char *)s2;

//     char *string = malloc(sizeof(char *));
//     char *res = string;

//     while (*p1 != '\0')
// {
//         *string = *p1;
//         string++;
//         p1++;
//     }
//     while (*p2 != '\0')
//     {
//         *string = *p2;
//         string++;
//         p2++;
// }
//     *string = '\0'; 

//     return (char *)res; 
// }




void mytolower(char* min){
	if ((min >= 65) && (min <= 90))
  	   min = min + 32; 
}

