from datetime import datetime, timedelta

class Task:
    def __init__(self, name, deadline, hardness_level, estimated_duration):
        self.name = name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.hardness_level = hardness_level
        self.estimated_duration = estimated_duration  # in hours
        self.days_remaining = (self.deadline - datetime.now()).days
        self.priority_score = self.calculate_priority()

    def calculate_priority(self):
        score = max(1, self.days_remaining - (self.estimated_duration // self.hardness_level))  # score could be negative
        if self.days_remaining < 3:
            score = max(1, self.days_remaining - score)  # deadline in less than three days bears more priority
        return score

    def __repr__(self):
        return (f"Task(name={self.name}, deadline={self.deadline.date()}, "
                f"days_remaining={self.days_remaining}, "
                f"hardness_level={self.hardness_level}, "
                f"duration={self.estimated_duration}, "
                f"priority={self.priority_score:.2f})")
