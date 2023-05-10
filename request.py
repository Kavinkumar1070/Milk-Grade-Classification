import requests

url='http://localhost:5000/predict_api'
r=requests.post(url,json={'pH':6,'Temprature':41,'Taste':1,'Odor':1,'Fat ':1,'Turbidity':1,'Colour':250})

print(r.json())



