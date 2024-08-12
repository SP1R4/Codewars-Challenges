class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def rank_difference(self, activity_rank):
        # Calculate the difference in rank between the user and the activity
        if self.rank * activity_rank > 0:
            return activity_rank - self.rank
        elif self.rank < 0 < activity_rank:
            return activity_rank - self.rank - 1
        elif self.rank > 0 > activity_rank:
            return activity_rank - self.rank + 1
        else:
            return activity_rank - self.rank

    def inc_progress(self, activity_rank):
        if activity_rank not in [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]:
            raise ValueError("Invalid activity rank")

        if self.rank == 8:
            return

        difference = self.rank_difference(activity_rank)

        if difference <= -2:
            return
        elif difference == -1:
            self.progress += 1
        elif difference == 0:
            self.progress += 3
        elif difference > 0:
            self.progress += 10 * difference * difference

        self.update_rank_and_progress()

    def update_rank_and_progress(self):
        while self.progress >= 100:
            self.progress -= 100
            self.rank = self.next_rank(self.rank)
            if self.rank == 8:
                self.progress = 0
                break

    def next_rank(self, current_rank):
        ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        index = ranks.index(current_rank)
        if index < len(ranks) - 1:
            return ranks[index + 1]
        return current_rank