from server.environment import FraudEnv

env = FraudEnv()

scores = []

for i in range(3):
    obs = env.reset()
    action = 1
    result = env.step(action)

    scores.append(result["reward"])

print("Scores:", scores)
print("Average Score:", sum(scores)/len(scores))