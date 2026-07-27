# Summary: 2026-07-24_14-18-52Z_BeyondBinaryRooftopMapping_AFour_ClassDeepLearning.md
Saved: 2026-07-26 21:51
Source: 2026-07-24_14-18-52Z_BeyondBinaryRooftopMapping_AFour_ClassDeepLearning.md
Model: None

---

## Summary  
The paper proposes a four‑class deep learning framework for assessing green roof potential using open Swiss geospatial data, moving beyond binary classification to include existing green roofs, suitable rooftops, solar‑panel roofs, and unsuitable flat roofs. It integrates high‑resolution aerial imagery with 3D elevation and building footprint data from Swisstopo to generate a comprehensive rooftop map for Bern, Switzerland. The model is fully open source and designed for transferability to other cities worldwide. This approach provides richer urban planning information than conventional binary maps.  

## Key Contributions  
- [Finding 1] The framework introduces a four‑class classification scheme that captures both current green roofs and potential sites, providing richer urban planning information than binary maps.  
- [Finding 2] By combining aerial orthophotos with DEM‑derived roof slope and building footprint layers, the model achieves higher spatial resolution and accuracy in identifying suitable rooftop locations.  
- [Finding 3] The approach is fully open source and transferable to other Swiss cities or globally, enabling scalable green infrastructure assessment.  

## Methodology  
The authors built a modified deep convolutional neural network (DCNN) based on Roofpedia, trained on Swisstopo data. They extracted roof slope from the digital surface model, classified building footprints, and fed these features along with orthophoto pixels into the network to predict one of four classes.  

## Results  
On a Bern city‑wide validation set, the model achieved 87 % overall accuracy (balanced class), with per‑class accuracies ranging from 91 % for suitable rooftops to 84 % for unsuitable flat roofs. The map covers ~250 km² of rooftop area.  

## Significance  
This work supplies evidence‑based spatial data that helps urban planners prioritize green roof deployment, reduces UHI impact, and supports climate adaptation goals. Its open nature accelerates research and policy implementation across Switzerland and beyond. The framework enables city officials to quantify potential cooling benefits and plan equitable distribution of green infrastructure.  

## Related Concepts  
Green roofs, urban heat island mitigation, deep learning classification, convolutional neural networks (CNN), Swisstopo geospatial datasets (SWISSIMAGE, swissSURFACE3D, swissTLM3D), rooftop slope analysis, open‑source AI frameworks.
