#Simple interest (EMI) inputs
amount=int(input("enter loan amount:"))
year=int(input("enter loan duration (in years):"))
annual_rate=0
N= year*12
# N=Total_number_of_monthly_installment
if (amount < 50000 ):
    annual_rate = 0.05
elif (amount <=100000):
    annual_rate=0.07
else:
    annual_rate=0.10
SI=(amount*annual_rate*year)/100
print (SI)

#if (EMI =  [[P x R x (1+R)^N] / [(1+R)^N – 1]])
EMI = ((amount*annual_rate*(1+annual_rate)**N)/((1+annual_rate)**N-1))
print(EMI)

