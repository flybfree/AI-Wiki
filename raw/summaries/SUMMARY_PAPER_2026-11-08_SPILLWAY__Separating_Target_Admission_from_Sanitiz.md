---
title: SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection
url: http://arxiv.org/abs/2611.07222v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-04_23-18-10Z_SPILLWAY_SeparatingTargetAdmissionfromSanitization.md
generated_at: 2026-11-08 21:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SPILLWAY introduces a deterministic, model-free defense mechanism that protects tool-using AI agents from prompt injection attacks by separating the admission of an action's target from the sanitization of injected text. The core insight is that action targets (such as email recipients or payment accounts) arrive in typed fields from tool outputs, while injected instructions appear as free text, enabling a rule-based check that requires no language model in the decision loop. Across multiple backbones and task suites, SPILLWAY achieves a near-zero attack success rate while maintaining the highest utility scores among compared defenses, all without triggering additional model calls or per-task planning.

## Key Takeaways
- SPILLWAY exploits the structural distinction between typed fields in tool outputs (e.g., an email sender or payment account number) and free-text regions where injected instructions appear. The admission check permits a tool call only when each target value that appears in tool output but not in the user's original task was returned by a read-only tool in a typed field, or is covered by a fixed delegation rule. This creates a deterministic floor that does not depend on any language model evaluating the attacker's text.
- The system includes a deterministic sanitizer that removes instruction-like regions matched by fixed rules before the model reads them, while retaining the removed spans as auditable evidence. A local judge component can restore a refused call but is explicitly constrained so it can never restore a call whose target lies within the removed text, preventing the sanitizer from being bypassed.
- Empirically, SPILLWAY produces zero redirects under standard templated injections across three backbones and seven task suites, a raw zero under a forged chat template attack, and a mean in-scope attack success of only 0.007 under a released reinforcement-learning attacker. It achieves the highest observed mean utility and composite scores (NRP, ERS) among defenses evaluated under the same attack, with no defense-triggered backbone re-run and almost no added model call overhead.

## Context
Prompt injection remains one of the most persistent security threats for autonomous AI agents that interact with external tools such as email clients, file systems, and payment processors. Existing runtime defenses typically place a language model in the decision path, making the safety check itself vulnerable to the same adversarial text it is meant to filter, while provenance-based defenses still require a model to plan or route each task before the final check. SPILLWAY addresses this gap by shifting the safety boundary to a deterministic, type-aware admission gate that operates independently of any model inference, representing a significant departure from the prevailing paradigm of model-in-the-loop defenses.

## Implications
For practitioners deploying personal AI agents that act on users' email, files, and payments, SPILLWAY offers an auditable refusal floor on where actions are directed without sacrificing task utility or adding latency through extra model calls. The approach is backbone-agnostic and requires no per-task planning, making it practical for production agent frameworks that must remain responsive and cost-efficient. More broadly, the typed-field-versus-free-text distinction suggests a generalizable architectural principle for agent safety: structural metadata from tool interfaces can serve as a trustworthy, model-independent signal for constraining agent behavior against adversarial inputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.07222v1)
