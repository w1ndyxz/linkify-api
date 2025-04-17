import requests

# ur token
bearerToken = '847392|kA2gPmmWTTrAbB3OpCMYk4zeX6yUf8zQWEr1t9Gh'

choose = input("1. Create link\n2. Edit link\n3. Delete link\n4. Get link\nChoose: ")

def createLink(authorization: str, link: str, name: str, mode: str, browser_targeting: bool):
    """
    - authorization: Bearer token
    - link: your link
    - name: link name
    - mode: monetization 1 - off, 2 - low, 3 - high 
    - browser_targeting: browser targeting
    """
    url = "https://kernel.linkify.ru/api/links.create"
    response = requests.post(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Authorization": f'Bearer {authorization}',
    }, json={
        "link": link,
        "name": name,
        "mode": mode,
        "browser_targeting": browser_targeting
    })

    if response.status_code in [200, 201]:
        data = response.json()
        print(f'Your link: {data['link']}')
        print(f'Monetization: {data['type']}')
        print(f'Browser Targeting: {data['browser_targeting']}')
        print(f'Name link: {data['title']}')
        print(f'User uid: {data['uid']}')
        print(f'Created time: {data['time']}')
        print(f'Edited time: {data['edited_at']}')
        print(f'Created link: https://ify.ac/{data['hash']}')
        return True
        # print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Error: {response.status_code}\n{response.text}")
        return False

def editLink(authorization: str, id: int, name: str, mode: str, browser_targeting: bool):
    """
    - authorization: Bearer token
    - id: link id
    - name: link name
    - mode: monetization 1 - off, 2 - low, 3 - high 
    - browser_targeting: browser targeting
    """
    url = "https://kernel.linkify.ru/api/links.edit"
    response = requests.post(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Authorization": f'Bearer {authorization}',
    }, json={
        "id": id,
        "name": name,
        "mode": mode,
        "browser_targeting": browser_targeting
    })

    if response.status_code in [200, 201]:
        print(response.json())
        return True
    else:
        print(f"Error: {response.status_code}\n{response.text}")
        return False

def deleteLink(authorization: str, id: int):
    """
    - authorization: Bearer token
    - id: link id
    """
    url = "https://kernel.linkify.ru/api/links.delete"
    response = requests.post(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Authorization": f'Bearer {authorization}',
    }, json={
        "id": id,
    })

    if response.status_code in [200, 201]:
        print(response.json())
        return True
    else:
        print(f"Error: {response.status_code}\n{response.text}")
        return False

def getLinks(authorization: str, page: int):
    """
    - authorization: Bearer token
    - page: id
    """
    url = f"https://kernel.linkify.ru/api/links.get?page={page}"
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Authorization": f'Bearer {authorization}',
    })

    if response.status_code in [200, 201]:
        data = response.json()
        print(f'Total pages: {data['total_pages']}')
        print("-" * 40)
        for link in data["links"]:
            print(f"Link id: {link['id']}")
            print(f"Your link: {link['target']}")
            print(f"Name link: {link['title']}")
            print(f"Monetization: {link['type']}")
            print(f"Browser target: {bool(link['browser_targeting'])}")
            print(f"Views: {link['views']}")
            print(f"Earnings: {link['earnings']}")
            print(f"Conversions: {link['conversions']}")
            print(f"Alias: https://ify.ac/{link['alias']}")
            print(f"Created time: {link['created_at']}")
            print(f"Edited time: {link['edited_at']}")
            print("-" * 40)
        # print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        return True
    else:
        print(f"Error: {response.status_code}\n{response.text}")
        return False


if choose not in ['1', '2', '3', '4']:
    print('bruh')
elif choose == '1':
    link = input("Link: ")
    name = input("Link name: ")
    mode = input("Monetization: ")
    browser_targeting = input("Browser targeting (y/n): ").strip().lower() == 'y'
    createLink(
        authorization=bearerToken,
        link=link,
        name=name,
        mode=mode,
        browser_targeting=browser_targeting
    )
elif choose == '2':
    id_ = int(input("Link id: "))
    name = input("New link name: ")
    mode = input("Monetization: ")
    browser_targeting = input("Browser targeting? (y/n): ").strip().lower() == 'y'
    editLink(
        authorization=bearerToken,
        id=id_,
        name=name,
        mode=mode,
        browser_targeting=browser_targeting
    )
elif choose == '3':
    id_ = int(input("Link id: "))
    deleteLink(
        authorization=bearerToken,
        id=id_,
    )
elif choose == '4':
    page = int(input("Page num: "))
    getLinks(
        authorization=bearerToken,
        page=page
    )
