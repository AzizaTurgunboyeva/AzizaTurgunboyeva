from datetime import datetime
from json import dumps
from os import system
system("cls")

class Error (Exception):
    pass

class Bank_account():
    def __init__(self,balance:float, name:str,id:str,phone_number:str) :
        self.__balance = balance
        self.__name = name
        self.__id = id
        self.__phone_number = phone_number
        self.__pay_hist = {}
    def get_info(self) :
        return f"""         <<Ma'lumotlar>>
    Balans:  {self.__balance}
    Ism:     {self.__name}
    ID:      {self.__id}
    Tel:     {self.__phone_number}
    """

    
    def printhist(self):
        return dumps(self.__pay_hist,indent=4)
    
    def get_id(self):
        return{self.__id}
    def get_name(self):
            return {self.__name}
    def get_balance(self):
        return {self.__balance}

    def set_name(self,payee:str):
        if not payee.replace(" ", "").isalpha() and isinstance(payee,str):
            raise Error("Ism faqat harflardan iborat bo'lishi kerak.")

        self.__name = payee
        return self.__name
       
        
        
    def set_phone_number(self,payee_number:str):
        if len(payee_number)!= 17:
            return False
        
        if not payee_number.startswith('998'):
            return False
        
        list=[90,91,94,95,99,33,50]
        chunk = payee_number[4:6]
        if chunk in list:
            return True
        raise Error (f"Bunday kodli nomer {chunk} Uzbga tegishlimas")
    
    
    def add_balance(self,value:float):
        if self.__balance < 0:
            return False
        self.__balance += value
        return True
    
      
    def deduct_balance(self, value:float):
        if value < 0:
            return False
        
        if self.__balance - value < 0:
            return False
        self.__balance -= value
        return True
            
    def transfer(self,recipient,summa:float,start=2):
        if summa <= 0:
            return False
        
        if self.__balance <summa:
            return False
        self.__balance -= summa
        
        recipient.add_balance(summa)
        vaqt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        vaqt1=vaqt
        if vaqt1 in self.__pay_hist.keys():
            while vaqt1 in self.__pay_hist.keys():
                vaqt1 = vaqt + " "+str(start)
                start+=1


        self.__pay_hist[vaqt1]={
            "type" : "Chiquvchi",
            "name" : recipient.__name,
            "to" : recipient.__id,
            "when":vaqt,
            "summa" : summa
           
        }
        
        recipient.__pay_hist[vaqt1]={
            "type" : "Kiruvchi",
            "name" : self.__name,
            "to" : self.__id,
            "when":vaqt,
            "summa" : summa
           
        }
        self.__balance+=summa            

    
obj =Bank_account(70.0,"Aziza","16987",'998 40 999 99 99')
obj2=Bank_account(100.0,"Birbalo","123",'998 90 112 32 32')

obj2.transfer(obj,10)
obj.transfer(obj2,5)
obj.transfer(obj2,5)


print(obj.get_info())
print(obj.get_name())
print(obj.set_name('Kamola'))
print(obj.set_phone_number('998 90 987 76 54'))
print(obj.add_balance(100.0))
print(obj.deduct_balance(100.0))


print(obj.printhist())
print(obj2.printhist())


