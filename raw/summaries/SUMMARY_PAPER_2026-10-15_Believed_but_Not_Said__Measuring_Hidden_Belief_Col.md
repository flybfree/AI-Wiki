---
title: Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions
url: http://arxiv.org/abs/2610.22138v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_16-12-07Z_BelievedbutNotSaid_MeasuringHiddenBeliefCollapsein.md
generated_at: 2026-10-15 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether multi-agent LLM discussion systems can reliably correct individual errors through peer critique, testing this assumption against adversarial agents that repeatedly assert plausible false answers. The authors find that belief collapse is far more severe than public agreement suggests: private belief adoption of false answers (51.6%) substantially exceeds public endorsement (19.7%), meaning much of the adversarial influence remains invisible within the discussion transcript itself.

## Key Takeaways
- Adversarial agents dramatically shift group outcomes in factual discussions: without any attacker, only 0.6% of benign agents adopt a false answer across six models and three factual-QA datasets, but a single adversarial agent raises this to 44.8%, and three adversarial agents push it to 60.5%, demonstrating that multi-agent consensus mechanisms are highly fragile against even minimal adversarial pressure.
- The paper reveals a critical inversion of classical conformity findings: while traditional social psychology studies report public agreement without private belief change, this work shows the opposite pattern. Benign agents privately hold the false answer in 51.6% of exposed turns while publicly endorsing it in only 19.7%, meaning the true extent of belief corruption is hidden from any observer reading only the public discussion log.
- Robustness against adversarial influence is not predicted by an agent's baseline factual knowledge. Agents that retain the correct answer often fail to actively defend it, and once a false answer is adopted by any benign agent, it spreads further among peers, indicating that the failure mode is not a knowledge gap but a failure of argumentative defense and social resistance.

## Context
Multi-agent LLM systems—where agents debate, critique, and cross-check one another—are increasingly deployed in research pipelines, automated fact-checking, and collaborative reasoning frameworks, with the implicit assumption that peer scrutiny will surface and correct individual hallucinations or errors. This paper directly challenges that assumption by introducing a controlled adversarial setup and measuring both public and private belief states, revealing that the architecture of multi-agent discussion may amplify rather than mitigate misinformation when even a small number of agents consistently assert plausible falsehoods.

## Implications
For practitioners building multi-agent LLM pipelines, this work signals that monitoring only public disagreement or agreement in agent transcripts is insufficient to detect belief corruption; hidden private belief shifts can silently propagate and persist even after adversarial agents are removed. System designers should incorporate private-belief probing mechanisms, adversarial stress-testing during development, and explicit defense protocols for agents holding correct answers, since baseline knowledge alone does not confer robustness against social pressure within the agent group.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22138v1)
