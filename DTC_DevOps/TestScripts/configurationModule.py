#!/usr/bin/env python3
# Example file for prefix list generation
#


class prefixList():
    def prefixes(self):
      print ("prefixes:")
    def tunnel(self, tunnelNumber):
      print ("tunnel:", tunnelNumber)


class customerAccount(prefixList):
    def customer(self):
      print ("Customer name: ")

    def account(self):
      prefixList.prefixes(self);
      print ("Customer Account: ")

class percentComp():
    
    def complete(self, finishNumber):
      if (finishNumber > 90):
        print(finishNumber, "% complete")
      elif (finishNumber > 80):
        print(finishNumber, "% complete")
      elif (finishNumber > 70):
        print(finishNumber, "% complete")
      elif (finishNumber > 60):
        print(finishNumber, "% complete")
      elif (finishNumber > 50):
        print(finishNumber, "% complete")
      elif (finishNumber > 40):
        print(finishNumber, "% complete")
      elif (finishNumber > 30):
        print(finishNumber, "% complete")
      elif (finishNumber > 20):
        print(finishNumber, "% complete")
      elif (finishNumber > 10):
        print(finishNumber, "% complete")
      else:
        print(finishNumber, "% complete")

    def remain(self, finishNumber):
      num = 0
      while (num < finishNumber): #continue
        #print("*" * num)
        num = num+1
        if (num % 10 == 0):
          print(num, "% complete")
          print("+" * num, "*" * num)
          #print("out num: ", num)  
        if (num == 100): break
    def undo(self,finishNumber):
      notnum = 100
      while (notnum > finishNumber -1):
        notnum = notnum-1
        if (notnum % 10 == 0):
          print(notnum, "% complete")
          print("-" * notnum, "*" * notnum)
        if (notnum < 10): break
    

    
def main():
    conf = prefixList()
    conf.prefixes()
    conf.tunnel(" The number of this tunnel")
    #conf.tunnel("3")
    conf.tunnel(3)
    conf2 = customerAccount()
    conf2.customer()
    conf2.account()
    conf3 = percentComp()
    #conf3.complete(100)
    conf3.remain(100)
    conf3.undo(0)


if __name__ == "__main__":
    main()






