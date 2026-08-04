---
title: Salami Attack: Stealthy Collusive Memory Poisoning against OpenClaw
url: http://arxiv.org/abs/2608.01637v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_03-17-26Z_SalamiAttack_StealthyCollusiveMemoryPoisoningagain.md
generated_at: 2026-08-03 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MemCollusion, a framework that creates collusive memory poisoning attacks by slicing adversarial objectives into small benign fragments. It demonstrates that multiple innocuous memories can together steer an LLM agent like OpenClaw toward unsafe behavior across sessions. Experiments show high success rates under strong memory‑saving conditions.

## Key Takeaways
- MemCollusion uses salami tactics to generate individually harmless yet collectively harmful memory fragments.
- The framework constructs memory coalitions through four design constraints and five theory‑informed strategies, leveraging a fine‑tuned generator.
- Evaluation on OpenClaw with two backbones across 48 scenarios yields an average Memory Save Rate of 81.3% and an Attack Success Rate of 75.0%, showing effectiveness even under benign dilution and memory defenses.

## Context
Long‑term memory in large language models offers benefits but also introduces vulnerabilities to adversarial manipulation, a concern highlighted by this work on collusive poisoning. The study adds to the growing body of research on persistent memory attacks beyond single record poisoning.

## Implications
For practitioners, MemCollusion underscores the need for robust defenses against compositional attacks that exploit multiple benign inputs. It calls for systematic testing of memory‑based models in realistic cross‑session scenarios to anticipate and mitigate such threats.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01637v1)
