import requests
import get_token
import products

def set_product_unpublish_status(token: str):
    # Endpoint for setting the product unpublish status
    url = products.SelectProductAndToURL(token) + '/unpublish.json'

    # Headers including the authorization token
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Making the POST request
    response = requests.post(url, headers=headers)

    # Checking the response
    if response.status_code == 200:
        print("Product unpublish status set successfully")
        print(response.json())
    else:
        print(f"Failed to set product unpublish status: {response.status_code} - {response.text}")
        if response.status_code == 400:
            error_message = response.json()
            print(f"Error message: {error_message}")
        return False

    return True

def set_product_publish_status(token: str, external_id: str, external_handle: str):
    # Endpoint for setting the product publish status to succeeded
    url = products.SelectProductAndToURL(token) + '/publishing_succeeded.json'

    # Headers including the authorization token
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Data to set the product publish status
    data = {
        "external": {
            "id": external_id,
            "handle": external_handle
        }
    }

    # Making the POST request
    response = requests.post(url, headers=headers, json=data)

    # Checking the response
    if response.status_code == 200:
        print("Product publish status set to succeeded successfully")
        print(response.json())
    else:
        print(f"Failed to set product publish status: {response.status_code} - {response.text}")
        if response.status_code == 400:
            error_message = response.json()
            print(f"Error message: {error_message}")
        return False

    return True

def main():
    # Get the API token from the file
    api_token = get_token.Get()

    # Status options
    status_options = ["unpublished", "published"]

    # Select the status
    status_index = input("Enter the status index (0 for unpublished, 1 for published): ")
    status = status_options[int(status_index)]

    if status == "unpublished":
        set_product_unpublish_status(api_token)
    elif status == "published":
        external_id = input("Enter the external ID: ")
        external_handle = input("Enter the external handle: ")
        set_product_publish_status(api_token, external_id, external_handle)

if __name__ == "__main__":
    main()
