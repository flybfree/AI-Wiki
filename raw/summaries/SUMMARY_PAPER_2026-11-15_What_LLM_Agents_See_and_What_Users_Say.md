---
title: What LLM Agents See and What Users Say
url: http://arxiv.org/abs/2611.17639v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-13_01-16-46Z_WhatLLMAgentsSeeandWhatUsersSay.md
generated_at: 2026-11-15 21:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the critical gap between what LLM agents observe through their tools and what users actually communicate, using presupposition theory from linguistics to formalize when an agent should act versus when it must ask first. The authors demonstrate that when tool outputs are ambiguous (e.g., a search returns only one record when two exist), agents act on false assumptions at rates comparable to unambiguous scenarios, but that presenting competing records or leveraging user-stated claims significantly reduces erroneous actions. The findings show that safe agent behavior depends heavily on how lookups present information and whether evaluations vary what tools show.

## Key Takeaways
- A theoretical bound shows that when lookups cannot distinguish one record from two, any agent acts without asking first as often with two records as with one, meaning ambiguity in tool output directly translates into agent overconfidence and incorrect actions.
- Under a role-only prompt, a count indicating a second record leaves most of 36 earlier agents acting on the single record they see, whereas listing both records stops most agents from acting incorrectly. However, when the user states a claim that a record refutes (e.g., "It is empty"), a count of the one item stops agents about as often as a full listing, and stating the claim mostly cuts acting when it is false.
- The newest Claude and GPT models always open a counted second record and then never act, suggesting improved model architectures handle ambiguity more cautiously. In a retail benchmark with a same-name, same-zip customer, a lookup returning that customer first led to wrong-account writes in about a quarter of conversations, while a lookup that checks a street the user knows kept completion near the one-customer level.

## Context
This work sits at the intersection of AI safety, tool-use evaluation, and computational linguistics, addressing a fundamental question in agentic AI: under what conditions should an autonomous agent act autonomously versus seek clarification. As LLM agents increasingly perform consequential actions like canceling reservations, deleting files, or modifying customer records, the paper reframes presupposition theory as a formal framework for auditing agent behavior. It highlights that current agent evaluations often assume tool outputs are unambiguous, masking a systematic failure mode where agents confidently act on incomplete or misleading information.

## Implications
For practitioners building agentic systems, this research mandates that safe writes require lookups designed to list or check competing records rather than returning a single best match, and that evaluation suites must deliberately vary what tools show to expose hidden failure modes. For the broader field, it signals that model capability improvements alone are insufficient; tool design, prompt structure, and user communication patterns jointly determine whether an agent acts safely. Industry deployments in customer service, file management, and retail operations should treat ambiguous tool outputs as a first-class safety concern rather than an edge case.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.17639v1)
