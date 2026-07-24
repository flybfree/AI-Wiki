---
title: Proactive Inpatient Bed Requests for Emergency Department Admissions
published: 2026-07-16T20:06:05Z
authors: QIan Cheng, Nilay Tanik Argon, Aniruddhan Ganesaraman, Serhan Ziya
url: http://arxiv.org/abs/2607.15432v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Proactive Inpatient Bed Requests for Emergency Department Admissions

## Abstract
Emergency department (ED) boarding occurs when admitted patients remain in the ED while awaiting inpatient beds. Boarding is a major driver of ED crowding and has been associated with poor patient outcomes. We propose a framework to help EDs reduce boarding time and length of stay by using information about current patients and bed availability to proactively request inpatient beds before admission decisions are finalized.   We formulate the problem as a Markov decision process in which predictions of each patient's admission probability and time to disposition are aggregated to guide early inpatient bed requests. This formulation leads to three data-driven policies based on approximate dynamic programming, reinforcement learning, and a newsvendor-type approach. Using a simulation model based on data from a large ED, we evaluate these policies across a wide range of settings. The simulation study shows that proactive aggregate bed requests can reduce average boarding times for admitted patients by 30-70\% and average length of stay for all ED patients by 6-15\%, while creating only modest idle time for prepared inpatient beds. The newsvendor heuristic provides the most attractive tradeoff between ED performance and inpatient bed idle time, whereas the reinforcement learning heuristic produces smoother bed-request patterns when stability in downstream hospital processes is especially important.   Our work shows how EDs can use prediction tools to make proactive bed-request decisions that improve ED operations while helping managers balance reductions in ED delays against inpatient bed idle time. Our findings also illustrate the value of evaluating both simple myopic heuristics and more sophisticated reinforcement learning-based approaches, since each can offer distinct advantages depending on the performance measures and implementation constraints most important to managers.

## Metadata
- **Published**: 2026-07-16T20:06:05Z
- **Authors**: QIan Cheng, Nilay Tanik Argon, Aniruddhan Ganesaraman, Serhan Ziya
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.15432v1)