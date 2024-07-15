def Get():
    api_token = ''
    with open('admin_token.txt') as f:
        api_token = f.read().strip()
    return api_token