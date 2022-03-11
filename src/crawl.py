import argparse
import re
from typing import Dict

from bs4 import BeautifulSoup
import pandas as pd
import requests
from tqdm import tqdm

requests.packages.urllib3.disable_warnings()

# Types
Pattern = dict[str, list[str]]


GA_PATTERNS: Pattern = {
    'script': [
        r'google-analytics.com/analytics',
        r'googletagmanager.com/gtm',
        r'googletagmanager.com/gtag',
        r'google_tag',
        r'gtm.*\.js',
        r'gtag.*\.js',
    ],
    'iframe': [
        r'googletagmanager.com/ns.html',
    ],
}

MATOMO_PATTERNS: Pattern = {
    'script': [
        r'_mtm',
        r'matomo',
        r'piwik',
    ],
}

SITEIMPROVE_PATTERNS: Pattern = {
    'script': [
        r'siteimproveanalytics.com'
    ]
}

PLAUSIBLE_PATTERNS: Pattern = {
    'script': [
        r'plausible.io',
    ]
}

ALL_PATTERNS: dict[str, Pattern] = {
    'google_analytics': GA_PATTERNS,
    'matomo': MATOMO_PATTERNS,
    'site_improve': SITEIMPROVE_PATTERNS,
    'plausible': PLAUSIBLE_PATTERNS,
}


def has_tracking_method(soup: BeautifulSoup, method: Pattern) -> bool:
    """
    Checks whether a webpage contains a tracking method, by iterating over all
    possible ways the tracking method can be included in the page.
    """
    for tag, patterns in method.items():
        for el in soup.find_all(tag):
            for pattern in patterns:
                if re.search(pattern, str(el)):
                    return True

    return False


def crawl_webpage(url: str, verify: bool = True) -> Dict[str, bool]:
    """
    Crawls a webpage to find out which tracking methods it uses.

    :param url: the URL to crawl
    :param verify: whether or not to verify the SSL certificate
    """
    r = requests.get(url, timeout=5, verify=verify)

    soup = BeautifulSoup(r.text, features='html.parser')

    return {
        method_name: has_tracking_method(soup, method)
        for method_name, method in ALL_PATTERNS.items()
    }


def get_tracking_methods(url: str) -> dict[str, bool]:
    """
    Crawls a webpage to find out which tracking methods it uses.

    Tries different combinations of http/https with and without www. prefix,
    to ensure we don't accidentally used the wrong URL. If none of the
    combinations works, we try disabling SSL certificate checking to see if
    that fixes the problem.

    :param url: the URL to crawl
    """
    base_url = re.sub(r'https?://(?:www.)?', 'https://', url)

    # URLs might not always have the correct protocol and format with or without www.
    # So, we try all combinations...
    urls = [
        base_url,
        base_url.replace('https://', 'https://www.'),
        base_url.replace('https://', 'http://'),
        base_url.replace('https://', 'http://www.'),
    ]

    for attempt in urls:
        try:
            return crawl_webpage(attempt)
        except:
            continue

    # If none of the URLs works, we might have a misconfigured SSL certificate.
    # By setting verify=False, we can still try to retrieve the webpage.
    for attempt in urls:
        try:
            return crawl_webpage(attempt, verify=False)
        except:
            continue

    return {method: None for method in ALL_PATTERNS}


def main(input_name: str, output_name: str):
    """
    Reads a dataset from a CSV file, and crawls all URLs to find tracking methods.
    """
    data = pd.read_csv(input_name)

    results = pd.DataFrame([
        get_tracking_methods(url)
        for url in tqdm(data['url'], desc='Website')
    ])

    output = pd.concat([data, results], axis=1)
    output.to_csv(output_name, index=False)

    # Get a basic first insight in the data
    print(results.describe())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crawl a set of URLs to detect tracking methods')

    parser.add_argument('input', help='The input CSV file containing URLs')
    parser.add_argument('output', help='The destination of the output CSV file')

    args = parser.parse_args()

    main(args.input, args.output)
