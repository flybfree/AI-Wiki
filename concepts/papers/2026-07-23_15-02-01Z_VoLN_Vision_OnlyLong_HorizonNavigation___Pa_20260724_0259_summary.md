# Summary: 2026-07-23_15-02-01Z_VoLN_Vision_OnlyLong_HorizonNavigation___Paradigm_.md
Saved: 2026-07-24 02:59
Source: 2026-07-23_15-02-01Z_VoLN_Vision_OnlyLong_HorizonNavigation___Paradigm_.md
Model: None

---

## Summary  
This paper introduces Vision‑Only Long‑Horizon Navigation (VoLN), a paradigm that replaces the usual route‑level instructions in Vision‑and‑Language Navigation with locally observable cues, enabling agents to navigate long‑distance goals without GPS or external spatial priors. The authors propose VoLN‑UAV as a benchmark for aerial navigation and provide VoLN‑MLLM, an initial baseline that predicts short‑horizon waypoints from visual observations, goal views, semantic tokens, and proprioception. Their experiments on the five‑environment Test‑Unseen split show modest success rates (7.4 % Easy, 4.5 % Normal, 1.8 % Hard), highlighting remaining challenges in evidence integration and closed‑loop stability.

## Key Contributions  
- [Finding 1] VoLN shifts route‑relevant information from externally supplied instructions to locally detectable in‑scene cues, creating a vision‑only navigation task.  
- [Finding 2] The authors introduce the VoLN‑UAV benchmark with long‑horizon flight, continuous 3D motion, large viewpoint changes, and context‑dependent beacon selection.  
- [Finding 3] The baseline model VoLN‑MLLM aligns self‑supervised visual features with a structured semantic space to predict short‑horizon waypoints.

## Methodology  
The authors adopt a multimodal learning strategy: first, they generate a large dataset of aerial trajectories (VoLN‑UAV) where each episode contains a goal view and a sequence of in‑scene cues. Next, they build VoLN‑MLLM by training a model to retrieve visual–semantic tokens from the observation history, then predict the next waypoint segment using those tokens together with proprioceptive data. The model operates end‑to‑end without relying on GPS or pre‑computed route structures.

## Results  
On the Test‑Unseen split across five environments, VoLN‑MLLM achieves success rates of 7.4 % for Easy episodes, 4.5 % for Normal episodes, and 1.8 % for Hard episodes. These results demonstrate that while the approach can navigate long horizons using only visual cues, performance remains limited by difficulties in integrating distant evidence and maintaining closed‑loop stability.

## Significance  
VoLN provides a clean experimental framework to evaluate how much reliance on external route instructions is necessary for long‑horizon navigation, offering insights into the trade‑off between instruction fidelity and sensor autonomy. The benchmark and baseline model serve as a reference point for future research aiming at more robust vision‑only navigation.

## Related Concepts  
Vision‑and‑Language Navigation (VLN), long‑horizon navigation, in‑scene cues, visual–semantic tokens, proprioception, UAV aerial navigation, Test‑Unseen benchmark.
