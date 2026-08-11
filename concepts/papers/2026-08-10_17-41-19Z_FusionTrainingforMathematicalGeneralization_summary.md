# Summary: 2026-08-10_17-41-19Z_FusionTrainingforMathematicalGeneralizationinLarge.md
Saved: 2026-08-11 00:03
Source: 2026-08-10_17-41-19Z_FusionTrainingforMathematicalGeneralizationinLarge.md
Model: None

---

## Summary  
The paper investigates Thinking Mode Fusion (TMF), a technique that merges concise non‑thinking responses with long‑form reasoning within a single large language model, to improve mathematical generalization. It systematically examines how the data ratio between thinking and non‑thinking supervision and the training schedule affect model performance. The authors find an asymmetric interaction where more non‑thinking data harms the thinking mode, that different schedules can mitigate this trade‑off, and that a negative correlation persists across settings. These insights provide concrete guidance for designing effective TMF training regimes.

## Key Contributions  
- **Finding 1:** Increasing the ratio of non‑thinking supervision reduces the accuracy of the thinking mode, revealing an asymmetric interaction between the two modes.  
- **Finding 2:** Various training schedules modulate this trade‑off, and the optimal schedule is data‑ratio dependent.  
- **Finding 3:** A negative correlation exists between non‑thinking and thinking mode supervision, highlighting an inherent tension that must be managed.

## Methodology  
The authors construct a benchmark that varies the thinking‑to‑non‑thinking data ratio across three levels while testing three distinct training schedules (e.g., alternating epochs, weighted loss weighting, and schedule switching). By systematically varying both the proportion of supervision each mode receives and the temporal pattern of updates, they can isolate their effects on model behavior. This experimental design allows a clear comparison of how schedule choices influence the balance between concise and extended reasoning.

## Results  
Experiments show that when non‑thinking data dominate (high ratio), the thinking mode’s accuracy drops significantly compared to balanced ratios. The training schedules produce distinct patterns: alternating epochs preserve some thinking performance, weighted loss weighting reduces the drop, while schedule switching yields the best trade‑off for moderate ratios. A quantitative correlation analysis confirms a negative relationship between supervision amounts and thinking output quality.

## Significance  
These findings are crucial because they reveal that TMF is not a simple additive fusion; the way training data and schedules are allocated can degrade reasoning ability if non‑thinking supervision overwhelms the model. By providing evidence‑based recommendations for schedule selection, practitioners can design models that reliably support both concise answers and deep mathematical problem solving without sacrificing one for the other.

## Related Concepts  
- Thinking Mode Fusion (TMF) – a unified approach to concise vs. long‑form responses.  
- Data ratio – proportion of supervision assigned to each mode during training.  
- Training schedule – temporal pattern of model updates and loss weighting.  
- Non‑thinking mode – generates brief, factual answers.  
- Thinking mode – performs step‑by‑step reasoning.  
- Generalization in large language models – ability to apply learned knowledge across diverse tasks.
