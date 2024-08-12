# 🎯 User Ranking System

This repository includes a solution for managing user rankings and progress in a ranking system. The `User` class provides methods to handle user progress and rank updates based on activity.

## 📝 Problem Description
Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.

### Business Rules:
- A user starts at rank -8 and can progress all the way to 8.
- There is no 0 (zero) rank. The next rank after -1 is 1.
- Users will complete activities. These activities also have ranks.
- Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
- The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of the activity
- A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next level
- Any remaining progress earned while in the previous rank will be applied towards the next rank's progress (we don't throw any progress away). The exception is if there is no other rank left to progress towards (Once you reach rank 8 there is no more progression).
- A user cannot progress beyond rank 8.
- The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error.

### The progress is scored like so:
- Completing an activity that is ranked the same as that of the user's will be worth 3 points
- Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
- Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
- Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The greater the difference between rankings the more the progression will be increased. The formula is 10 * d * d where d equals the difference in ranking between the activity and the user.

### Logic Examples:
- If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
- If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
- If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
- If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being upgraded to rank -7 and having earned 60 progress towards their next rank
- If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)

### Code Usage Examples:
```
user = User()
user.rank # => -8
user.progress # => 0
user.inc_progress(-7)
user.progress # => 10
user.inc_progress(-5) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
```

### Key Methods

- **`rank_difference(activity_rank)`**:
  - Calculates the difference in rank between the user and an activity's rank.

- **`inc_progress(activity_rank)`**:
  - Increments the user's progress based on the rank difference and updates the user's rank accordingly.

- **`update_rank_and_progress()`**:
  - Updates the user's rank and progress when the progress reaches or exceeds 100.

- **`next_rank(current_rank)`**:
  - Determines the next rank in the ranking system.

### Code Implementation

```python
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
```

### How It Works

- **Rank Difference Calculation**:
  - Determines how far the activity's rank is from the user's current rank and computes the progress accordingly.
  
- **Progress Increment**:
  - Based on the rank difference, the user's progress is incremented. Special cases handle progress increments for ranks that are either significantly higher or lower.

- **Rank Update**:
  - When progress reaches 100 or more, the user's rank is updated to the next rank, and the progress is reset.

- **Rank Progression**:
  - Uses a predefined list of ranks to determine the next rank.
