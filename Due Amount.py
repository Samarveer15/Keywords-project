def calculate_due_amount(p, r,):
    
    i = (p* r ) / 100
    
    total_due = p + i
    return total_due


p = float(input("Enter the principal amount: "))
r= float(input("Enter the rate of interest: "))



due_amount = calculate_due_amount(p, r,)


print(f"The total amount due is: {due_amount}")