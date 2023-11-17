# Progress Report

> If the grant is still active, provide a short summary of progress towards the
> deliverables (maximum of 250 words).


# Proposal Purpose

> Describe the purpose of the proposal in one sentence (maximum of 200
> characters including spaces).  Example: To develop a comprehensive, validated
> atlas of the human kidney at single-cell resolution open to the entire
> scientific and clinical community.


# Proposal Summary

> Provide a short summary of the application (maximum of 500 words)
> (auto-filled from LOI; update if needed)



Matplotlib is the foundational data visualization library for the Scientific
Python Ecosystem, with over a million users, including researchers in
bio-medical imaging, microscopy, and genomics.  Matplotlib is used by
researchers across the entire scientific workflow from initial data exploration
and visualization, to evaluating the output of AI/ML models, to publishing
finalized figures.


For the past 20 years Matplotlib has been
maintained by a vibrant, primarily volunteer, community.  However we have grown
too big and widely used to continue on solely volunteer effort.  For the past
42 months CZI EOSS support for developers has had a positive effect on the
project by complementing and enabling, not replacing, volunteer work.  We
propose to continue this effort.


The primary component of the
proposed work is the continued maintenance of the library and its community.
Maintenance covers a wide range of tasks including triaging and fixing bugs,
reviewing Pull Requests, tagging and building releases, keeping the continuous
integration services running, and mentoring new contributors.  These tasks are
essential for the project's health; though each individually is small, they are
frequently time critical and sometimes tedious.  It is unfair and impractical
to rely solely on volunteers to accomplish such tasks.


A major
improvement enabled by supported developers has been our transition to a
regular release schedule.  Currently, feature releases are now made at a
regular 2-per-year schedule, typically with 3 bugfix releases between them.
This regularity, roughly doubling our previous average rate, allows downstream
projects and users to rapidly benefit from ongoing improvements in
Matplotlib.


In addition to on-going and routine maintenance,
there are substantial but incremental enhancements to Matplotlib that require
long blocks of dedicated effort to implement.  Without supported developers,
such projects can drag out for months to years or stall altogether.  Examples
include fixing long-standing rendering and performance issues, overhauling
build systems to match the changing Python ecosystem, homogenizing and
smoothing the API, and new user-facing functionality.  Projects to be pursued
with the funding requested here will be selected in consultation with
downstream biomedical libraries.


Finally, supported developers
improve the management of the project.  We now have the time and bandwidth to
make strategic decisions about the direction of the project to ensure the long
term health and viability of Matplotlib.  An important part of project
management is community management: fostering, diversifying, and growing our
community.  Supported developers are able to perform outreach: attending
conferences, mentoring sprints, or teaching tutorials.  We must ensure that our
community is open and welcoming to everyone who wants to join, with
opportunities to contribute in a spectrum of roles as their interests and
skills develop.


We propose to continue full support (1 FTE) for
Elliott Sales de Andrade and partial support (.15 FTE) for Thomas Caswell.  The
effort will be split with approximately .7 FTE for maintenance, .25 FTE for
medium sized enhancements, and .2 FTE for community and project
management.


# work Plan

> A description of the proposed work for which funding is being requested,
> including resources the applicants will provide that are not part of the
> requested funding. For software development-related work (e.g., engineering,
> product design, user research), specify how the work fits into the existing
> software project roadmap. For community outreach related activities (e.g.,
> sprints, training), specify how these activities will be organized, the
> target audience, and expected outcomes (maximum of 750 words)


# Milestones and Deliverables

> List expected milestones and deliverables, and their expected timeline. Be
> specific and include where possible any goals for metrics the software
> project(s) are expected to reach upon completion of the grant. Please use a
> third-person voice (maximum of 500 words).

# Existing Support

> List active and recently completed (previous two calendar years) financial or
> in-kind support for the software project(s), including duration, total costs
> in USD, and source of funding. Include any previous funding for these
> software projects received from CZI, Wellcome, and/or Kavli outside of the
> EOSS program (maximum of 250 words).


# Landscape Analysis

> Describe the other software tools (either proprietary or open source) that
> the audience for this proposal primarily uses. How do the software project(s)
> in this proposal compare to these other tools in terms of user base size,
> usage, and maturity? How do existing tools and the project(s) in this
> proposal interact? (maximum of 250 words). (auto-filled from LOI; update if
> needed)


Matplotlib is the most widely used and de-facto standard visualization library
in Python (over 1M monthly users) and is a mature library (20+ years old) with
over 1,500 individual code contributors.  In addition to being directly used by
scientists, it is a core dependency of libraries and applications that
implement domain-specific visualizations.  To aid users in discovering these
extensions we maintain a lightly curated list of third-party extensions [1] and
have been assigned a Trove classifier on PyPI [2] that allows downstream
developers to self-identify as Matplotlib extensions.


Given the
centrality of visualization to data analysis across all domains, no single tool
can satisfy all needs.  There are a range of tools not built on Matplotlib (see
[3] for a long but not exhaustive list) that target use cases that Matplotlib
is not well suited for.  Outside of the Python ecosystem, a wide range of
biomedical visualization libraries and applications exist in R or Java.
Proprietary solutions such as MATLAB or Tableau may also be used in various
scientific fields.


Matplotib's ubiquity and maturity provide
users with a stable and easily understood tool on which to build both bespoke
and reproducible visualizations.  Its availability in the Python ecosystem
allows for direct integration with data processing and modelling tools in a
familiar environment.


[1] https://matplotlib.org/mpl-third-party/
[2] https://pypi.org/search/?q=&o=&c=Framework+%3A%3A+Matplotlib
[3] https://pyviz.org/tools.html


# Diversity, Equity, and Inclusion Statement

> Advancing DEI is a core value for this program, and we are requesting
> information on your efforts in this area. Describe any efforts the software
> project(s) named in this proposal have undertaken to increase diversity,
> equity, and inclusion with respect to their contributors and audience. Please
> see examples from applications funded in previous cycles (maximum of 250
> words)
