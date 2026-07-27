# Summary: 2026-07-24_15-20-56Z_UniversalBCIPersonalization_OneAPIforFrozenEEGTrun.md
Saved: 2026-07-26 21:53
Source: 2026-07-24_15-20-56Z_UniversalBCIPersonalization_OneAPIforFrozenEEGTrun.md
Model: None

---

## Summary  
The paper introduces Nimbus Personalizer, a universal API that enables personalization of frozen EEG encoders without per‑architecture fine‑tuning pipelines. By placing a lightweight Bayesian head on top of BrainState (optionally an affine mid‑tier), the system allows OEMs to swap trunks while keeping the same integration contract. The authors demonstrate that this approach recovers most of the performance gain from full fine‑tuning with orders‑of‑magnitude less adaptation wall time, making personalization scalable across heterogeneous architectures.

## Key Contributions  
- A trunk‑agnostic API for personalizing frozen EEG encoders without per‑architecture fine‑tune pipelines.  
- Empirical evidence that the Bayesian head recovers most of the performance gain of full fine‑tuning while requiring orders‑of‑magnitude less adaptation wall time.  
- Subject‑level confidence intervals show clear gains in 12/18 cells, supporting the API’s utility where embedding capacity exists.

## Methodology  
The authors built Nimbus Personalizer as a contract between a frozen trunk encoder and a Bayesian head that sits on top of BrainState (optionally an affine mid‑tier). They train the head end‑to‑end using a small subset of data per subject, bootstrap confidence intervals at the subject level, and compare against warm‑start fine‑tuning or PEFT. The same surface runs across EEGNet, Shallow, Deep, Conformer, ATCNet trunks and the REVE foundation encoder.

## Results  
Across 18 cells from four MI datasets, the head provides comparable accuracy to full fine‑tune while adaptation time is reduced by orders of magnitude. Calibration‑only‑when‑clean holds in 12/18 cells. Subject confidence intervals are zero where no gain; positive gains appear only when capacity exists.

## Significance  
This work decouples personalization from architecture, enabling OEMs to swap trunks without rebuilding pipelines, and offers a cost‑effective alternative to full fine‑tuning, accelerating BCI deployment.

## Related Concepts  
Frozen encoders, Bayesian heads, BrainState, affine mid‑tier, PEFT, LDA on embeddings, trunk‑agnostic API, personalization wall time, confidence intervals, foundation models (REVE).
