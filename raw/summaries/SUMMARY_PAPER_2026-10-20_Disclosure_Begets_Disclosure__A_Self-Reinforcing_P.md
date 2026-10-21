---
title: Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory
url: http://arxiv.org/abs/2610.28315v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_14-52-57Z_DisclosureBegetsDisclosure_ASelf_ReinforcingPrivac.md
generated_at: 2026-10-20 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how persistent memory in LLM agents creates a self-reinforcing privacy loop: when an agent consults stored personal attributes during dialogue, its responses carry those values forward as presuppositions, which users then affirm or leave uncorrected, causing further attributes to accumulate in the record over successive sessions. Through multi-session simulations across four support models, the authors demonstrate that memory use raises response quality but also increases empirical leakage—the proportion of personal attributes correctly inferred from the accumulated conversation record—with the gap widening over time. The study identifies the agent's own presuppositions as the primary driver of this loop and shows that constraining the agent's output is far more effective at reducing leakage than filtering user inputs or anonymizing stored data.

## Key Takeaways
- Memory-conditioned responses introduce earlier attribute values as presuppositions into subsequent turns, and users either affirm these presuppositions or fail to correct them, effectively converting the agent's guesses into recorded facts. This creates a feedback loop where each session's memory retrieval seeds the next session's disclosures, amplifying leakage over time rather than remaining a one-time event.
- Users cannot independently break the loop: actively correcting a value still discloses the attribute, declining to discuss a topic shifts later predictions toward sensitive defaults, and leaving incorrect values unchallenged entrenches them in the record. The burden of mitigation therefore falls disproportionately on the agent's generation behavior rather than on user vigilance.
- The most effective intervention is instructing the agent not to state or presuppose stored attributes in its responses, which brings leakage down to approximately the no-memory baseline while preserving most of the quality improvements that memory provides. By contrast, filtering user utterances or anonymizing stored data sacrifices a substantial portion of the personalization benefits without comparably reducing leakage.

## Context
As LLM agents transition from stateless chatbots to persistent, personalized assistants deployed in healthcare, education, and customer support, the accumulation of personal attributes across sessions becomes a structural privacy concern rather than a hypothetical one. This paper addresses a gap in the literature by showing that privacy leakage is not merely a function of what users voluntarily disclose but is actively manufactured by the agent's own memory-conditioned generation, a mechanism that existing data-protection frameworks and consent models do not account for.

## Implications
For practitioners building memory-augmented agents, the findings argue for output-side guardrails—prompt-level instructions that prevent the agent from restating or presupposing stored personal attributes—as a more efficient privacy control than input filtering or data anonymization pipelines. For regulators and product designers, the self-reinforcing nature of the loop means that privacy audits must evaluate multi-session trajectories rather than single interactions, since leakage compounds in ways that single-turn assessments systematically underestimate.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28315v1)
