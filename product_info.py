import requests
from typing import Optional
import products
import get_token
import pyperclip

def GetProductInfo(token: str) -> Optional[dict]:
    url = products.SelectProductAndToURL(token) + '.json'

    # Headers including the authorization token
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Making the GET request
    response = requests.get(url, headers=headers)

    # Ensuring the response encoding is set to UTF-8
    response.encoding = 'utf-8'

    # Checking the response
    if response.status_code == 200:
        product_info = response.json()
        return product_info
    else:
        print(f"Failed to retrieve product info: {response.status_code} - {response.text}")
        return None

def SelectInfoFromProduct(product_info: dict) -> None:
    if not product_info:
        print("No product information available.")
        return

    keys = list(product_info.keys())
    for i, key in enumerate(keys):
        print(f"{i}: {key}")

    while True:
        try:
            selected_indices = input("Enter the indices of the information you want to see, separated by commas: ")
            selected_indices = [int(index.strip()) for index in selected_indices.split(',')]
            if all(0 <= index < len(keys) for index in selected_indices):
                break
            else:
                print("Invalid indices. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

    selected_info = {keys[index]: product_info[keys[index]] for index in selected_indices}
    print("\nCopied To The Clipboard:\n")
    for key, value in selected_info.items():
        print(f"{key}: {value}")
        pyperclip.copy(f"{value}")

# Example usage
api_token = get_token.Get()
product_info = GetProductInfo(api_token)
SelectInfoFromProduct(product_info)