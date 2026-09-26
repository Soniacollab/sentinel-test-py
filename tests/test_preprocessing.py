import unittest

from app.preprocessing import clean_user_input


class CleanUserInputTests(unittest.TestCase):
    def test_normalizes_username_and_score(self):
        result = clean_user_input({"username": "  Alice ", "user_score": "85.5"})

        self.assertEqual(result["username"], "alice")
        self.assertEqual(result["user_score"], 85.5)

    def test_missing_score_defaults_to_zero(self):
        result = clean_user_input({"username": "Alice"})

        self.assertEqual(result["user_score"], 0.0)

    def test_none_score_defaults_to_zero(self):
        result = clean_user_input({"username": "Alice", "user_score": None})

        self.assertEqual(result["user_score"], 0.0)

    def test_empty_score_defaults_to_zero(self):
        result = clean_user_input({"username": "Alice", "user_score": ""})

        self.assertEqual(result["user_score"], 0.0)


if __name__ == "__main__":
    unittest.main()