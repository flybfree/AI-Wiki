---

title: "Summary: OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories"
url: http://arxiv.org/abs/2605.04036v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-05_17-55-25Z_OpenSeeker_v2_PushingtheLimitsofSearchAgentswithIn.md
generated_at: "2026-06-11 10:28"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper demonstrates that a simple supervised fine‑tuning (SFT) approach can achieve state‑of‑the‑art performance on frontier search agents when trained with informative and high‑difficulty trajectories. The authors report OpenSeeker‑v2 surpassing heavy pipeline models across four benchmarks while using only 10.6 k data points.

## Key Takeaways
- SFT with a modest dataset of 10.6 k points reaches state‑of‑the‑art results, outperforming the industry standard CPT+SFT+RL pipeline.
- OpenSeeker‑v2 is the first SOTA search agent in its model scale and paradigm to be built by an academic team using only SFT.
- The model exceeds Tongyi DeepResearch on BrowseComp (46.0 % vs 43.4 %), BrowseComp‑ZH (58.1 % vs 46.7 %), Humanity’s Last Exam (34.6 % vs 32.9 %) and xbench (78.0 % vs 75.0 %).

## Context
Deep search is a critical competency for large language models, yet its development relies on costly industrial pipelines involving pre‑training, continual pre‑training, supervised fine‑tuning, and reinforcement learning. This work shows that effective training can be achieved with lightweight methods.

## Implications
The findings suggest that academic teams can compete with industry leaders without massive resources, lowering the barrier to entry for frontier search research. Open‑sourcing the model weights will enable broader experimentation and democratize access to high‑quality search agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.04036v1)
