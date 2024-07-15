import requests
from typing import Tuple, Optional
import shops

def SelectProductId(token: str) -> Tuple[int, int]:
    shop_id = shops.SelectShopId(token)

    # The endpoint for listing products in a shop
    url = f'https://api.printify.com/v1/shops/{shop_id}/products.json'

    # Headers including the authorization token
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Making the GET request
    response = requests.get(url, headers=headers)

    # Checking the response
    if response.status_code == 200:
        products = response.json()
        for i, product in enumerate(products['data']):
            print(f"{i}: {product['title']}")
    else:
        print(f"Failed to list products: {response.status_code} - {response.text}")

    # Select one of the products
    product_index = input("Enter the product index: ")
    return (shop_id, products['data'][int(product_index)]['id'])

def SelectProductAndToURL(token: str) -> str:
    shop_id, product_id = SelectProductId(token)
    return f'https://api.printify.com/v1/shops/{shop_id}/products/{product_id}'