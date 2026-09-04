---
title: FiMI Banking: A Sovereign Model for Indian Retail Banking
url: http://arxiv.org/abs/2609.03960v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_14-56-59Z_FiMIBanking_ASovereignModelforIndianRetailBanking.md
generated_at: 2026-09-03 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FiMI Banking, a controlled Indian retail‑banking environment designed to evaluate conversational agents that must answer product questions and handle account requests safely within regulatory limits. Using preference optimization and verifiable‑reward reinforcement learning, the study shows measurable improvements in safe refusal rates and task performance with fewer generated tokens.

## Key Takeaways
- Preference optimization raises out‑of‑scope refusals from 52% to 80%, demonstrating its effectiveness at preventing unsafe responses.  
- Reinforcement learning boosts edge‑case accuracy from 0.509 to 0.718 and order‑sensitive task performance from 0.590 to 0.679 while reducing token usage by 29%.  
- The two approaches address complementary needs: preference optimization ensures safety, reinforcement learning enhances efficiency.

## Context
This work addresses a key limitation of general‑purpose language models in regulated domains where accurate tool use and cautious behavior are essential. By grounding the model on vetted banking data and synthetic customer profiles, FiMI Banking provides a realistic testbed for evaluating conversational agents that interact with financial services.

## Implications
The findings suggest that combining preference optimization with verifiable‑reward reinforcement learning can yield safer, more efficient banking assistants. Practitioners may adopt this hybrid strategy to meet compliance requirements while optimizing resource usage in real‑world retail banking applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03960v1)
