---
title: Eternal Sunshine of the Spotless Mind: Systematically Erasing LLM's Memories
url: http://arxiv.org/abs/2609.36414v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-29_00-11-56Z_EternalSunshineoftheSpotlessMind_SystematicallyEra.md
generated_at: 2026-09-29 20:50
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates the capability of persistent large language models to systematically erase user memories stored in external systems upon deletion requests. The authors demonstrate that current LLMs fail to reliably delete information, often retaining data even when they claim to have forgotten it or operate within constrained contexts. To address this gap, the study introduces the DeLLM framework, which utilizes a provenance graph and dynamic context construction to achieve high-fidelity memory deletion without compromising model utility.

## Key Takeaways
- Current persistent LLM architectures are fundamentally unable to guarantee the deletion of shared information; models frequently retain sensitive data despite explicit user requests, verbal claims of forgetting, or operational constraints like limited context windows, highlighting a critical reliability gap in privacy-preserving AI systems.
- Simply removing messages that match deletion keywords or IDs is ineffective because conversational interactions create complex message dependencies where information persists implicitly through references and contextual links, necessitating a more sophisticated approach than direct message elimination.
- The proposed DeLLM framework resolves these

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.36414v1)
