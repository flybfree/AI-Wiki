---
title: CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts
url: http://arxiv.org/abs/2611.17115v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-12_17-07-22Z_CapLite_Prompt_InjectionDefenseforSmallLanguageMod.md
generated_at: 2026-11-15 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether small language model (SLM) agents can be trusted to generate the security artifacts (programs, privilege policies, dependency graphs, constraint lists) that existing prompt-injection defenses like CaMeL, Progent, IPIGuard, and DRIFT depend upon. The authors demonstrate that across 15 open-weight models, 13 of which fall between 1.7B and 12B parameters, these models consistently fail to produce reliable security artifacts, leaving agents vulnerable to injection attacks. They then introduce CapLite, a defense that derives its policy directly from tool schemas rather than from model-written artifacts, achieving zero successful attacks across 13,935 AgentDojo episodes while using only 17.1k tokens per episode.

## Key Takeaways
- Existing enforcement defenses fundamentally assume the agent's own model can author sound security artifacts. The authors test 15 open-weight models and find that 13 of them (1.7B–12B parameters) produce policies, graphs, or constraints that admit attacks in 14, 13, and 11 models respectively for Progent, IPIGuard, and DRIFT, while CaMeL's generated programs fail to execute in up to 68% of episodes. This reveals a critical fragility in the assumption that small models can self-author security guarantees.
- CapLite sidesteps model-written artifacts entirely by deriving its policy from tool schemas, committing all write calls before any tool result is read, and admitting a write only when every argument determining the recipient, amount, object, or destination is explicitly stated in the user's original request. This design guarantees write integrity: injected text cannot introduce a new write, and no write can reach a target the user did not specify.
- In evaluation, CapLite achieves 29.0% utility under attack, comparable to CaMeL's 27.2%, while consuming 17.1k tokens per episode—roughly 18% of CaMeL's token budget and fewer tokens than every other enforcement defense or even the undefended agent. It attains the highest utility-per-token ratio among all enforcement defenses tested.

## Context
Prompt injection remains one of the most persistent security threats to LLM-based agents that interact with external tools and untrusted data. The prevailing defense strategy in 2025–2026 has been to have the agent's own model generate a security artifact that a separate code layer then enforces. This paper challenges that paradigm by showing it breaks down for the small, locally deployable models that dominate edge and cost-sensitive deployments. By proving that SLMs cannot reliably author their own security constraints, the authors expose a gap between the theoretical soundness of enforcement defenses and their practical viability for the models most organizations actually run.

## Implications
For practitioners deploying agents on constrained hardware or in privacy-sensitive environments where small models are the only option, CapLite offers a defense that does not depend on the model's ability to reason about its own security, making it robust precisely where existing defenses fail. The dramatically lower token cost—18% of CaMeL's—also makes enforcement-based prompt-injection defense economically feasible at scale, potentially shifting industry practice away from large-model-only security architectures. More broadly, the finding that model-written security artifacts are unreliable for SLMs suggests that future agent-security research should prioritize schema-derived, structural guarantees over model-generated policies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.17115v1)
