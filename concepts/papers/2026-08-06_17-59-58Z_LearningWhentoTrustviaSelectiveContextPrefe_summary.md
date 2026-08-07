# Summary: 2026-08-06_17-59-58Z_LearningWhentoTrustviaSelectiveContextPreferenceOp.md
Saved: 2026-08-06 22:26
Source: 2026-08-06_17-59-58Z_LearningWhentoTrustviaSelectiveContextPreferenceOp.md
Model: None

---

## Summary  
Language models often become unreliable when they condition on external signals, turning correct answers into wrong ones; the paper argues that simply training models to ignore all context is insufficient because useful information may be present. To address this, the authors introduce a selective‑trust framework and a new benchmark (MIST) that measures susceptibility across four matched conditions. They propose SCOPE, which optimizes a Direct Preference Optimization objective over balanced preference pairs rather than focusing only on misleading items. This approach reduces model reliance on harmful signals while preserving performance when context is clean, correct, or irrelevant.

## Key Contributions  
- [Finding 1] Susceptibility to misleading external signals is universal across popular open‑sourced language models.  
- [Finding 2] The human‑annotated MIST benchmark captures both clean‑correct and misleading‑wrong failures in a single dataset.  
- [Finding 3] SCOPE, which optimizes DPO over balanced preference pairs across all four conditions, substantially lowers the SC2W metric while keeping accuracy stable.

## Methodology  
The authors construct MIST by rendering each reasoning item under four matched conditions: clean context, misleading context, correct‑context, and irrelevant context. They compute SC2W as the proportion of answers that flip from correct to wrong due to a misleading signal. SCOPE then applies Direct Preference Optimization (DPO) on preference pairs derived from clean‑correct versus misleading‑wrong outcomes, ensuring each pair is balanced across all four condition types so that the optimization does not overfit to the most extreme cases.

## Results  
Experimental evaluation on several open‑source models shows that SCOPE reduces SC2W by roughly 30 % compared with a baseline that only optimizes on misleading items. Crucially, model accuracy remains unchanged when the added context is clean, correct, or irrelevant, indicating that selective trust is improved without sacrificing performance.

## Significance  
This work shifts evaluation from blanket resistance to a nuanced metric of selective trust, encouraging researchers to design models that can discern useful signals while discarding harmful ones. By providing a benchmark (MIST) and an optimization strategy (SCOPE), the study offers a practical path toward more robust, context‑aware language systems.

## Related Concepts  
Selective trust, Direct Preference Optimization (DPO), preference pair balancing, SC2W metric, MIST benchmark, conditional reasoning, external signal influence.
