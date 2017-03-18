#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    const char *s = "Monty Python\n";
    const char *zmienna = "USERNAME";
    char buf[100];
    char * zmienna_wyjsciowa;
    char *path;

    printf("%s", s); 
    scanf("%s", &buf);
    printf("to jest jakis ciag %s\n", buf);
    const char * tmp = getenv("USERNAME");

    path = malloc(strlen(tmp) + 1);
      if (!path) {

          printf("Error\n");
	      return 0;
	        }
    strcpy(path, tmp);
    printf("path = %s\n", path);
    //printf("zmienna to %s\n", zmienna_wyjsciowa);

    return 0;
} 
