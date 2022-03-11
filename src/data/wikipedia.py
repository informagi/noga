from argparse import ArgumentParser

from bs4 import BeautifulSoup
import pandas as pd
import requests
from tqdm import tqdm


def get_german_university_wiki_pages() -> list[dict[str, str]]:
    """
    Retrieves a list of German education institutes from the German Wikipedia overview.
    """
    german_wiki = 'https://de.wikipedia.org'
    german_uni_page = 'https://de.wikipedia.org/wiki/Liste_der_Hochschulen_in_Deutschland'

    r = requests.get(german_uni_page)
    soup = BeautifulSoup(r.text, features='html.parser')

    rows = soup.find('table').find_all('tr')[1:]

    return [
        {
            'url': german_wiki + path if (path := row.find('td').find('a')['href']).startswith('/wiki/') else path,
            'name': row.find('td').find('a').text.strip(),
            'type': 'Universiteit' if 'Uni' in row.find_all('td')[2].text else 'Hogeschool',
            'country': 'Germany',
        }
        for row in rows
    ]


def get_dutch_university_wiki_pages() -> list[dict[str, str]]:
    """
    Retrieves a list of Dutch education institutes from the Dutch Wikipedia overview.
    """
    dutch_wiki = 'https://nl.wikipedia.org'
    dutch_uni_page = 'https://nl.wikipedia.org/wiki/Lijst_van_hogeronderwijsinstellingen_in_Nederland'

    r = requests.get(dutch_uni_page)
    soup = BeautifulSoup(r.content.decode(), features='html.parser')

    lists = soup.find('div', attrs={'class': 'mw-parser-output'}).find_all('ul', recursive=False)

    get_uni_type = lambda t: 'Universiteit' if 'uni' in t.lower() else 'Hogeschool' if 'hoge' in t.lower() else 'Overig'

    wiki_urls = []
    for l in lists:
        items = l.find_all('li', recursive=False)
        for item in items:
            sub_list = item.find('ul')
            if sub_list is None:
                a = item.find('a')
                wiki_urls.append({
                    'url': dutch_wiki + a['href'] if a['href'].startswith('/wiki/') else a['href'],
                    'name': a.text.strip(),
                    'type': 'Universiteit',
                    'country': 'Netherlands',
                })
                continue

            uni_type = item.find('b').text.strip()

            for li in sub_list.find_all('li', recursive=False):
                a = li.find('a')

                if a.has_attr('class') and 'new' in a['class']:
                    wiki_urls.append({
                        'url': a['title'],
                        'name': a.text.strip(),
                        'type': get_uni_type(uni_type),
                        'country': 'Netherlands',
                    })
                else:
                    wiki_urls.append({
                        'url': dutch_wiki + path if (path := a['href']).startswith('/wiki/') else path,
                        'name': a.text.strip(),
                        'type': get_uni_type(uni_type),
                        'country': 'Netherlands',
                    })

    return wiki_urls


def get_dutch_municipality_wiki_pages() -> list[dict[str, str]]:
    """
    Retrieves a list of Dutch municipalities from the Dutch Wikipedia overview.
    """
    dutch_wiki = 'https://nl.wikipedia.org'
    municipalities_page = 'https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_gemeenten'

    r = requests.get(municipalities_page)
    soup = BeautifulSoup(r.text, features='html.parser')

    rows = soup.find('table').find_all('tr')[1:]

    return [
        {
            'url': dutch_wiki + a['href'] if (a := row.find('th').find_all('a')[-1])['href'].startswith('/wiki/') else a['href'],
            'name': row.find('th').find('span', attrs={'class': 'sortkey'}).text.strip(),
            'type': 'Gemeente',
            'country': 'Netherlands',
        }
        for row in rows
    ]


def extract_webpage_from_wiki_page(name: str, url: str) -> str:
    """
    Given an URL for a Wikipedia entry on an education institute or municipality, extracts the URL of the
    entity's webpage.
    """
    if not url.startswith('http'):
        print(f'[!] No data found for {name}...')
        return input(f'[*] Enter URL for {name} ({url}): ')

    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode(), features='html.parser')

    table = soup.find('table', attrs={'class': 'infobox'})

    if table is not None:
        trs = [tr for tr in table.find_all('tr')
               if tr.find('th') is not None and tr.find('th').text.strip() == 'Website'
               or tr.find('td') is not None and tr.find('td').text.strip() == 'Website']
        if len(trs) > 0:
            if a := trs[0].find('a'):
                return a['href']
            return trs[0].find_all('td')[-1].text.strip()

        other_link = table.find('a', string='Website')
        if other_link is not None:
            return other_link['href']

    weblinks_ids = ['Weblinks', 'Externe_links', 'Externe_link']

    for weblinks_id in weblinks_ids:
        weblinks_title = soup.find('span', attrs={'id': weblinks_id})

        if weblinks_title is not None:
            weblinks = weblinks_title.parent.find_next('ul')
            return weblinks.find('li').find('a')['href']

    print(f'[!] Not found for {name}... ')
    result = input(f'[*] Enter URL for {name} ({url}): ')

    if result:
        return result

    raise ValueError(f'Not found for {url}')


def clean_url(url: str) -> str:
    """
    Ensures a URL contains the http(s):// prefix.
    """
    if not url.startswith('http'):
        return 'https://' + url
    return url


def main(output_name: str):
    """
    Retrieves a list of URLs for:
    - German education institutes
    - Dutch education institutes
    - Dutch municipalities

    Does so by scraping the corresponding Wikipedia articles.
    """
    data = get_german_university_wiki_pages()
    data.extend(get_dutch_university_wiki_pages())
    data.extend(get_dutch_municipality_wiki_pages())

    for entry in tqdm(data, desc='Wiki page'):
        entry['url'] = clean_url(extract_webpage_from_wiki_page(entry['name'], entry['url']))

    output = pd.DataFrame(data)
    output.to_csv(output_name, index=False)


if __name__ == '__main__':
    parser = ArgumentParser(description='Retrieves university and municipality data from Wikipedia')

    parser.add_argument('output', help='The destination of the retrieved data')

    args = parser.parse_args()

    main(args.output)
