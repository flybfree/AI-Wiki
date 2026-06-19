---

title: "SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning"
url: http://arxiv.org/abs/2605.18209v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-18_10-54-55Z_SPATIOROUTE_DynamicPromptRoutingforZero_ShotSpatia.md
generated_at: "2026-06-11 10:42"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces SpatioRoute, a dynamic prompt generation method for zero-shot spatial question answering in egocentric video without fine-tuning or 3D inputs. It combines a rule‑based router and an LLM‑driven approach, achieving up to 5 % accuracy improvement over fixed prompts.

## Key Takeaways
- SpatioRoute provides two routing modes—rule‑based SpatioRoute‑R and LLM‑driven SpatioRoute‑L—that generate task‑specific prompts from the question alone, eliminating the need for 3D point clouds or model fine‑tuning.  
- The method yields a consistent accuracy boost of up to five percent across multiple vision‑language models on the SQA3D benchmark.  
- Chain‑of‑Thought prompting degrades performance on Qwen series models, showing that question‑aware routing outperforms uniform reasoning instructions.

## Context
Spatial visual question answering (VQA) is a core challenge in multimodal AI, where models must infer relationships among 3D objects and scene elements. This work advances the field by demonstrating that prompt engineering alone can match or exceed fine‑tuned training for zero‑shot tasks.

## Implications
For developers building video assistants, SpatioRoute offers a lightweight way to improve spatial reasoning without costly data collection or additional compute. It also highlights the importance of task‑specific prompting over generic instruction sets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.18209v1)
