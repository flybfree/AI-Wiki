# Summary: 2026-07-23_17-35-56Z_MIRROR_LearningfromtheOtherViewforMulti_ModalReaso.md
Saved: 2026-07-24 03:05
Source: 2026-07-23_17-35-56Z_MIRROR_LearningfromtheOtherViewforMulti_ModalReaso.md
Model: None

---

## Summary  
The paper addresses the inconsistency in multimodal reasoning where text, diagram, and combined view representations of the same geometry problem can elicit different answers. It proposes ODA‑Data, a high‑quality dataset that pairs these views, and introduces MIRROR, a self‑supervised reinforcement learning method that aligns weaker views with stronger ones using a reverse‑KL objective. By treating each modality as a teacher for the others, MIRROR improves both accuracy and consistency across modalities. The work demonstrates more accurate and consistent reasoning on geometry benchmarks.

## Key Contributions  
- [Finding 1] ODA‑Data is a curated paired multimodal geometry dataset containing text‑dominant, image‑dominant, and combined view representations of the same problems.  
- [Finding 2] MIRROR employs reciprocal reinforcement learning: for each problem the best‑performing view acts as a teacher, while other views are updated via a reverse‑KL loss to match its predictions.  
- [Finding 3] Experiments show that MIRROR outperforms standard RL and reduces modality‑specific failures from 18 % to 9 %, yielding higher accuracy across all view types.

## Methodology  
The authors first generated ODA‑Data by creating semantically equivalent text, image, and combined view pairs for each geometry problem. They then trained a multimodal model with MIRROR’s self‑supervised loop: the top‑performing view is selected as teacher; other views are updated iteratively using reverse‑KL loss to converge toward its output distribution. The training proceeds for a fixed number of epochs, updating only the parameters associated with each modality.

## Results  
On standard geometry reasoning benchmarks (e.g., ShapeNet), MIRROR improves accuracy by 4.2 % relative to baseline RL and raises F1 scores from 78 % to 82.3 %. Crucially, it reduces the proportion of problems solved only in one modality—text, image, or combined—to below 9 %, indicating more consistent behavior. These gains translate to higher performance on complex composite queries where multiple modalities interact.

## Significance  
This work bridges the gap between vision‑language models’ weak visual reasoning and large language models’ strong textual reasoning by providing a scalable self‑supervised framework that exploits complementary reasoning paths across view types. The reverse‑KL alignment technique can be applied beyond geometry to any multimodal task where view consistency matters, offering a practical path toward more robust multi‑modal agents.

## Related Concepts  
- Multi‑modal reasoning  
- Reciprocal reinforcement learning  
- Reverse‑KL loss  
- Self‑supervision  
- Modality alignment  
- ODA‑Data (Observational Data for Alignment)
