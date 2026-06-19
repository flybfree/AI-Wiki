---

title: 'Phasor Memory Networks: Stable Backpropagation Through Time for Scalable Explicit Memory'
published: "2026-05-13T11:28:06Z"
authors: Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung
url: http://arxiv.org/abs/2605.13370v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Phasor Memory Networks: Stable Backpropagation Through Time for Scalable Explicit Memory



**Source**: [Original Paper](http://arxiv.org/abs/2605.13370v1)
## Abstract
For over a decade, explicit memory architectures like the Neural Turing Machine have remained theoretically appealing yet practically intractable for language modeling due to catastrophic gradient instability during Backpropagation Through Time. In this work, we break this stalemate with \textit{Phasor Memory Network} (PMNet), a novel architecture that structurally resolves memory volatility through \textit{Unitary Phasor Dynamics} and \textit{Hierarchical Learnable Anchors}. Rather than relying on brute-force scaling, we present a mechanistic proof-of-concept in a controlled byte-level setting. By constraining recurrent state updates to phase rotations on a complex unit circle, PMNet preserves gradient norms and inherently prevents divergence without the need for specialized initialization. We empirically demonstrate the active actuation of the memory module through a synthetic Copy-Paste task, where PMNet utilizes an expansive \textit{85-slot hierarchical memory tree} ($=\sum^{4}_{h=1}4^{h-1}$) to achieve near 100\% exact retrieval across temporal distances that completely exceed the local sliding window attention's receptive field. Furthermore, despite being a compact 119M parameter model trained on 18.8B tokens, PMNet matches the zero-shot long-context robustness of a Mamba model that is three times larger. Our ablation studies and gradient analyses confirm that the historical failure of explicit memory was a structural alignment problem, which PMNet effectively overcomes, providing a theoretically grounded foundation for scalable sequence modeling.

## Metadata
- **Published**: 2026-05-13T11:28:06Z
- **Authors**: Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.13370v1)