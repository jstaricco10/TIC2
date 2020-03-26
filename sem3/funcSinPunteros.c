#include <stdio.h>



void my_strcpy(char s1[], char s2[])
int
main(){
	
	char hola[] = "hola";
	char copia[] = "HOLA";



	//Prueba de strlen
	//int largo = my_strlen(hola);
	//printf("%d\n", largo);

	//Prueba de strcpy
	//my_strcpy(copia,hola);
	//printf("%s\n",copia );

	//Prueba de strcmp
	int comp =my_strcmp(hola,copia);
	printf("%d\n",comp );

	//Prueba de strcasecmp
	// int comp2 = my_strcasecmp(hola,copia);
	// printf("%d\n", comp2);


	return 0;
}

int my_strlen(char s[]){
	int len = 0;

	while (s[len] !=  '\0'){
		len++;
	}

	return len;
}

void my_strcpy(char s1[], char s2[]){
	int lugar = 0;

	while (s2[lugar] != '\0'){
		s1[lugar] = s2[lugar];
		lugar++;
	}

	printf("%s\n",s1);
}


int my_strcmp(char s1[], char s2[]){

	int lugar = 0;
	int resta = 0;

	while (s1[lugar] != '\0' && s2[lugar] != '\0'){
		resta = s1[lugar] - s2[lugar];
		lugar++;
	}
	return resta;
}


int my_strcasecmp(char s1[], char s2[]){

	int lugar = 0;
	int resta = 0;

	while (s1[lugar] != '\0' && s2[lugar] != '\0'){
	
	if ((s1[lugar] >= 65) && (s1[lugar] <= 90))
  	    s1[lugar] = s1[lugar] + 32; 

  	if ((s2[lugar] >= 65) && (s2[lugar] <= 90))
  	    s2[lugar] = s2[lugar] + 32;   

  	resta = s1[lugar] - s2[lugar];
		lugar++;

	}
	return resta;
}








