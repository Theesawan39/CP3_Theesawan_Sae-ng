totalPrice=float(input("total="))
def VatCalculate(totalPrice): 
    Result=totalPrice+(totalPrice*7/100)
    return Result
print(VatCalculate(totalPrice))