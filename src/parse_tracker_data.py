import argparse
import os
import json
import re

import pandas as pd


ANALYTICS_URLS = {
    'google_analytics': ['google-analytics.com', 'googletagmanager.com'],
    'matomo': ['matomo', 'piwik'],
    'site_improve': ['siteimproveanalytics.com'],
    'plausible': ['plausible.io'],
    'gov_metric': ['govmetric.com'],
}


def normalize_url(url: str) -> str:
    """Normalizes a URL to a uniform representation without http(s)://, www. and trailing slash."""
    return re.sub(r'https?://(?:www.)?', '', url.rstrip('/'))


def read_tracker_data(tracker_dir: str) -> dict[str, dict[str, bool]]:
    """
    Reads all output files from the Tracker Data Collector and detects which analytics methods are used.
    """

    results = {}

    for tracker_file in os.listdir(tracker_dir):
        with open(os.path.join(tracker_dir, tracker_file)) as _file:
            tracker_data = json.load(_file)

        request_urls = [r['url'] for r in tracker_data['data']['requests']]
        results[normalize_url(tracker_data['initialUrl'])] = {
            analytics_name: any(
                analytics_url in request_url
                for analytics_url in analytics_urls
                for request_url in request_urls
            )
            for analytics_name, analytics_urls in ANALYTICS_URLS.items()
        }

    return results


def main(input_name: str, tracker_dir: str, output_name: str):
    """
    Reads a dataset from a CSV file, and retrieves all analytics methods as collected by the Tracker Data Collector.
    """

    data = pd.read_csv(input_name)
    tracker_data = read_tracker_data(tracker_dir)

    results = pd.DataFrame([
        tracker_data.get(normalize_url(url), {method: None for method in ANALYTICS_URLS})
        for url in data['url']
    ])

    output = pd.concat([data, results], axis=1)
    output.to_csv(output_name, index=False)

    # Get a basic first insight in the data
    print(results.describe())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check the Tracker Data Collector data for analytics methods')

    parser.add_argument('input', help='The input CSV file containing URLs')
    parser.add_argument('tracker_dir', help='The directory containing the Tracker Data Collector output')
    parser.add_argument('output', help='The destination of the output CSV file')

    args = parser.parse_args()

    main(args.input, args.tracker_dir, args.output)
