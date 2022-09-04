
#include <errno.h>
#include <fcntl.h> 
#include <string.h>
#include <termios.h>
#include <stdio.h>	
#include <unistd.h>
#include <stdlib.h>
#include "Terminal.h"

int Terminal::configPort(int fd, int sp){
    struct termios tty;
    tcgetattr(fd, &tty);
    cfsetospeed(&tty, (speed_t)speed);
    cfsetispeed(&tty, (speed_t)speed);
     tty.c_cflag |= CLOCAL | CREAD;
    tty.c_cflag &= ~CSIZE;
    tty.c_cflag |= CS8;         /* 8-bit characters */
    tty.c_cflag &= ~PARENB;     /* no parity bit */
    tty.c_cflag &= ~CSTOPB;     /* only need 1 stop bit */
    tty.c_cflag &= ~CRTSCTS;    /* no hardware flowcontrol */

    tty.c_lflag |= ICANON | ISIG;  /* canonical input */
    tty.c_lflag &= ~(ECHO | ECHOE | ECHONL | IEXTEN);

    tty.c_iflag &= ~IGNCR;  /* preserve carriage return */
    tty.c_iflag &= ~INPCK;
    tty.c_iflag &= ~(INLCR | ICRNL | IUCLC | IMAXBEL);
    tty.c_iflag &= ~(IXON | IXOFF | IXANY);   /* no SW flowcontrol */

    tty.c_oflag &= ~OPOST;

    tty.c_cc[VEOL] = 0;
    tty.c_cc[VEOL2] = 0;
    tty.c_cc[VEOF] = 0x04;
tcsetattr(fd, TCSANOW, &tty);
}

int Terminal::openPort(char* p){
	int f;											
	f = open(p, O_RDWR | O_NOCTTY | O_NDELAY);	
	if (f == -1) {
		printf("Error opening %s: %s\n",p, strerror(errno));
	} else {
		fcntl(f, F_SETFL, 0);																	
	}
	return(f);
}
Terminal::Terminal(char* p ,int s){
	port=p;
	speed=s;

}
void Terminal::readData(){
	unsigned char buf[80];
    int rdlen;
   
    rdlen = read(fd, buf, sizeof(buf) - 1);
    if (rdlen > 0) {
       unsigned char   *p;     
	   //printf("%d",rdlen);
        for  ( p = buf; rdlen > 0; ++p, --rdlen )
            {   
                printf(" %x", *p);}
        printf("\n");
    } else if (rdlen < 0) {
            printf("Error from read: %d: %s\n", rdlen, strerror(errno));
    } else {  
            printf("Timeout from read\n");
    }     
}

Terminal::~Terminal(){
	close(fd);	
}
