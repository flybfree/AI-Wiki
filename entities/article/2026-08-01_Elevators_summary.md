# Summary: 2026-08-01_Elevators.md
Saved: 2026-08-01 00:03
Source: 2026-08-01_Elevators.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
The article explores how elevators operate using simple and sophisticated algorithms such as SCAN, LOOK, and Otis’ RSR system, highlighting that wait times are not uniform but follow a distribution where the p90 (the time 90 % of riders experience) is what passengers most notice. It explains why these algorithms matter for both passenger satisfaction and building efficiency.

## Key Takeaways  
- The SCAN algorithm is the oldest method, moving from lobby to top floor before reversing, which creates unnecessary long waits.  
- LOOK improves on this by stopping only as high as needed, reducing wait times but still limited in real‑time responsiveness.  
- RSR dynamically scores each car based on ETA, load, direction, and idle proximity, re‑optimizing every few seconds to match the most suitable elevator.

## Context  
This discussion reflects broader AI challenges of dynamic resource allocation: assigning tasks to agents (elevator cars) in real time while accounting for constraints such as capacity, location, and priority. The RSR scoring resembles reinforcement‑learning reward functions that balance multiple objectives, a pattern increasingly used in autonomous vehicle routing, cloud load balancing, and logistics optimization.

## Implications  
Understanding elevator wait distributions informs AI research on latency metrics (p90) and the design of adaptive scheduling policies. For the industry, better algorithms translate into higher passenger satisfaction, lower energy consumption, and more reliable building operations—demonstrating how micro‑scale real‑time decision making can be a testbed for larger AI systems that must balance competing goals under uncertainty.
