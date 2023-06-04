from bidict import bidict


class Matches:
    matches=bidict({1:'I',5:'V',10:'X',50:'L',100:'C'})

m=Matches()
print(m.matches.inverse['I'])


class Converter:
    @staticmethod
    def roman_to_arabic(value):
        pass
    @staticmethod
    def arabic_to_roman(value):
        pass


class RomanNum:
    def __init__(self,value):
        self.romanvalue=0
        self.arabicvalue=0
        if isinstance(value,str):
            self.arabicvalue=10 # это заглушка , тебе нужно будет это перевести с помощью алгоритма 
            self.romanvalue='X'
        elif isinstance(value,int): 
            self.arabicvalue=10
            self.romanvalue='X' # это заглушка , тебе нужно будет это перевести с помощью алгоритма 
    def __add__(self,value):
        if isinstance(value,RomanNum):
            return RomanNum(value.arabicvalue+self.arabicvalue)
        elif isinstance(value,int):
            return RomanNum(value+self.arabicvalue)
        

# a=RomanNum(10)
# b=RomanNum(10)
# c=a+b
# print(c.arabicvalue)
'''
1) Сделать алгоритмы конвертации 
2) Сделать хорошую архитектуру см стр. 20 
'''