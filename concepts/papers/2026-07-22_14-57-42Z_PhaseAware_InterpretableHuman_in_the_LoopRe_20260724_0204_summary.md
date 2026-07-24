# Summary: 2026-07-22_14-57-42Z_PhaseAware_InterpretableHuman_in_the_LoopRehabilit.md
Saved: 2026-07-24 02:04
Source: 2026-07-22_14-57-42Z_PhaseAware_InterpretableHuman_in_the_LoopRehabilit.md
Model: None

---

## Summary  
PhaseAware is a compact human‑in‑the‑loop framework that continuously scores rehabilitation progress by integrating phase‑aware descriptors and body‑group features through a gated residual network. The model produces interpretable review cues that highlight the most relevant movement stages and anatomical regions for each prediction, enabling clinicians to verify automated assessments without fully trusting them. On the UI‑PRMD deep‑squat protocol it reduces root‑mean‑square error (RMSE) to 0.0230, an 88.9 % improvement over the accepted baseline. The approach is designed for resource‑constrained settings where clinicians can monitor boundary cases and triage decisions.

## Key Contributions  
- PhaseAware achieves an RMSE of 0.0230, an 88.9 % reduction relative to the accepted UI‑PRMD baseline.  
- It generates structured review cues that highlight movement stages and body regions most relevant to each prediction.  
- The gated residual architecture stabilizes feature representation, allowing deployment in low‑resource clinical environments.

## Methodology  
The authors constructed a temporal backbone conditioned on phase and body‑group descriptors using a gated residual pathway. This conditional gating preserves fine‑grained sequential features while preventing overfitting. Input video data from the UI‑PRMD deep‑squat protocol is processed to generate both a continuous quality score and interpretable cues, with the architecture’s memory footprint kept under 10 MB.

## Results  
On UI‑PRMD, PhaseAware’s RMSE is 0.0230 (88.9 % lower than baseline). The model transfers to the KIMORE squatting subset with comparable accuracy. Generated cues align closely with clinician expectations for boundary‑case monitoring and are useful for human‑in‑the‑loop triage rather than autonomous decision‑making.

## Significance  
By delivering interpretable, low‑resource scoring that can be embedded in clinical workflows, PhaseAware supports safe human‑in‑the‑loop oversight. It improves monitoring of patients at risk of injury and facilitates integration of automated assessment into information systems without compromising clinician control.

## Related Concepts  
rehabilitation scoring, phase‑aware descriptors, body‑group features, gated residual networks, human‑in‑the‑loop AI, boundary‑case monitoring, UI‑PRMD protocol, KIMORE dataset.
