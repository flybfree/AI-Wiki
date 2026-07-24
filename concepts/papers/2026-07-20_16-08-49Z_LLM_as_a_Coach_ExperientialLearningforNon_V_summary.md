# Summary: 2026-07-20_16-08-49Z_LLM_as_a_Coach_ExperientialLearningforNon_Verifiab.md
Saved: 2026-07-24 00:22
Source: 2026-07-20_16-08-49Z_LLM_as_a_Coach_ExperientialLearningforNon_Verifiab.md
Model: None

---

## Summary  
The paper introduces Experiential Learning (EL), a method that replaces the limited scalar reward of reinforcement learning with richer feedback obtained from an LLM‑as‑a‑Coach, thereby preserving fine‑grained preferences and enabling transferable experiential knowledge. By converting each on‑policy response into detailed contextual distillation, EL conditions a teacher model whose internalized knowledge is then used to improve the policy. Experiments across two policy families show that EL consistently outperforms traditional rubric‑based RL on held‑out and unseen open‑ended tasks while generalizing beyond the training distribution and mitigating reward hacking.  

## Key Contributions  
- [Finding 1] Experiential Learning repurposes the LLM‑as‑a‑Judge model into a high‑bandwidth coach that distills per‑response feedback into transferable experiential knowledge, preserving fine‑grained response preferences that scalar rewards discard.  
- [Finding 2] The on‑policy context distillation mechanism internalizes the coach’s assessment as structured knowledge that conditions a teacher model and is directly incorporated into the policy update process.  
- [Finding 3] EL consistently outperforms scalar‑reward RL on both held‑out and unseen open‑ended tasks, demonstrates superior generalization, and reduces reward hacking compared to traditional reinforcement learning baselines.  

## Methodology  
The authors first take an existing LLM that serves as a judge for task responses and transform it into a coach that generates detailed feedback for each policy output. This feedback is then distilled into contextualized knowledge using on‑policy context distillation, where the teacher model extracts patterns from the coach’s assessment and updates its parameters. The updated teacher model conditions the policy’s next step generation, effectively turning the coach’s rich textual evaluation into an experiential learning signal. Experiments compare this EL framework against standard scalar‑reward reinforcement learning setups on two families of policies (one using the same LLM as reward function, another using a proprietary reward model).  

## Results  
Across all experiments, EL achieved higher task success rates and better performance metrics than scalar‑reward RL. The policy that receives coach‑derived feedback generalized to unseen tasks with greater accuracy and showed fewer instances of reward hacking. Statistical analysis confirmed the superiority of EL in both held‑out and unseen scenarios, supporting the claim that richer feedback yields more robust learning.  

## Significance  
This work establishes experiential knowledge as a superior learning signal for post‑training on non‑verifiable tasks, moving beyond the limitations of scalar rewards that compress rich textual evaluations into single numbers. By providing dense supervision and preserving nuanced preferences, EL offers a pathway to more reliable and adaptable AI agents in open‑ended environments.  

## Related Concepts  
Reinforcement learning, LLM‑as‑a‑Judge, scalar rewards, experiential knowledge, context distillation, teacher‑student model updating, reward hacking mitigation.
