# Summary: 2026-08-07_04-06-50Z_Multi_PerspectiveTriadInteractionGraphNeuralNetwor.md
Saved: 2026-08-09 22:40
Source: 2026-08-07_04-06-50Z_Multi_PerspectiveTriadInteractionGraphNeuralNetwor.md
Model: None

---

## Summary  
This paper proposes MTI‑GNN, a Multi‑Perspective Triad Interaction Graph Neural Network that detects cognitive distortions by modeling Beck’s triad of negative self, world, and future perspectives as complementary components. By leveraging an LLM to decompose utterances into these three perspectives, the model constructs perspective‑specific similarity graphs encoded via a GNN. A novel Triad Interaction module captures cross‑perspective dependencies through source‑conditioned updates and gating, while Prototype‑Guided Perspective Fusion aggregates labels in a label‑expanded manner. The approach is trained on multi‑lingual datasets with extensive distortion annotations.

## Key Contributions  
- [Finding 1] Incorporates three complementary perspectives (self, world, future) into a graph neural network framework to capture their interdependencies.  
- [Finding 2] Introduces a Triad Interaction module that models cross‑perspective dependencies via source‑conditioned updates and feature‑wise gating.  
- [Finding 3] Implements Prototype‑Guided Perspective Fusion with label‑expanded supervision, enabling effective aggregation across all available distortion annotations.

## Methodology  
The authors first use a large language model to parse each user utterance into three perspective vectors representing self, world, and future. These vectors are used to build similarity graphs where nodes represent utterances and edges encode pairwise similarity within each perspective. A Multi‑Perspective GNN processes these graphs, producing perspective‑specific embeddings. The Triad Interaction module then applies sequential source‑conditioned updates and gating mechanisms to fuse information across perspectives while preserving their distinct dynamics. Finally, Prototype‑Guided Perspective Fusion aggregates the fused embeddings using label‑expanded prototypes that incorporate all distortion categories present in the training set.

## Results  
On a test set of 9,764 samples from Korean, English, and Chinese sources covering ten distortion categories, MTI‑GNN achieved state‑of‑the‑art performance, surpassing all supervised variants and outperforming eight zero‑shot/few‑shot generative models. Leave‑one‑perspective‑out analyses confirmed that each perspective contributes meaningfully to detection accuracy.

## Significance  
By explicitly modeling the psychological triad structure rather than treating distortions as isolated labels, MTI‑GNN offers a more interpretable and robust framework for computational mental health applications, potentially improving diagnostic accuracy across languages and cultural contexts.

## Related Concepts  
Beck’s cognitive triad, graph neural networks (GNN), multi‑perspective decomposition, prototype‑guided fusion, label‑expanded supervision, cross‑perspective gating, similarity graphs, zero‑shot/few‑shot generation.
