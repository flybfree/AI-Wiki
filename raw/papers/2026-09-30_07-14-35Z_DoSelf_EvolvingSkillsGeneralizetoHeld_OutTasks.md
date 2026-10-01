---
title: Do Self-Evolving Skills Generalize to Held-Out Tasks?
published: 2026-09-30T07:14:35Z
authors: Xihao Piao, Zifeng Wang, Zhen Chen
url: http://arxiv.org/abs/2609.39148v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Self-Evolving Skills Generalize to Held-Out Tasks?

## Abstract
AI agents can externalize what they learn from past tasks into reusable \emph{skills}, such as procedures, checklists, code, or other executable artifacts, that can be retrieved and reused when solving new tasks. Self-evolving skill methods keep rewriting these skills after each round of practice on training tasks, and the skill is then used on new tasks of the same kind. We ask a question: does the improvement a skill shows on its training tasks carry over to new test tasks? We test five self-evolving methods and a one-shot skill on six benchmarks, with the same model, the same agent, and the same train/test split for every method. Of the 21 skills that improve on their training tasks, 5 keep all of that improvement on the test tasks, 13 keep part of it, and 3 keep none of it. No existing method is best everywhere. When we read the skills, the ones that carry over badly often fix details that should depend on the task, such as column names and output files, or turn a fix for one failure into a rule for every task. An LLM judge that reads the skill content can often see this: it ranks finished skills the same way the test results do in 86\% of pairs. But it predicts the effect of a single edit poorly, so edits still have to be tested by running them. Based on these findings, we describe Generalizable Skill Optimization (GSO), which keeps only a guide for writing skills and writes a new skill for each task; it scores highest on all six benchmarks.

## Metadata
- **Published**: 2026-09-30T07:14:35Z
- **Authors**: Xihao Piao, Zifeng Wang, Zhen Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39148v1)