---
title: Pandora's Toolbox Or Why Agent Safety Cannot Be Verified
url: http://arxiv.org/abs/2611.25325v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-19_01-00-38Z_Pandora_sToolboxOrWhyAgentSafetyCannotBeVerified.md
generated_at: 2026-11-20 21:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper by Franco and Gershenson demonstrates that the safety of present AI agents—constructed by coupling a fixed language model with a general computing device—is fundamentally undecidable. The authors prove that no algorithm can determine whether an agent will execute a dangerous program that is semantically equivalent to a known hazardous one, rendering common safety mechanisms like guardrails, blacklists, and certifications inherently incomplete. Even under finite constraints, the safety verification problem remains computationally intractable, classified as PSPACE-complete.

## Key Takeaways
- Safety undecidability arises from the coupling of a language model with a general-purpose computing device: given any dangerous program, no algorithm can predict whether an agent will execute a semantically equivalent program. This is a formal impossibility result, not merely a practical limitation, meaning that complete safety verification for such agents is theoretically impossible regardless of how sophisticated the checking algorithm becomes.
- Under finite constraints such as bounded context, bounded values, and bounded running time, safety becomes decidable but remains PSPACE-complete even when the full description of the agent is known. This means that while a theoretical solution exists in constrained settings, the computational cost grows so steeply that practical verification becomes infeasible for realistic agent configurations.
- Safety is not a compositional property: agents that are individually proven safe can still collectively produce unsafe behavior when grouped together. This undermines the common engineering assumption that verifying each component independently guarantees the safety of the whole system, which is a critical concern for multi-agent architectures.

## Context
As AI agents increasingly integrate language models with tool-use capabilities, code execution environments, and multi-agent orchestration, the field has relied heavily on heuristic safety measures such as guardrails, content filters, and certification frameworks. This paper situates those practices within formal computability and complexity theory, revealing that the very architecture of modern agents—LLM plus general computing—introduces undecidability at a foundational level. It connects to broader discussions in AI safety about the limits of formal verification, the halting problem analogies in agent behavior prediction, and the growing complexity of multi-agent systems deployed in production environments.

## Implications
For practitioners and industry leaders, this work suggests that no amount of additional guardrails, whitelists, or certification processes can guarantee complete safety for agents built on the current LLM-plus-computing-device paradigm; safety must instead be approached through relaxed, probabilistic, or risk-bounded notions rather than absolute guarantees. For the research community, the PSPACE-completeness result and the non-compositionality finding demand new verification frameworks that account for emergent behavior in multi-agent systems, shifting the focus from proving individual agent safety to managing collective risk. This has direct consequences for regulatory approaches, product design, and the deployment of autonomous agents in safety-critical domains such as healthcare, finance, and infrastructure management.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.25325v1)
