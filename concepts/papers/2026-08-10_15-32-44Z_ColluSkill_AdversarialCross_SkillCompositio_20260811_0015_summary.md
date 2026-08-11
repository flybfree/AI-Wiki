# Summary: 2026-08-10_15-32-44Z_ColluSkill_AdversarialCross_SkillCompositionforEva.md
Saved: 2026-08-11 00:15
Source: 2026-08-10_15-32-44Z_ColluSkill_AdversarialCross_SkillCompositionforEva.md
Model: None

---

## Summary  
The paper identifies a blind spot in current skill scanners that only inspect individual skills, thereby overlooking risks that arise when multiple locally plausible skills are composed into a harmful workflow. To address this gap, the authors propose ColluSkill, an adversarial framework that deploys several innocuous sub‑skills through LLM‑driven chain planning and scanner feedback refinement to create a coordinated attack. They also introduce ChainGuard, a context‑aware scanner that reconstructs cross‑skill dependencies at the workflow level. The study demonstrates that these approaches can both evade existing defenses with high success rates and improve detection of malicious intent.

## Key Contributions  
- [Finding 1] Current skill scanners focus on individual skills, leaving cross‑skill composition vulnerabilities unexamined.  
- [Finding 2] ColluSkill constructs a multi‑skill chain using artifact passing and execution handoffs to evade single‑skill checks.  
- [Finding 3] ChainGuard reconstructs cross‑skill dependencies to identify workflow‑level threats.

## Methodology  
The authors first conducted an empirical survey of existing skill scanners, observing that each only evaluates a single skill in isolation. This limitation inspired the design of ColluSkill as a collusive multi‑skill‑chain attack that leverages LLM chain planning and feeds scanner feedback back into the process to preserve chain semantics while minimizing suspicious signals. For ChainGuard, they built a pipeline where the scanner’s output is used to model how installed skills interact, thereby reconstructing dependencies between sub‑skills.

## Results  
Experiments on six representative skill scanners show that ColluSkill achieves an average attack success rate of 96.0 %, outperforming both single‑skill and multi‑skill baselines. Meanwhile, ChainGuard reduces the attack success rate to 22.5% while allowing 99.5 % of benign workflows to pass, confirming its effectiveness in detecting chain‑level risks.

## Significance  
This work underscores the necessity of chain‑level security analysis for LLM‑based agent ecosystems, where malicious intent emerges from the composition rather than any single component. It advances both offensive methodology and defensive scanning techniques, providing a template for future research on collaborative attacks and robust skill‑ecosystem protection.

## Related Concepts  
- Skill scanners  
- Adversarial attacks  
- LLM chain planning  
- Artifact passing  
- Execution handoffs  
- Cross‑skill dependencies  
- Chain‑level security
