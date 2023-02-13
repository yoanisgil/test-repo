import sys
import json


if __name__ == "__main__":
    assert len(sys.argv) > 1
    json_object = json.load(open(sys.argv[1]))
    print(json_object["name"])

