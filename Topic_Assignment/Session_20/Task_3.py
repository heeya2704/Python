# Create a Movie class with a private attribute _rating (float between 0 and 10). 
# Write getter and setter methods for _rating. The setter should only allow values 
# between 0 and 10; if an invalid value is given, print an error message.
# Constraint: Do not allow direct access to _rating outside the class.

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self._rating = 0.0
        self.set_rating(rating)

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        if 0.0 <= rating <= 10.0:
            self._rating = rating
        else:
            print(f"Error: Invalid rating '{rating}'. Rating must be between 0 and 10.")

# Example usage:
movie = Movie("Inception", 8.8)
print(f"Movie: {movie.title}, Rating: {movie.get_rating()}")

print("\nAttempting to set invalid rating (12.5):")
movie.set_rating(12.5)

print("\nAttempting to set valid rating (9.0):")
movie.set_rating(9.0)
print(f"Movie: {movie.title}, Updated Rating: {movie.get_rating()}")
