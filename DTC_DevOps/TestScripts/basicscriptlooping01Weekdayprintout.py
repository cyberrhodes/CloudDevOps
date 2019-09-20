#!/usr/bin/env python3
# Example file for HelloWorld
#

def main():
  x = 0
  y = 0
  # define a while loop
  while (x < 5):
     print (x)
     x = x + 1
     
  while (y < 5):
     print (y)
     y = y + 1

  # define a for loop
  for x in range(5,10):
    print (x)

  for y in range(5,10):
    print (y)
      


  # use a for loop over a collection
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:
    print (d)

  # use a for loop over a collection of protocol
  protocols = ["http 80","https 443","RDP 3389","SSH 22","SNMP 161/162","DNS 53","DHCP 67/68","FTP 20/21"]
  for p in protocols:
    print (p)
  
  # use the break and continue statements
  for x in range(5,10):
    #if (x == 7): break
    #if (x % 2 == 0): continue
    print (d)


  # the use of break
  for y in range(5,10):
    print (p)

  
  #using the enumerate() function to get index 
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate(days):
    print (i, d)

  # use a for loop over a collection of protocol
  protocols = ["http 80","https 443","RDP 3389","SSH 22","SNMP 161/162","DNS 53","DHCP 67/68","FTP 20/21"]
  for s,p in enumerate(protocols):
    print (s,p)

    
if __name__ == "__main__":
  main()
