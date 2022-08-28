#pragma once
#include <errno.h>
#include <fcntl.h> 
#include <string.h>
#include <termios.h>
#include <unistd.h>

class Terminal{


public:
int set_terminal_attributs(int fd, int speed, int parity);
void set_blocking (int fd, int should_block);

Terminal();
~Terminal();
};