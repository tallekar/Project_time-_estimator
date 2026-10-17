import pandas as pd
import random

data = []

for _ in range(500):  # change to 1000+
    employees = random.randint(2, 10)
    complexity = random.randint(2, 10)
    experience = random.randint(1, 8)
    modules = random.randint(4, 20)
    working_hours = random.randint(6, 9)
    deadline_pressure = random.randint(1, 3)
    requirement_clarity = random.randint(2, 5)

    # Formula to simulate real-world logic
    time_days = (
        complexity * 3 +
        modules * 1.2 -
        experience * 1.5 -
        employees * 0.8 +
        deadline_pressure * 2 +
        (6 - requirement_clarity) * 1.5
    )

    time_days = int(max(10, time_days + random.randint(-3, 3)))

    data.append([
        employees, complexity, experience, modules,
        working_hours, deadline_pressure, requirement_clarity,
        time_days
    ])

df = pd.DataFrame(data, columns=[
    "employees", "complexity", "experience", "modules",
    "working_hours", "deadline_pressure", "requirement_clarity",
    "time_days"
])

df.to_csv("project_data.csv", index=False)

print("Dataset created!")