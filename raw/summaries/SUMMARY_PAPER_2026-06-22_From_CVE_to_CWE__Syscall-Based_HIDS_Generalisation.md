---
title: "Summary: From CVE to CWE: Syscall-Based HIDS Generalisation"
url: http://arxiv.org/abs/2606.22581v1
type: paper-summary
date: 2026-06-22
source_paper: 2026-06-21_16-34-39Z_FromCVEtoCWE_Syscall_BasedHIDSGeneralisation.md
generated_at: 2026-06-22 22:00
model: nvidia/nemotron-3-nano-4b
---
# Summary: 2026-06-22 From Cve To Cwe  Syscall-Based Hids Generalisation

## Summary
The paper investigates whether a one‑class anomaly detector trained on normal syscall traces from CVEs sharing the same CWE class can detect unseen CVEs within that class. Experiments across six scenarios show mixed results: the combined CWE‑307 detector achieves F1 ≈ 0.698 at a calibrated false‑positive rate of 5 %, while detectors for CWE‑89 and CWE‑434 perform poorly (F1 ≤ 0.21). The study also finds that cross‑CVE transfer depends on the breadth of the source normal profile rather than the CWE label, and that calibrated FPR is essential for honest reporting.

## Key Takeaways
- A one‑class Isolation Forest trained only on normal syscall windows from CVEs with a common CWE can detect new instances of that same CVE with moderate performance (F1 ≈ 0.698 at 5 % FPR).  
- Detectors built for CWE‑89 and CWE‑434 collapse to low precision, indicating limited generalisation across different weakness families.  
- The effectiveness of cross‑CVE transfer is governed by how comprehensive the source normal profile is rather than by the CWE label itself.

## Context
This work extends HIDS research that traditionally relies on per‑CVE signatures to a more scalable approach using CWE‑level generalisation, which aligns with AI’s trend toward unsupervised anomaly detection and feature abstraction. By treating vulnerability families as latent classes, the method mirrors how machine‑learning models learn invariant representations from limited labeled data.

## Implications
For security engineers, this suggests that building HIDS models around CWE families may reduce maintenance effort but requires careful calibration of false positives to avoid alert fatigue. Practitioners should focus on extracting rich, representative syscall features and ensure detectors are trained with a fixed target FPR to obtain reliable generalisation metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.22581v1)
