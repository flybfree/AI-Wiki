---

title: "Summary: Flow-OPD: On-Policy Distillation for Flow Matching Models"
url: http://arxiv.org/abs/2605.08063v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-08_17-50-15Z_Flow_OPD_On_PolicyDistillationforFlowMatchingModel.md
generated_at: "2026-06-11 10:30"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-05-08 17-50-15Z Flow Opd On Policydistillationforflowmatchingmodel


## Summary
This paper introduces Flow‑OPD, a post‑training framework that combines on‑policy distillation with flow matching to align heterogeneous objectives in text‑to‑image models. By first fine‑tuning domain‑specialized teachers with single‑reward GRPO and then merging them via flow‑based cold start and trajectory supervision, the method achieves strong alignment while preserving image fidelity.

## Key Takeaways
- The two‑stage teacher creation uses single‑reward GRPO to let each expert reach its performance ceiling independently.  
- Flow‑OPD employs a three‑step orchestration of on‑policy sampling, task‑routing labeling, and dense trajectory supervision to consolidate expertise into one student policy.  
- Manifold Anchor Regularization provides full‑data supervision from a task‑agnostic teacher, anchoring generation to a high‑quality manifold and reducing aesthetic degradation.

## Context
The work addresses the “seesaw effect” where scalar rewards cause reward hacking in flow matching models, a problem that limits their ability to align multiple tasks. Recent on‑policy distillation techniques have proven effective for language models, but few have been adapted to multimodal generation pipelines.

## Implications
Flow‑OPD demonstrates that integrating on‑policy methods can yield substantial gains in both visual quality and task performance without sacrificing fidelity, offering a scalable approach for building generalist text‑to‑image systems. Practitioners can leverage this framework to reduce alignment costs while improving downstream metrics such as GenEval and OCR accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.08063v1)
