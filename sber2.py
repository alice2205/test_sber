import requests

def main():
    base_url = 'https://postman-echo.com'
    response_home = requests.get(base_url)

    if response_home.status_code == 200:
        print("Успешно зашли на сайт:", base_url)
    else:
        print(f"Ошибка при заходе на сайт {base_url}: {response_home.status_code}")
        return  

    login_url = base_url + '/basic-auth'
    response_auth = requests.get(login_url, auth=("postman", "password"))

    if response_auth.status_code == 200:
        print("Успешная авторизация!")
        print(response_auth.json())
    else:
        print("Ошибка авторизации!", response_auth.text)


if __name__ == "__main__":
    main()