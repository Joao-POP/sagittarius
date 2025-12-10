import json
from sys import stderr
from pprint import pp
from enum import Enum, IntEnum

# print(f"Engine temperature too high: {eng["temp"]} >= {SafeThreshold.MAX_ENG_TEMP}, shutdown is recommended.", file=stderr)

class SafeThreshold(IntEnum):
	MAX_OIL_TEMP = 70
	MAX_ENG_TEMP = 100

class Error(Enum):
	TEMP_TOO_HIGH = 1

def check_for_errors(data):
	errors = []

	eng = data["engine"]

	if eng["temp"] >= SafeThreshold.MAX_ENG_TEMP:
		pass

	return errors

def report_errors(errors):
	for e in errors:
		print(e)

def append(data, errors):
	pass

def main():
	with open("data.json", "r", encoding="utf-8") as json_data:
		data = json.load(json_data)

		errors = check_for_errors(data)

		if errors:
			report(errors)
			append(data, errors)
	return

if __name__ == "__main__":
	main()