---
title: Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI
url: http://arxiv.org/abs/2610.38095v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-28_00-28-08Z_Nemotron3_5SuperandLightning_Open_EfficientMixture.md
generated_at: 2026-11-01 21:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
NVIDIA introduces Nemotron 3.5 Super and Nemotron 3.5 Lightning, two open-weight Mixture-of-Experts Hybrid Mamba-Transformer models designed for reasoning, long-context understanding, and agentic AI workloads. Super is a 120B-parameter (12B active) multimodal model while Lightning is a 30B-parameter (3B active) text model, both trained through a comprehensive pipeline combining large-scale distillation, long-context training, supervised fine-tuning, reinforcement learning, and multi-teacher on-policy distillation. The models achieve strong performance on agentic benchmarks such as SWE-bench Pro (51.78%) while maintaining high inference efficiency, including up to 4,856 output tokens/s/GPU on GB200 hardware.

## Key Takeaways
- Nemotron 3.5 Super achieves 51.78% on SWE-bench Pro, surpassing the larger Nemotron 3 Ultra despite using approximately 4.6x fewer active parameters, demonstrating that architectural efficiency through Mamba-Transformer hybrids and Mixture-of-Experts routing can outperform brute-force scaling in agentic software-engineering tasks. The post-training pipeline combining RLVR, RLHF, and multi-teacher on-policy distillation (MOPD) transforms a text-only base model into a multimodal agent capable of reasoning over text, images, video, and interactive tool environments.
- The models incorporate native speculative decoding with post-training MTP boosting that improves acceptance length by up to 21.8% under probabilistic draft sampling, while NVFP4 quantization achieves 99.62% median accuracy recovery relative to BF16 precision. Inference optimizations enable sustained throughput of at least 50 tokens/s/user while reaching peak throughput of 4,856 output tokens/s/GPU on GB200, making these models practical for production deployment at scale.
- Indic continued pretraining improves Indian-language benchmark performance by up to 9.82 percentage points, and agentic mid-training strengthens software-engineering capabilities and robustness across diverse agent harnesses. Test-time scaling through parallel agent execution and self-verification further extends capability without additional training, offering a practical path to improved reasoning quality at inference time.

## Context
This paper sits at the intersection of several major trends in large language model development: the shift from dense Transformer architectures toward hybrid Mamba-Transformer designs for improved efficiency, the growing emphasis on agentic AI systems that interact with tools and environments, and the push toward open-weight models that can be deployed at scale. NVIDIA's approach of combining Mixture-of-Experts sparsity with linear-attention Mamba components addresses the fundamental tension between model capability and computational cost that has constrained the deployment of frontier models. The comprehensive post-training pipeline, including reinforcement learning with verifiable rewards and multi-teacher distillation, reflects the industry's maturation beyond simple supervised fine-tuning toward more sophisticated alignment strategies.

## Implications
For practitioners and industry stakeholders, these models represent a practical path toward deploying capable agentic AI systems without the prohibitive compute costs of dense frontier models, particularly for software engineering automation, multilingual applications, and long-context reasoning tasks. The open-weight nature and quantization-friendly design (NVFP4 with near-lossless accuracy recovery) lower barriers for organizations seeking to build custom agentic workflows on their own infrastructure. The demonstrated efficiency gains—achieving superior SWE-bench performance with 4.6x fewer active parameters—suggest that architectural innovation and training methodology can rival or exceed pure parameter scaling, potentially reshaping how the industry allocates compute budgets for next-generation AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.38095v1)
