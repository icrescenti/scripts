import sys
import requests
import json

def main():
	if (len(sys.argv) < 2):
		return

	r = requests.get(sys.argv[1])

	print("Status code: " + str(r.status_code) + " (" + str(requests.status_codes._codes[r.status_code][0]) + ")")
	print("--------------------")

	if(r.status_code == 200):
		pretty_json = json.loads(r.text)
		print(json.dumps(pretty_json, indent=2))
	else:
		print(r.text)

main()