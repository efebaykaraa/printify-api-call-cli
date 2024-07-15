import requests
import get_token
import products

def update_product_status(token: str, url: str, new_status: str):
    # Headers including the authorization token
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Data to update the product status
    data = {
        "status": new_status
    }

    # Making the PUT request
    response = requests.put(url, headers=headers, json=data)

    # Checking the response
    if response.status_code == 200:
        print("Product status updated to published successfully")
    else:
        error_message = response.json()
        if response.status_code == 400:
            if error_message.get("errors", {}).get("reason") == "Product is disabled for editing":
                print("The product is disabled for editing. Please ensure the product is enabled or contact Printify support.")
            else:
                print(f"Failed to update product status: {response.status_code} - {response.text}")

# Token from file
api_token = get_token.Get()

# Get the product URL
url = products.SelectProductAndToURL(api_token)

# Status to update the product to
status = input("Enter the status (unpublished, publishing, published): ").strip()

# Update the product status
update_product_status(api_token, url, status)