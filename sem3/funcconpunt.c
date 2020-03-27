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
	

	char holapunt[] = "hol";
	char juamnapunt[] = " hol ";

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

	int comp =my_strcmp(holapunt,juamnapunt);
	printf("%d\n",comp );

	//Prueba de strcasecmp:
	// int compcase;
	// compcase =my_strcasecmp(holapunt,juamnapunt);
	// printf("%d\n",compcase );


	//Prueba strcat
	// char* resultado = my_strcat(holapunt,juamnapunt);
	// printf("%s\n",resultado);

	//Prueba strend
	// int validez = my_strend(holapunt,juamnapunt);
	// printf("%d\n", validez);

	/*
	La función index() devuelve un puntero a la 1ª ocurrencia del carácter c en la cadena s.

       La función rindex() devuelve un puntero a la última ocurrencia del carácter c en la cadena
       s.

    strstr : Returns a pointer to the first occurrence of str2 in str1, or a null pointer if str2 is not part of str1.	   
    */



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
	while((*s1 = *s2) != '\0'){
		s1++;
		s2++;
	}
}


int my_strcmp(char *s1, char *s2){
	int resta;
	resta = 0;

	resta = *s1 - *s2;
	while (resta == 0) {
        if (*s1 == '\0' || *s2 == '\0')
            break;
		s1++;
        s2++;
        resta = *s1 - *s2;
     }

	if (*s1 == '\0' && *s2 == '\0')
      return 0;
    else
      return resta;	
}

int my_strcasecmp(char *s1, char *s2){
	// int resta;
	// resta = 0;
	// while(*s1 != '\0' && *s2 != '\0' && resta == 0){

	// 	if ((*s1 >= 65) && (*s1 <= 90))
	// 	{
	// 	//mytolower(*s1);
	// 		*s1 = *s1 + 32;
	// 	}
	// 	if ((*s2 >= 65) && (*s2 <= 90))
	// 	{
	// 		*s2 = *s2 + 32;	
	// 	//mytolower(*s2);
	// 	}
	// 	resta = *s1 - *s2;
	// 	s1++;
	// 	s2++;
	// }
	// return resta;

	int resta;
	resta = 0;

	if ((*s1 >= 65) && (*s1 <= 90))
		*s1 = *s1 + 32;
	if ((*s2 >= 65) && (*s2 <= 90))
		*s2 = *s2 + 32;


	resta = *s1 - *s2;
	while (resta == 0) {
        if (*s1 == '\0' || *s2 == '\0')
            break;
		s1++;
        s2++;
        if ((*s1 >= 65) && (*s1 <= 90))
		*s1 = *s1 + 32;
		if ((*s2 >= 65) && (*s2 <= 90))
		*s2 = *s2 + 32;

        resta = *s1 - *s2;
     }

	if (*s1 == '\0' && *s2 == '\0')
      return 0;
    else
      return resta;	
}

char* my_strcat(char *dest, char *src){
	
	char *temp = dest; 

	while (*dest)
		dest++;
	while(*dest = *src){
		dest++;
		src++;
	}
	return temp;
}

int my_strend(char *s, char *end){
	
	char* aux = end; // nos va a servir
	// para ver si es el principio de end

	while(*s)
		s++;
	while(*end)
		end++;
	while(end > aux){
		if (*end != *s)
			return 0;
		end--;
		s--;
	}
	return 1;
}
char * my_strncpy(char *s1, char *s2, int n){
	// se copia como maximo n bytes err 4 y 5
	int i;
	i = 0;
		while((*s1 = *s2) != '\0' && i<=n){
		s1++;
		s2++;
		i++;
	}
	return (char *) s1; 
}

char * my_strncat(char *dest, char *src, int n){

	char *temp = dest;
	int i = 0; 

	while (*dest){
		dest++;
		i++;
		if(i > n)
			return (char *) temp;		
	}
	while(*dest = *src){
		dest++;
		src++;
		i++;
		if(i > n)
			return (char *) temp;	
	}
	return (char *) temp;
}

int my_strncmp(char *s1, char *s2, int n){
	int i = 0; //numero de bytes comparados
	int resta;
	resta = 0;
	while(*s1 != '\0' && *s2 != '\0' && resta == 0 && i<=n){
		resta = *s1 - *s2;
		s1++;
		s2++;
		i++;
	}

	return resta;
	//eroror case 1 ,2 ,6
}







void mytolower(char* min){
	if ((min >= 65) && (min <= 90))
  	   min = min + 32; 
}

