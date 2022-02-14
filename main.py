import requests
from bs4 import BeautifulSoup
import sys


def main():
    # define url, create soup and results, define page elements to be found
    alignment = input("Enter an alignment, options are: 'left', 'leftcenter', 'right-center' and 'right': ")
    url = "https://mediabiasfactcheck.com/%s/" % alignment
    page = requests.get(url)
    page_soup = BeautifulSoup(page.content, "html.parser")
    results = page_soup.find(id="mbfc-table")
    page_elements = results.find_all("td")

    # iterate through page elements, printing out all names and URLs of websites, given that is provided in HTML
    for page_element in page_elements:
        site_info = page_element.text
        print(site_info)

    input("Enter any key to quit: ")
    sys.exit()


if __name__ == "__main__":
    main()
