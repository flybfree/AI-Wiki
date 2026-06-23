---
title: From CVE to CWE: Syscall-Based HIDS Generalisation
published: 2026-06-21T16:34:39Z
authors: Alexander V. Kozachok, Stanislav G. Vyugov, Shamil G. Magomedov
url: http://arxiv.org/abs/2606.22581v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From CVE to CWE: Syscall-Based HIDS Generalisation

## Abstract
Host intrusion detection systems (HIDS) based on system-call traces are typically trained and evaluated against individual Common Vulnerabilities and Exposures (CVE) instances. In operational settings, however, defenders need to recognise new exploits of an already known type of weakness. We empirically examine whether a one-class anomaly detector trained on the normal behaviour of a set of CVEs that share a Common Weakness Enumeration (CWE) class generalises to a different, unseen CVE inside the same class. Using six scenarios drawn from LID-DS-2021 and grouped into three CWE families (CWE-307 broken authentication, CWE-89 SQL injection, CWE-434 unrestricted file upload), we extract a 66-dimensional Peng-Guo-style feature vector per sliding window and train Isolation Forest and SGD One-Class SVM detectors with normal-only thresholds calibrated to fixed target false positive rates. We define and answer four research questions covering self-detection, asymmetric cross-CVE transfer, the value of a combined CWE-level normal profile, and the effect of feature filtering on transferability. The combined CWE-307 detector reaches F1 = 0.6976 at calibration target FPR = 0.05 (precision = 0.8994, recall = 0.5698), whereas CWE-89 and CWE-434 collapse to F1 <= 0.21 under the same protocol. Cross-CVE transfer turns out to be strongly direction-dependent and dominated by the breadth of the source normal profile rather than by the CWE label. We conclude that CWE-level generalisation in HIDS is empirically attainable for some but not all weakness families with current syscall features, and we argue that calibrated FPR is a methodological prerequisite for honest reporting in this setting.

## Metadata
- **Published**: 2026-06-21T16:34:39Z
- **Authors**: Alexander V. Kozachok, Stanislav G. Vyugov, Shamil G. Magomedov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.22581v1)