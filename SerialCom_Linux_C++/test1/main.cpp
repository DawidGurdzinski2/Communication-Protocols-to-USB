
#include <errno.h>
#include <fcntl.h> 
#include <string.h>
#include <termios.h>
#include <stdio.h>	
#include <unistd.h>
#include <stdlib.h>
#include "Terminal.h"



int main()
{   int i=0;
    char *portname = "/dev/ttyACM0";   
    int written;
	Terminal w(portname,B115200);
	w.fd=w.openPort(portname);
	w.configPort(w.fd,B115200);
    while(1){
        if(i==0){
        char message[] = "e";
        int messageSize = strlen(message);
        written = write(w.fd, message, messageSize);
        printf("\nTotal bytes written: %d\n", written);
        w.readData();
        w.readData();
        w.readData();
        }
        if(i==10){
        char message[] = "g";
        int messageSize = strlen(message);
        written = write(w.fd, message, messageSize);
        printf("\nTotal bytes written: %d\n", written);
        
        }
        if(i==20){
        char message[] = "e";
        int messageSize = strlen(message);
        written = write(w.fd, message, messageSize);
        printf("\nTotal bytes written: %d\n", written);
        
        }
        if(i>=10){
            w.readData();
            w.readData();
            w.readData();
        }
        i++;
        printf("%d",i);


    }
}