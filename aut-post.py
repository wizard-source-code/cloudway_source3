import requests
import time

url = 'https://wordpress-1291025-4684693.cloudwaysapps.com/wp-admin/admin.php?page=wp-mail-smtp-tools&tab=test'
headers = {
    'Host': 'wordpress-1291025-4684693.cloudwaysapps.com',
    'Cookie': 'wordpress_sec_2e73b304987ab86c993073a2a80d1501=gladiat00r-user2%40intigriti.me%7C1720706270%7CJS8uoJzmI5ahlr3JpuU5hR5Mus3d1HiL5QT2Pgta2dG%7Ca101105db9a6026baf0cbffd7543ea8fa27179cdee21748308b789b52bca793a; wp-settings-time-1=1720534746; wordpress_test_cookie=WP%20Cookie%20check; breeze_folder_name=799748587e50919ffababcc330a4bf0cc1f6ac83; wordpress_logged_in_2e73b304987ab86c993073a2a80d1501=gladiat00r-user2%40intigriti.me%7C1720706270%7CJS8uoJzmI5ahlr3JpuU5hR5Mus3d1HiL5QT2Pgta2dG%7C1108729392b6c22547a6840fa44d5b746e80d5d8e16c84824cbc0510d473f182; mcfw-wp-user-cookie=MXw1fDE0LDE3LDIyLDI4LDI5LDQxLDU2LDU4LDYxLDYzfDM5ODI3XzRlMDYwZGQ2N2IyM2U5NWEwNWRiZWRjNzA3MzRjM2VlNjFjZTliODlkOTM0YzMwNDY1NTE1NTM0YWFhMzY5YTg%3D; mcfw-bypass-cookie=d6672f69ac116c0b6732a68ff0675a9c42db027b99cb65258525720d66a2bfd5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://wordpress-12910251291025-4684693.cloudwaysapps.com/wp-admin/admin.php?page=wp-mail-smtp-tools',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://wordpress-1291025-4684693.cloudwaysapps.com',
    'Upgrade-Insecure-Requests': '2',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=1',
    'Te': 'trailers'
}

# Define the payload
payload = {
    '_wpnonce': '715b78b9ab',
    '_wp_http_referer': '/wp-admin/admin.php?page=wp-mail-smtp-tools',
    'wp-mail-smtp[test][email]': 'gladiat00r-user2@intigriti.me',
    'wp-mail-smtp[test][html]': 'yes',
    'wp-mail-smtp-post': '1'
}

# Initialize the counter
counter = 0

def send_post_request():
    global counter
    try:
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            counter += 1
            print(f'200 OK response received {counter}.')
            return True
        else:
            print(f'Unexpected response: {response.status_code} - {response.text}')
            return False
    except requests.RequestException as e:
        print(f'Request failed: {e}')
        return False

def main():
    while True:
        if send_post_request():
            time.sleep(1)
        else:
            time.sleep(5)

if __name__ == '__main__':
    main()
