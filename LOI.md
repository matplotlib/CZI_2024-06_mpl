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
bio-medical imaging, microscopy, and genomics.  Matplotlib is used by
researchers across the entire scientific workflow from initial data exploration
and visualization, to evaluating the output of AI/ML models, to publishing
finalized figures.

For the past 20 years Matplotlib has been maintained by a vibrant, primarily
volunteer, community.  However we have grown too big and widely used to
continue on solely volunteer effort.  For the past 42 months CZI EOSS support
for developers has had a positive effect on the project by complementing and
enabling, not replacing, volunteer work.  We propose to continue this effort.

The primary component of the proposed work is the continued maintenance of the
library and its community.  Maintenance covers a wide range of tasks including
triaging and fixing bugs, reviewing Pull Requests, tagging and building
releases, keeping the continuous integration services running, and mentoring
new contributors.  These tasks are essential for the project's health; though
each individually is small, they are frequently time critical and sometimes
tedious.  It is unfair and impractical to rely solely on volunteers to
accomplish such tasks.

A major improvement enabled by supported developers has been our transition to
a regular release schedule.  Currently, feature releases are now made at a
regular 2-per-year schedule, typically with 3 bugfix releases between them.
This regularity, roughly doubling our previous average rate, allows downstream
projects and users to rapidly benefit from ongoing improvements in Matplotlib.

In addition to on-going and routine maintenance, there are substantial but
incremental enhancements to Matplotlib that require long blocks of dedicated
effort to implement.  Without supported developers, such projects can drag out
for months to years or stall altogether.  Examples include fixing long-standing
rendering and performance issues, overhauling build systems to match the
changing Python ecosystem, homogenizing and smoothing the API, and new
user-facing functionality.  Projects to be pursued with the funding requested
here will be selected in consultation with downstream biomedical libraries.

Finally, supported developers improve the management of the project.  We now
have the time and bandwidth to make strategic decisions about the direction of
the project to ensure the long term health and viability of Matplotlib.  An
important part of project management is community management: fostering,
diversifying, and growing our community.  Supported developers are able to
perform outreach: attending conferences, mentoring sprints, or teaching
tutorials.  We must ensure that our community is open and welcoming to everyone
who wants to join, with opportunities to contribute in a spectrum of roles as
their interests and skills develop.

We propose to continue full support (1 FTE) for Elliott Sales de Andrade and
partial support (.15 FTE) for Thomas Caswell.  The effort will be split with
approximately .7 FTE for maintenance, .25 FTE for medium sized enhancements,
and .2 FTE for community and project management.


# Value to Biomedical Users

> Describe the expected value of the proposed work to the biomedical research
community (maximum of 250 words).

Scientific Python libraries in biomedical and other fields rely on Matplotlib
for visualization using Matplotlib as either a direct dependency or in their
documentation and standard user process.  These include other general purpose
tools, such as scikit-learn, networkx, pandas, xarray, and scikit-image that
are used by biomedical researchers, and biomedical-specific projects such
CellProfiler, scanpy, starfish, nipy, MNE-python, DeepLabCut.  In total CZI has
funded at least 32 proposals that depended on Matplotlib, including all of the
projects listed here.

The proposed work will help ensure the health and continuing growth of
Matplotlib as a foundational component.


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
in Python (over 1M monthly users) and is a mature library (20+ years old) with
over 1,500 individual code contributors.  In addition to being directly used by
scientists, it is a core dependency of libraries and applications that
implement domain-specific visualizations.  To aid users in discovering these
extensions we have been assigned a Trove classifier on PyPI [1].

Given the centrality of visualization to data analysis across all domains, no
single tool can satisfy all needs.  There are a range of tools not built on
Matplotlib (see https://pyviz.org/tools.html for a long but not exhaustive
list) that target use cases that Matplotlib is not well suited for.  Outside of
the Python ecosystem, a wide range of biomedical visualization libraries and
applications exist in R or Java.  Proprietary solutions such as MATLAB or
Tableau may also be used in various scientific fields.

Matplotib's ubiquity and maturity provide users with a stable and easily
understood tool on which to build both bespoke and reproducible visualizations.
Its availability in the Python ecosystem allows for direct integration with
various data processing and modelling tools in a familiar environment.

[1] https://pypi.org/search/?q=&o=&c=Framework+%3A%3A+Matplotlib

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

# Examples of Matplotlib: DO NOT INCLUDE
* [Deep Universal Probabilistic Programming](http://pyro.ai/) - used in
  examples and tutorials
* [SciPy: Fundamental Tools for Biomedical Research](https://scipy.org/) - used
  post-analysis
* [scikit-learn](https://scikit-learn.org/stable/) - used to visualize model
  results and effectiveness
* [Digital Biomarker Discovery Pipeline](https://dbdp.org/) - used to visualize
  digital biomarkers (sleep tracking, blood sugar monitoring, etc.)
* [DeepLabCut](http://www.mackenziemathislab.org/deeplabcut) - visualization of
  pose estimation
* [FastSurfer - a fast and accurate deep-learning based neuroimaging
  pipeline](https://deep-mi.org/research/fastsurfer/) - visualization of
  predictions and confusion matrix
* [bcbio-nextgen - Validated, scalable, community developed variant calling,
  RNA-seq and small RNA analysis](https://bcbio-nextgen.readthedocs.io/) - used
  for validation plots
* [Scanpy - Single-Cell Analysis in Python](https://scanpy.readthedocs.io/) -
  used for visualizing results of clustering, marker genes, etc.
* [phasorpy - analysis of fluorescence lifetime and hyperspectral images using
  the phasor approach](https://www.phasorpy.org/) - based on mpl
* [nilearn - Machine learning for NeuroImaging in
  Python](https://nilearn.github.io/stable/index.html) - plots glass brain,
  clustering results, object recognition, etc.
* [QIIME 2 - next-generation microbiome bioinformatics platform that is
  extensible, free, open source, and community developed](https://qiime2.org/)
  - used in various plugins for their needs
* [NumPy](https://numpy.org) - used for doc examples
* [Pandas - high-performance, easy-to-use data
  structures](https://pandas.pydata.org/) - used for various plots
* [scikit-image - Image processing in Python](https://scikit-image.org/) - used
  for doc examples
* [Xarray - N-D labeled arrays and datasets in Python](https://xarray.dev/) -
  used for plotting of datasets
* [PyMC3 - Bayesian Modeling in Python](https://docs.pymc.io/) - used for
  various statistical and in-algorithm plots
* [ArviZ - Exploratory analysis of Bayesian
  models](https://python.arviz.org/en/stable/) - used as default plotting
  backend
* [MDAnalysis - An object-oriented toolkit to analyze molecular dynamics
  trajectories](https://www.mdanalysis.org/) - used for examples and
  visualization
* [NetworkX - Network Analysis in Python](https://networkx.org/) - used to show
  network graphs
* [Nibabel - Access a multitude of neuroimaging data
  formats](https://nipy.org/nibabel/) - used for orthographic slice viewer
* [Orange Data Mining](https://orangedatamining.com/) - used for clusters and
  regressions
* [COMBINE lab - COMputational BIology and Network Evolution
  lab](http://combine-lab.github.io/) - used in various analyses
* [pyOpenMS - mass spectrometry, specifically for the analysis of proteomics
  and metabolomics data](https://pyopenms.readthedocs.io/) - used for
  domain-specific plots
* [MNE-Python - exploring, visualizing, and analyzing human neurophysiological
  data](https://mne.tools/stable/index.html) - used for siganls, topographies,
  images, and other domain-specific plots
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
* [Integrative Genomics Viewer](https://igv.org/doc/desktop/)
