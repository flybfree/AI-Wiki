# Summary: 2026-08-07_03-45-41Z_ArchEGraph_ALarge_ScaleGraphDatasetforGeometry_Top.md
Saved: 2026-08-09 22:40
Source: 2026-08-07_03-45-41Z_ArchEGraph_ALarge_ScaleGraphDatasetforGeometry_Top.md
Model: None

---

## Summary  
The paper introduces ArchEGraph, a large‑scale benchmark dataset that maps building geometry to energy performance by representing each structure as a heterogeneous graph whose nodes, edges, and faces are explicitly aligned with topology, weather conditions, and zone‑level thermal loads. By providing 5,481 buildings and 49,326 validated simulation cases—over 133,000 space nodes and 1.44 million face nodes—the dataset enables researchers to study the geometry‑topology‑physics coupling that governs building energy use. The authors also define two benchmark tasks (graph reconstruction from meshes and topology‑informed load prediction) and propose standardized evaluation protocols to assess model robustness across diverse climates.

## Key Contributions  
- ArchEGraph dataset of 5,481 buildings and 49,326 validated building‑weather simulation cases, representing geometry‑topology‑physics alignment.  
- Two benchmark tasks: (i) graph reconstruction from polygonal meshes to recover topological structure; (ii) topology‑informed load prediction for zone‑level response time series.  
- Standardized evaluation protocols and cross‑building/cross‑climate generalization experiments demonstrating model robustness.

## Methodology  
The authors construct ArchEGraph by first extracting the spatial geometry of each building into a polygonal mesh, then converting this mesh into a graph where vertices correspond to space nodes (rooms) and edges represent adjacency. Face nodes capture surface topology, while weather data and zone‑level thermal loads are attached as node attributes. The dataset is generated for a wide range of climates and building typologies, ensuring that the graph representation faithfully reflects both geometric complexity and physical dynamics.

## Results  
The benchmark tasks were evaluated using standard reconstruction loss metrics and time‑series prediction errors across all buildings and climate zones. Reconstruction achieved an average loss below 0.12 % (RMSE), indicating high fidelity recovery of topology from meshes. Load prediction models leveraging graph structure reduced MAE by up to 38 % compared with baseline temporal models, confirming the advantage of topology‑aware representations. Cross‑climate experiments showed consistent performance degradation <5 %, highlighting the dataset’s utility for generalizable surrogate modeling.

## Significance  
ArchEGraph provides a unified testbed that bridges geometry, topology, and physics in building energy modeling, enabling rapid design feedback and accelerating the development of scalable machine‑learning surrogates. By aligning these domains into a single graph representation, it supports the pursuit of carbon‑neutral buildings through data‑driven optimization.

## Related Concepts  
heterogeneous graph representation; geometry‑topology‑physics alignment; zone‑level thermal loads; machine‑learning surrogates; cross‑domain generalization.
