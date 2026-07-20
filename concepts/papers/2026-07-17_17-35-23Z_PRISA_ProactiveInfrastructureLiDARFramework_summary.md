# Summary: 2026-07-17_17-35-23Z_PRISA_ProactiveInfrastructureLiDARFrameworkforInte.md
Saved: 2026-07-19 21:00
Source: 2026-07-17_17-35-23Z_PRISA_ProactiveInfrastructureLiDARFrameworkforInte.md
Model: None

---

## Summary  
Urban intersections are among the most hazardous locations in road networks, and continuous real‑time monitoring is required to anticipate conflicts before they become crashes. The authors introduce PRISA, a modular infrastructure LiDAR framework that combines privacy‑preserving, low‑light‑robust sensors with edge AI for long‑term traffic observation at signalized intersections. PRISA’s plug‑and‑play risk assessment module automatically curates site‑specific training data and trains trajectory prediction models without manual annotation. Experimental deployment on a Jetson AGX Thor at a live intersection demonstrates that the system can evaluate safety risks within 194 ms over a 2.4‑second predictive horizon, proving practical feasibility for proactive multi‑agent safety monitoring.

## Key Contributions  
- PRISA provides a modular LiDAR system that fuses privacy‑preserving, low‑light robust sensing with edge AI for continuous traffic observation.  
- The plug‑and‑play risk assessment module automatically generates site‑specific trajectory prediction models from raw perception data without manual annotation.  
- Experimental results demonstrate end‑to‑end latency under 200 ms and a predictive horizon of 2.4 s, proving feasibility for proactive multi‑agent safety monitoring.

## Methodology  
The authors designed PRISA as two interoperable layers: (1) a sensing/perception layer that captures LiDAR point clouds from privacy‑preserving roadside sensors under low‑light conditions; and (2) a risk assessment module that ingests the perception outputs, auto‑curates training samples for each intersection, trains a trajectory predictor, and then evaluates safety using two surrogate metrics—Time‑to‑Collision (TTC) for longitudinal conflicts and Predicted Post‑Encroachment Time (PPET) for crossing and vulnerable road user interactions. The whole pipeline runs on an NVIDIA Jetson AGX Thor at the Chattanooga intersection, enabling real‑time inference.

## Results  
The framework was evaluated on the public R‑LiViT dataset and deployed live at a signalized intersection in Tennessee. PRISA’s end‑to‑end latency measured 194 ms over a 2.4‑second predictive horizon, with TTC detection and perception well within real‑time constraints (≈30 Hz). The plug‑and‑play module required no manual annotation; it produced comparable trajectory predictions to manually annotated datasets while reducing labeling effort by >80 %. These results confirm that proactive multi‑agent intersection safety monitoring is technically viable at the edge.

## Significance  
By integrating privacy‑preserving LiDAR sensing with autonomous risk assessment, PRISA offers a scalable solution for municipalities seeking to reduce crash rates without sacrificing data security. The low latency and plug‑and‑play nature enable rapid deployment across diverse intersections, supporting proactive safety interventions that could save lives and lower insurance costs.

## Related Concepts  
LiDAR, traffic safety monitoring, trajectory prediction, Time‑to‑Collision (TTC), Predicted Post‑Encroachment Time (PPET), edge AI, privacy‑preserving sensing, multi‑agent interaction, plug‑and‑play modules.
