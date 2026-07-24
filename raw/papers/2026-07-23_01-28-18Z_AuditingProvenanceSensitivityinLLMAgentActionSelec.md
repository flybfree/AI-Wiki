---
title: Auditing Provenance Sensitivity in LLM Agent Action Selection
published: 2026-07-23T01:28:18Z
authors: Junchi Liao
url: http://arxiv.org/abs/2607.20827v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Provenance Sensitivity in LLM Agent Action Selection

## Abstract
LLM agents choose tools and arguments from context that mixes user requests, tool outputs, retrieved records, memory, and untrusted text. Evidence can be relevant without being authorized to determine a decision, so a correct action need not be grounded only in permitted evidence. We introduce a target-specific authorization audit that labels context factors separately for each tool and argument target. Its primary test holds the task, proposition, position, and policy fixed while changing only the proposition's source authority. We then test behavior when valid evidence is weakened and use context-subset interactions as a secondary localization diagnostic. Across 450 controlled next-action tasks and multiple open-weight LLM families, trusted and untrusted variants produce different actions in 5.4 percent of competing cases versus 1.7 percent of supporting cases. Under controlled degradation, unauthorized competition is retained in a full-correct, mixed-error, clean-correct pattern in 2.4 percent of comparisons, with a 95 percent confidence interval from 2.1 to 3.0 percent. These are controlled stress-set rates, not deployment prevalence. The models respond to textual source-authority cues, but this does not prevent untrusted evidence from influencing their actions.

## Metadata
- **Published**: 2026-07-23T01:28:18Z
- **Authors**: Junchi Liao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20827v1)