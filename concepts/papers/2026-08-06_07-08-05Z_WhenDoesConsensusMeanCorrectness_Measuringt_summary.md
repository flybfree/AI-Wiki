# Summary: 2026-08-06_07-08-05Z_WhenDoesConsensusMeanCorrectness_MeasuringtheAgree.md
Saved: 2026-08-06 22:05
Source: 2026-08-06_07-08-05Z_WhenDoesConsensusMeanCorrectness_MeasuringtheAgree.md
Model: None

---

## Summary  
The authors investigate whether the agreement among model outputs for perturbed inputs can be taken as a reliable proxy for correctness, proposing to measure the coupling between this agreement and actual accuracy using a novel method that preserves semantics through re‑rendering. They generate RENDEQ (Render‑Equivalence Sets) where images are programmatically created and redrawn, eliminating ground‑truth errors while preserving meaning. By evaluating three open‑weight vision language models on these sets, they demonstrate that agreement can be a useful reliability signal when it is calibrated to the model’s error diffuseness.

## Key Contributions  
- [Finding 1] Re‑rendering outperforms resampling in both accuracy and reliability across all tested models.  
- [Finding 2] Agreement beats an evidence‑carrying baseline (mean token log‑probability) on two of three models, tying the third, which reverses a previously buggy replication caused by rendering‑pipeline issues.  
- [Finding 3] Fine‑tuning on the model’s own cross‑render consensus reduces accuracy in every one of five replication runs, showing an opposite sign to earlier natural‑image results.

## Methodology  
The authors built RENDEQ as a generator that produces pairs of images derived from the same programmatic drawing process; redrawing such images yields semantically equivalent outputs with no ground‑truth errors. They use these sets to compute model agreement (the proportion of identical predictions) and compare it to accuracy measured on the original data. The reliability signal is derived without relying on external labels, allowing a label‑free assessment. Experiments also include fine‑tuning the models on their own consensus outputs to observe calibration effects.

## Results  
Re‑rendered images achieve higher accuracy and stronger reliability than resampled alternatives, indicating that preserving semantics through re‑rendering yields better performance. Agreement correlates with correctness only above a threshold set by how diffuse the model’s errors are; when errors are highly dispersed, agreement becomes less informative. Fine‑tuning on consensus data consistently lowers accuracy across five runs, suggesting that encouraging agreement can degrade calibration.

## Significance  
This work provides a direct measurement of the agreement‑accuracy coupling for scientific figures, revealing that agreement is not universally trustworthy and can be harmed by model error diffuseness. It challenges the common practice of using label‑free consensus as a self‑training target in vision language models, highlighting the need to consider rendering pipeline factors such as plotting libraries.

## Related Concepts  
Agreement, accuracy, reliability, consensus, semantics‑preserving re‑rendering, render‑equivalence sets (RENDEQ), open‑weight VLMs, token log‑probability baseline, error diffuseness, fine‑tuning impact.
