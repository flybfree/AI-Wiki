# Summary: 2026-07-30_15-50-10Z_WhyAreGUIAgentsCorrectbutLate_DecodeontheDecision_.md
Saved: 2026-07-30 22:17
Source: 2026-07-30_15-50-10Z_WhyAreGUIAgentsCorrectbutLate_DecodeontheDecision_.md
Model: None

---

## Summary  
The paper investigates why computer‑use agents often generate the right action but only after a GUI window has already closed, attributing this delay to expensive autoregressive decoding on the decision‑time critical path. It introduces Adaptive Anticipatory Policy Trees (AAPT), a method that pre‑computes a bounded conditional policy tree during idle periods so that when an event occurs the correct action can be executed instantly without invoking the model’s text generation pipeline. The contribution is both theoretical—identifying the root cause of “correct but late” behavior—and practical—a ready‑to‑deploy solution that improves success rates while eliminating incorrect actions.

## Key Contributions  
- Identify that GUI agents are correct but late because their decision‑time critical path relies on costly autoregressive decoding.  
- Propose Adaptive Anticipatory Policy Trees (AAPT), which pre‑builds a bounded conditional policy tree with observable guards, deadlines and branch‑specific actions sized to cover the model’s own latency.  
- Demonstrate via paired trials that AAPT raises success from 0.50 to 0.79 within the contested window (p = 1.8×10⁻³) with zero incorrect actions, while reactive baselines achieve zero success.

## Methodology  
During idle screen periods the frozen multimodal model constructs a bounded conditional policy tree whose branches are guarded by observable conditions and each branch carries a deadline equal to the expected decoding latency of that branch. A lightweight observer continuously watches for change‑gated frames; when it detects an event, it matches the frame to the pre‑prepared branch and triggers the corresponding action instantly, bypassing any new text generation. Experiments include paired trials with registered endpoints, exact McNemar tests, a preparation‑time sweep, and ablations that isolate fast observer decoding, valid tree planning, and accurate branch routing.

## Results  
AAPT improves success from 0.50 to 0.79 within the decision window (p = 1.8×10⁻³) with no incorrect actions. Open‑loop and predict‑and‑replan baselines score zero because they still decode during execution. A pre‑registered oracle probe points to branch routing as the causal bottleneck, not the hypothesis about decoding latency. Reproducing on an independent general‑purpose multimodal model over 126 paired trials yields p = 4.9×10⁻¹³. On an external benchmark AAPT matches a reactive baseline overall while they complement each other.

## Significance  
The findings show that anticipatory planning can dramatically boost GUI agent performance without sacrificing correctness, addressing a long‑standing user experience problem in interactive AI systems. By decoupling execution from real‑time decoding, AAPT offers a scalable way to make agents feel “instant” while remaining reliable.

## Related Concepts  
autoregressive decoding latency, conditional policy trees, guard‑based branching, decision‑time critical path, McNemar test, pre‑registered endpoints, reactive vs. predictive agents, branch routing bottleneck.
