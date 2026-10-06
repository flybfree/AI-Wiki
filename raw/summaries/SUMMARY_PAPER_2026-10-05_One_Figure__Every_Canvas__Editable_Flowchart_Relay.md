---
title: One Figure, Every Canvas: Editable Flowchart Relayout via Agentic Pipeline
url: http://arxiv.org/abs/2610.06852v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_17-59-54Z_OneFigure_EveryCanvas_EditableFlowchartRelayoutvia.md
generated_at: 2026-10-05 22:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces an agentic pipeline for aspect-ratio-adaptive flowchart relayout, enabling a single pipeline figure from a machine learning paper to be faithfully restructured across diverse canvas formats such as paper columns, 16:9 slides, portrait posters, 1:1 social teasers, and 9:16 phone previews. The proposed system, factored into Parse, Style, and Layout stages each guarded by a critic agent, achieves 68.6% Content Fidelity on a curated benchmark of 100 flowcharts across five aspect ratios, substantially outperforming prior methods that range from 11.2% to 41.4%.

## Key Takeaways
- The authors formalize aspect-ratio-adaptive flowchart relayout as a distinct task, emphasizing that any silently broken connection in a repurposed flowchart misrepresents the underlying computational method, and they explicitly design their pipeline so that connectivity is checked and prevented from being broken at every stage.
- The agentic pipeline is structured into three stages—Parse, Style, and Layout—where each stage pairs a main agent with a critic that combines deterministic constraint checks with VLM visual feedback, ensuring structural faithfulness and hallucination-free output rather than relying on a single monolithic generation step.
- Outputs are produced as draw.io-editable mxGraph XML, making the relaid-out flowcharts directly editable by researchers, and the evaluation uses Gemini 3.1 Pro validated against human judgments on a benchmark of 100 flowcharts at five aspect ratios, yielding 68.6% Content Fidelity compared to 11.2–41.4% for image-to-image stretching models, text-to-image agentic systems, and parse-then-render systems.

## Context
This work sits at the intersection of document layout automation, agentic AI pipelines, and visual reasoning, addressing a persistent practical pain point in the ML research community where authors must manually reformat figures for conferences, slides, posters, and social media. Prior approaches—image-to-image models that stretch blocks, text-to-image agentic systems that hallucinate content, and parse-then-render systems that mis-route edges—each fail in characteristic ways, leaving no reliable automated solution. By decomposing the problem into verifiable stages with explicit connectivity checking, the paper advances the broader trend of using multi-agent critic architectures to enforce structural correctness in generative AI tasks.

## Implications
For academic researchers and industry practitioners who routinely repurpose pipeline diagrams across publication venues, presentation formats, and social media channels, this pipeline offers a practical tool that preserves methodological accuracy while producing directly editable outputs, reducing manual redrawing effort and the risk of misrepresenting a method through a broken edge. More broadly, the staged agent-with-critic design demonstrates a transferable pattern for any task where structural fidelity must be guaranteed against hallucination, suggesting that explicit constraint-checking loops paired with VLM feedback can serve as a general recipe for trustworthy layout generation in document AI, diagram editing, and automated publishing workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06852v1)
