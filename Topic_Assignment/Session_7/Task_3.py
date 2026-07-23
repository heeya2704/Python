# Build a Python script that takes your Flipkart cart total and 
# applies the following logic: if total > 2000, print 'You get a 10% discount'; 
# elif total > 1000, print 'You get a 5% discount'; else print 'No discount available'.

cart_total = float(input("Enter your Flipkart cart total: "))

if cart_total > 2000:
    print("You get a 10% discount")
elif cart_total > 1000:
    print("You get a 5% discount")
else:
    print("No discount available")