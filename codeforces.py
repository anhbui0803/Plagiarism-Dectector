import requests
from datetime import datetime
import random
import string
import hashlib
from urllib.parse import urlencode
from collections import OrderedDict
import json
from scrapeSol import *

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def getRequest(methodName, parameter):
    url = 'https://codeforces.com/api/' + methodName
    key = 'bfe498f058a6a1293e2573d0453bc4a700da3dad'
    secret = '3a79525fbce7d21321c792ee41d099a7edd21822'
    parameter['apiKey'] = key
    parameter['time'] = str(int(datetime.now().timestamp()))
    parameter = OrderedDict(sorted(parameter.items()))

    rand = get_random_alphanumeric_string(6)
    hashStr = rand + '/' + methodName + '?' + urlencode(parameter) + '#' + secret

    # print(hashStr)
    parameter['apiSig'] = rand + hashlib.sha512(hashStr.encode('utf-8')).hexdigest()
    # print(parameter)

    return requests.get(url, params = parameter).json()

if __name__ == "__main__":
    parameter = {"contestId": "413925"}
    # 152946507
    resultJson = getRequest("contest.status", parameter)
    finalJson = json.dumps(resultJson, indent = 4, ensure_ascii = False)
    
    with open("testing.json", "w", encoding = "utf-8") as outfile:
        outfile.write(finalJson)
    
    pointsDict = []
    with open("testing.json", "r", encoding = "utf-8") as json_file:
        data = json.load(json_file)
        for item in data["result"]:
            if (item["verdict"] == "OK"):
                index = item["problem"]["index"]
                subID = item["id"]
                handle = item["author"]["members"][0]["handle"]
                points = item["points"]
                scrapeSol(index, subID, handle)
                
        
        # writing to a auto generate file
        # (index bài)_(submission id)_(handle).txt
        # fileName = index + subID + handle
        # with open(fileName, "w", encoding = "utf-8") as f:
        #     f.write()
    
    
# Data cần lấy ra
    # submission id
    # index bài
    # handle người nộp
    # verdict: "OK" hoặc "PARTIAL"
    # => Lưu vào file .txt, định dạng: (index bài)_(submission id)_(handle)