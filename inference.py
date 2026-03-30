from server.environment import FraudEnv

env = FraudEnv()

total_score = 0

for i in range(3):
    print("\n--- Episode", i+1, "---")

    obs = env.reset()
    print("Observation:", obs)

    action = 1

    result = env.step(action)
    print("Result:", result)

    total_score += result["reward"]

print("\nFinal Score:", total_score)