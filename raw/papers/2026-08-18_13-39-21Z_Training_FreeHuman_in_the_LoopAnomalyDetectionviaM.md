---
title: Training-Free Human-in-the-Loop Anomaly Detection via Memory Bank Correction
published: 2026-08-18T13:39:21Z
authors: Ayusha Abbas, Saram Abbas, Kabita Adhikari
url: http://arxiv.org/abs/2608.17775v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training-Free Human-in-the-Loop Anomaly Detection via Memory Bank Correction

## Abstract
Anomaly detectors are hardest to deploy exactly where training data is scarcest: a newly commissioned production line has a handful of verified "golden" samples and no machine-learning engineer on the factory floor. We present a training-free human-in-the-loop framework in which a domain expert corrects a PatchCore detector by direct memory bank editing: no retraining, no gradients, no original training data. A false-positive correction inserts the reviewed image's normal patches through a self-calibrating novelty gate admitting only those beyond the median pool-normal nearest-neighbour distance. From a bank built on only ten golden samples, operator corrections close a median 66% of the gap to an uncorrected fully trained bank (mean 80%, raised by three categories that overshoot parity), significantly improving 12 of 15 MVTec AD categories and harming none: ten samples plus corrections outperform hundreds of samples without them. On already-trained banks the headroom is smaller and concentrated where the bank undersamples normal appearance (gated: toothbrush +0.10, metal nut +0.09, zipper +0.05, screw +0.05), and no category except grid is significantly harmed. Evaluation uses a held-out protocol (20 splits per category, Holm-corrected Wilcoxon), because corrected images entering the bank inflate naive evaluation toward AUROC 1.0 by memorisation. Passive and active querying are statistically indistinguishable; a matched-label-budget control attributes gains to deployment-time label production at 43% of exhaustive-review cost; a defect-memory extension fails decisively. Feedback is simulated from ground truth; live expert trials, where mislabelling is costliest on small banks, remain future work.

## Metadata
- **Published**: 2026-08-18T13:39:21Z
- **Authors**: Ayusha Abbas, Saram Abbas, Kabita Adhikari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17775v1)