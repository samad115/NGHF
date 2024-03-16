import csv
class Process1:
    def registration(self,username,password,phoneno,pincode,city):
        self.uname=username
        self.pswd=password
        self.phno=phoneno
        self.pin=pincode
        self.city=city        
        with open('users.csv','a',newline='') as file:
            store=csv.writer(file)
            store.writerow([self.uname,self.pswd,self.phno,self.pin,self.city])
    def login(self,username,password):
        with open('users.csv','r',newline='') as file:
            read=csv.DictReader(file)
            for row in read:
                if row['uname']==username and row['pswd']==password:
                    return 1
            print('INVALID USERNAME AND PASSWORD') 