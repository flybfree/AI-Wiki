---
title: Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models
url: http://arxiv.org/abs/2611.11571v1
type: paper-summary
date: 2026-11-11
source_paper: 2026-11-08_19-33-25Z_TreatingtheModelasanUntrustedComponent_Determinist.md
generated_at: 2026-11-11 21:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper argues that prompt injection in tool-using LLM agents is a structural problem rather than a prompt-wording problem, and proposes treating the model itself as an untrusted component. The authors compare in-prompt defenses (hardened prompts, spotlighting, LLM detectors) against deterministic enforcement mechanisms placed outside the model—specifically four reference monitors of increasing strength, human approval gates, and taint tracking—evaluated through an effect-based oracle in an executable environment of 13 tasks and 12 tools. Real-model evaluation on Qwen2.5-1.5B and Qwen2.5-7B shows that deterministic task-bound monitors dramatically reduce admitted attack actions (1.3%–7.7%) compared to the models' raw obedience rates (64%–84%), while simulation results indicate that no guardrail stack survives a persistent adaptive attacker, but the task-bound monitor holds severe actions at zero.

## Key Takeaways
- Deterministic enforcement outside the model vastly outperforms in-prompt guardrails: behind the task-bound monitor, Qwen2.5-1.5B and Qwen2.5-7B proposed the attacker's call in 64% and 84% of attack episodes, yet the monitor admitted only 1.3% and 7.7% respectively, demonstrating that structural enforcement is far more reliable than prompt-based defenses whose effectiveness varies unpredictably with model size.
- A persistent adaptive attacker or a compromised model drives every in-prompt guardrail stack to 100% attack success under an assumed erosion law, whereas the task-bound monitor maintains severe actions at 0.0%; taint-triggered human review further reduces residual harm by 62%, but a human approval layer without a deterministic monitor fails against approval spamming unless each episode enforces a deterministic approval budget.
- Implementation quality of the monitor is critical: a naive monitor admits 18 of 33 effective attack variants, a hardened one admits 6, and a capability-bound one admits only 1, showing that the engineering rigor of the enforcement layer directly determines security outcomes.

## Context
Prompt injection has become one of the most widely acknowledged security vulnerabilities in agentic AI systems, yet most published defenses remain in-prompt mitigations that depend on model compliance. This paper shifts the framing from "how do we instruct the model to resist?" to "how do we enforce policy regardless of what the model outputs?"—a systems-security perspective more aligned with traditional information-flow control and mandatory access control in operating systems. The work is situated within the growing body of research on agent safety, tool-use security, and the recognition that LLMs cannot be trusted as security boundaries, making it relevant to the broader effort to build provably safe autonomous agents.

## Implications
For practitioners deploying tool-using agents in production, the findings suggest that safety architecture must place enforcement outside the model: deterministic monitors, capability-bound policies, and taint tracking should be treated as mandatory infrastructure rather than optional guardrails. The dependence of guardrail effectiveness on model size and the failure of human approval without deterministic budgets warn against over-relying on any single defense layer. For the research community, the paper provides a reproducible evaluation harness with an effect-based oracle, argument-fuzzing attackers, and severity-weighted harm metrics that can serve as a benchmark for future agent-security work, while its explicit acknowledgment of limitations—two open-weights models, static attacks, simulation-only human/taint results—sets a standard for honest evaluation reporting.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.11571v1)
