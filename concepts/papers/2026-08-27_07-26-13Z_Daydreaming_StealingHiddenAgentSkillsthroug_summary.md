# Summary: 2026-08-27_07-26-13Z_Daydreaming_StealingHiddenAgentSkillsthroughBlack_.md
Saved: 2026-08-28 06:19
Source: 2026-08-27_07-26-13Z_Daydreaming_StealingHiddenAgentSkillsthroughBlack_.md
Model: qwen3.8-flash-next-iq3_xxs

---

## Summary
This paper introduces "Daydreaming," a novel execution-only attack designed to extract hidden agent skills from hosted AI providers through black-box task interactions. The authors address a critical security gap where existing disclosure defenses fail to prevent customers from reconstructing valuable proprietary skills by submitting ordinary tasks the service is built to complete. By adaptively creating crafted tasks that distinguish possible hidden behaviors, Daydreaming successfully recovers the functional capabilities of multi-file skills without direct access to the underlying instructions or code. The study demonstrates that hiding skill files and filtering direct text disclosure are insufficient to prevent functional reconstruction, highlighting a significant vulnerability in current agent service architectures.

## Key Contributions
- **Introduction of the Daydreaming Attack:** The authors propose a new attack vector that steals multi-file agent skills purely through execution-based interactions, bypassing traditional disclosure filters that block requests for skill text or direct reproduction.
- **Formalization of Threat Levels:** The paper defines three nested threat levels of access—Differential, Trace, and Output—to rigorously categorize the information available to an attacker, focusing on the "Output" level where only final responses and returned files are visible.
- **High-Fidelity Skill Reconstruction:** Daydreaming achieves a capability recovery rate of 86.8% across multiple skills and victim models, outperforming the previous state-of-the-art method, SigLeak, by nearly four times, while using a median of only 32 victim calls per skill.

## Methodology
The authors approach the problem by treating agent skills as bundles of instructions, reference data, and executable helpers that are kept secret by hosted providers. Daydreaming operates as an execution-only attack where the victim agent is never asked to reveal the skill or grade a reconstruction. Instead, the attacker adaptively generates crafted tasks whose outputs serve as probes to distinguish between possible hidden behaviors. The method employs attacker-controlled "shadow agents" to select optimal task designs that maximize information gain. Once behavioral patterns are identified, the system completes each file component of the skill using stored victim results and local execution checks to verify correctness. This process is evaluated under the strictest "Output" threat model, ensuring that the reconstruction relies solely on the final responses and returned files provided by the black-box service.

## Results
The experimental evaluation was conducted across seven distinct agent skills and four different victim models. Daydreaming successfully recovered 86.8% of the original skill's capability under the Output threat level. This performance significantly outperforms SigLeak, a prior disclosure defense method, by almost four times. Notably, the attack achieves this high reconstruction fidelity with a median of only 32 victim calls per skill, even when disclosure defenses are actively enabled. These results demonstrate that functional reconstruction is highly efficient and effective, requiring minimal interaction with the target service to extract valuable proprietary knowledge.

## Significance
This research is significant because it challenges the assumption that hiding skill files and filtering direct disclosure requests are sufficient security measures for hosted agent services. By demonstrating that functional reconstruction is possible through normal task usage, the paper highlights a fundamental vulnerability in the business model of selling access to specialized agent capabilities. It suggests that providers must consider stronger protection mechanisms beyond simple text filtering, as the functional essence of a skill can be "stolen" through cleverly designed black-box interactions. This has implications for intellectual property protection in AI services and the design of future agent architectures.

## Related Concepts
- **Agent Skills:** Bundles of instructions, reference data, and executable helpers enabling specialized tasks.
- **Black-Box Task Interaction:** Interacting with a system without access to its internal code or instructions.
- **Execution-Only Attack:** An attack strategy that infers internal logic solely from the outputs of executed tasks.
- **Differential, Trace, and Output Threat Levels:** A formalized hierarchy of attacker access to information.
- **Shadow Agents:** Auxiliary agents used by the attacker to optimize task design for information extraction.
- **Functional Reconstruction:** Recreating the capability of a system without access to its source code or original prompts.

## Original research paper

[Canonical original paper: http://arxiv.org/abs/2608.26733v1](http://arxiv.org/abs/2608.26733v1)
