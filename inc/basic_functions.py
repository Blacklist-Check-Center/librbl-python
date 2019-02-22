import urllib
import os

name_of_the_file=""

def write_to_file(response, name_of_the_file="temp.txt")
    file = open(name_of_the_file, "a")
    file.write(response)
    file.close()

def hasipback(url, secure=true)
    hostname = url
    response = os.system("host " + hostname)
    write_to_file(response)
    if ()
    response = os.system("ping -c 1 " + hostname)
