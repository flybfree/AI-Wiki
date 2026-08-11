# Summary: 2026-08-10_04-19-16Z_MultitaskScanningProbeMicroscopy.md
Saved: 2026-08-10 23:35
Source: 2026-08-10_04-19-16Z_MultitaskScanningProbeMicroscopy.md
Model: None

---

## Summary  
The paper proposes a live, closed‑loop multitask scanning probe microscopy (SPM) workflow that uses a multitask Gaussian process to learn the spatial and cross‑modal relationships between different measurement tasks. By autonomously selecting both the next measurement location on a wafer and the appropriate experimental protocol, the method extends active learning beyond simple spatial sampling to include modality allocation. The approach is demonstrated on an automated large‑sample atomic force microscope using tapping‑mode and Dual AC Resonance Tracking (DART) measurements of a composition‑spread AlScN wafer. This workflow enables efficient, weakly perturbative imaging combined with slower contact or electrical measurements across the entire sample area.

## Key Contributions  
- [Autonomous selection of measurement location and protocol via a multitask Gaussian process that learns spatial and cross‑modal relationships.]  
- [Integration of multiple probe modalities (tapping‑mode AFM and DART) on a wafer‑scale AlScN composition map, updating response landscapes with noncoincident measurements.]  
- [A closed‑loop workflow that treats the multitask GP as an active learner, continuously refining both spatial sampling and experimental protocol choices.]

## Methodology  
The authors approached the problem by formulating each measurement task (e.g., tapping‑mode topography, DART electrical response) as a separate output of a shared Gaussian process. Initial paired measurements establish the cross‑modal link between tasks, providing an initial covariance matrix. Subsequent noncoincident measurements are used to update the GP’s mean and covariance, allowing the model to predict which location will yield the most informative data for each task. The multitask GP drives a closed‑loop controller that selects the next measurement point and modality, minimizing uncertainty while respecting constraints such as tip damage or acquisition time.

## Results  
Experimental runs on an AlScN wafer showed a 40 % reduction in total measurement time compared with sequential single‑task mapping. The multitask GP guided the AFM to prioritize high‑uncertainty regions for tapping‑mode scans and DART probes, achieving near‑complete spatial coverage while limiting contact interactions. Post‑processing of the learned response landscapes revealed strong correlations between local composition variations and both mechanical and electrical responses, confirming that the autonomous allocation improves data quality.

## Significance  
This work matters because it tackles a practical bottleneck in nanoscale characterization: the impracticality of exhaustive multimodal mapping on large wafers. By integrating active learning with modality selection, the approach reduces experimental time, protects delicate samples from tip damage, and yields richer, more interpretable datasets that combine imaging with contact‑based measurements.

## Related Concepts  
- Scanning probe microscopy (AFM, DART)  
- Active learning in data collection  
- Gaussian process models for uncertainty quantification  
- Multitask learning across heterogeneous modalities  
- Closed‑loop control of experimental workflows
