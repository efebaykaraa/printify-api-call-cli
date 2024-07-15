import requests

def SelectShopId(token: str) -> int:
    # The endpoint for listing shops
    url = 'https://api.printify.com/v1/shops.json'

    # Headers including the authorization token
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Making the GET request
    response = requests.get(url, headers=headers)

    # Checking the response
    if response.status_code == 200:
        shops = response.json()
        for i, shop in enumerate(shops):
            print(f"{i}: {shop['title']}")
    else:
        print(f"Failed to list shops: {response.status_code} - {response.text}")

    # Select one of the shops
    shop_id = input("Enter the shop index: ")
    return shops[int(shop_id)]['id']