import webbrowser
import time
import os

# Path to Microsoft Edge (check if it's installed in this location)
edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

# Register Edge browser
webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))

# Open the URL in Edge
url = "https://yousseftrabelsi.streamlit.app/"
webbrowser.get("edge").open(url)

# Wait for 15 seconds
time.sleep(15)

# Close Edge browser
os.system("taskkill /F /IM msedge.exe")
