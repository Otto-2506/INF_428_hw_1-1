import random
import unittest

def generate_random_data(department_count=5, user_range=(10, 200), threat_range=(0, 90), importance_range=(1, 5)):
    departments = []
    for _ in range(department_count):
        users = random.randint(user_range[0], user_range[1])
        threat_scores = [random.randint(threat_range[0], threat_range[1]) for _ in range(users)]
        importance = random.randint(importance_range[0], importance_range[1])
        departments.append({
            "users": users,
            "threat_scores": threat_scores,
            "importance": importance
        })
    return departments

def calculate_aggregated_threat_score(departments):
    total_weighted_score = 0
    total_importance = 0
    
    for department in departments:
        if len(department["threat_scores"]) == 0:
            continue
        
        avg_threat_score = sum(department["threat_scores"]) / len(department["threat_scores"])
        weighted_score = avg_threat_score * department["importance"]
        total_weighted_score += weighted_score
        total_importance += department["importance"]
    
    if total_importance == 0:
        return 0
    
    aggregated_score = total_weighted_score / total_importance
    return min(90, max(0, aggregated_score))

class TestCyberSecurityScore(unittest.TestCase):
    
    def test_aggregated_score_no_outliers(self):
        departments = generate_random_data(department_count=5, user_range=(10, 200), threat_range=(50, 60), importance_range=(3, 3))
        score = calculate_aggregated_threat_score(departments)
        print(f"Test 'test_aggregated_score_no_outliers': {score}")
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)

    def test_aggregated_score_with_high_variance(self):
        departments = generate_random_data(department_count=5, user_range=(50, 150), threat_range=(0, 90), importance_range=(2, 5))
        score = calculate_aggregated_threat_score(departments)
        print(f"Test 'test_aggregated_score_with_high_variance': {score}")
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)
    
    def test_aggregated_score_with_uneven_importance(self):
        departments = generate_random_data(department_count=5, user_range=(50, 150), threat_range=(0, 90), importance_range=(1, 5))
        score = calculate_aggregated_threat_score(departments)
        print(f"Test 'test_aggregated_score_with_uneven_importance': {score}")
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)

    def test_edge_case_min_values(self):
        departments = [{"users": 10, "threat_scores": [0]*10, "importance": 1} for _ in range(5)]
        score = calculate_aggregated_threat_score(departments)
        print(f"Test 'test_edge_case_min_values': {score}")
        self.assertEqual(score, 0)

    def test_edge_case_max_values(self):
        departments = [{"users": 200, "threat_scores": [90]*200, "importance": 5} for _ in range(5)]
        score = calculate_aggregated_threat_score(departments)
        print(f"Test 'test_edge_case_max_values': {score}")
        self.assertEqual(score, 90)

    def test_no_users(self):
        departments = [{"users": 0, "threat_scores": [], "importance": 3} for _ in range(5)]
        score = calculate_aggregated_threat_score(departments)
        print(f"Test 'test_no_users': {score}")
        self.assertEqual(score, 0)

if __name__ == "__main__":
    unittest.main()
