# Summary: 2026-07-20_16-08-49Z_LLM_as_a_Coach_ExperientialLearningforNon_Verifiab.md
Saved: 2026-07-24 00:32
Source: 2026-07-20_16-08-49Z_LLM_as_a_Coach_ExperientialLearningforNon_Verifiab.md
Model: None

---

## Summary  
The paper introduces Experiential Learning (EL), a method that replaces the scalar reward of traditional reinforcement‑learning (RL) with richer feedback from an LLM‑as‑a‑Coach, preserving fine‑grained textual assessments. By repurposing the judge’s evaluation into transferable experiential knowledge, EL conditions a teacher model whose on‑policy context is distilled back to the policy. This higher‑bandwidth channel yields dense supervision and maintains distinct quality profiles among responses. The authors show that EL consistently outperforms rubric‑based RL on both held‑out and unseen open‑ended tasks.

## Key Contributions  
- [Finding 1] Experiential Learning repurposes the LLM‑as‑a‑Judge feedback into a teacher model that conditions the policy via on‑policy context distillation.  
- [Finding 2] EL provides dense supervision and preserves fine‑grained preferences, leading to superior performance compared with scalar rewards on held‑out and unseen tasks.  
- [Finding 3] The method generalizes beyond the training distribution and mitigates reward hacking, indicating a more robust learning signal.

## Methodology  
The authors adopt reinforcement learning for open‑ended tasks but use an LLM as a coach rather than a scalar reward function. Each on‑policy response is evaluated by the coach, whose assessment is distilled into contextual experiential knowledge that is fed to a teacher model. The teacher updates the policy through context‑conditioned updates. Two policy families are compared: (i) policies that receive feedback from themselves and (ii) proprietary models serving as coaches. This setup contrasts with conventional rubric‑based RL where only a numeric reward is used.

## Results  
Experiments on two distinct policy families demonstrate that EL yields significantly higher task success rates than scalar‑reward RL across both held‑out and unseen open‑ended tasks. The method also shows better generalization to novel tasks and reduces instances of reward hacking, confirming the superiority of experiential knowledge over compressed rewards.

## Significance  
By offering a richer, more generalizable learning signal, EL addresses a fundamental limitation of scalar‑reward RL: loss of fine‑grained feedback. This contributes to safer, more reliable training for non‑verifiable tasks where precise quality assessment is crucial and where reward hacking can be detrimental.

## Related Concepts  
Reinforcement Learning, LLM‑as‑a‑Judge, Experiential Learning, on‑policy context distillation, scalar reward, rubric‑based RL, teacher model, fine‑grained preferences, reward hacking.
