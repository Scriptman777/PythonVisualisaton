import requests

# Get response from the random.org API - 20 numbers from 1 to 10.
# API documentation: https://www.random.org/clients/http/
response = requests.get('https://www.random.org/integers/?num=20&min=1&max=10&col=1&base=10&format=plain&rnd=new')
# Get content from response, in this case it is a byte string, so it needs to be decoded
content = response.content.decode("utf-8") 
# Numbers are separated by newline characters
numbers = content.split('\n')
# Last item is empty, sinc string ends with a newline
numbers.remove('')
# Priting the response will show HTTP code, this might be useful for debugging
print(response)
# Result is a list of random numbers
print(numbers)

