from playwright.sync_api import sync_playwright
# from requests_html_playwright import HTMLSession
import re


url = 'https://www.ibood.com/s-nl/f/beeld-geluid/6119218'

headers = {
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0'
}


regex = re.compile(r'LG.*TV')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    page.wait_for_timeout(1000)

    elements = page.locator('h2').all_inner_texts()
    for element in elements:
        # text = element.inner_text()
        if regex.search(element):
            print(element)
            print(80*'-')

    page.wait_for_timeout(10000)
    browser.close()
