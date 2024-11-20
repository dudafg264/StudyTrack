import requests
from datetime import datetime
import os

# Get Pixela credentials
USERNAME = os.getenv('USERNAME')
TOKEN = os.getenv('TOKEN')
GRAPH_ID = os.getenv('GRAPH_ID')

def status(response):
    if response.status_code == 200:
        print("Process completed successfully!")
    else:
        print(f"Error... Status code: {response.status_code}")

# Get today's date
today = datetime.now()
today_str = today.strftime("%Y%m%d")

# Set headers
headers = {
    "X-USER-TOKEN": TOKEN
}

# User input to choose action
response = input("Would you like to \n1.add a new study day\n2.update an existing one\n3.delete a record?\nType 1, 2 or 3: ")

if response == "1":
    # Add new study day
    pixel_config = {
        "date": today_str,
        "quantity": input("How many hours did you study today? "),
    }
    pixel_post = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
    response_post = requests.post(url=pixel_post, json=pixel_config, headers=headers)
    status(response_post)

elif response == "2":
    # Update existing record
    date_to_update = input("Enter the date of the record to update (format: YYYYMMDD): ")
    pixel_put_config = {
        "quantity": input("How many hours did you study on this day? "),
    }
    pixel_put = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"
    response_put = requests.put(url=pixel_put, json=pixel_put_config, headers=headers)
    status(response_put)

elif response == "3":
    # Delete record
    date_to_delete = input("Enter the date of the record to delete (format: YYYYMMDD): ")
    delete = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete}"
    response_delete = requests.delete(url=delete, headers=headers)
    status(response_delete)
