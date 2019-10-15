
﻿# # pyATS-for-RestAPI
A Reference for applying request library along with PyATS for Rest API Testing

    class Validator():
	    isJSON(payload):
	    isInt(payload):
	    isFloat(payload):
	    isList(payload):
	    isDict(payload):
	    isDate(payload,format="%Y-%m-%d"):
	    checkAttribute(payload=[],attributes=[]):
	    
    class DataConvertor():
        def stringToJson(x)
        def jsonToString(x,indent=1)

    class RestConnector():
      def get(url, params={}, headers={}, proxies={})
      def post(url, params={}, headers={}, body={}, requestType="raw", proxies={})
	    
	    







