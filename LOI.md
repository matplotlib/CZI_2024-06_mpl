# Proposal Title

> Maximum of 60 characters, including spaces.

# Amount Requested

> Total budget amount requested in USD, including indirect costs; this number
should be between $100,000 USD and $400,000 USD total costs over a two-year
period.  Enter whole numbers only (no dollar signs, commas, or cents).

# Proposal Summary/Scope of Work

> Provide a short summary of the work being proposed (maximum of 500 words).

Matplotlib is the foundational data visualization library for the Scientific
Python Ecosystem, with over a million users, including researchers in
bio-medical imaging, microscopy, and genomics.  For the past 18 years
Matplotlib has been maintained by a vibrant, primarily volunteer, community.
However we have grown too big and widely used to continue on solely volunteer
effort.  For the past 15 months CZI EOSS support for developers has had a
positive effect on the project by complementing and enabling, not replacing,
volunteer work.  We propose to continue this effort.

The primary component of the proposed work is the continued maintenance of the
library.  Maintenance covers a wide range of tasks including triaging and
fixing bugs, reviewing Pull Requests, tagging and building releases, and
keeping the continuous integration services running.  These tasks are essential
for the project's health; though each individually is small, they are
frequently time critical and tedious.  It is unfair and impractical to rely
solely on volunteers to accomplish such tasks.

With only volunteer effort we had an ever growing backlog of Issues and PRs.
This risks missing good ideas and is both discouraging to new contributors and
distracting to the core developers.  In contrast, with CZI support we have
decreased our backlog of open Issues and PRs despite an increase in the number
submitted over the last 15 months.

In addition to on-going and routine maintenance, there are substantial, but
incremental, enhancements to Matplotlib that require long blocks of dedicated
effort to implement.  Without funding, this type of project can drag out for
months to years or stall altogether.  Examples include fixing long-standing
rendering and performance issues, deep-dive explanatory documentation,
homogenizing and smoothing the API, and new user-facing functionality.
Projects to be pursued with the funding requested here will be selected in
consultation with downstream biomedical libraries.

Finally, supported developers improve the management of the project.  We now
have the time and bandwidth to make strategic decisions about the direction of
the project to ensure the long term health and viability of Matplotlib.  An
important part of project management is community management: fostering,
diversifying, and growing our community.  This requires dedicated effort, over
long periods of time, beyond what can be sustained by volunteers alone.  We
must ensure that our community is open and welcoming to everyone who wants to
join, with opportunities to contribute in a spectrum of roles as their
interests and skills develop.

We propose to continue full support (1 FTE) for Elliott Sales de Andrade and
partial support (.2 FTE) for Thomas Caswell.  The effort will be split with
approximately .75 FTE for maintenance, .25 FTE for medium sized enhancements,
and .2 FTE for community and project management.


# Value to Biomedical Users

> Describe the expected value of the proposed work to the biomedical research
community (maximum of 250 words).

Scientific Python libraries in biomedical and other fields rely on Matplotlib
for visualization.  The proposed work will help ensure the health and
continuing growth of this foundational component.  Matplotlib is a direct
dependency of many other packages in the Scientific Python Ecosystem.  These
include other general purpose tools, such as scikit-learn, networkx, pandas,
xarray, and scikit-image that are used by biomedical researchers, and
biomedical-specific projects such CellProfiler, scanpy, starfish, nipy,
MNE-python, DeepCutLab.  All of these projects have received CZI funding.

# Open Source Software Projects

> Indicate the number of software projects involved in your proposal (up to
five).  Complete the table with the following information for each software
project.

## Software project name

* Main code repository (e.g., GitHub URL), enter in format
  https://www.example.com.
  https://github.com/matplotlib/matplotlib
* Homepage URL (if none, re-enter the main code repository URL), enter in
  format https://www.example.com.
  https://matplotlib.org

# Landscape Analysis

> Briefly describe the other software tools (either proprietary or open source)
that the audience for this proposal primarily uses.  How do the software
project(s) in this proposal compare to these other tools in terms of user base
size, usage, and maturity?  How do existing tools and the project(s) in this
proposal interact?  (maximum of 250 words)

Matplotlib is the most widely used and de-facto standard visualization library
in Python (over 1M monthly users) and is a mature library (18+ years old) with
over 1,250 individual code contributors.  In addition to being directly used by
scientists, it is a core dependency of libraries and applications that
implement domain-specific visualizations.  To aid users in discovering these
extensions we have been assigned a Trove classifier on PyPI [1].

Given the centrality of visualization to data analysis across all domains, no
single tool can satisfy all needs.  There are a range of tools not built on
Matplotlib (see https://pyviz.org/tools.html for a long but not exhaustive
list) that target use cases that Matplotlib is not well suited for.

[1] https://pypi.org/search/?q=&o=&c=Framework+%3A%3A+Matplotlib

Other options:

* [MR sequence diagrams in Python](https://pypi.org/project/mrsd/)
* [A package for simulating polysome profiles from Ribo-Seq
  data](https://pypi.org/project/polyan/)
* [MSA visualization python package for sequence
  analysis](https://pypi.org/project/pyMSAviz/)
* [Use interactive matplotlib to label images for
  classification](https://pypi.org/project/mpl-image-labeller/)
* [A tool for plotting CAFE5 gene family expansion/contraction
  result](https://pypi.org/project/cafeplotter/)
* [A complete processing pipeline for anatomical neuronal
  tracing](https://pypi.org/project/braintracer/)
* [Context specific and dynamic gene regulatory network reconstruction and
  analysis](https://pypi.org/project/dictys/)

Non-Python:

* ggplot in R
* Excel
* Tableau?
* [Integrative Genomics
  Viewer](https://software.broadinstitute.org/software/igv/)

# Category

> Choose the two categories that best describe the software project(s) audience:

* Bioinformatics
* Single-cell biology
* Structural biology
* Clinical research
* Genomics
* Neuroscience
* Infectious disease
* Imaging
* Data management and workflows
* Machine learning and data analysis
* Visualization

# Previous funding:

* Have you ever received grant funding from CZI, the Wellcome Trust, or the
  Kavli Foundation?  Select Yes or No.  YES
* Please check the box(es) of the organization(s) from which you received
  funding.  CZI
* Did you previously apply for funding under the CZI EOSS program?  Select Yes
  or No.  YES
  * If yes, have you previously received funding under the CZI EOSS program?  If
    yes, please provide your application ID in the format EOSS1-0000000001.
    EOSS-0000000100, EOSS3-0000000149, EOSS4-0000000187
