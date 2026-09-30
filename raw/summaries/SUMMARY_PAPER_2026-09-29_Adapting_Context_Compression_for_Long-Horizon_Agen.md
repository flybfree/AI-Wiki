---
title: Adapting Context Compression for Long-Horizon Agents with Counterfactual Continuations
url: http://arxiv.org/abs/2609.36526v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-29_02-18-13Z_AdaptingContextCompressionforLong_HorizonAgentswit.md
generated_at: 2026-09-29 20:41
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces PAIR (Prompt Adaptation using Interventional Rollouts), a method designed to improve context compression for long-horizon agents by isolating compression-induced errors from inherent agent stochasticity. The authors demonstrate that compression primarily degrades reliability before affecting solvability and identify that severe performance drops often concentrate at isolated compression events, which can be diagnosed using matched counterfactual continuations. PAIR dynamically revises structured compression prompts based on these diagnoses to achieve superior cross-run reliability, bringing compressed execution performance nearly on par with uncompressed baselines without modifying the downstream agent architecture.

## Key Takeaways
- Existing evaluation methods for prompt-adaptation struggle because comparing full and compressed trajectories fails to isolate individual compression errors due to confounding agent stochasticity; the research establishes that compression degrades reliability first, meaning agents become less consistent in their outputs even if they retain the ability to solve tasks.
- By employing matched counterfactual continuations that compare execution from identical agent states with versus without compression, the study reveals that severe degradation is not uniform across the context but concentrates at specific, isolated compression events, enabling targeted diagnosis rather than relying on holistic performance comparisons.
- The proposed PAIR framework identifies compressions that degrade subsequent execution and revises relevant sections of a fixed compression template; this approach achieves the strongest cross-run reliability among compressed

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.36526v1)
