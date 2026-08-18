---
title: PL-Guard: Probabilistic Logic Reasoning for LLM Guardrails
published: 2026-08-16T10:58:19Z
authors: Satchit Chatterji, Shihan Wang, Giovanni Sileno, Erman Acar
url: http://arxiv.org/abs/2608.15673v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PL-Guard: Probabilistic Logic Reasoning for LLM Guardrails

## Abstract
Large language model guardrails can be viewed as policy-consistency problems: a system must determine which policy-relevant facts hold in a prompt-response pair and what those facts imply under a given policy. Common approaches, including policy prompting and LLM-as-a-judge pipelines, often overlap the tasks of semantic grounding and policy reasoning: the model both interprets the prompt-response pair and reasons about whether a policy has been violated. This can lead to unsafe compliance with harmful prompts, or refusals to assist benign ones. To separate grounding and reasoning roles, we propose PL-Guard, a neurosymbolic guardrail architecture. Using a symbolic policy interface consisting of predicates and ProbLog rules, a local LLM grounds prompt-response pairs into predicate probabilities using renormalized True/False token scores, while ProbLog performs explicit probabilistic rule inference over the symbolic policy. On the XSTest benchmark, an offline Qwen-based evaluator finds that PL-Guard with a hand-curated policy reduces unsafe compliance from 22.0% for the base model to 0.5%, and below the 6.0% rate of an LLM-as-a-judge baseline. This comes at the cost of higher over-refusal than the LLM-as-a-judge baseline, 14.4% versus 5.2%. These results suggest that separating neural grounding from probabilistic symbolic reasoning can expose the safety-helpfulness tradeoff while making the guardrail's intermediate reasoning steps explicit and auditable.

## Metadata
- **Published**: 2026-08-16T10:58:19Z
- **Authors**: Satchit Chatterji, Shihan Wang, Giovanni Sileno, Erman Acar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15673v1)