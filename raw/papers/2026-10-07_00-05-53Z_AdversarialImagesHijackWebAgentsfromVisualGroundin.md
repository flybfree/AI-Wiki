---
title: Adversarial Images Hijack Web Agents from Visual Grounding to Browser Execution
published: 2026-10-07T00:05:53Z
authors: Wanjing Han, Levi Taiji Li, Mu Zhang, Yue Jiang, Guanhong Tao
url: http://arxiv.org/abs/2610.09240v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adversarial Images Hijack Web Agents from Visual Grounding to Browser Execution

## Abstract
Modern web agents built on large vision-language models process webpages, select relevant UI elements, and translate model outputs into browser actions. Existing visual red-teaming approaches use adversarial visual content to manipulate this process. However, they primarily target model inference and do not explicitly account for structured input processing or action post-processing. Consequently, model-level success does not establish control over browser execution and cannot reliably characterize end-to-end agent robustness. To address this gap, we formulate red teaming for vision-grounded web agents as an end-to-end grounding-to-execution problem, and introduce WebMirage, a framework that crafts localized visual perturbations that cause agents to select attacker-controlled content and execute the corresponding browser action across varying webpage renderings. It uses a role-slot abstraction and webpage recomposition to capture competition among webpage elements, and dataflow analysis to align optimization with action post-processing. We evaluate WebMirage across four agent configurations and six VLM backbones on 2,250 tasks covering 13 public websites and a sandbox benchmark. WebMirage achieves an average attack success rate of 91.9%, compared with 17.4% for the strongest baseline, and remains effective against three agent-level defenses.

## Metadata
- **Published**: 2026-10-07T00:05:53Z
- **Authors**: Wanjing Han, Levi Taiji Li, Mu Zhang, Yue Jiang, Guanhong Tao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09240v1)