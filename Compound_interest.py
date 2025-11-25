P = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate (%): "))
T = float(input("Enter time in years: "))

interest_type = input("Do you want Simple or Compound interest? ").lower()

if interest_type == "simple":
    # Simple Interest
    SI = (P * R * T) / 100
    A = P + SI
    print("Simple Interest:", SI)
    print("Total Amount:", A)

elif interest_type == "compound":
    # Compound Interest (yearly compounding)
    A = P * (1 + R/100)**T
    CI = A - P
    print("Compound Interest:", CI)
    print("Total Amount:", A)

else:
    print("Invalid choice! Please type 'simple' or 'compound'.")
