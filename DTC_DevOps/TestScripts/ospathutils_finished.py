#
# Example file for working with os.path module
#

import os
import sys
import platform
from os import path
import datetime
from datetime import date, time, timedelta
import time



#def convertenvirons(sysvariables):
#  myenv = os.environ
# for myenvs in myenv:
#    f.write(myenvs.getenviron)



def main():
  # Print the name of the OS
  print (os.name)
  print (os.environ)
  print (sys.platform)
  print (platform.system)

  

  # Open a file for writing and create it if it doesn't exist
  f = open("Iamhereifnofileexistedprior.txt","w+")
  f.write(str(" OS: %s\r\n" % os.name))
  f.write(str(" Environ: %s\r\n" % os.environ))
  f.write(str(" Platform: %s\r\n" % sys.platform))
  f.write(str(" System: %s\r\n" % platform.system))

  # close the file when done
  f.close()

  
  # Check for item existence and type
  print ("Item exists: " + str(path.exists("dyterr.txt")))
  print ("Item is a file: " + str(path.isfile("dyterr.txt")))
  print ("Item is a directory: " + str(path.isdir("dyterr.txt")))
  
  # Work with file paths
  print ("Item's path: " + str(path.realpath("dyterr.txt")))
  print ("Item's path and name: " + str(path.split(path.realpath("dyterr.txt"))))
  
  # Get the modification time
  t = time.ctime(path.getmtime("dyterr.txt"))
  print (t)
  print (datetime.datetime.fromtimestamp(path.getmtime("dyterr.txt")))
  
  # Calculate how long ago the item was modified
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("dyterr.txt"))
  print ("It has been " + str(td) + " since the file was modified")
  print ("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == "__main__":
  main()
  


  
