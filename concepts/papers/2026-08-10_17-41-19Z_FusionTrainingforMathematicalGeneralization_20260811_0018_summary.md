# Summary: 2026-08-10_17-41-19Z_FusionTrainingforMathematicalGeneralizationinLarge.md
Saved: 2026-08-11 00:18
Source: 2026-08-10_17-41-19Z_FusionTrainingforMathematicalGeneralizationinLarge.md
Model: None

---

## Summary  
The paper investigates how training a large language model in two complementary modes—thinking and non‑thinking—affects mathematical generalization. It introduces Training Mode Fusion (TMF) and studies the interplay between the proportion of each mode’s data and the order in which they are trained. The goal is to uncover optimal schedules that maximize both modes’ performance.

## Key Contributions  
- Increasing the ratio of non‑thinking supervision degrades the accuracy of the thinking mode, revealing an asymmetric trade‑off.  
- Different training schedules can mitigate or exacerbate this trade‑off, indicating schedule dependence on data ratio.  
- A negative correlation between supervision amounts for the two modes is quantified, highlighting inherent tension.

## Methodology  
The authors construct a benchmark with multiple thinking‑to‑non‑thinking data ratios and three distinct training schedules. They systematically vary the proportion of data allocated to each mode and observe model performance across cycles. Experiments are conducted on a set of mathematical problem‑solving tasks, measuring both modes’ outputs.

## Results  
Experiments show that when non‑thinking data dominate, thinking accuracy drops sharply; conversely, balanced ratios improve overall performance. Schedule A (alternating blocks) yields the best trade‑off for moderate ratios, while schedule B (long training in one mode) harms the other. The negative correlation reaches a peak at high non‑thinking ratios.

## Significance  
Understanding this tension informs practical TMF design, enabling researchers to avoid unintended degradation of reasoning capabilities when scaling up non‑thinking supervision. It also offers a principled framework for balancing efficiency and accuracy in large language model training.

## Related Concepts  
- Training Mode Fusion (TMF)  
- Data ratio  
- Training schedule  
- Non‑thinking mode  
- Thinking mode  
- Mathematical generalization
