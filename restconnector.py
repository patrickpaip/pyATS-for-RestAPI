import requests
import json
from datetime import datetime

class DataConvertor():
    def stringToJson(self,x):
        return json.loads(x)
    def jsonToString(self,x,indent=1):
        return json.dumps(x,indent=indent)

class Validator():
    def isJSON(self,payload):
        try:
            json.loads(payload)
            return True
        except:
            return False
    
    def isInt(self,payload):
        try:
            return isinstance(payload,int)
        except:
            return False

    def isFloat(self,payload):
        try:
            return isinstance(payload,float)
        except:
            return False

    def isList(self,payload):
        try:
            return isinstance(payload,list)
        except:
            return False
            
    def isDict(self,payload):
        try:
            return isinstance(payload,dict)
        except:
            return False

    def isDate(self,payload,format="%Y-%m-%d"):
        try:
            datetime.strptime(payload,format)
            return True
        except:
            return False
    # CHECKS IF ATTRIBUTES EXIST IN PAYLOAD
    # COMPATIBLE WITH DICT AND LIST
    def checkAttribute(self,payload=[],attributes=[]):
        try:
            if(not isinstance(attributes,list)):
                return False
            for x in attributes:
                if(x not in payload):
                    return False
            return True
        except:
            return False

class RestConnector():
    # Used for GET Requests
    def get(self, url, params={}, headers={}, proxies={}):
        try:
            response = requests.get(
                url, headers=headers, params=params, proxies=proxies)
            if(response.status_code != 200):
                return {
                    "endpointinfo": {
                        "url": url,
                        "params": params,
                        "headers": headers,
                        "proxies": proxies
                    },
                    "status": 'failure',
                    "message": "Request Code {}".format(response.status_code),
                    "err_code": 1001,
                    "data": None
                }
            else:
                    return {
                        "endpointinfo": {
                            "url": url,
                            "params": params,
                            "headers": headers,
                            "proxies": proxies
                        },
                        "status": 'success',
                        "message": "None",
                        "err_code": 0,
                        "data": response.text
                    }
        except Exception as e:
            return {
                "endpointinfo": {
                    "url": url,
                    "params": params,
                    "headers": headers,
                    "proxies": proxies
                },
                "status": 'failure',
                "message": "Unable to Reach Endpoint",
                "err_code": 1002,
                "data": None
            }

    def post(self, url, params={}, headers={}, body={}, requestType="raw", proxies={}):
        try:
            if(requestType == "raw"):
                body = json.dumps(body)
            response = requests.post(
                url, headers=headers, params=params, data=body, proxies={})
            if(response.status_code != 200):
                return {
                    "endpointinfo": {
                        "url": url,
                        "params": params,
                        "headers": headers,
                        "proxies": proxies,
                        "requestType": requestType,
                        "body": body
                    },
                    "status": 'failure',
                    "message": "Request Code {}".format(response.status_code),
                    "err_code": 1001,
                    "data": None
                }
            else:
                return {
                    "endpointinfo": {
                        "url": url,
                        "params": params,
                        "headers": headers,
                        "proxies": proxies,
                        "requestType": requestType,
                        "body": body
                    },
                    "status": 'success',
                    "message": "None",
                    "err_code": 0,
                    "data": response.text
                }
        except Exception as e:
            return {
                "endpointinfo": {
                    "url": url,
                    "params": params,
                    "headers": headers,
                    "proxies": proxies,
                    "requestType": requestType,
                    "body": body
                },
                "status": 'failure',
                "message": "Unable to Reach Endpoint",
                "err_code": 1002,
                "data": None
            }
