---
title: Cross-Centaur: Modeling Individual Decision-Making Across Psychological Tasks with Language Models
url: http://arxiv.org/abs/2610.23157v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_08-55-00Z_Cross_Centaur_ModelingIndividualDecision_MakingAcr.md
generated_at: 2026-10-18 20:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Cross-Centaur, a language model fine-tuned to predict an individual participant's decisions across different psychological tasks by leveraging their observed behavior in a source task. The authors construct Cross-Psych-101, a dataset linking 591 participants across 12 distinct decision-making tasks, and demonstrate that Cross-Centaur outperforms both off-the-shelf LLMs and the prior Centaur model on held-out participants, both within and across tasks. Probing analyses reveal that the model's hidden representations encode participant-specific behavioral tendencies that generalize across task domains.

## Key Takeaways
- The authors release Cross-Psych-101, a novel dataset containing 591 participants and 261,551 valid decisions spanning 12 tasks across four categories (Bandit, Tradeoff, Structure, and Social), which uniquely links the same individuals across multiple experimental paradigms—a gap that existing large-scale behavioral datasets fail to address.
- Cross-Centaur is trained to predict a participant's actions in a target task using only the target-task description, the source-task description, and the same participant's actual behavior in the source task, enabling cross-task individual-level prediction rather than population-level generalization.
- The model outperforms both generic LLMs and the Centaur baseline on held-out participants, and probing analyses of its hidden states show that participant-level behavioral regularities are encoded in a way that transfers across task boundaries, suggesting the model captures stable individual decision-making signatures.

## Context
The broader research program of using LLMs as computational models of human cognition has progressed from population-level behavioral prediction (as in Centaur) toward the harder goal of modeling individual differences. Prior datasets aggregated decisions across participants without preserving identity links, effectively limiting models to learning average behavioral patterns. Cross-Centaur addresses this limitation by introducing cross-task participant linkage, pushing the field toward personalized cognitive modeling and raising methodological questions about how to construct behavioral datasets that preserve individual identity across experimental paradigms.

## Implications
For cognitive science researchers, this work demonstrates that individual-level behavioral data spanning multiple task domains can substantially improve predictive accuracy over population-level approaches, suggesting that future behavioral datasets should be designed with cross-task participant linkage as a priority. For practitioners in human-computer interaction, behavioral economics, and personalized AI systems, the ability to predict how a specific individual will behave in an unseen task from their behavior in a known task opens pathways toward adaptive interfaces, personalized decision aids, and more faithful computational models of human choice. The public release of Cross-Psych-101 on HuggingFace also provides a shared benchmark that can accelerate follow-up research on individual-level cognitive modeling with language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23157v1)
