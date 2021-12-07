import requests
session = requests.Session()
print(session.cookies.get_dict())
response = session.get('https://stackoverflow.com/questions/25091976/python-requests-get-cookies')
print(session.cookies.get_dict())