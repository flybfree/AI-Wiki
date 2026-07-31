---
title: STEREODISCO: Discovering Stereotypicality in LLMs
url: http://arxiv.org/abs/2607.27824v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_08-03-36Z_STEREODISCO_DiscoveringStereotypicalityinLLMs.md
generated_at: 2026-07-30 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces STEREODISCO, a framework that maps the semantic differential method to LLM internal representations by probing the model’s activation space for approximately 2,000 candidate axes derived from WordNet antonyms. Applied to social‑group stereotypes with LLAMA‑3 and MISTRAL models, it finds that the models agree on group ratings more than humans do and uncovers new stereotypical axes such as humble vs. proud and cowardly vs. brave.

## Key Takeaways
- STEREODISCO builds a large set of semantic axes from WordNet antonyms and uses probing to recover them in LLM activation space, revealing which axes are encoded by the model.
- The two LLMs (LLAMA‑3‑8B-INSTRUCT and MISTRAL‑7B-INSTRUCT) show higher agreement on social group stereotypes than human annotators, indicating that LLM‑encoded stereotype content diverges from social psychology findings.
- New axes like humble vs. proud and cowardly vs. brave are identified as stereotypical in the models and confirmed by independent human annotation.

## Context
Current research on AI bias often focuses on a limited set of semantic dimensions derived from social psychology, leaving many potential axes unexplored. This work broadens that scope by systematically probing thousands of candidate axes within LLM representations, offering a more comprehensive view of how stereotypes are encoded in large language models.

## Implications
For practitioners developing responsible AI, understanding which internal axes drive stereotype generation can inform bias mitigation strategies beyond surface‑level filtering. The discovery of novel axes suggests that current fairness audits may miss important dimensions, prompting the need for broader evaluation frameworks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27824v1)
