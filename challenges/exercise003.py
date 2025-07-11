# Create a list comprehension that processes a list of student scores to find all scores
# that are above the average, then calculate how many points each score is above the average.
# Round the differences to 1 decimal place.

scores = [85, 92, 78, 96, 88, 73, 91, 82, 89, 94]

# Write your list comprehension here:

#above_average_differences = 

average_score = sum(scores) / len(scores)
print (average_score)
above_averages = [score for score in scores if score > average_score]
print(above_averages)
difference= [round(score - average_score, 1) for score in above_averages]
print(difference)
difference2= [round(score - sum(scores) / len(scores), 1) for score in scores if score > average_score]
print(difference2)
# result wanted = [ results for list item in lists ]
# Expected results: [1.4, 8.4, 2.4, 7.4, 5.4, 10.4]