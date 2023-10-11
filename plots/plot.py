# plotting
import json

with open('/tmp/gh_dump.json', 'r') as fin:
    d_issues = json.load(fin)


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
        label=f"{label}s closed/{freq}",
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

    ax.legend()

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
