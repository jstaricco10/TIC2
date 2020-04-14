/* Programa que borra archivos a partir de los
nombres pasados como argumentos. Por ej: .unlink aborrar.txt
Se usa la llamada al sistema:
int unlink(const char *pathname);
*/

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <error.h>

#include <unistd.h>


int main(int argc, char const *argv[])
{
	int fd; 	 //descriptor del archivo
	int flags = O_CREAT|O_EXCL|O_WRONLY|O_TRUNC; //man creat o man open
	mode_t mode = S_IRUSR|S_IWUSR|S_IRGRP|S_IROTH; //0644 - rw para duenio, r para grupo y otros

	while(--argc > 0){
		if((fd = unlink(*++argv)) < 0){
			error (0, errno, "No se pudo crear el archivo %s", *argv);
		} else {
			fprintf(stderr, "archivo %s borrado, descriptor desasignado %d. \n", *argv ,fd);
		}
	}
	exit(0);
}
