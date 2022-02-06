import requests

# Get data from API. More info: https://gorest.co.in/
response = requests.get('https://gorest.co.in/public/v1/users')
# Get JSON from response
json_response = response.json()
# This JSON has two parts 'meta' and 'data'. Take just the data portion
json_data = json_response.get('data')
# Create a dictionary
gender_count = {'male': 0, 'female': 0}
# Go through the data, each user object is a JSON
for user in json_data:
    gender = user.get('gender')
    if gender == 'male':
        gender_count['male'] = gender_count['male'] + 1
    if gender == 'female':
        gender_count['female'] = gender_count['female'] + 1
# Final data
print(gender_count)