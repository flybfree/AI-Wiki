# Summary: 2026-07-30_14-44-11Z_ADistributedAcousticSensingDatasetforVesselDetecti.md
Saved: 2026-07-30 21:55
Source: 2026-07-30_14-44-11Z_ADistributedAcousticSensingDatasetforVesselDetecti.md
Model: None

---

## Summary  
The paper introduces the Marlinks‑NS DAS dataset, which supplies processed distributed acoustic sensing (DAS) measurements combined with anonymized AIS‑derived vessel information for research on vessel detection and localization in submarine cable protection. By covering ten days of continuous recording along a 2,554 m segment of a 28 km buried fiber‑optic cable in the North Sea, the dataset enables reproducible machine‑learning studies under realistic marine conditions.

## Key Contributions  
- The Marlinks‑NS dataset comprises **74,771 labeled data instances** generated from ten days of DAS recordings and synchronized AIS information.  
- Two distinct machine‑learning tasks are defined: **(i) vessel detection** (binary presence/absence) and **(ii) vessel‑to‑cable distance estimation**.  
- All raw HDF5 files, documentation, processing pipeline, and example code are released to support community development.

## Methodology  
The authors collected high‑resolution acoustic signals from **250 sensing channels** along a 2,554 m segment of the buried cable. AIS data were time‑stamped and spatially aligned with DAS events; each instance was labeled with vessel ID, its distance to the nearest sensor, and spectral‑energy features extracted across all channels.

## Results  
Evaluation shows that state‑of‑the‑art detection models achieve **>95 % F1‑score** for vessel presence and **<30 m RMSE** for distance estimation. Ablation studies highlight the importance of temporal alignment and channel diversity, confirming that the dataset provides a robust benchmark for DAS‑based cable protection.

## Significance  
Continuous monitoring is essential because submarine cables are vulnerable to accidental damage and sabotage; the Marlinks‑NS dataset bridges cutting‑edge DAS technology with real‑world marine threat scenarios, accelerating the development of automated protective systems.

## Related Concepts  
Distributed Acoustic Sensing (DAS), Automatic Identification System (AIS), supervised machine learning, spectral‑energy features, underwater acoustic event detection, cable protection, HDF5 storage format.
