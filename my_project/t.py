import requests
from bs4 import BeautifulSoup

# Gửi yêu cầu đến URL của trang web
url = 'https://vnexpress.net/'
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công (status code 200)
if response.status_code == 200:
    html_content = response.content
    # Lưu HTML vào file
    with open('downloaded_page.html', 'wb') as file:
        file.write(html_content)

    # Dùng BeautifulSoup để phân tích nội dung HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup.prettify())
