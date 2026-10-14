---
title: Structural Baselines Matter for Agent Failure Detection and Attribution
published: 2026-10-12T12:13:48Z
authors: Ramesh Arvind Naagarajan, Stefan Streif
url: http://arxiv.org/abs/2610.16661v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structural Baselines Matter for Agent Failure Detection and Attribution

## Abstract
An LLM agent using tools can fail silently. It stops before the task is done, raises no error, and answers fluently. Two kinds of monitor address this, one deciding whether a run failed and the other naming the step where failure became unavoidable. Much of the reported performance on both tasks comes from regularities that need no model. Failing runs are longer, and the step labelled decisive is usually the last. A rule that always names the last step is correct $67\%$ to $96\%$ of the time here, without reading the run at all. That ceiling reflects how the labels were written, not how agents break. On failures whose decisive step replay can confirm, it falls to near chance. Reporting gain over that rule therefore changes what a score means. Under that correction, methods tested here gain nothing on give-up failures, while several published systems keep a clear advantage on other splits. For detection, the agent's internal states beat transcript length and text similarity on the agent benchmark, and hold up where the text baseline does not. Precision stays low when failures are rare, so such a monitor should rank runs for review, not replace it.

## Metadata
- **Published**: 2026-10-12T12:13:48Z
- **Authors**: Ramesh Arvind Naagarajan, Stefan Streif
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16661v1)