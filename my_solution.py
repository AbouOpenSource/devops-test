# Python code to check balanced parenthesis

import requests
import sys

from checker import checker

URL = "http://localhost:5000/input"
if __name__ == '__main__':
    if len(sys.argv) == 1:
        try:
            response = requests.get(URL)
            data = response.text
            if checker(data):
                print("FROM WEB")
                print("INPUT: {} -- RESULT: OK!".format(data))
            else:
                print("FROM WEB")
                print("INPUT: {} -- RESULT: BAD INPUT :(".format(data))
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)

    else:
        data = sys.argv[1:]
        data = "".join(data).strip()
        if checker(data):
            print("FROM INPUT")
            print("INPUT: {} -- RESULT: OK!".format(data))
        else:
            print("FROM INPUT")
            print("INPUT: {} -- RESULT: BAD INPUT :(".format(data))
