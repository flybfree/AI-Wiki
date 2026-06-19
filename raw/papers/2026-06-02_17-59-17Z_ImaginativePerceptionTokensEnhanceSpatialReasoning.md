---

title: Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models
published: "2026-06-02T17:59:17Z"
authors: Mahtab Bigverdi, Lindsey Li, Weikai Huang, Yiming Liu, Jaemin Cho, Jieyu Zhang, Tuhin Kundu, Chris Dangjoo Kim, Zelun Luo, Linda Shapiro, Ranjay Krishna
url: http://arxiv.org/abs/2606.03988v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models



**Source**: [Original Paper](http://arxiv.org/abs/2606.03988v1)
## Abstract
Vision language models (VLMs) excel at many tasks but still struggle with spatial reasoning when critical information is not directly observable. Many such problems require imaginative perception: inferring what would be seen from an unseen viewpoint, tracing paths through occluded spaces, or integrating partial observations into a coherent spatial representation. We introduce Imaginative Perception Tokens (IPT), intermediate perceptual representations that externalize what a VLM would perceive under alternative spatial configurations while remaining consistent with the observed input.   To study this capability, we formulate three tasks, Perspective Taking (PET), Path Tracing (PT), and Multiview Counting (MVC), and construct datasets of approximately 20K examples with ground truth imaginations, answers, and evaluation benchmarks. Using the unified VLM BAGEL as the backbone, IPT supervision consistently improves spatial reasoning and often outperforms textual chain of thought training, even without generating images at inference time. On MVC, IPT improves accuracy by 3.4% and achieves competitive performance with strong closed-source models on PT. We further find that combining IPT and label-only supervision yields additional gains, whereas textual chain of thought can substantially degrade performance, suggesting a modality mismatch when spatial computation is forced through language. Overall, IPT provides a principled supervision signal for reasoning about unobserved spatial structure, improving generalization while producing interpretable intermediate representations.

## Metadata
- **Published**: 2026-06-02T17:59:17Z
- **Authors**: Mahtab Bigverdi, Lindsey Li, Weikai Huang, Yiming Liu, Jaemin Cho, Jieyu Zhang, Tuhin Kundu, Chris Dangjoo Kim, Zelun Luo, Linda Shapiro, Ranjay Krishna
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.03988v1)