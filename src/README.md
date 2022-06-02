# NoGA analysis code

In this directory, you can find the code used for the experiments in which we analysed the analytics usage of university and municipality websites.

## Poetry

We used [Poetry](https://python-poetry.org/) for dependency management. To run the code in this repository, download Poetry and install the dependencies using the command:

    poetry install

Then, you can either start a shell in this virtual environment using:

    poetry shell

Or, you can run single commands in the virtual environment using:

    poetry run python3 script.py

## Data

We ran three different experiments, for which we collected the datasets from two different sources.

1. To perform an analysis of universities worldwide, we used the CSRankings dataset.
2. To perform an analysis of Dutch and German universities, as well as Dutch municipalities, we scraped the URLs from Wikipedia.

The data collection is contained within the `data` directory.

### CSRankings

[CSRankings](https://csrankings.org) offers a database of researchers and publications from Computer Science institutions all around the world. To obtain a list of URLs for universities worldwide, we found all homepages of researchers contained in the CSRankings database, and kept only those that refer to a university domain. In more detail, we performed the following steps:

1. We downloaded a full list of researchers, alongside their affiliation and the URL of their homepage, from the [CSRankings GitHub repository](https://github.com/emeryberger/CSRankings).
2. For each researcher, we took their homepage, and decided whether this homepage is hosted on a university website. To do so, we used some heuristics (e.g. whether the domain ends with `.edu`, or whether it contains the academic suffix `*.ac.*`). For cases that could not be decided automatically, we manually confirmed whether the domain belongs to an academic institution.
3. We kept all the domains of homepages that were hosted on an academic institution, assuming that the university's homepage is hosted at the root of that domain.

   For instance, if we have the homepage https://cs.ru.nl/~johndoe/, we add https://ru.nl to the list of university websites.

This procedure is contained in the script `data/csrankings.py`. To generate the CSRankings dataset, we used the following command:

    python3 data/csrankings.py data/csrankings_raw.csv data/csrankings.csv

### Wikipedia

For Dutch universities, German universities and Dutch municipalities, we created a set of custom scrapers that:

1. Retrieve a list of Wikipedia entries from the corresponding Wikipedia article ([Dutch universities](https://nl.wikipedia.org/wiki/Lijst_van_hogeronderwijsinstellingen_in_Nederland), [German universities](https://de.wikipedia.org/wiki/Liste_der_Hochschulen_in_Deutschland) and [Dutch municipalities](https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_gemeenten))
2. For each Wikipedia entry, retrieves the corresponding article and extracts the URL.
3. If we cannot automatically extract the URL (e.g. if a municipality has no Wikipedia article), we manually enter it.

To scrape all URLs from Wikipedia, we used the following command:

    python3 data/wikipedia.py data/wikipedia.csv

## Crawlers

Given a list of URLs from the datasets described above, we'd like to be able to determine which analytics methods are used on each domain. To do so, we used two different analysis methods: a static analysis and a dynamic analysis.

### Static analysis

The static analysis is done using a simple crawler. For each URL in the input, we retrieve the corresponding webpage, and find scripts that indicate that an analysis method is being used. For instance, we look for scripts with the URL `googletagmanager.com` to find Google Analytics, and we look for the `_mtm` variable to detect Matomo scripts. This simple, static crawler is defined in the `crawl.py` script. To crawl the Wikipedia dataset, we used the following command:

    python3 crawl.py data/wikipedia.csv output/crawl_output_wikipedia.csv

### Dynamic analysis

The static analysis suffered from an inability to handle webpages that were generated dynamically using JavaScript. This includes Single Page Applications using ReactJS or AngularJS, but also pages in which the analytics script is only loaded after a popup was shown or accepted. To improve the accuracy of our analysis, we also used a dynamic crawler in the form of the [DuckDuckGo Tracker Radar Collector](https://github.com/duckduckgo/tracker-radar-collector).

The Tracker Radar Collector is a browser-based crawler, which supports the execution of scripts and other dynamic page content. It is meant to capture third party requests, which is ideal for our use case. To use it for our purposes, we simply ran the collector on our list of URLs, and for each page we obtained a list of outgoing requests. Please refer to the Tracker Radar Collector repository for information on how to run it.

We could parse the collector's output (in the `tracker_crawl_data` directory) and join the results to our existing Wikipedia dataset, using the `parse_tracker_data.py` script, with the following command:

    python3 parse_tracker_data.py data/wikipedia.csv tracker_crawl_data output/crawl_output_tracker.csv

## Analysis

To analyse the results and generate the correct figures for our blogpost, we used the `analyse_results.py` script.

    python3 analyse_results.py
