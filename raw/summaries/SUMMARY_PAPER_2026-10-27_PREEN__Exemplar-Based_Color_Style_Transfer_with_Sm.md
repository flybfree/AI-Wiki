---
title: PREEN: Exemplar-Based Color Style Transfer with Smartphone Editor Presets
url: http://arxiv.org/abs/2610.36896v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_09-30-35Z_PREEN_Exemplar_BasedColorStyleTransferwithSmartpho.md
generated_at: 2026-10-27 22:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
PREEN (Preset Regression via an Exemplar-based Editor Network) reframes color style transfer as a regression problem that predicts a compact vector of 29 editor slider parameters rather than generating a raster image. By using a style-transfer teacher to create pseudo-presets and training a CLIP-conditioned regressor refined with LoRA under a CIELAB loss, PREEN achieves state-of-the-art pixel- and perceptual-fidelity on the PST50 benchmark while running at sub-second on-device latency. The method also introduces a single inference-time strength knob that traces a continuous default-to-vivid trajectory, allowing users to trade off reference fidelity against standalone photo quality without retraining.

## Key Takeaways
- PREEN casts color style transfer as regression onto the 29 parameters of a deterministic smartphone image editor, producing an interpretable, editor-consumable preset vector instead of a raster output. This makes the result directly usable in existing editing pipelines and human-editable, a significant departure from typical neural style-transfer approaches that output opaque pixel arrays.
- Supervision is solved by training a style-transfer teacher whose outputs are inverted back into the editor's parameter space to create pseudo-presets, which then pretrain a CLIP-conditioned regressor. This regressor is further refined with LoRA fine-tuning under an image-level CIELAB loss, bridging the gap between arbitrary real-world style references and the structured parameter space of a concrete editor.
- The low-dimensional parameter subspace enables a single inference-time strength knob that produces a continuous default-to-vivid trajectory in one forward pass, with every intermediate state remaining a valid editor preset. A two-axis human study confirms that raters prefer the vivid end for matching a reference style but the default end as a standalone photograph, demonstrating that the knob spans this trade-off without any retraining.

## Context
Color style transfer has traditionally relied on generative models that output raster images, making results opaque, difficult to edit further, and computationally expensive to run on mobile devices. PREEN sits at the intersection of parameter-efficient fine-tuning (LoRA), contrastive vision-language conditioning (CLIP), and practical consumer photography tooling, demonstrating that structured regression into a known editor's parameter space can outperform generative baselines on fidelity metrics. The work also highlights the broader challenge of supervision in style transfer, where no ground-truth preset exists for arbitrary reference images, and proposes a teacher-inversion pipeline as a generalizable solution.

## Implications
For mobile photography and consumer editing applications, PREEN's sub-second on-device latency and compact 29-parameter output make it directly deployable in smartphone editors without cloud inference, lowering the barrier for high-quality style transfer at scale. For the research community, the pseudo-preset supervision strategy and the continuous strength-knob mechanism offer a template for building interpretable, controllable style-transfer systems that respect existing editing workflows. Practitioners in photo-editing software can integrate such preset-based pipelines to give users transparent, tunable control over style intensity rather than a binary apply-or-discard decision.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36896v1)
