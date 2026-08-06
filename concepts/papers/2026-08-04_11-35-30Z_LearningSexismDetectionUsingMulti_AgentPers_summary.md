# Summary: 2026-08-04_11-35-30Z_LearningSexismDetectionUsingMulti_AgentPerspectivi.md
Saved: 2026-08-05 20:21
Source: 2026-08-04_11-35-30Z_LearningSexismDetectionUsingMulti_AgentPerspectivi.md
Model: None

---

## Summary  
The paper addresses the problem that human sexism detection labels often disagree because annotators genuinely perceive bias differently, yet most NLP systems collapse this diversity into a simple majority vote. To preserve these varied perspectives, the authors introduce Multi‑Agent Perspectivist Preference Optimization (MAP‑PO), a framework that clusters annotators by their labeling behavior and fine‑tunes separate large language models to reproduce each cluster’s style. MAP‑PO then optimizes agents’ preferences using both individual and team‑level rewards, allowing the system to respect minority viewpoints while still aligning with the overall majority label. This approach retains annotator diversity that is otherwise discarded.

## Key Contributions  
- **Finding 1**: Without fine‑tuning the agents converge to near‑identical behavior, demonstrating that cluster‑specific training is essential for preserving distinct perspectives.  
- **Finding 2**: Training each agent only on its own cluster’s labels pushes it far beyond the intended cluster, causing over‑representation and misalignment with the cluster’s true annotation style.  
- **Finding 3**: Adding a shared team‑level training signal consistently keeps each agent calibrated to its cluster, improving overall calibration without sacrificing diversity.

## Methodology  
The authors first analyze the EXIST 2024 dataset of labeled English and Spanish tweets by clustering annotators based on their labeling patterns rather than demographic attributes. Each identified cluster is then fine‑tuned with a dedicated large language model agent whose sole task is to reproduce that cluster’s annotation behavior. MAP‑PO orchestrates these agents through a preference optimization loop that combines individual reward signals (encouraging each agent to stay true to its cluster) and team‑level rewards (ensuring the collective output reflects the majority label). The coordination uses reinforcement learning with a multi‑agent policy gradient, allowing agents to negotiate their outputs while respecting both personal and group objectives.

## Results  
Experiments were conducted in four settings: English and Spanish texts using two different backbone language models. In all cases, each agent reproduces the labels of its own cluster, and together they reproduce the majority label across the dataset. Crucially, agents that are not fine‑tuned behave almost identically, confirming the necessity of per‑cluster training. Agents trained solely on their cluster’s labels overfit and deviate from the cluster’s style, whereas the shared team signal restores proper calibration. These findings hold uniformly across languages and backbones.

## Significance  
By preserving annotator diversity rather than discarding it through majority voting, MAP‑PO yields sexism detection models that are more robust to nuanced human judgments and less prone to systematic bias. The framework demonstrates that retaining multiple perspectives can improve both fairness and accuracy in NLP tasks that rely on human labeling.

## Related Concepts  
Multi‑agent learning, perspectivist modeling, preference optimization, clustering of annotators, large language model fine‑tuning, team vs individual rewards, reinforcement learning policy gradients.
