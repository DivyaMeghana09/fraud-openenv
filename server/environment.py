import random

class FraudEnv:
    def __init__(self):
        self.tasks = [
            {"level": "easy", "data": {"duration": 10, "frequency": 10}, "label": 1},
            {"level": "medium", "data": {"duration": 60, "frequency": 3}, "label": 0},
            {"level": "hard", "data": {"duration": 30, "frequency": 7}, "label": 1}
        ]
        self.step_count = 0

    def reset(self):
        self.current_task = random.choice(self.tasks)
        self.step_count = 0

        print("Task Level:", self.current_task["level"])

        return {
            "observation": self.current_task["data"],
            "reward": 0.0,
            "done": False
        }

    def step(self, action):
        correct = self.current_task["label"]

        # reward logic
        if action == correct:
            reward = 1.0
        else:
            reward = 0.0

        self.step_count += 1

        return {
            "observation": self.current_task["data"],
            "reward": reward,
            "done": True
        }