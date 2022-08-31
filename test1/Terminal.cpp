
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
tty.c_cflag |= (CLOCAL | CREAD);    
tty.c_cflag &= ~CSIZE;
tty.c_cflag |= CS8;         
tty.c_cflag &= ~PARENB;    
tty.c_cflag &= ~CSTOPB;     
tty.c_cflag &= ~CRTSCTS;    
tty.c_iflag &= ~(IGNBRK | BRKINT | PARMRK | ISTRIP | INLCR | IGNCR | ICRNL | IXON);
tty.c_lflag &= ~(ECHO | ECHONL | ICANON | ISIG | IEXTEN);
tty.c_oflag &= ~OPOST;
tty.c_cc[VMIN] = 1;
tty.c_cc[VTIME] = 1;
tcsetattr(fd, TCSANOW, &tty);
}

int Terminal::openPort(char* p){
	int f;											
	f = open(p, O_RDWR | O_NOCTTY | O_SYNC);	
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

Terminal::~Terminal(){

	
}
