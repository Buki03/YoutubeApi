#import requests
from googleapiclient.discovery import build


api_key = 'AIzaSyBYEm6tajdTkAod1-X0dCDHvJyE8Nzw9oY'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
  part='statistics',
  forUsername='shafer5'
)

response = request.execute()
print(response)

# access_token = 'AIzaSyCFcxaRYuKJpUHYLGxOUkzkpXJHy6_d28o'
# url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet'

# headers = {
#     'Authorization': f'Bearer {access_token}'
# }

# response = requests.get(url, headers=headers)

# print(response.json())