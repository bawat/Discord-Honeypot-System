import requests
import json
import os

_HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
}


def refresh_token(token_file):
    path = os.path.join('Tokens', token_file)
    with open(path, 'r') as f:
        data = json.load(f)

    response = requests.post(
        'https://discord.com/api/v9/auth/login',
        json={'login': data['email'], 'password': data['password']},
        headers=_HEADERS
    )
    result = response.json()

    if response.status_code == 200 and 'token' in result:
        data['token'] = result['token']
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        return result['token']

    if 'captcha_key' in result:
        print(f"[TOKEN_REFRESH] Refresh blocked by captcha for {token_file}.")
    elif 'mfa' in result:
        print(f"[TOKEN_REFRESH] Refresh requires MFA for {token_file}.")
    else:
        print(f"[TOKEN_REFRESH] Refresh failed for {token_file}: {response.status_code} {result}")

    return None
