# Use an AI tool like ChatGPT or Copilot to generate a lambda function 
# that filters out all odd numbers from a list of IPL scores [101, 98, 120, 77, 88], 
# then test the code in your Python environment and paste the working code here.

ipl_scores = [101, 98, 120, 77, 88]

even_scores = list(filter(lambda score: score % 2 == 0, ipl_scores))

print(even_scores)