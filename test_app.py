import unittest

class TestApplication(unittest.TestCase):
    def test_application_message(self):
        message = "Hello from Jenkins CI/CD!"
        self.assertEqual(message, "Hello from Jenkins CI/CD!")

if __name__ == "__main__":
    unittest.main()