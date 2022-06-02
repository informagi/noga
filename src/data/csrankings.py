from argparse import ArgumentParser
import re
import subprocess
from urllib.parse import urlparse
from typing import Optional

import tldextract
import pandas as pd
import pycountry
import whois


def country_code_to_full(code: str) -> Optional[str]:
    """
    Transforms a country code into the country's full name.
    """
    code = code.upper()
    if code == 'UK':
        return 'United Kingdom'
    if country := pycountry.countries.get(alpha_2=code):
        return country.name
    if country := pycountry.countries.get(alpha_3=code):
        return country.name
    return None


def get_country(domain: str) -> Optional[str]:
    """
    Given a domain name, tries to find out which country it belongs to.
    Does so by inspecting the TLD, and if that does not work, by using whois.
    """
    # Python whois does not support .edu domains correctly, so we do those ourselves.
    if domain.endswith('.edu'):
        r = subprocess.Popen(['whois', domain], stdout=subprocess.PIPE)
        text = r.stdout.read().decode()

        if match := re.search(r'Registrant:\n(?:\t[^\n]+\n)+\t([^\n]+)', text):
            code_or_country = match.group(1)
            return country_code_to_full(code_or_country) or code_or_country
        return None

    # Try to match based on the TLD
    if country := country_code_to_full(domain.split('.')[-1]):
        return country

    code_or_country = whois.whois(domain, command=True).country

    if code_or_country is None:
        return None

    return country_code_to_full(code_or_country) or code_or_country


def get_domain(url: str) -> str:
    """
    Extracts a domain from an URL.
    """
    extracted = tldextract.extract(url)
    return f'{extracted.domain}.{extracted.suffix}'


def clean_csrankings_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the CSRankings dataset, by finding all listed homepages, and
    verifying whether the corresponding domain name belongs to an academic
    institution. As a result, the output dataset should contain a list of
    homepages of academic institutions, combined with the institution's
    country.
    """
    num_entries = len(data)

    results = []
    domains_considered = set()

    for i, row in data.iterrows():
        university = row['affiliation']

        domain = get_domain(row['homepage'])
        scheme = urlparse(row['homepage']).scheme
        url = f'{scheme}://{domain}'

        if domain in domains_considered:
            continue

        domains_considered.add(domain)

        # Shortcut, as we know that .edu and .ac.XX are always bound
        # to academic instances
        parts = domain.split('.')
        if 'edu' in parts or 'ac' in parts:
            country = get_country(domain)
            results.append({
                'university': university,
                'url': url,
                'country': country,
            })
            continue

        # If we don't know, we simply have to ask the user if this is an
        # academic instance.
        x = input(f'[{i}/{num_entries}] {university}: {url}? ')
        if not x.startswith('n'):
            country = get_country(domain)
            results.append({
                'university': university,
                'url': url,
                'country': country,
            })

    return pd.DataFrame(results)


if __name__ == '__main__':
    parser = ArgumentParser(description='Cleans data for the CSRankings dataset')

    parser.add_argument('input', help='The input CSV file containing the raw CSRankings data')
    parser.add_argument('output', help='The destination of the cleaned data')

    args = parser.parse_args()

    result = clean_csrankings_data(pd.read_csv(args.input))
    result.to_csv(args.output, index=False)
