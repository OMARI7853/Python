print("=== Interest Calculator ===")
print("1. Simple Interest")
print("2. Compound Interest")

choice = input("Enter 1 for Simple Interest or 2 for Compound Interest: ")

P = float(input("Enter Principal amount: "))
R = float(input("Enter Annual Interest rate (%): "))
T = float(input("Enter Time in years: "))

if choice == "1":
    # Simple Interest
    SI = (P * R * T) / 100
    A = P + SI
    print("\n--- Simple Interest Result ---")
    print("Simple Interest:", round(SI, 2))
    print("Total Amount:", round(A, 2))

elif choice == "2":
    # Compound Interest (yearly)
    A = P * (1 + R/100)**T
    CI = A - P
    print("\n--- Compound Interest Result ---")
    print("Compound Interest:", round(CI, 2))
    print("Total Amount:", round(A, 2))

else:
    print("\nInvalid choice! Please choose 1 or 2.")
