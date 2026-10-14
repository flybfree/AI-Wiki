---
title: What Counts as the Same Task? Executable Contracts for Robustness Evaluation of Tool-Using Agents
published: 2026-10-10T02:18:56Z
authors: Shaikh Akib Shahriyar, MD. Akil Raihan Iftee, Armon Barton, Matthew Wright
url: http://arxiv.org/abs/2610.14477v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Counts as the Same Task? Executable Contracts for Robustness Evaluation of Tool-Using Agents

## Abstract
Robustness tests for tool-using agents often change the agent's environment, for example by hiding a hostile note in an invoice, and then judge the agent by what it does. The result tells us about the original task only if the changed test case is still a valid test of that task. Many evaluations decide this with weak rules, such as accepting any well-formed edit or any edit that stays close to the original in embedding space. We propose executable task contracts. A contract states which facts define a task, which edits are allowed, and what finishing the task means, and it checks each changed test case before the agent runs. We compare validity rules by scoring the same 14,336 stored agent runs under each rule. Across four encoders, embedding thresholds allowed 75-100% of edits that changed the task, such as swapping the payee, yet rejected 24-45% of valid hostile notes. With a MiniLM cosine threshold, Mistral appeared vulnerable on all 64 tasks, but only 26 had a successful valid attack. Replaying a saved solution and allowing edits to benchmark fields fail in similar ways. Evaluations should state, and check, what counts as the same task.

## Metadata
- **Published**: 2026-10-10T02:18:56Z
- **Authors**: Shaikh Akib Shahriyar, MD. Akil Raihan Iftee, Armon Barton, Matthew Wright
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14477v1)