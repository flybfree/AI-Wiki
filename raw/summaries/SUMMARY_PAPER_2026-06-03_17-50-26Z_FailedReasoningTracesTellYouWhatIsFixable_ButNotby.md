---

title: Failed Reasoning Traces Tell You What Is Fixable (But Not by Reading Them)
url: http://arxiv.org/abs/2606.05145v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-03_17-50-26Z_FailedReasoningTracesTellYouWhatIsFixable_ButNotby.md
generated_at: "2026-06-11 10:52"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper argues that discarded failure traces from language model rollouts contain diagnostic information about which test‑time interventions can recover a given failure. By extracting three structural features from the trace structure, the authors show that these features cluster failures into stable regimes and enable a training‑free routing rule that improves rescue performance by 12.2 % on hard, steerable problems.

## Key Takeaways
- The three trajectory features are derived solely from the pattern of available interventions, not from the text itself, allowing recovery structure to be recovered from failed rollout signatures.
- These features cluster failures into stable regimes and improve test‑time accuracy by 20 % over a baseline on challenging tasks.
- A training‑free routing rule lifts rescue performance by 12.2 % specifically on the deployment‑relevant Steerable‑Hard subset where retries are insufficient.

## Context
Post‑training language models often fail on reasoning problems, and current practice treats failure traces as irrelevant data. The paper proposes a view that these traces encode recoverability structure, offering an alternative to simply spending more compute.

## Implications
Practitioners can use failed trace signatures to guide test‑time interventions without retraining or accessing model weights, reducing wasted compute on unrecoverable failures and providing insight into post‑training method performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.05145v1)
