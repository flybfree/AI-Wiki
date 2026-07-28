# Summary: 2026-07-27_15-36-06Z_Bit_AccurateFPGAEvaluationofLearnedFeatureGatingin.md
Saved: 2026-07-27 21:45
Source: 2026-07-27_15-36-06Z_Bit_AccurateFPGAEvaluationofLearnedFeatureGatingin.md
Model: None

---

## Summary  
The paper evaluates learned feature gating in a fixed‑point Fourier‑Feature Automatic Modulation Classifier on an FPGA, measuring the trade‑off between classification performance and hardware cost. It compares gated versus ungated models trained with both post‑training quantization (PTQ) and quantization‑aware training (QAT), showing that gating reduces test accuracy while increasing resource usage.

## Key Contributions  
- Finding 1: Learned feature gating degrades classification performance on the test set for both PTQ and QAT training seeds.  
- Finding 2: The hardware implementation of the gate adds significant FPGA resources (ALMs, registers, DSP blocks) without offsetting accuracy gains.  
- Finding 3: Intermediate values from one training seed are preserved across board predictions, indicating stable quantization.

## Methodology  
The authors designed a classifier using 24 sparse DFT‑energy features and 8 phase/statistical features fed into an 32‑to‑128‑to‑11 multilayer perceptron. Two architectures were built: one without gating and another with a learned 32‑element gate inserted before the MLP. Both models were trained with PTQ and QAT using two matching seeds, producing eight checkpoints that were compiled independently for an Intel Cyclone V FPGA. Evaluation was performed over 352 000 physical‑board classifications.

## Results  
Ungated models outperform gated ones: mean accuracy loss of –0.784 % under PTQ and –0.616 % under QAT. The gate adds roughly 1,318 adaptive logic modules (ALMs), 1,557 registers, 4 DSP blocks, and 3,140 processing cycles. All 352 000 board predictions match an independent integer reference, and 3,760 intermediate values from one training seed also align.

## Significance  
The study demonstrates that learned gating, while beneficial in software, is costly on FPGA and does not improve hardware‑friendly accuracy, highlighting the need for efficient quantization strategies. This finding guides future work toward models where feature reweighting yields both performance gains and low‑cost hardware implementation.

## Related Concepts  
Learned feature reweighting, post‑training quantization (PTQ), quantization‑aware training (QAT), Fourier‑Feature representation, automatic modulation classification (AMC), fixed‑point implementation, adaptive logic modules (ALMs), DSP blocks, Intel Cyclone V FPGA, MLP classifier.
