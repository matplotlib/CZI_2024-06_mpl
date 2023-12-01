# Progress Report

> If the grant is still active, provide a short summary of progress towards the
> deliverables (maximum of 250 words).

- releases targets hit
- hit responsiveness targets
- hitting issue and PR targets
- projects
  - meson
  - website overhaul
  - pybind11 move
  - high-dpi refactor (on-going)
  - multi-path collection drawing (on-going)
  - add  GTK4 backend
  - high-dpi for GTK4
  - finish font fallback from GSOC
  - setting ps language level
  - wrote mission statement
  - widget support of pymne

- timely issue resolution
  - macosx + py312 segfault
  - interaction with gc.collect
  - subtle color palette bug in PDF backend

Over the period of the currently active grant, we believe we have successfully
achieved our targets:

- Feature releases are now made at a regular 2-per-year schedule, typically
  with 3 bugfix releases between them.
- Initial response to all issues / new PRs within a week
- Resolve majority of new issues / PRs within 1 month
- Resolve 75 issues / quarter
- Merge or close 75 PRs / quarter

We have implemented several larger projects, including changing build systems
to Meson, overhauling our website, and moving extensions to pybind11.  We
identified several medium size projects, such as adding a new GTK4 backend
(with high DPI support), completing font fallback work started by our Google
Summer of Code student, and writing our mission statement.  At this time, two
medium-size projects -- a high DPI refactor, and knockout group-based
collection drawing -- have been started and are in progress.


# Proposal Purpose

> Describe the purpose of the proposal in one sentence (maximum of 200
> characters including spaces).  Example: To develop a comprehensive, validated
> atlas of the human kidney at single-cell resolution open to the entire
> scientific and clinical community.



To support the continued maintenance, growth, development, and community
engagement of Matplotlib, the foundational plotting library of the Scientific
Python Ecosystem.


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

- finish mplgui
- more flexible axis ticking and labeling
- upgrade freetype / move to raqm

- performance improvements

- legends
- getting rid of mpl-toolkits

The proposed work can be broadly classified into three parts:

- on-going and routine maintenance of Matplotlib;
- implementation of several mid-sized features;
- community and project management.

These tasks underpin the long term health of the library but are ill-suited to
be accomplished solely with volunteer effort.

The primary component of the proposed work is the continued maintenance of
Matplotlib.  Maintenance covers a wide range of tasks including triaging and
fixing bugs, reviewing Pull Requests, tagging and building releases, and
keeping the continuous integration services running.  These tasks are essential
for the project's health; though each individually is small, they are
frequently time critical and tedious.  It is unfair and impractical to rely
solely on volunteers to accomplish such tasks.

For the past 42 months CZI EOSS support for developers has had a positive
effect on the project by complementing and enabling, not replacing, volunteer
work.  We propose to continue this effort.  The dedicated support has allowed
us to promptly fix critical bugs -- including a Python version specific
segfault in a new CPython release -- and extremely subtle bugs, such as a bug
in generating incorrect color palette in PDF output.

In addition to routine maintenance there are substantial improvements to the
library that can require concentrated effort.  We propose to focus on three
large projects: generalizing and improving the performance of the Axis ticking
system, modernizing the font handling code to support variable fonts and
complex text rendering (required for languages such as Arabic, Bengali, and
Hebrew), and to overhaul how we manage GUI windows.  In addition we will
identify five medium-sized projects.

The tick location and formatting machinery in Matplotlib is flexible, but this
flexibility comes at a performance cost, architecturally prevents hierarchical
labeling, and reduces API usability by making seemingly simple tasks extremely
complex.  While the work to design the new API is significant, our primary
concern will be to complete this work while minimizing the impact on existing
users.  Because tick labeling is so fundamental to plotting even small changes
to the API will have significant impact on our users.  Although we have had
discussion about these issues since at least 2015, it has been intractable with
volunteer effort.

Matplotlib currently does not support complex shaping, including bidirectional
text, context sensitive shaping, and ordering, required to correctly render
some non-Latin scripts including Arabic, Devanagari, and Hebrew.  Further,
Matplotlib does not support modern font formats, color fonts, or OpenType font
variations.  There is an existing external implementation of this support that
can be adapted for the main library.  This is a low risk project that will
allow users to plot in their native languages and leverage modern fonts.

The Matplotlib pyplot module provides bindings to several UI toolkits, along
with stateful management of the figure life-cycle.  These toolkit windows and
figures are intertwined in ways that can be unintuitive to users, and contrary
to expectations set by newer notebook-based development styles.  We have
produced a prototype that overhauls this UI management and allows more
independent control of the figure life-cycle compared to its UI appearance, and
we propose to integrate this prototype into the main library.

We propose to continue full support (1 FTE) for Elliott Sales de Andrade and
partial support (.08 FTE) for Thomas Caswell along with travel and equipment
support for 2 years.  The effort will be split with approximately .73 FTE for
maintenance, .25 FTE for medium sized enhancements, and .1 FTE for community
and project management.  We also propose to fund Code of Conduct incident
response training.



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



- EOSS3-0000000149, (Jan 2021 - Jan 2022) 1yr, 250k$, CZI
- EOSS4-0000000, (Jan 2022 - Jan 2022) 2yr, 250k$, CZI

- NASA

- Google summer of code (2021, 2023) 1 full time student per summer, in-kind, Google
- Google season of docs (2023) 1 technical writer part time, in-kind, Google



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
