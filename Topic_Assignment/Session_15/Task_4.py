# Refactor the following buggy code to handle exceptions correctly 
# so it never crashes and always prints 'Thank you for using the calculator' 
# at the end, even if an exception occurs:<br><br>def calculate_average_rating(total_rating, num_reviews):
# <br> return total_rating / num_reviews<br>print(calculate_average_rating(500, 0))

def calculate_average_rating(total_rating, num_reviews):
    try:
        if num_reviews == 0:
            raise ValueError("Number of reviews cannot be zero.")
        return total_rating / num_reviews
    except ValueError as e:
        print(f"Error: {e}")
        return None
    finally:
        print("Thank you for using the calculator.")
        
# Example usage:
average_rating = calculate_average_rating(500, 0)