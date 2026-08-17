# Summary: 2026-08-14_07-26-38Z_DemystifyingAgentSkills_WhyTheyWork_UntilTheyDon_t.md
Saved: 2026-08-16 21:42
Source: 2026-08-14_07-26-38Z_DemystifyingAgentSkills_WhyTheyWork_UntilTheyDon_t.md
Original paper: [arXiv](http://arxiv.org/abs/2608.14036v1)
Model: None

---

## Summary  
The paper investigates why LLM agent skills succeed or fail during inference, moving beyond aggregate success metrics to understand the mechanisms behind skill effectiveness. It proposes a taxonomy of skill‑use modes and identifies key factors such as representation, outcome annotation, retrieval difficulty, and cross‑framework robustness. By combining quantitative experiments with paired trajectory analysis, it reveals that skills primarily stabilize execution rather than inject facts. The study also shows that retrieval precision degrades sharply as pool size increases.

## Key Contributions  
- Finding 1: Skills work when noisy trajectories become procedural anchors that stabilize execution.  
- Finding 2: Retrieval pools beyond ~5 items cause precision drops from 29.6 % to 3.3 %, indicating a bottleneck.  
- Finding 3: Skill failure is linked to brittle assumptions, incompatible contexts, or insufficient adaptation.

## Methodology  
The authors conducted controlled experiments across multiple LLMs and agent harnesses, normalizing 8,135 trial records into 238 unique labels from 240 open‑coded records. They performed quantitative comparisons between skill‑enabled agents and the baseline Workflow Memory while also conducting paired trajectory analysis to trace execution patterns. The data were normalized and categorized using a taxonomy of three high‑level categories and twelve skill‑use modes.

## Results  
In matched comparisons, skills improved task success by 6.06 points over Workflow Memory. Retrieval precision fell from 29.6 % with five items to 3.3 % with one hundred items, highlighting the bottleneck effect. Procedural anchoring accounted for 65.7 % of skill cases versus only 4.5 % for explicit knowledge injection. Skills failed in contexts where assumptions were violated or adaptation was insufficient.

## Significance  
These findings shift evaluation from simple success rates to mechanistic understanding, enabling more reliable self‑evolving agents that can adapt skills appropriately. By exposing the limits of retrieval and the importance of procedural stabilization, the work guides safer deployment of skill‑based LLMs in real‑world settings.

## Related Concepts  
- LLM agents  
- Skill harnesses  
- Retrieval precision  
- Procedural anchoring  
- Workflow Memory  
- Cross‑framework robustness
