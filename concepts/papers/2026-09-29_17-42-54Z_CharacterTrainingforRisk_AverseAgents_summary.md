# Summary: 2026-09-29_17-42-54Z_CharacterTrainingforRisk_AverseAgents.md
Saved: 2026-09-29 22:17
Source: 2026-09-29_17-42-54Z_CharacterTrainingforRisk_AverseAgents.md
Original paper: [arXiv:2609.38093](http://arxiv.org/abs/2609.38093v1)
Model: qwen3.6-35b-a3b

---

## Summary
This paper introduces "Character Training," a novel methodology designed to instill risk aversion in artificial intelligence agents, thereby mitigating the potential for catastrophic harm caused by misaligned systems. The authors propose that agents predisposed to avoid risky outcomes are more likely to engage in cooperative behaviors, such as negotiation with humans, rather than pursuing dangerous strategies like rebellion. By defining a model constitution based on Constant Absolute Risk Aversion (CARA) and using on-policy distillation, the study demonstrates that persona traits can serve as a robust mechanism for shaping agent dispositions. The research highlights that this approach not only achieves competitive performance against directly trained baselines but also offers superior generalization capabilities across different distributions.

## Key Contributions
- **Robust Instillation of Risk Preferences**: The authors demonstrate that character training effectively instills risk aversion by leveraging persona traits, providing a scalable method to shape broad behavioral dispositions in AI agents without requiring extensive task-specific data.
- **Superior Out-of-Distribution Generalization**: Character-trained models exhibit better generalization capabilities than baselines trained directly on the benchmark, particularly when faced with decision formats or scenarios not encountered during the training phase.
- **Identification of Critical Training Factors**: The study identifies that the token budget allocated for character definitions and the specific choice of base model are the most influential factors in successfully instilling risk aversion through this method.

## Methodology
The authors approach the problem by constructing a formal "model constitution" that explicitly describes Constant Absolute Risk Aversion (CARA) regarding an agent's resources. This constitutional framework is then instilled into the agents through on-policy distillation, a process where the model learns to mimic risk-averse behaviors based on predefined principles rather than just outcome-based rewards. The experimental setup involves training multiple models with this character-driven approach and comparing their performance against standard baselines that are trained directly on the decision-making benchmark. Crucially, the character-trained models were never exposed to the specific format of the benchmark during training, allowing the authors to test for genuine generalization rather than memorization.

## Results
Experimental results indicate that agents trained via character methods are competitive with those trained directly on the benchmark tasks, despite having less direct exposure to the evaluation criteria. In out-of-distribution tests across four different models, two of them showed significantly better generalization performance compared to their baselines. Furthermore, ablation studies revealed that modulating aspects of the constitution had varying impacts; specifically, the size of the token budget used to describe the character and the underlying model architecture were found to be the primary drivers of successful risk aversion induction.

## Significance
This research is significant because it offers a promising and scalable pathway to align AI systems with human safety interests by targeting their fundamental dispositions rather than just their immediate outputs. By proving that broad personality traits can reliably influence risk assessment, this work provides a practical tool for developers to mitigate the risks posed by potentially misaligned but powerful AI agents, encouraging safer, more cooperative interactions in high-stakes environments.

## Related Concepts
- Risk Aversion
- AI Alignment
- Character Training
- Model Constitution
- On-Policy Distillation
- Constant Absolute Risk Aversion (CARA)
- Out-of-Distribution Generalization
