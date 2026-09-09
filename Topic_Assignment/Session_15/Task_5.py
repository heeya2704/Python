# Write a function called safe_divide_for_zomato that takes two numbers 
# (bill amount and number of people), uses try, except, else, and finally to 
# divide the bill and print the result, print a custom error if division by zero, 
# and always print 'Split calculation done' at the end.

def safe_divide_for_zomato(bill_amount, number_of_people):
    try:
        if number_of_people == 0:
            raise ValueError("Number of people cannot be zero.")
        result = bill_amount / number_of_people
    except ValueError as e:
        print(f"Error: {e}")
        result = None
    else:
        print(f"Each person should pay: {result}")
    finally:
        print("Split calculation done")
        
# Example usage:
bill_amount = float(input("Enter total bill amount: "))
number_of_people = int(input("Enter number of people: "))
safe_divide_for_zomato(bill_amount, number_of_people)