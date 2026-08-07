# Summary: 2026-08-06_03-32-43Z_WhenExperienceBecomesInstruction_TrajectoryPoisoni.md
Saved: 2026-08-06 20:31
Source: 2026-08-06_03-32-43Z_WhenExperienceBecomesInstruction_TrajectoryPoisoni.md
Model: None

---

## Summary  
Self‑evolving skill (SES) systems translate agent trajectories into persistent skills, allowing untrusted experience to become trusted instruction. The paper introduces **PoisonedEvolution**, a trajectory‑poisoning attack that lets an attacker inject bounded evidence into the promotion pipeline without seeing private pools or evolution logic. Experiments on six mainstream LLM evolvers and the Trace2Skill pipeline show high success rates, indicating that malicious behavior can be embedded as instruction with only modest support.

## Key Contributions  
- **Attack framework**: PoisonedEvolution enables trajectory‑poisoning where an attacker contributes bounded evidence to influence skill evolution.  
- **Empirical performance**: At 10 % attacker support the attack embeds target behaviors in 546/600 trials (91 % SER) on SkillClaw and 369/600 (61.5 %) on Trace2Skill, demonstrating transfer across evolution architectures.  
- **Success determinants**: Ablations reveal that recurring support, causal framing, and domain‑aligned encoding are the primary factors driving attack success.

## Methodology  
The authors construct a skill‑visible black‑box attacker that can observe target skills and submit evidence to an SES pipeline. They evaluate four security‑effect families using inert canary specifications across six mainstream LLM evolvers (SkillClaw) and the Trace2Skill pipeline. The evaluation follows three stages—Inclusion, Evolution Attribution, and Realization—measuring how often the poisoned behavior is promoted as instruction.

## Results  
With 10 % attacker support, PoisonedEvolution achieves a success rate of 91 % on SkillClaw (546/600 trials) and 61.5 % on Trace2Skill (369/600 trials). In a controlled study, three consistent attacker records suffice to contaminate a batch of 30 records, while a single record is far weaker. Ablation studies confirm that frequency of support, causal framing, and domain alignment are the main contributors to success.

## Significance  
These findings expose evidence promotion as a critical security boundary for self‑evolving agents: seemingly benign experience can be weaponized to embed malicious instructions, undermining trust in skill distillation pipelines. The results highlight the vulnerability of SES systems to subtle poisoning attacks that persist across different evolution architectures.

## Related Concepts  
- Self‑evolving skill (SES) systems  
- Trajectory distillation into persistent skills  
- Skill bank / skill pool  
- Poisoning attacks on learning pipelines  
- Inclusion, Evolution Attribution, Realization steps  
- Evidence promotion  
- LLM evolvers
