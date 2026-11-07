
candidates = [
    {
        "id": "C001",
        "name": "Arun",
        "skills": ["Python", "SQL", "ML"],
        "experience": 3,
        "score": 92,
        "priority": "High"
    },
    {
        "id": "C002",
        "name": "Bhavana",
        "skills": ["Java", "Spring", "SQL"],
        "experience": 5,
        "score": 85,
        "priority": "Medium"
    },
    {
        "id": "C003",
        "name": "Charan",
        "skills": ["Python", "ML", "AI", "SQL"],
        "experience": 4,
        "score": 95,
        "priority": "High"
    }
]


def get_candidates():
    return candidates


def check_eligibility(candidate, minimum_experience=2):
    return candidate["experience"] >= minimum_experience
