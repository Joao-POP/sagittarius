import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, "../")

import main

TEST_DATA_PATH = Path('test_data.json')

class TestErrorChecking(unittest.TestCase):
	def setUp(self):
		with open(TEST_DATA_PATH, "r", encoding="utf-8") as test_data_json:
			self.test_data = json.load(test_data_json)

	# "Should have detected too high an oil temperature"
	def test_check_for_errors(self):
		self.assertEqual(main.check_for_errors(self.test_data), [main.Error.OIL_TEMP_TOO_HIGH])

if __name__ == "__main__":
	unittest.main()