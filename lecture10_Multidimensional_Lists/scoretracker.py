class ScoreTracker:
    def __init__(self):
        self.score_tracker = []

    def submit_score(self, score):
        #append the score to the score tracker
        self.score_tracker.append(score)
        #sort the scores in descending order
        self.score_tracker.sort(reverse=True)
        return None


    def get_scores(self):
        #return the top 5 scores using slicing [0:5:1]
        top_5_scores = self.score_tracker[0:5]
        print(f"Top 5 scores are:")
        # use enomurate to display the position of the score. Enumarete returns a tuple with the position and the score
        for position, score in enumerate(top_5_scores, 1):
            print(f"{position}: {score}")
        return 
    
score_tracker = ScoreTracker()

#submit scores
score_tracker.submit_score(1000)
score_tracker.submit_score(250)
score_tracker.submit_score(601)
score_tracker.submit_score(420)
score_tracker.submit_score(90000)
score_tracker.submit_score(555)
score_tracker.submit_score(390)
score_tracker.submit_score(720)

# display scores
print(f"Scores in the list are {score_tracker.score_tracker}\n")

# display top 5 scores
score_tracker.get_scores()