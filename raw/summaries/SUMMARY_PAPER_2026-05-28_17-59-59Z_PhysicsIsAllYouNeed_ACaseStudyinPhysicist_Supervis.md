---

title: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
url: http://arxiv.org/abs/2605.30353v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-28_17-59-59Z_PhysicsIsAllYouNeed_ACaseStudyinPhysicist_Supervis.md
generated_at: "2026-06-11 10:49"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper presents a case study of a physicist supervising an AI coding agent over twelve days to develop the CLAX‑PT module. The results show that supervision design, not model scaling, determines whether the software is trustworthy.

## Key Takeaways
- The agent resolved ten tasks autonomously but failed three due to treating symptom reduction as root cause, leading to unphysical code changes.
- Supervision practices such as testing at diverse parameter points, shared changelogs, and a rule against unphysical patches were essential for catching errors missed by oracle tests.
- The fudge factor was corrected within the same session, highlighting that rapid fixes can mask deeper architectural flaws.

## Context
The study illustrates how AI agents currently operate within fixed code structures, optimizing coefficients without proposing alternative architectures. This limits their ability to generate scientifically meaningful solutions beyond predefined boundaries.

## Implications
For researchers and developers, this work underscores the need for supervisory frameworks that encourage architectural innovation rather than mere parameter tuning. It also suggests that trustworthy scientific AI requires explicit constraints against unphysical modifications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.30353v1)
