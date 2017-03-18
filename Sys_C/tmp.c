#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv, char** envp)
{
	char buf[100];
 	scanf("%s", &buf);

	setenv("USERNAME", "WARTOSC", 1);

  char** env;
    for (env = envp; *env != 0; env++)
      {
          char* thisEnv = *env;
	      printf("%s\n", thisEnv);    
	        }
		  return(0);
		  }
