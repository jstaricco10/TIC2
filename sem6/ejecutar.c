#include "minish.h"
#include <string.h>



int ejecutar(int argc, char **argv){
	//ver si el comando es interno, es decir si esta en el array y si es
	//asi se ejecuta si no se invoca a externo
	//se retorna el status de retorno del comando

	for(int i = 0; builtin_arr[i].cmd != NULL;i++){
		if(strcmp(builtin_arr[i].cmd, argv[0]))
			return (builtin_arr[i].func)(argc,argv);
	}
	return -1;
}