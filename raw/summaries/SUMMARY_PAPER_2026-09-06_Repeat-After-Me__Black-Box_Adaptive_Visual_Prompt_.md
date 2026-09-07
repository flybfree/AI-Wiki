---
title: Repeat-After-Me: Black-Box Adaptive Visual Prompt Injection
url: http://arxiv.org/abs/2609.04533v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-03_22-44-45Z_Repeat_After_Me_Black_BoxAdaptiveVisualPromptInjec.md
generated_at: 2026-09-06 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Repeat-After-Me, a black‑box adaptive visual prompt injection technique that can extract personally identifiable information or trigger malicious tool calls from frontier commercial vision language models. The authors demonstrate success rates above 80% on open‑weight models and over 47% on GPT‑5.5, showing the attack works even when the benign user prompt is unrelated to the injected task and does not authorize it.

## Key Takeaways
- Repeat-After-Me achieves high ASRs (80%+ on Qwen3.6‑27B, 47% on GPT‑5.5) without requiring a long or format‑compliant tool call string.  
- Optimizations made for one surrogate model retain roughly half of the original ASR when transferred to two commercial models, indicating cross‑sample transferability.  
- The attack can be deployed in real‑world OpenClaw deployments to overwrite TOOLS.md and enable remote code execution or secret exfiltration.

## Context
Prompt injection remains a critical security challenge for AI agents that consume untrusted data from web pages, documents, or emails. While text‑based attacks have been highly effective, visual prompt injection has historically struggled with commercial vision models due to the need for precise native tool calls. This work bridges that gap by providing an adaptive method that bypasses such constraints.

## Implications
For practitioners, Repeat-After-Me highlights the need for robust defenses against both textual and visual prompt injections in multimodal AI systems. The ability of a minimal image injection to compromise sensitive behavior underscores the importance of securing model outputs and input pipelines across diverse deployment environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04533v1)
