---
title: Before You Poll with LLMs: A Deliberative Diagnostic Framework
published: 2026-09-14T16:41:48Z
authors: Ahmed Wali, Hassaan Tayyab
url: http://arxiv.org/abs/2609.15849v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Before You Poll with LLMs: A Deliberative Diagnostic Framework

## Abstract
Can LLMs reason through new information like humans, or do they merely retrieve cached opinions? This is critical for silicon sampling, where LLM personas simulate public opinion at scale. Current evaluations test only whether personas hold the right opinions -- a static snapshot. But opinion research increasingly depends on dynamic fidelity: whether personas update beliefs in response to new arguments, as humans do during deliberation. No existing benchmark tests this. We introduce the Deliberative Polling Diagnostic Framework, which compares human and LLM belief shifts after identical informational interventions. Grounded in deliberative polling, it surfaces failures invisible to static evaluation: models that produce plausible partisan opinions can still misrepresent how those opinions change. Applying the framework to five frontier models using data from America in One Room (526 personas, 72 questions), we find that every model fails, each in a unique manner. GPT-5.1 exhibits reversal: its personas become more hostile toward the opposing party after balanced information, while humans become less so. This reversal is selective (80% on outgroup vs. 26% on policy questions) and symmetric across partisan identities. Gemini 2.0 Flash, Claude Sonnet 4.5, and Llama 3.3 70B exhibit overshoot, shifting correctly but at 5-7x human magnitude. DeepSeek V3 exhibits rigidity with near-zero change. Targeted ablations reveal that policy content triggers these failures and that they are identity-specific: GPT-5.1 reverses on outgroup questions but overshoots on ingroup; Gemini shows the inverse. We term this signature self-sycophancy: conformity to the model's internal stereotype of the persona rather than reasoning from the information provided. Our framework offers a concrete protocol: run the deliberative diagnostic before trusting LLM personas to mimic revised beliefs.

## Metadata
- **Published**: 2026-09-14T16:41:48Z
- **Authors**: Ahmed Wali, Hassaan Tayyab
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15849v1)