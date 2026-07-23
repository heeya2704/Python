# Build a recursive function format_number_short(n) that takes a number 
# (like a follower count on Instagram or YouTube) and returns it as a string 
# in short format: 1500 as '1.5K', 1200000 as '1.2M', 500 as '500'.

def format_number_short(n):
    if n < 1000:
        return str(n)
    elif n < 1000000:
        return f"{n / 1000:.1f}K"
    elif n < 1000000000:
        return f"{n / 1000000:.1f}M"
    else:
        return format_number_short(n / 1000)

print(format_number_short(500))
print(format_number_short(1500))
print(format_number_short(1200000))