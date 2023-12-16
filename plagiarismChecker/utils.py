import requests
from bs4 import BeautifulSoup
import re


def scrape(string, user_agent):
    try:
        while True:
            print(string.get('text'))
            try:
                url = f"https://www.bing.com/search?q=%22{string.get('text')}%22"
                break
            except requests.exceptions.ConnectionError:
                pass
        print("Checking: ", url)

        headers = {
            'authority': 'www.bing.com',
            'user-agent': user_agent
        }

        response = requests.request("GET", url, headers=headers)
        soap = BeautifulSoup(response.text, "html.parser")
        links_info = soap.find("ol", id="b_results")
        links = links_info.find_all("h2")
        html_data = ''.join(str(item) for item in links)
        find_all_links = BeautifulSoup(html_data, 'html.parser')
        all_links_tags = find_all_links.find_all("a")
        print([web_links["href"] for web_links in all_links_tags])
        return {"links": [web_links["href"] for web_links in all_links_tags], "context": string.get("text"), "id": string.get("id")}
    except Exception as e:
        print(f"Error {string}: {e}")
        return {"links": [], "context": string}


def scrape_and_check(data, user_agent, context_data, response_cache):
    context = data.get("context")
    matched = False
    for links in data.get("links"):
        if links in response_cache:
            text = response_cache[links]
        else:
            try:
                while True:
                    try:
                        res = requests.get(links, headers={'user-agent': user_agent}, timeout=4)
                        break
                    except requests.exceptions.ConnectionError:
                        pass
                soup = BeautifulSoup(res.text, 'html.parser')
                text = soup.get_text()
                response_cache[links] = text
            except:
                continue

        if context in text:
            context_data[context] = {
                "web_url": links,
                "matched": True,
                "context": context,
                "id": data.get("id")
            }
            matched = True
            break
        print("Link: ", context, matched)

    if not matched:
        context_data[context] = {
            "web_url": "",
            "matched": False,
            "context": context,
            "id": data.get("id")
        }

