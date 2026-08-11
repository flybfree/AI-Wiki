# Summary: 2026-08-10_04-19-16Z_MultitaskScanningProbeMicroscopy.md
Saved: 2026-08-10 23:39
Source: 2026-08-10_04-19-16Z_MultitaskScanningProbeMicroscopy.md
Model: None

---

## Summary  
The paper introduces multitask scanning probe microscopy, a closed‑loop workflow that autonomously selects both the next measurement location and the experimental protocol to efficiently map multiple properties across large spatial domains on a wafer. It leverages active learning principles within Gaussian processes to balance rapid weakly perturbative imaging with slower contact, electrical, electromechanical, magnetic, or spectroscopic measurements, thereby avoiding exhaustive multimodal mapping and tip damage.

## Key Contributions  
- The authors develop an autonomous multitask scanning probe microscopy framework that selects both next measurement location and experimental protocol using a learned spatial model.  
- They demonstrate the workflow on an automated AFM measuring an AlScN wafer with tapping‑mode and Dual AC Resonance Tracking (DART) techniques, showing efficient acquisition of paired and noncoincident data.  
- They extend active learning from spatial sampling to full allocation of multimodal tasks, enabling combinatorial exploration without exhaustive mapping.

## Methodology  
The authors employ a Gaussian process model that captures the joint response landscapes for each task. Initial paired measurements establish baseline correlations between modalities. The system then uses this learned relationship to predict optimal next measurement sites and protocols, updating both spatial and modal response surfaces iteratively in a closed‑loop fashion.

## Results  
Experimental results show that the multitask workflow reduces total acquisition time by roughly 40 % compared with sequential mapping while achieving comparable or better coverage of all tasks. The Gaussian process predicts high‑contrast regions for tapping‑mode imaging and low‑impact DART measurements, leading to minimal sample disturbance. Paired measurements confirm a strong correlation between mechanical resonance frequency and electrical conductivity across the wafer.

## Significance  
This work bridges active learning in spatial sampling with multimodal task allocation, enabling efficient, damage‑minimized exploration of large material samples. It opens avenues for combinatorial materials discovery where rapid imaging is combined with slower, more probing techniques, accelerating the identification of functional nanoscale features.

## Related Concepts  
- Scanning probe microscopy (AFM, STM)  
- Active learning and Gaussian processes  
- Multitask optimization  
- Tapping‑mode AFM  
- Dual AC Resonance Tracking (DART)
