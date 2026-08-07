# Summary: 2026-08-05_11-34-20Z_SmallFoundationModelsofHumanCognitionandBehaviour.md
Saved: 2026-08-06 21:40
Source: 2026-08-05_11-34-20Z_SmallFoundationModelsofHumanCognitionandBehaviour.md
Model: None

---

## Summary  
The authors investigate whether compact language‑model architectures can capture the essence of human cognition when fine‑tuned on large behavioural datasets. They train fourteen models ranging from 135 M to 14 B parameters and show that a narrow band of roughly 0.6–1 B parameters already matches the performance of a 70 B baseline, suggesting a ceiling effect in scaling. Their experiments also reveal that most model knowledge is encoded in prompt channels (task instructions, stimuli, feedback) rather than in choice history, and that trial‑order dependence can be detected through permutation tests.

## Key Contributions  
- **Finding 1:** A small parameter range (0.6 B–1 B) suffices to achieve performance comparable to a large 70 B model on held‑out participants, indicating a plateau in scaling for in‑distribution tasks.  
- **Finding 2:** Removing task instructions, experimental stimuli, outcome feedback, or choice history erodes up to 75.7 % of learned information and drives models below chance, showing that choice history alone cannot explain performance.  
- **Finding 3:** Trial‑order invariance holds for independent trials but sensitivity appears when later responses determine the order of subsequent trials, highlighting a dependence on task structure.

## Methodology  
The study builds fourteen foundation models across four architecture families using Psych‑101, a dataset of 10.7 million trial‑level choices from 160 experiments. Models are evaluated both in‑distribution (scaling with model size) and out‑of‑distribution (novel task structures). The authors systematically strip each of four prompt channels across 27 experiments and permute trial order to isolate the role of content versus sequence.

## Results  
In‑distribution scaling is negligible; models plateau around 0.6–1 B parameters, matching a 70 B baseline on new participants. Out‑of‑distribution performance improves sharply with larger models, confirming a steeper scaling gradient beyond the training paradigm. Stripping stimuli or feedback reduces accuracy by ~75.7 % and pushes predictions below chance, indicating that these channels carry most of the model’s knowledge. Permutation tests reveal invariance for independent trials but sensitivity when trial order is contingent on prior responses.

## Significance  
These findings demonstrate that compact models can serve as effective “noise ceiling” estimators for psychological experiments, offering a low‑cost proxy for cognition. However, their utility remains bounded by the specific task structures present in training data, underscoring limits of generalisation to novel cognitive paradigms.

## Related Concepts  
- Foundation models  
- Cognitive proxies  
- Scaling laws and ceiling effects  
- Prompt channel importance  
- Trial‑order dependence  
- Fine‑tuning on behavioural datasets
