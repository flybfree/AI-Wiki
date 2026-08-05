# Summary: 2026-07-28_13-52-12Z_SharedVoxel_Map_BasedCooperativeIndoorUAVGuidancew.md
Saved: 2026-07-28 20:30
Source: 2026-07-28_13-52-12Z_SharedVoxel_Map_BasedCooperativeIndoorUAVGuidancew.md
Model: None

---

## Summary  
The paper proposes a cooperative indoor UAV guidance framework that jointly leverages a shared voxel‑map world model and a multi‑agent Soft Actor‑Critic (MASAC) controller to enable multiple drones to navigate complex, GNSS‑denied environments. By fusing 360 LiDAR scans into a compact bird’s‑eye‑view representation, each drone receives an ego‑aligned local crop of the map while still contributing to a global occupancy model. The learned policy combines map features, near‑field obstacle data, and peer state information through a centralised training regime that yields decentralised continuous actions. This design achieves high success rates in simulated corridor navigation and demonstrates stable operation in real‑world experiments.

## Semantic links
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 4 title terms overlap; 17 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 4 title terms overlap; 121 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A shared voxel‑map occupancy representation enables scalable spatial fusion across multiple UAVs, reducing redundant perception overhead while preserving a common understanding of the environment.  
- [Finding 2] The integrated “integrate‑in‑world, act‑in‑ego” architecture allows each agent to operate locally with continuous control yet remain coordinated through a centrally trained policy.  
- [Finding 3] Offline imitation fine‑tuning bridges sim‑to‑real mismatch, delivering robust performance in GNSS‑denied indoor settings where prior methods fail.

## Methodology  
The authors first construct a voxel‑map from the concatenated LiDAR scans of all drones, then compress this map into a bird’s‑eye‑view (BEV) that is projected onto each drone’s local coordinate frame. The BEV, together with per‑drone obstacle observations and compact goal/peer‑state encodings, serves as input to a multi‑agent Soft Actor‑Critic network trained in a centralised fashion. After training, the policy is exported to the drones for real‑time execution. To mitigate domain shift, the simulation policy is fine‑tuned using imitation learning from recorded trajectories captured on a physical testbed.

## Results  
In simulated corridor navigation tasks with varying obstacle densities, the learned MASAC controller achieved a 90.3 % success rate, surpassing Astar planning (≈78 %), an artificial potential‑field controller (≈65 %), and a prior guidance method (≈52 %). Real‑world experiments in GNSS‑denied indoor environments with two UAVs demonstrated stable cooperative operation across increasingly challenging obstacle layouts, maintaining success rates above 80 % over extended missions.

## Significance  
This work advances the state of cooperative indoor UAV guidance by providing a unified spatial substrate that scales to many agents and enables learned, decentralised control. The combination of shared voxel‑map representation with MASAC offers a path toward more flexible, robust navigation systems that can be deployed in real‑time without heavy central coordination.

## Related Concepts  
- Voxel‑map occupancy model  
- Bird’s‑eye‑view (BEV) compression  
- Multi‑agent Soft Actor‑Critic (MASAC)  
- Integrate‑in‑world / act‑in‑ego design  
- Offline imitation fine‑tuning
