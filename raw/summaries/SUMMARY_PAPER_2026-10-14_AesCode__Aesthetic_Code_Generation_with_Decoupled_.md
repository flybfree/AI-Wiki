---
title: AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards
url: http://arxiv.org/abs/2610.18860v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_17-59-31Z_AesCode_AestheticCodeGenerationwithDecoupledCross_.md
generated_at: 2026-10-14 02:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AesCode is a framework for generating information-rich visual artifacts (slides, posters, dashboards) as code by combining content-grounded code generation with aesthetic guidance derived from a reference image generated from the same prompt. The paper introduces a design graph representation that decomposes the target visual into attributable properties, enabling decoupled cross-modal rewards—deterministic verifiers for parsable properties and a VLM-based judge with a Visual Graph Rubric for non-parsable aesthetic qualities—optimized jointly through reinforcement learning. The resulting AesCode-8B and AesCode-32B models achieve visual quality scores comparable to closed-source frontier models like GPT-5.5 and Claude Opus 4.8, improving over same-scale Qwen3-VL baselines by 31.1 and 22.4 percentage points respectively.

## Key Takeaways
- AesCode addresses a fundamental gap in code-based visual generation: code models lack visual feedback about how layout and color choices manifest on a canvas, while image generators cannot reliably reproduce requested content. By using a reference image as aesthetic guidance while grounding code generation in the content prompt, AesCode bridges this gap without sacrificing verifiable correctness.
- The design graph representation is central to the method: it describes the entire canvas and makes each visual property attributable, enabling the derivation of complementary cross-modal rewards. Deterministic verifiers score properties that can be parsed from code and rendering output, while a VLM judge evaluates non-parsable aesthetic properties using a sample-specific Visual Graph Rubric (VGR) tied to graph elements and relations. Per-channel normalization during reinforcement learning ensures these decoupled rewards jointly improve spatial planning, aesthetic quality, and verifiable correctness without one dominating the other.
- The authors construct a dedicated benchmark that scores verifiable correctness and visual quality separately, with visual scores validated as highly consistent with human judgments. Ablation studies confirm that AesCode benefits from reference images both as model input and as a source of visual rewards, and the 8B and 32B variants reach performance comparable to closed-source frontier models, demonstrating that open-weight models can match proprietary systems when trained with properly structured cross-modal reward signals.

## Context
This work sits at the intersection of code generation, visual design, and reinforcement learning with verifiable rewards, a rapidly growing area where models are trained to produce outputs that can be programmatically checked. Prior approaches either generate code without visual feedback or generate images without structured, editable outputs, leaving a gap for applications requiring both aesthetic quality and content fidelity. AesCode's use of a design graph to decompose visual targets into attributable properties represents a novel structuring mechanism that makes reinforcement learning signals more targeted and interpretable than monolithic reward models.

## Implications
For practitioners building tools that produce editable, verifiable visual artifacts—such as automated slide generators, dashboard builders, or poster design assistants—AesCode demonstrates that open-weight models can achieve frontier-level visual quality when trained with properly decoupled reward signals, reducing dependence on proprietary APIs. The design graph and Visual Graph Rubric framework also offer a reusable template for evaluating and improving any code-generating system that must satisfy both structural correctness and aesthetic criteria, potentially guiding future work in reinforcement learning for multimodal generation tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18860v1)
