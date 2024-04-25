import requests
def get_synthetic_monitors_config():
   elk_username = 'pawankumar8819@hotmail.com'
   elk_password = 'Elkdyna@2024'
   elk_endpoint = 'https://c12f8edc0d5249aab3844895b6e7ba7a.us-east-1.aws.found.io:9243/app/synthetics'
   response = requests.get(elk_endpoint, auth=(elk_username, elk_password))
   if response.status_code == 200:
       return response.json()
   else:
       print(f"Failed to fetch synthetic monitors config. Status code: {response.status_code}")
       return None
synthetic_monitors_config = get_synthetic_monitors_config()
if synthetic_monitors_config:
   print(synthetic_monitors_config)