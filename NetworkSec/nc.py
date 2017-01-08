import sys
import socket
import getopt
import threading
import subprocess

# global variables definition
listen  = False
command = False
upload  = False
execute = ""
target  = ""
upload_destination = ""
port               = 0


def usage():
    print("NC tool")
    print()
    print("Usage: ./tool")
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
