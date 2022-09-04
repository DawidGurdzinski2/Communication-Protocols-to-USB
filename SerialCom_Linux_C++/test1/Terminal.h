#pragma once
#include <errno.h>
#include <fcntl.h> 
#include <string.h>
#include <termios.h>
#include <unistd.h>
#include <stdlib.h>

class Terminal{

char* port;
int speed;

public:
int fd;
int configPort(int,int);
int openPort(char*);
void readData();
Terminal(char* ,int);
~Terminal();
};