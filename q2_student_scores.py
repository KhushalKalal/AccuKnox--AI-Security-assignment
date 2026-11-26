import requests
import matplotlib.pyplot as plt

# Assumption: the selected demo API provides user data rather than test scores.
# We derive a deterministic demo score from age to demonstrate API retrieval,
# average calculation, and visualization as required by the assignment.
url = "https://dummyjson.com/users"
response = requests.get(url, timeout=20)

if response.status_code == 200:
    data = response.json()
    students = []
    scores = []

    for user in data.get("users", [])[:10]:
        students.append(user["firstName"])
        scores.append((user["age"] * 2) % 101)

    average_score = sum(scores) / len(scores)

    print("Student Scores:")
    for name, score in zip(students, scores):
        print(f"{name}: {score}")

    print(f"\nAverage Score: {average_score:.2f}")

    plt.bar(students, scores)
    plt.xlabel("Students")
    plt.ylabel("Test Score")
    plt.title("Student Test Scores")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("student_scores.png")
    plt.show()
else:
    print("Failed to fetch data.")
    print("Status Code:", response.status_code)
