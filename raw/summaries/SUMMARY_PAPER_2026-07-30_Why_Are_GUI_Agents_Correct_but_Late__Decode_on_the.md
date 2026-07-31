---
title: Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path, Tested with Pre-Compiled Policy Trees
url: http://arxiv.org/abs/2607.28399v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_15-50-10Z_WhyAreGUIAgentsCorrectbutLate_DecodeontheDecision_.md
generated_at: 2026-07-30 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why computer‑use agents often act too late on transient GUI events, attributing the delay to expensive autoregressive decoding that occurs after the relevant window has closed. By introducing Adaptive Anticipatory Policy Trees (AAPT), the authors eliminate this latency without altering the underlying model and achieve a measurable increase in success rate from 0.50 to 0.79 within the contested decision window, with no incorrect actions generated.

## Key Takeaways
- AAPT pre‑computes a bounded conditional policy tree during idle periods that includes observable guards, pre‑authorized actions, and branch deadlines sized to cover the model’s own decoding latency.  
- When an event occurs, a lightweight observer matches change‑gated frames to a prepared branch and executes the corresponding action instantly without generating new text.  
- The improvement is statistically significant (p = 1.8×10⁻³) in paired trials, while open‑loop baselines achieve zero success because they still decode during execution.

## Context
Computer‑use agents that interact with graphical user interfaces rely on autoregressive language models to generate actions, which introduces a bottleneck when the UI changes rapidly. This latency can cause agents to miss transient events or produce stale responses, limiting their usefulness in real‑world applications where timely interaction is critical.

## Implications
AAPT demonstrates that pre‑planning can offset model decoding delays, offering a practical solution for integrating AI agents into GUI workflows without sacrificing accuracy. Practitioners can adopt this approach to improve responsiveness and reliability of automated UI interactions, especially when candidate actions are known in advance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28399v1)
