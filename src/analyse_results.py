import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('seaborn')

ANALYTICS_METHODS = {
    'google_analytics': 'Google Analytics',
    'matomo': 'Matomo',
    'plausible': 'Plausible',
    'site_improve': 'SiteImprove',
}


def plot_csrankings(filename: str = None):
    """
    Plots the percentage of universities (per country) that use Google Analytics.
    """
    df = pd.read_csv('output/crawl_output_csrankings.csv')
    per_country = df.groupby('country').agg(
        google_analytics=('google_analytics', 'sum'),
        total=('url', 'count'),
    )
    per_country['percentage'] = per_country['google_analytics'] / per_country['total'] * 100
    per_country = per_country[per_country['total'] >= 5].sort_values('percentage')

    plt.clf()
    fig, ax = plt.subplots(figsize=(11.2, 6.4))

    hbars = ax.barh(per_country.index, per_country['percentage'], label='Google Analytics usage (%)')
    labels = [
        ' {:d}% ({:d}/{:d})'.format(round(r['percentage']), r['google_analytics'], r['total'])
        for _, r in per_country.iterrows()
    ]
    ax.bar_label(hbars, labels=labels)

    ax.set_title('Wereldwijd gebruik van Google Analytics bij universiteiten')
    ax.set_xlabel('Google Analytics gebruik (%)')
    ax.set_xlim((0, 100))

    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)


def plot_dutch_municipalities(result_set: str, filename: str = None):
    """
    Plots the distribution of analytics methods being used by Dutch municipalities.
    """
    if result_set not in ('wikipedia', 'tracker'):
        raise ValueError(f'Result set \'{result_set}\' does not exist!')
    df = pd.read_csv(f'output/crawl_output_{result_set}.csv')

    if result_set == 'tracker':
        ANALYTICS_METHODS['gov_metric'] = 'GovMetric'

    municipalities = df[
        (df['type'] == 'Gemeente') &
        (df['country'] == 'Netherlands') &
        (~df['google_analytics'].isna())
    ]

    percentages = municipalities[list(ANALYTICS_METHODS)].mean() * 100

    data, labels = [], []

    for label, name in ANALYTICS_METHODS.items():
        data.append(percentages[label])
        labels.append(name)

    plt.clf()
    fig, ax = plt.subplots()

    ax.bar(labels, data)
    ax.set_ylabel('Gebruik analyticsmethoden (%)')
    ax.set_title('Gebruik analyticsmethoden bij Nederlandse gemeenten')

    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)

    if result_set == 'tracker':
        ANALYTICS_METHODS.pop('gov_metric')


def plot_universities_for_country(ax: plt.Axes, country: str, result_set: str):
    """
    Plots the distribution of analytics methods being used by universities in a specific country.
    """
    if country not in ('Netherlands', 'Germany'):
        raise ValueError(f'Country \'{country}\' does not exist!')

    if result_set not in ('wikipedia', 'tracker'):
        raise ValueError(f'Result set \'{result_set}\' does not exist!')

    df = pd.read_csv(f'output/crawl_output_{result_set}.csv')

    organisations = df[
        (df['country'] == country) &
        (df['type'].isin(['Hogeschool', 'Universiteit'])) &
        (~df['google_analytics'].isna())
    ]

    percentages = organisations[['type'] + list(ANALYTICS_METHODS)].groupby('type').mean() * 100

    locs = np.arange(len(percentages))
    width = 1 / (len(ANALYTICS_METHODS) + 1)

    for i, (label, name) in enumerate(ANALYTICS_METHODS.items()):
        current_locs = locs + (i - len(ANALYTICS_METHODS) / 2) * width
        tick_label = list(percentages.index) if i == len(ANALYTICS_METHODS) // 2 else None

        ax.bar(current_locs, percentages[label], width=width, align='edge', tick_label=tick_label, label=name)

    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
    ax.set_ylabel('Gebruik analyticsmethoden (%)')


def plot_universities(result_set: str, filename: str = None):
    """
    Plots the distribution of analytics methods being used by universities in The Netherlands and Germany.
    """
    if result_set not in ('wikipedia', 'tracker'):
        raise ValueError(f'Result set \'{result_set}\' does not exist!')

    fig, axes = plt.subplots(1, 2, sharey=True, figsize=(9.6, 4.8))

    plot_universities_for_country(axes[0], 'Netherlands', result_set)
    plot_universities_for_country(axes[1], 'Germany', result_set)

    axes[0].set_title('Universiteiten in Nederland')
    axes[1].set_title('Universiteiten in Duitsland')

    fig.suptitle('Gebruik analyticsmethoden bij universiteiten in Nederland en Duitsland')

    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)


def main():
    plot_csrankings('plot/worldwide.png')
    plot_dutch_municipalities('tracker', 'plot/municipalities.png')
    plot_universities('tracker', 'plot/universities_nl_de.png')


if __name__ == '__main__':
    main()
