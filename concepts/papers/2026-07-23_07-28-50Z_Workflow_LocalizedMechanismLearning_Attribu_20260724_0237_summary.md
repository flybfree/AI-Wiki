# Summary: 2026-07-23_07-28-50Z_Workflow_LocalizedMechanismLearning_Attribution_Gu.md
Saved: 2026-07-24 02:37
Source: 2026-07-23_07-28-50Z_Workflow_LocalizedMechanismLearning_Attribution_Gu.md
Model: None

---

## Summary  
The paper introduces **Workflow-Localized Mechanism Learning (WML)**, a method that enables frozen language‑model agents to reuse external procedural knowledge more effectively by locally pinpointing where a failure occurs, which mechanism caused it, and how third‑party skills should be patched. It proposes a six‑module Workflow‑Guided Skill Optimization (WGSO) loop that routes single‑mechanism defects to low‑level resources and relational defects across mechanisms to higher‑level composition protocols. The approach integrates attribution‑guided repair with skill optimization for structured agent workflows, aiming to minimize token usage while preserving successful tasks.

## Key Contributions  
- Finding 1: Node–Mechanism Attribution identifies the failed workflow node, implicated mechanisms, and smallest valid edit target.  
- Finding 2: Workflow‑Guided Skill Optimization (WGSO) loop selects provenance‑ and scope‑aware third‑party knowledge, applies bounded patches, evaluates candidates, and stores verified outcomes in optimizer memory.  
- Finding 3: WML achieves higher hard accuracy on SpreadsheetBench (90.33 ± 1.53 for DeepSeek, 74.67 ± 3.51 for Qwen3.6‑Flash) compared to baseline; it also improves WikiTableQuestions denotation accuracy.

## Methodology  
The authors approached the problem by modeling agent skill execution as a directed workflow of nodes and mechanisms. They built an attribution mechanism that analyzes failure traces to pinpoint which node and internal mechanism caused the error, then classified defects as single‑mechanism (L3) or relational (L2). The WGSO loop iterates: retrieve candidate third‑party skills matching provenance and scope; generate bounded patches; evaluate patched workflows using a validation set; commit successful patches to optimizer memory. This closed‑loop ensures localized, minimal edits.

## Results  
On SpreadsheetBench, WML yields 90.33 ± 1.53 hard accuracy for DeepSeek and 74.67 ± 3.51 for Qwen3.6‑Flash; without optimization the baseline transfer to WikiTableQuestions is 84.00 ± 2.00 denotation accuracy. On Compiler‑Supported50, WML attains the highest hard‑PASS rate and lowest cost per successful task, with compiled execution reducing tokens and calls relative to a direct SkillAgent while preserving most successful tasks.

## Significance  
This work bridges the gap between external skill artifacts and frozen language models by providing a systematic, locally informed repair strategy that maximizes knowledge reuse without retraining. By minimizing token usage and call overhead, WML offers a scalable path toward efficient, modular AI agents capable of long‑term skill evolution.

## Related Concepts  
- Workflow modeling  
- Mechanism attribution  
- Skill optimization loop  
- Provenance‑aware patching  
- L2/L3 routing  
- Structured agent skills
