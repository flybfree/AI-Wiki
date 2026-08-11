# Summary: 2026-08-09_13-44-26Z_AIEvaluationShouldMeasureVerificationCost_NotCorre.md
Saved: 2026-08-10 23:22
Source: 2026-08-09_13-44-26Z_AIEvaluationShouldMeasureVerificationCost_NotCorre.md
Model: None

---

## Summary  
The paper argues that current AI evaluation focuses solely on output correctness and overlooks the operational difficulty of detecting errors under realistic resource limits. It introduces Verification‑Cost Errors (VCEs) as a new failure mode defined by correct input‑output pairs that verifiers fail to identify within a deployment verification budget, proposing a conceptual instrument to capture this dimension.

## Key Contributions  
- [Finding 1] The definition of VCEs as incorrect input-output pairs that a declared fraction of the verifier population fails to detect within the verification budget available in a given deployment context.  
- [Finding 2] Empirical evidence from code generation and multi‑modal document understanding showing that high benchmark accuracy can mask significant verification effort, with VCE rates exceeding 30 % despite near‑perfect scores.  
- [Finding 3] A proposal for AI evaluation frameworks that explicitly account for verification cost relative to a budget as an operational dimension.

## Methodology  
The authors first operationalized VCEs by creating scenarios where verifiers are constrained by limited time or computational resources, then measured both detection rates and latency under those constraints. They compared these results against standard benchmark accuracy metrics to highlight the trade‑off between correctness and verification effort.

## Results  
Experiments demonstrated that models achieving near‑perfect benchmark scores still suffered high VCE rates: a large fraction of correct outputs were not flagged, leading to VCE percentages above 30 % in some cases. Detection time increased linearly as the budget was reduced, underscoring the cost associated with verification.

## Significance  
This work shifts focus from static correctness to dynamic reliability under resource constraints, encouraging developers to design verification systems that balance detection effort and error exposure. It also prompts a rethinking of AI safety metrics beyond simple pass/fail scores.

## Related Concepts  
- Hallucination (traditional notion of false outputs)  
- Verification budget (resource limit for inspectors)  
- Plausibility bias (confidence in plausible outputs)  
- Operational dimension (evaluation based on real‑world constraints)
