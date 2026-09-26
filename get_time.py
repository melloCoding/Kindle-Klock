# file: get_time.py
# purpose: just get the time and date and return it as easily readable json
# this is being done through an api because I do not want to rely on the kindle's clock
# as I have seen it be VERY unreliable during normal use
import requests
import json



api_url = "https://timeapi.io/api/v1/timezone/zone?timeZone=America%2FNew_York"

