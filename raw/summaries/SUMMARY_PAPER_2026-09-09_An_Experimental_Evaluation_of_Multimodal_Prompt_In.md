---
title: An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks
url: http://arxiv.org/abs/2609.09404v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-08_20-00-03Z_AnExperimentalEvaluationofMultimodalPromptInjectio.md
generated_at: 2026-09-09 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MMPIBench, a benchmark for multimodal prompt injection attacks on agentic AI frameworks that combine language models with tools and visual inputs. It tests six attack carriers across seven frameworks and five foundation models to see how often injected instructions reach the planning stage and trigger tool calls. The results show attacks succeed in only about 1% of runs but are attempted in 12.8%, highlighting a narrow gap at the perception step.

## Key Takeaways
- Attacks complete in roughly 1% of runs, indicating they are rare successes despite being attempted in nearly 13% of trials.
- The planning stage is where most attacks are blocked, as models often read the injected instruction and refuse to act on it.
- One model never attempts an attack and detects injection in about 60% of cases, while two others attempt it only 24%, showing variation in robustness.

## Context
Agentic AI systems that can plan, remember, and interact with external tools are becoming more common, creating new attack surfaces. Visual inputs like OCR text or EXIF metadata provide stealthy ways to inject instructions without user interaction, raising security concerns for real-world deployments.

## Implications
This study underscores the need for robust perception layers that can detect and reject malicious visual cues before they reach planning logic. Practitioners should prioritize model-level defenses over framework-specific patches, especially as multimodal inputs expand beyond vision to audio signals.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09404v1)
