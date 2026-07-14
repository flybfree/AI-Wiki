---
title: "Summary: Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines"
url: http://arxiv.org/abs/2606.25838v1
type: paper-summary
date: 2026-06-24
source_paper: 2026-06-24_13-51-42Z_EdgesBeforeEmbeddings_AConfidence_AwareBlurGatefor.md
generated_at: 2026-06-24 21:00
model: nvidia/nemotron-3-nano-4b
---
# Summary: 2026-06-24 Edges Before Embeddings  A Confidence-Aware Blur G

## Summary
The paper introduces MagikaDocumentFromPixel, a lightweight CPU‑friendly image quality gate that classifies images as sharp, blurred, or uncertain in about 7 ms on a single core. By adding an Edge Prior Module (EPM) to MobileNetV3‑Large and training it at 384×384 resolution, the system achieves F1 = 0.9803 with a 17 MB ONNX artifact, improving over a fixed‑scale baseline by +1.3 points.

## Key Takeaways
- The recipe selected from an 46‑configuration, 8‑sweep empirical search isolates input resolution as the dominant lever and shows architecture capacity only pays off at ≥ 384 px.
- A confidence‑aware routing formalism grounded in classical selective prediction guides the gate’s decision making.
- The Edge Prior Module provides a Laplacian‑magnitude auxiliary channel that gives the network direct access to spectral evidence, lifting test F1 by +1.3 points.

## Context
Vision‑language pipelines suffer from silent degradation when input images are blurry, causing unnecessary compute on OCR and VLM tasks. This work addresses that inefficiency with a fast, CPU‑based quality gate that can be integrated directly into existing models without major architectural changes.

## Implications
For practitioners, the gate reduces latency and resource usage while preserving downstream performance, offering a practical solution for edge deployment. The recurring design pattern observed across Magika content‑type detection, risk‑controlled OCR with VLMs, and DocVLM suggests that confidence‑aware blur gating is a valuable component in robust vision pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.25838v1)
