# Summary: 2026-07-28_09-24-17Z_CoTinyVLA_Chain_of_ThoughtDistillationforaSub_Bill.md
Saved: 2026-07-28 20:22
Source: 2026-07-28_09-24-17Z_CoTinyVLA_Chain_of_ThoughtDistillationforaSub_Bill.md
Model: None

---

## Summary  
CoTinyVLA introduces a sub‑billion‑parameter vision‑language‑action (VLA) model that translates natural‑language commands into robot actions while meeting strict embedded‑robot memory constraints. The authors achieve this by replacing the need for larger backbones with structured supervision, which reorganizes training data and inference pipelines rather than increasing model size. By integrating three complementary components—dual‑view temporal input, hierarchical chain‑of‑thought distillation, and paraphrase augmentation—the system attains robust performance across a wide range of perturbations on the LIBERO‑Plus benchmark. The result is a 0.9 B‑parameter backbone that outperforms all seven‑billion‑parameter baselines by several points on every suite.

## Key Contributions  
- A 0.9 B action model using a Qwen3.5‑0.8 B backbone reaches higher performance than the strongest 7 B baselines through structured supervision rather than sheer size.  
- The three components—dual‑view temporal input, hierarchical CoT distillation, and paraphrase augmentation—are separable and each contributes significantly to gains across different perturbation axes.  
- Structured supervision enables a small model to exceed all benchmark suites on the hardest tasks (e.g., Robot Initial States), demonstrating that organization of training data can outweigh raw parameter count.

## Methodology  
CoTinyVLA builds the action model around a Qwen3.5‑0.8 B backbone and trains it on LIBERO‑Plus perturbed tasks spanning seven dimensions. The dual‑view temporal input supplies 16 history frames per step from two cameras, annotated with textual camera and time markers to guide planning. Hierarchical chain‑of‑thought distillation transfers knowledge from a 35 B teacher into an episode‑level “Plan” span and chunk‑level “Think” spans that encode task phase, gripper state, and next subaction. Paraphrase augmentation expands the 40 base commands into 800 variants to increase data diversity. During inference, the model consumes only ~2.25 GiB of GPU memory, with the episode Plan identified as the load‑bearing component; replacing it incurs a 40–45 point drop in success.

## Results  
On LIBERO‑Plus spanning 10,030 perturbed tasks, CoTinyVLA achieves Spatial 90.8 %, Object 87.3 %, Goal 86.6 % and Long 80.7 %. It surpasses the strongest 7 B baselines by 4.7, 2.8, 15.9 and 3.0 points respectively on all four suites, with no zero‑margin intervals. Ablation experiments show that frame allocation between cameras and time contributes ~8.6 points alone. The model’s memory footprint is minimal compared to larger models while delivering superior robustness.

## Significance  
The work proves that structured supervision can let a sub‑billion‑parameter VLA surpass large, memory‑hungry baselines on robotics benchmarks, directly addressing the hardware constraints of embedded robots. This approach lowers deployment costs and opens the door for real‑time, low‑power action planning without sacrificing performance.

## Related Concepts  
Chain‑of‑Thought (CoT) reasoning, distillation, vision‑language‑action modeling, LIBERO‑Plus benchmark, structured supervision, hierarchical planning, paraphrase augmentation.
