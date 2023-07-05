print("Interest Calculator")
print("-------------------")

p_amt = int(input("Enter the Amount(P):₹ "))
n_years = int(input("Enter Deposit period in Years(N): "))
intr_rate = int(input("Enter Interest Rate(R): "))/100

interest = p_amt * n_years * intr_rate

print(f"Interest of ₹{p_amt} for {n_years} Years is: ₹",interest)

