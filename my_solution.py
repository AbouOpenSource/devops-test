# Python code to check balanced parenthesis

import requests
import sys
import os

RUN_IN_DOCKER = os.environ.get('RUN_IN_DOCKER', False)

if RUN_IN_DOCKER:
    #adress container containing server
    URL = "http://server:5000/input"
else:
    URL = "http://localhost:5000/input"
from checker import checker

if __name__ == '__main__':
    if len(sys.argv) == 1:
        try:
            response = requests.get(URL)
            data = response.text
            if checker(data):
                print("INPUT: {} -- RESULT: OK!".format(data))
            else:
                print("INPUT: {} -- RESULT: BAD INPUT :(".format(data))
        except requests.exceptions.HTTPError as error:
            print("The server isn't launched")
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
