
print( f"NameError -  {type(NameError)} - {issubclass(NameError, BaseException)}")
try:
    print( "start cod")
    print(  10/0)
    print("no error")
except NameError:
    print( "we have an error")
except ZeroDivisionError:
    print( "we have an error")
    print( "code after capsule")
#_________________________________________________________________________________
def chek(var_1):
    if type(var_1)!=str:
        raise TypeError(f"Sorry,we can`t work with{type(var_1)},"f"we need class str")
    else:
        return var_1
first_var=5
chek(first_var)
#--------------------------------------------______________________________
class catError(Exception):
    def __str__(self):
        return f" такою кількістю грошей ви не купите котика"
def check_material(amout_money,limit_valuet):
    if amout_money>limit_valuet:
        return f"грошей достатньо"

    else:

        raise catError(amout_money)

money=1200
check_material(money,2500)




























#23456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100