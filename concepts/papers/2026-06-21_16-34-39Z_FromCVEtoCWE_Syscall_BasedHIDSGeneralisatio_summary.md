title: "Summary: 2026-06-21_16-34-39Z_FromCVEtoCWE_Syscall_BasedHIDSGeneralisation.md"
# Summary: 2026-06-21_16-34-39Z_FromCVEtoCWE_Syscall_BasedHIDSGeneralisation.md
Saved: 2026-06-22 22:01
Source: 2026-06-21_16-34-39Z_FromCVEtoCWE_Syscall_BasedHIDSGeneralisation.md
Model: None

---


## Summary  
This paper investigates whether a host intrusion detection system (HIDS) that relies on syscall traces can be trained to detect anomalies across different Common Vulnerabilities and Exposures (CVE) instances that belong to the same Common Weakness Enumeration (CWE) class. The authors empirically test this hypothesis by training one‑class anomaly detectors on normal syscall behaviour derived from six LID‑DS‑2021 scenarios grouped into three CWE families, then evaluating their ability to generalise to unseen CVEs within those families. Their work demonstrates that while some weakness families support robust cross‑CVE detection, others fail dramatically, highlighting the limits and conditions of CWE‑level generalisation in HIDS.

## Key Contributions  
- [Finding 1] CWE‑level generalisation in HIDS is empirically attainable for some but not all weakness families with current syscall features.  
- [Finding 2] Cross‑CVE transfer is strongly direction‑dependent and dominated by the breadth of the source normal profile rather than by the CWE label itself.  
- [Finding 3] Calibrated false positive rate (FPR) is a methodological prerequisite for honest reporting in this setting.

## Methodology  
The authors extract a 66‑dimensional Peng‑Guo style feature vector from sliding windows of syscall traces for each scenario, producing a total of six CVE examples per CWE family. They train two one‑class anomaly detectors—Isolation Forest and SGD One‑Class SVM—using only the normal‑behaviour data, calibrating their thresholds to achieve a fixed target false positive rate (FPR = 0.05). The detectors are then evaluated on unseen CVEs within the same CWE families, measuring detection performance via F1 score.

## Results  
The combined CWE‑307 detector reaches an F1 of 0.6976 at the calibrated FPR target (precision = 0.8994, recall = 0.5698). In contrast, detectors for CWE‑89 and CWE‑434 collapse to F1 ≤ 0.21 under identical conditions. Cross‑CVE transfer shows a strong directionality: detection works well when the source profile is broad (e.g., CWE‑307), but fails when it is narrow or when moving from one family to another, indicating that feature richness matters more than the CWE label.

## Significance  
These findings provide empirical evidence that generic HIDS can exploit shared syscall patterns across CVEs sharing a CWE class, offering a pathway for scalable intrusion detection. However, the results also reveal that not all weakness families are equally generalisable, underscoring the need for careful feature selection and calibrated FPR to avoid over‑confident or misleading alerts.

## Related Concepts  
- CVE (Common Vulnerabilities and Exposures)  
- CWE (Common Weakness Enumeration)  
- HIDS (Host Intrusion Detection System)  
- Syscall traces  
- Isolation Forest  
- SGD One‑Class SVM  
- Anomaly detection  
- False positive rate calibration
