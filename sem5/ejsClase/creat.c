/* Programa que crea archivos vacios a partir de los
nombres pasados como argumentos. Por ej: creat vacio.txt
Se usa la llamada al sistema:
int open(const char *pathname, int flags, mode_t mode);
*/

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <error.h>


int main(int argc, char const *argv[])
{
	int fd; 	 //descriptor del archivo
	int flags = O_CREAT|O_EXCL|O_WRONLY|O_TRUNC; //man creat o man open
	mode_t mode = S_IRUSR|S_IWUSR|S_IRGRP|S_IROTH; //0644 - rw para duenio, r para grupo y otros

	while(--argc > 0){
		if((fd = open(*++argv,flags,mode)) < 0){
			error (0, errno, "No se pudo crear el archivo %s", *argv);
		} else {
			fprintf(stderr, "archivo %s creado, descriptor asignado %d. \n", *argv ,fd);
		}
	}
	exit(0);
}
