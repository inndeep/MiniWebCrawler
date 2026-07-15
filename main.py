import argparse
from email.mime import text

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def user_input():
    parser = argparse.ArgumentParser(description="Python Web Crawler")
    parser.add_argument("-u","--url",dest="target_url",required=True,help="Enter target url")
    return parser.parse_args()


def send_request(target_url):
    try:
        response = requests.get(target_url)
        if not (response.status_code == 200):
            print(f"Status code is :{response.status_code}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(e)


def web_crawler_func(text_response, base_url):
    soup = BeautifulSoup(text_response, "lxml")
    link_list = set()
    for link in soup.find_all("a", href=True):
        extracted_href = link.get("href")
        if not extracted_href:
            continue
        clean_url = urljoin(base_url, extracted_href)
        link_list.add(clean_url)
    js_list = set()
    for file in soup.find_all("script", src=True):
        extracted_js = file.get("src")
        if not extracted_js:
            continue
        clean_js = urljoin(base_url, extracted_js)
        js_list.add(clean_js)
    form_list = set()
    for file in soup.find_all("form", action=True):
        extracted_form = file.get("action")
        if not extracted_form:
            continue
        clean_form = urljoin(base_url, extracted_form)
        form_list.add(clean_form)

    return link_list, js_list, form_list


def print_result(js_files, links, forms):
    # Terminal Renk Kodları
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'  # Rengi normale döndürmek için kritik!

    if js_files:
        print(f"{GREEN}[+] JAVASCRIPT FILES{RESET}")
        print("-" * 50)
        for js in js_files:
            print(f"{YELLOW}{js}{RESET}")
        print()

    if links:
        print(f"{GREEN}[+] LINKS{RESET}")
        print("-" * 50)
        for link in links:
            print(link) # Normal linkleri terminalin varsayılan renginde bıraktık
        print()

    if forms:
        print(f"{GREEN}[+] FORMS (DATA TARGETS){RESET}")
        print("-" * 50)
        for form in forms:
            print(f"{RED}{form}{RESET}")
        print()

args = user_input()
base_url = args.target_url

text_response = send_request(base_url)

if text_response:
    links, js_files, forms = web_crawler_func(text_response, base_url)
    print_result(js_files, links, forms)
else:
    print("[-] The target site could not be reached or there was no response.")
