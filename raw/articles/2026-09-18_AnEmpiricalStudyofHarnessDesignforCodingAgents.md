---
title: An Empirical Study of Harness Design for Coding Agents
date: 2026-09-18
url: https://arxiv.org/abs/2609.20804
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://arxiv.org/abs/2609.20804
source_feed: Hacker News
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-18 10:25
---

# An Empirical Study of Harness Design for Coding Agents

## Full Article

Computer Science > Artificial Intelligence
arXiv:2609.20804
(cs)
[Submitted on 17 Sep 2026]
Title:
An Empirical Study of Harness Design for Coding Agents
Authors:
Run-Ze Fan
,
Zihao Zhang
,
Simin Ma
,
Yebowen Hu
,
Shouju Wang
,
Kaiqiang Song
,
Fei Liu
,
Hamed Zamani
,
Xiaoyang Wang
View a PDF of the paper titled An Empirical Study of Harness Design for Coding Agents, by Run-Ze Fan and 8 other authors
View PDF
HTML (experimental)
Abstract:
Coding harnesses shape how autonomous coding agents translate model capabilities into long-horizon software-engineering performance, yet existing work typically evaluates harnesses as monolithic systems, leaving the effectiveness of individual components unclear. To enable component-level comparisons, we study this question with a lightweight coding harness whose execution loop is fixed while three components are varied: planning, action space, and context management. Across four models evaluated on SWE-Bench Verified and Terminal-Bench 2.1, we evaluate 176 matched settings spanning five context-management strategies, four context-window budgets, and targeted ablations of planning and action space. We find that: (1) Context management becomes increasingly valuable as the context-window budget tightens, with most of its benefit coming from preventing context-overflow failures. (2) Staging rule-based elision before LLM-based summarization provides the strongest overall efficiency among the context-management strategies, whereas making elided content recoverable adds machinery that models rarely use and yields no accuracy gain. (3) Planning shifts from an accuracy scaffold for weaker models to a cost saver for stronger models, with little change in accuracy. (4) Predefined tools improve performance for models with weaker bash proficiency, whereas bash-capable models can operate effectively with a bash-only interface and achieve substantially lower cost, especially on command-line-centric tasks. Trajectory-level analysis explains these effects: context management extends execution trajectories without substantially altering agent behavior, planning changes where trajectories stop, and the action space changes the granularity at which code is written. These findings inform model- and budget-aware harness design and provide a modular framework for evaluating future harness components.
Comments:
43 pages
Subjects:
Artificial Intelligence (cs.AI)
; Computation and Language (cs.CL); Machine Learning (cs.LG); Software Engineering (cs.SE)
Cite as:
arXiv:2609.20804
[cs.AI]
(or
arXiv:2609.20804v1
[cs.AI]
for this version)
https://doi.org/10.48550/arXiv.2609.20804
Focus to learn more
arXiv-issued DOI via DataCite (pending registration)
Submission history
From: Run-Ze Fan [
view email
]
[v1]
Thu, 17 Sep 2026 17:58:07 UTC (6,713 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled An Empirical Study of Harness Design for Coding Agents, by Run-Ze Fan and 8 other authors
View PDF
HTML (experimental)
TeX Source
view license
Current browse context:
cs.AI
< prev
|
next >
new
|
recent
|
2026-09
Change to browse by:
cs
cs.CL
cs.LG
cs.SE
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
export BibTeX citation
Loading...
BibTeX formatted citation
×
loading...
Data provided by:
Bookmark
[BibSonomy]
[Reddit]
Bibliographic Tools
Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer
(
What is the Explorer?
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?
)
Litmaps Toggle
Litmaps
(
What is Litmaps?
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?
)
DagsHub Toggle
DagsHub
(
What is DagsHub?
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?
)
Core recommender toggle
CORE Recommender
(
What is CORE?
)
Author
Venue
Institution
Topic
About arXivLabs
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community?
Learn more about arXivLabs
.
Which authors of this paper are endorsers?
|
Disable MathJax
(
What is MathJax?
)

## Metadata
- **Source**: [Original Article](https://arxiv.org/abs/2609.20804)
