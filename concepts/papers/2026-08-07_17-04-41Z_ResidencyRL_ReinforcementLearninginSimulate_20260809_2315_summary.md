# Summary: 2026-08-07_17-04-41Z_ResidencyRL_ReinforcementLearninginSimulatedClinic.md
Saved: 2026-08-09 23:15
Source: 2026-08-07_17-04-41Z_ResidencyRL_ReinforcementLearninginSimulatedClinic.md
Model: None

---

## Summary  
The paper proposes ResidencyRL, a reinforcement learning framework for training AI agents to perform multi‑turn clinical decision‑making within simulated residency encounters. It pairs an RL policy with LLM simulators that generate adversarial patient dialogues and tool calls, using a structured reward covering diagnostic accuracy, management quality, communication, documentation, and safety. The approach aims to learn sequential clinical reasoning beyond static knowledge bases. Evaluation shows improved performance on held‑out benchmarks.

## Key Contributions  
- ResidencyRL learns multi‑turn clinical decision sequences via RL in simulation.  
- Achieves a 7 % boost in diagnostic accuracy under adversarial conditions compared to baseline LLM models.  
- Demonstrates transferable improvements across six clinical axes of the AMIE benchmark and other multi‑visit assessments.

## Methodology  
The authors constructed a simulated residency environment where an AI agent interacts with patients through up to 60 dialogue turns and 8 tool calls per trajectory. An LLM simulator generates realistic, adversarial patient responses and medical records. The RL policy is trained using PPO on this structured reward function that evaluates each component of clinical reasoning.

## Results  
On held‑out evaluations, the ResidencyRL agent improves diagnostic accuracy from 81 % to 88 %, a 7 % relative gain, while reducing missed red‑flag rates by 31 %. Blinded expert clinicians preferred the trained agent in 87.6 % of side‑by‑side comparisons. The model outperforms the base model on all six clinical axes of AMIE and shows consistent directional improvements on AgentClinic and CRAFT‑MD.

## Significance  
This work demonstrates that sequential clinical decision‑making can be learned through multi‑turn RL, offering a path toward AI agents that mimic the progressive autonomy of residency training. The findings suggest that reinforcement learning can systematically address blind spots such as premature closure in medical reasoning.

## Related Concepts  
- Reinforcement Learning; Multi‑turn dialogue simulation; Large Language Models (LLMs); Structured reward design; Clinical decision making; Premature closure mitigation; AMIE benchmark; AgentClinic; CRAFT‑MD.
