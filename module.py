import random
import pandas as pd
class bank():
    def __init__(self):
        self.data = [["Suresh",123,2000,5000],["Raina",124,400,1000],["Virat",125,6000,2000]]
        self.trans = pd.DataFrame(columns=["AccNo","Transaction Type","Amount"])
        self.creditscr = pd.DataFrame(columns=["AccNo", "Credit","Membership"])
    def chkbal(self,accno):
        for i in self.data[1]:
            if i[1]==accno:
                print("Your Bal: ",i[1])
            else:
                print("Invalid AccNO")


    def create(self,name,bal,fd):
        accno = self.data[len(self.data)-1][1] + 1
        new = [name,accno,bal,fd]
        self.data.append(new)
        print("Name: ",name)
        print("AccNo: ",accno)
        print("Balance: ",bal)
        print("Fixed Dep: ",fd)
        print("Your Account Created")


    def deposit(self,accno,depamt):
        idx=0
        for i in self.data:
            if i[1] == accno:
                idx=self.data.index(i)
                break



  #Service Provided:
 #1.Acc Cretion
 #2.Deposit
 #3.Withdraw
 #4.Fixed Deposit
 #5.Exit
 #2
 #vEnter Accno: 123
 #Enter Deposit amt: 2000
 #Your Balance:  4000
 #c:\Users\priya\Desktop\VS Code\test3\module.py:58: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
   #nooftrans = self.trans["AccNo"].value_counts()[accno]
 #Traceback (most recent call last):
   #File "c:\Users\priya\Desktop\VS Code\test3\menu.py", line 30, in <module>        
     #bank.deposit(accno,depamt)
   #File "c:\Users\priya\Desktop\VS Code\test3\module.py", line 58, in deposit       
     #nooftrans = self.trans["AccNo"].value_counts()[accno]
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^
   #File "C:\Users\priya\AppData\Roaming\Python\Python312\site-packages\pandas\core\series.py", line 1118, in __getitem__
     #return self._values[key]
      #      ~~~~~~~~~~~~^^^^^
 #IndexError: index 123 is out of bounds for axis 0 with size 0
 #PS C:\Users\priya\Desktop\VS Code\test3>       
       
 #in this i cant understand error at all.      
        
        if depamt > 100000:
            pan = input("Enter Pan No.: ")
            if len(pan) != 5:
                print("Ivalid Pan")
            else:
                self.data[idx][2] += depamt
                print("Your Balance: ",self.data[idx][2])
                self.trans=self.trans.append( {
                    "AccNo": accno,
                    "Transaction Type": "Deposit",
                    "Amount": +depamt
                        
                    },ignore_index=True)
        else:
                self.data[idx][2] += depamt
                print("Your Balance: ",self.data[idx][2])
                self.trans=self.trans._append( {
                        "AccNo.": accno,
                        "Transaction Type": "Deposit",
                        "Amount": +depamt
                },ignore_index=True)

        nooftrans = self.trans["AccNo"].value_counts()[accno]
        if nooftrans == 0:
            self.creditscr({
                "AccNo": accno,
                "Credit": 10,
                "Membership": "None"
            },ignore_index=True)
        else:
            crdpts = nooftrans * 10
            if crdpts < 50:
                memship="None"
            elif crdpts >=50:
                memship="Silver"
            elif crdpts >= 100:
                memship="Gold"
            elif crdpts >=150:
                memship="Diamond" 
            self.creditscr({
                "AccNo": accno,
                "Credit": crdpts,
                "Membership": memship
            },ignore_index=True)


    def withdraw(self,accno,witamt):
        for i in self.data:
            if i[1] == accno:
                idx = self.data.index(i)
                break
        if witamt > self.data[idx][2]:
                print("Insufficiant Fund.")
        else:
            self.data[idx][2] -= witamt
            print("Your Balance: ",self.data[idx][2])
            self.trans=self.trans._append( {
                        "AccNo.": accno,
                        "Transaction Type": "Deposit",
                        "Amount": -witamt
                },ignore_index=True)

                

            
    def fd(self,accno,fdamt,yrs):
        rtn = 0
        for i in self.data:
            if i[1] == accno:
                idx = self.data.index(i)
                break
        
        if fdamt > 50000:
            rtn = (10000 * yrs) + self.data[idx][3]
            print("Your Return is: ",rtn)
        else:
            print ("FD should be above Rs.50000.")
                        
    def transaction(self):
         print(self.trans)