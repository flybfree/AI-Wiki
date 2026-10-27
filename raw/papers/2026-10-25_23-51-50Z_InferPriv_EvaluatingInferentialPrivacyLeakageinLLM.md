---
title: InferPriv: Evaluating Inferential Privacy Leakage in LLM Assistants
published: 2026-10-25T23:51:50Z
authors: Pengrun Huang, Yiwei Fu, Luoxi Meng, Kamalika Chaudhuri
url: http://arxiv.org/abs/2610.34640v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# InferPriv: Evaluating Inferential Privacy Leakage in LLM Assistants

## Abstract
Large language model (LLM)-based personal agents are increasingly deployed to handle everyday tasks on users' behalf. These agents have access to private user information, while their tasks involve communicating with third parties; this raises a critical privacy concern that agents may inappropriately reveal sensitive user information to these recipients. Existing benchmarks primarily assess direct privacy leakage, where an agent explicitly states a pre-specified secret or attribute. However, they do not capture \textit{inferential leakage}, where the model leaves indirect cues in the reply that implicitly leaks sensitive attributes. We introduce \textsc{InferPriv}, a benchmark that measures whether an honest-but-curious recipient can infer a user's sensitive attributes from an LLM's reply on routine task. Evaluating five frontier models, we find that inferential leakage substantially exceeds direct leakage across models and prompts. Under a privacy-aware system prompt, GPT-6.1-Sol, Sonnet-5.5, and Gemini-3.8-Flash achieve near-zero direct leakage, yet the inferential leakage rate remains between 16.2--25.2\%. These findings suggest that evaluating explicit leakage alone can substantially understate the privacy risks.

## Metadata
- **Published**: 2026-10-25T23:51:50Z
- **Authors**: Pengrun Huang, Yiwei Fu, Luoxi Meng, Kamalika Chaudhuri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34640v1)