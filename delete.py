import requests
import get_token
import select_shops
import select_products

# Token from file
api_token = get_token.Get()

# Shop ID
shopId = select_shops.SelectShopId(api_token)

# Product ID
productId = select_products.SelectProductId(api_token, shopId)


# The endpoint for deleting a product
url = f'https://api.printify.com/v1/shops/{shopId}/products/{productId}.json'

# Headers including the authorization token
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

# Making the DELETE request
response = requests.delete(url, headers=headers)

# Checking the response
if response.status_code == 204:
    print("Product deleted successfully")
else:
    print(f"Failed to delete product: {response.status_code} - {response.text}")