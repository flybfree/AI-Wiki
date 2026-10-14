---
title: HarnessTTT: Learn to Optimize Harness at Test-Time for Scientific Discovery
url: http://arxiv.org/abs/2610.17370v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_20-27-32Z_HarnessTTT_LearntoOptimizeHarnessatTest_TimeforSci.md
generated_at: 2026-10-14 00:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
HarnessTTT introduces a test-time learning framework that trains a harness proposer to generate executable discovery scaffolds—comprising system prompts, reusable skills, tools, middleware, and execution controls—while keeping the underlying executor model frozen. Across fourteen scientific discovery tasks spanning mathematics, systems engineering, GPU kernel optimization, heuristic programming, astrodynamics, and biology, the method consistently outperforms prior approaches like OpenEvolve and discovery-fine-tuned models, demonstrating that the search procedure itself can be learned and optimized at inference time.

## Key Takeaways
- HarnessTTT decouples the search strategy from the executor: a trainable proposer generates structured harnesses that guide budgeted discovery rollouts, while the executor (e.g., a 9B model) remains completely frozen. This separation means the quality of the search procedure is improved without any fine-tuning of the base model, using a discovery-oriented policy-gradient objective that combines gap-normalized rewards, leave-one-out advantages (RLOO), and max-sharpening to favor high-performing proposals.
- On eleven benchmark tasks, HarnessTTT with a frozen 9B executor outperforms OpenEvolve using the same executor, with improvements such as raising circle packing scores from 1.17 to 2.64. It also surpasses the discovery-fine-tuned Finch-9B by up to 92% and achieves the best open-weight sub-10B result on nine tasks. Notably, it reaches 0.380919 on the Erdős minimum overlap problem, edging past the best human reference of 0.380927.
- Learned harnesses transfer across model scales and architectures: scaling both proposer and executor to 27B improves on eleven of fourteen tasks, and transferring the harnesses discovered with smaller models to GPT-5.5 matches or exceeds the strongest reported system of any backbone on nine of fourteen tasks, showing that the search scaffolds encode generalizable discovery strategies rather than model-specific tricks.

## Context
This work sits at the intersection of test-time compute scaling, automated scientific discovery, and agentic AI systems. Prior approaches such as OpenEvolve and discovery-fine-tuned models treat the search procedure as fixed or bake optimization into model weights, limiting adaptability. HarnessTTT reframes the problem by treating the harness—the structured instructions, tools, and execution controls that guide a search—as a learnable artifact optimized through reinforcement learning at inference time. This aligns with a broader trend in AI research toward separating what a model knows from how it is asked to search, enabling smaller models to punch above their weight through better procedural scaffolding.

## Implications
For practitioners, HarnessTTT suggests that significant performance gains in scientific discovery pipelines can be achieved without retraining or fine-tuning large models, by instead optimizing the procedural scaffolds that guide their search behavior. This has practical cost implications: organizations can deploy smaller, cheaper frozen executors and invest compute in learning effective harnesses, then transfer those harnesses to more powerful models when needed. For the broader field, the finding that learned search strategies transfer across model scales and architectures points toward a future where discovery workflows become modular and portable, decoupling algorithmic search intelligence from any single model's weights.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17370v1)
