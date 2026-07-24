---
title: Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems
url: http://arxiv.org/abs/2607.14611v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_06-13-48Z_BadMemory_EvaluatingPromptInjectionRisksfromMemory.md
generated_at: 2026-07-23 23:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how persistent memory mechanisms in agentic AI systems create a new vulnerability to prompt injection attacks. By testing Anthropic Claude Code and OpenAI Codex with four models, the authors demonstrate that while external overwrites are hard to force, malicious content already stored in memory can steer current and future behavior, showing variable success rates across systems.

## Key Takeaways
- The presence of persistent memory files allows planted payloads to influence both present and subsequent sessions without needing direct file manipulation.  
- Attack effectiveness depends heavily on the specific agent model, its memory architecture, and the nature of the adversarial goal.  
- Multi‑session attack sequences reveal that once a malicious entry is embedded, it can persist across interactions, complicating defense strategies.

## Context
Agentic AI systems increasingly rely on long‑term memory to remember preferences and knowledge, enhancing their usefulness but also expanding the attack surface for sophisticated threats. This research highlights how the very features designed for improvement become potential weak points in a rapidly evolving threat landscape.

## Implications
For developers, protecting memory updates is essential without sacrificing adaptive capabilities. The findings urge industry adoption of secure update mechanisms that isolate malicious content while preserving legitimate learning processes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14611v1)
