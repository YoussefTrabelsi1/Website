import requests

url = "https://yousseftrabelsi.streamlit.app/"  # Replace with your actual URL

try:
    response = requests.get(url, timeout=10)
    print(f"App pinged successfully, status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error pinging app: {e}")
