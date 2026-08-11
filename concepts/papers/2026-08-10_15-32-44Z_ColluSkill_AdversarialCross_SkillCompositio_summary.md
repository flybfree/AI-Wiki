# Summary: 2026-08-10_15-32-44Z_ColluSkill_AdversarialCross_SkillCompositionforEva.md
Saved: 2026-08-10 23:53
Source: 2026-08-10_15-32-44Z_ColluSkill_AdversarialCross_SkillCompositionforEva.md
Model: None

---

## Summary  
Current skill‑scanner defenses in LLM‑based agent systems focus on evaluating each skill in isolation, which leaves a blind spot for attacks that exploit the composition of multiple locally safe skills into a harmful workflow. This paper introduces ColluSkill, an adversarial cross‑skill composition framework, and ChainGuard, a context‑aware scanner designed to detect such chain‑level threats. By decomposing malicious intent into interdependent sub‑payloads and using LLM‑driven chain planning with feedback refinement, the authors demonstrate that existing single‑skill or multi‑skill defenses are ineffective against coordinated attacks. The study empirically validates these claims on a suite of real‑world skill scanners.

## Key Contributions  
- [Finding 1] Existing skill scanners only inspect individual skills, creating an unexamined vulnerability to cross‑skill composition attacks that become dangerous only when executed together.  
- [Finding 2] ColluSkill is proposed as a collusive multi‑skill‑chain attack framework that leverages LLM‑based chain planning and scanner‑feedback refinement to hide malicious intent in seemingly benign sub‑skills.  
- [Finding 3] ChainGuard is introduced, a context‑aware skill‑chain scanner that reconstructs cross‑skill dependencies, artifact flows, and downstream behaviors to identify risks that emerge at the workflow level.

## Methodology  
The authors first conducted an empirical audit of six representative skill scanners to understand their single‑skill inspection mechanisms. They then designed ColluSkill by decomposing a complete malicious intent into independent sub‑payloads that are embedded in distinct skills, using LLM chain planning to order these payloads and scanner feedback refinement to mask suspicious signals. The attack is evaluated against the same scanners, while ChainGuard is implemented as a tool that jointly analyzes candidate skills with the installed environment to reconstruct cross‑skill dependencies and artifact flows.

## Results  
Experiments show ColluSkill achieves an average attack success rate of 96.0 % and outperforms both single‑skill (≈30 %) and multi‑skill (≈78 %) baseline attacks. ChainGuard reduces the attack success rate to 22.5 % while allowing 99.5 % of benign workflows to pass, confirming its effectiveness in mitigating chain‑level threats without excessive false positives.

## Significance  
This work highlights a critical blind spot in current agent security: defenses that treat skills as isolated units miss the composite risk introduced by their interaction. By emphasizing chain‑level analysis, ColluSkill and ChainGuard provide a more holistic approach to securing LLM‑driven skill ecosystems, encouraging developers and security researchers to adopt context‑aware scanning techniques.

## Related Concepts  
skill scanners, cross‑skill composition, malicious intent decomposition, artifact passing, execution handoffs, LLM chain planning, scanner feedback refinement, context‑aware scanning, skill‑chain dependencies, benign workflow preservation.
