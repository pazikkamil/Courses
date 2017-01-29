import sys
import socket
import getopt
import threading
import subprocess
import argparse

# global variables definition
listen  = False
command = False
upload  = False
execute = ""
target  = ""
upload_destination = ""
port               = 0


def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

    # print("NC tool")
    # print()
    # print("Usage: ./{app} -t target_host -p port".format(app=sys.argv[0]))
    # print("-l --listen listen [host]:[port]")
    # print("-e --execute=file_to_run launches file if connected")
    # print("-c --command interactive mode")
    # print("-u --upoad=destination if connected saves file")
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()
    else:
        usage()

main()
