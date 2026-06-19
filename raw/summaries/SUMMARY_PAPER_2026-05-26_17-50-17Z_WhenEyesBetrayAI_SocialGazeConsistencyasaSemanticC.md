---

title: "Summary: When Eyes Betray AI: Social Gaze Consistency as a Semantic Cue for AI-Generated Image Detection"
url: http://arxiv.org/abs/2605.27348v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-26_17-50-17Z_WhenEyesBetrayAI_SocialGazeConsistencyasaSemanticC.md
generated_at: "2026-06-11 10:47"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces Social Gaze Consistency as a high-level semantic cue for detecting AI-generated images by analyzing the mutual coherence of gaze direction, head‑eye alignment, and pupil placement between interacting individuals. Experiments show that this cue improves detection accuracy on COCOAI Interaction and Person subsets.

## Key Takeaways
- A controlled diagnostic dataset with region-specific perturbations enforces strict pair-level grouping, preventing generator‑fingerprint memorization as an optimization shortcut.
- Block‑Compositional Caption Supervision uses a single 5‑block reasoning skeleton that remains invariant across 1,250 macro‑combined captions, decoupling reasoning consistency from surface diversity.
- Cross‑architecture validation demonstrates the same supervision boosts FakeVLM by +3.7 pp and Effort by +1.3 pp on COCOAI Interaction and Person subsets respectively.

## Context
Recent generative models have largely closed low-level artifact detection gaps, yet high‑level semantic cues remain underexploited for image authenticity. This work demonstrates that such cues can be a powerful alternative to pixel‑based methods.

## Implications
Providing a reliable, backbone‑agnostic cue enables integration of Social Gaze Consistency into existing AI systems without relying on low‑level artifacts, thereby enhancing robustness across diverse generator suites.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.27348v1)
