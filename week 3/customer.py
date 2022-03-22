class customer:
    
    def __init__(self,name,adharCard,PhoneNum,pannum,Dob,Address,Account_num):
        self.name=name
        self.adharCard=adharCard
        self.PhoneNum=PhoneNum
        self.Dob=Dob
        self.pannum=pannum
        self.Address=Address
        self.Account_num=Account_num
        self.bs=bs
        
    def updateAccount(self,name,adharCard,PhoneNum,Dob,Address,Account_num):
        pass
    
    def createAccount(self,name,adharCard,PhoneNum,Dob,Address,Account_num):
        pass
    
    def BankStatement(self,bs):
        return bs