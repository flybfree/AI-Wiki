---
title: Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems
published: 2026-10-21T20:25:11Z
authors: Daniel Ruiz, Luca Luceri, Emilio Ferrara
url: http://arxiv.org/abs/2610.30418v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems

## Abstract
Modern LLM agents can retrieve information from accessible documents, and then disclose a sensitive conclusion assembled from them. This mosaic effect creates a critical risk for agents operating over confidential data. We quantify its realization with 30 synthetic cybersecurity, medical, and military examples, yielding 10,800 final answers from three LLM agents in controlled simulation and 1,440 answers from live agents in two open-source harnesses. Even under benign queries designed to be answerable from one document, GPT-5.6-Sol, the best performing model tested, discloses forbidden composites in 7.08% of answers (95% CI: 3.75-10.67%) in simulation, with worse disclosure rates in live harnesses. Adding visible classification headers and explicit aggregation rules reduces pooled disclosure rates substantially, yet unsafe disclosures persist in 32.37% of simulated answers (95% CI: 28.33-36.19%) across all intents despite these safeguards. Furthermore, increased refusals do not guarantee confidentiality, since significant refusals reveal the prohibited conclusion regardless. These results point to a troubling conclusion: sensitive data leaks via mosaic-style events are an observed confidentiality failure mode in the evaluated settings at non-negligible rates. They motivate stronger controls on what agents may infer and disclose in sensitive data environments with mixed-clearance users.

## Metadata
- **Published**: 2026-10-21T20:25:11Z
- **Authors**: Daniel Ruiz, Luca Luceri, Emilio Ferrara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30418v1)