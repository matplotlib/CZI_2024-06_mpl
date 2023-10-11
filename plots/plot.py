# plotting
import datetime
import json

with open('gh_dump.json', 'r') as fin:
    d_issues = json.load(fin)

# Avoid backport PRs.
d_issues = [i for i in d_issues if i['user']['id'] != 39504233]


def split_issuse_from_pr(all_issues):
    issues = []
    prs = []

    for issue in all_issues:
        if 'pull_request' in issue:
            prs.append(issue)
        else:
            issues.append(issue)

    return issues, prs


issues, prs = split_issuse_from_pr(d_issues)

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


def plot_by(gh_issues, *, ax=None, freq="M", label, show_net=True, show_rolling=False):
    opened = pd.Series(
        1,
        index=[
            datetime.datetime.strptime(p["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            for p in gh_issues
        ],
    )
    closed = pd.Series(
        -1,
        index=[
            datetime.datetime.strptime(p["closed_at"], "%Y-%m-%dT%H:%M:%SZ")
            for p in gh_issues
            if p["state"] != "open"
        ],
    )
    all_at = pd.concat([closed, opened])
    opened_by, closed_by = map(
        lambda x: x.groupby(pd.Grouper(freq=freq)), (opened, closed)
    )
    if ax is None:
        fig, ax = plt.subplots()
    if show_net:
        all_at.sort_index().cumsum().plot(lw=2, ax=ax, label=f"net open {label}")
    (close_step,) = ax.step(
        closed_by.sum().index,
        closed_by.sum().values,
        where="pre",
        label=f"{label} closed/{freq}",
    )
    (open_step,) = ax.step(
        opened_by.sum().index,
        opened_by.sum().values,
        where="pre",
        label=f"{label} opened/{freq}",
    )
    if show_rolling:
        for data, step in [(opened_by, open_step), (closed_by, close_step)]:
            ax.plot(
                data.sum().rolling(3).mean().index,
                data.sum().rolling(3).mean().values,
                color=step.get_color(),
                lw=2,
            )

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.legend()


try:
    with open('gh_releases.json', 'r') as fin:
        releases = json.load(fin)
    names = releases['names']
    dates = releases['dates']
except FileNotFoundError:
    # Try to fetch a list of Matplotlib releases and their dates
    # from https://api.github.com/repos/matplotlib/matplotlib/releases
    import urllib.request

    url = 'https://api.github.com/repos/matplotlib/matplotlib/releases'
    url += '?per_page=100'
    data = json.loads(urllib.request.urlopen(url, timeout=1).read().decode())

    dates = []
    names = []
    for item in data:
        if 'rc' not in item['tag_name'] and 'b' not in item['tag_name']:
            dates.append(item['published_at'].split("T")[0])
            names.append(item['tag_name'])

    with open('gh_releases.json', 'w') as fin:
        json.dump({'names': names, 'dates': dates}, fin)

# Convert date strings (e.g. 2014-10-18) to datetime
dates = [datetime.datetime.strptime(d, "%Y-%m-%d") for d in dates]

minors = [d for n, d in zip(names, dates) if n.endswith('.0')]
micros = [d for n, d in zip(names, dates) if not n.endswith('.0')]

fig, ax = plt.subplots(1, 2, layout='constrained', figsize=(25, 12))
plot_by(issues, ax=ax[0], label='Issues')
plot_by(prs, ax=ax[1], label='PRs')
for a in ax:
    a.xaxis.grid()
    a.vlines(minors, -100, 100, color='r')
    a.vlines(micros, -50, 50, color='k', alpha=0.1)
fig.savefig('fig1.png')


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


data = {
    "Pull Requests opened": [1656, 1752],
    "Pull Requests closed": [1613, 1775],
    "Issues opened": [795, 1108],
    "Issues closed": [756, 999],
}
labels = ["2019", "2020"]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, sharey=True)

for ax, typ in zip((ax1, ax2), ["Pull Requests", "Issues"]):
    open_lab = f"{typ} opened"
    close_lab = f"{typ} closed"
    rects2 = ax.bar(
        x - width / 2,
        data[open_lab],
        width,
        label='opened',
        color="k",
        edgecolor="w",
        hatch="/",
    )
    rects1 = ax.bar(
        x + width / 2,
        data[close_lab],
        width,
        label='closed',
        color="w",
        edgecolor="k",
        hatch="\\",
    )
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.set_xlabel("Year")
    ax.set_title(typ)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
ax2.legend(ncol=2)

ax1.set_ylabel("#")
ax1.set_ylim(top=2000)
fig.set_size_inches(6.3, 2.75)

fig.savefig('fig2.png')
plt.show()
# ax2.bar(['2019', '2020'], data['issue closed'], color='C2', width=.7)
# ax2.bar(['2019', '2020'], data['issue opened'], color='C3', width=.5)
