import requests
import get_token
import products

# Token from file
api_token = get_token.Get()

# The endpoint for deleting a product
url = products.SelectProductAndToURL(api_token) + '.json'

# Headers including the authorization token
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

# Making the DELETE request
response = requests.delete(url, headers=headers)

# Checking the response
if response.status_code == 200:
    print("Product deleted successfully")
else:
    print(f"Failed to delete product: {response.status_code} - {response.text}")