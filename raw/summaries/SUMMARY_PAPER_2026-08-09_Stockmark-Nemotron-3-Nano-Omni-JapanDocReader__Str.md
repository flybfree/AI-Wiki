---
title: Stockmark-Nemotron-3-Nano-Omni-JapanDocReader: Structured Document Parsing via Capability Injection and Forgetting Control
url: http://arxiv.org/abs/2608.06758v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_03-24-59Z_Stockmark_Nemotron_3_Nano_Omni_JapanDocReader_Stru.md
generated_at: 2026-08-09 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Stockmark‑Nemotron‑3‑Nano‑Omni‑JapanDocReader, a Japanese document understanding model derived from the large reasoning multimodal model Nemotron‑3‑Nano‑Omni‑30B‑A3B. The authors focus on structured document parsing through capability injection and forgetting control, achieving strong parsing performance while minimizing loss of VQA abilities. Their experiments demonstrate that parsing‑centric fine‑tuning improves parsing but causes notable VQA forgetting.

## Key Takeaways
- Parsing‑centric SFT using only structured Japanese document data yields a large boost in parsing accuracy but leads to measurable degradation in the model’s original VQA capabilities.  
- Mixed SFT, which combines both parsing and VQA data, restores most of the VQA performance while retaining near‑optimal parsing results, showing that balanced training mitigates forgetting.  
- Applying DAPO‑based RL on top of the mixed SFT checkpoint further enhances structured parsing beyond what SFT alone can achieve, forming the basis for the released final model.

## Context
The work addresses a growing need in AI to maintain specialized capabilities within large multimodal models as they are fine‑tuned for new tasks. By separating and preserving distinct abilities through controlled training regimes, researchers aim to reduce catastrophic forgetting—a common challenge when updating models for domain‑specific tasks like Japanese document parsing.

## Implications
For industry practitioners developing multilingual document processing systems, this approach offers a practical framework to integrate language understanding with structured data extraction without sacrificing overall model utility. It also provides a template for future research on capability injection and forgetting control in large reasoning models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06758v1)
