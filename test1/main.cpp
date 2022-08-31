
#include <errno.h>
#include <fcntl.h> 
#include <string.h>
#include <termios.h>
#include <stdio.h>	
#include <unistd.h>
#include <stdlib.h>
#include "Terminal.h"



int main()
{
    char *portname = "/dev/ttyACM1";
 
    
   
	Terminal w(portname,B115200);
	w.fd=w.openPort(portname);
	w.configPort(w.fd,B115200);


    do {
        unsigned char buf[80];
        int rdlen;

        rdlen = read(w.fd, buf, sizeof(buf) - 1);
        if (rdlen > 0) {

            unsigned char   *p;
  
            for (p = buf; rdlen-- > 0; p++)
                {printf(" %x", *p);
                printf("%d",rdlen);}
            printf("\n");

        } else if (rdlen < 0) {
            printf("Error from read: %d: %s\n", rdlen, strerror(errno));
        } else {  
            printf("Timeout from read\n");
        }     
            

    } while (1);
}