---
title: Evaluating LLM Creativity through Long-Tail Performance
url: http://arxiv.org/abs/2610.12998v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_05-03-18Z_EvaluatingLLMCreativitythroughLong_TailPerformance.md
generated_at: 2026-10-11 20:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes a unified framework for evaluating LLM creativity by formalizing it as task-specific performance in the long tail of a reference input-output distribution. The authors ground this approach in the novelty-quality product formulation and validate it empirically across 15 creativity benchmarks and 26 open-weight models, demonstrating that creativity benchmarks occupy deeper tail regions than standard benchmarks and that higher-tail model rankings better align with human creativity judgments. They introduce q@Tail(α), a lower-cost diagnostic metric that measures mean task quality on the tail fraction of an existing benchmark, revealing substantial room for improving LLM creativity through stronger tail performance.

## Key Takeaways
- The authors formalize a shared notion of creativity across diverse benchmarks by defining it as performance in the long tail of a reference input-output distribution, using n-gram absence from pretraining data as a novelty proxy. This provides a principled, unified target that transcends the wide variation in task and metric design across existing creativity benchmarks.
- Empirical evaluation across 15 benchmarks and 26 open-weight models shows that creativity benchmarks lie further in the tail regions than standard benchmarks, and that model rankings derived from higher-tail subsets of each benchmark align more closely with human creativity judgments collected in LM-Arena, validating the long-tail framing as a meaningful signal.
- The proposed q@Tail(α) metric offers a lower-cost creativity diagnostic that measures mean task quality on the tail fraction of an existing benchmark. Applying it to creativity-promoting methods reveals substantial room to improve LLM creativity, suggesting that current methods are insufficient at pushing models into genuinely novel output regions.

## Context
The field of LLM evaluation has proliferated numerous creativity benchmarks with heterogeneous task designs and scoring metrics, making it difficult to determine whether they measure a coherent underlying capability or merely idiosyncratic artifacts of benchmark construction. This paper addresses that fragmentation by proposing a distributional lens—long-tail performance—that unifies disparate benchmarks under a single theoretical construct rooted in the novelty-quality product. By connecting model behavior to the statistical structure of reference text distributions, the work bridges the gap between benchmark engineering and cognitive theories of creativity, offering a principled way to assess whether models genuinely produce novel, high-quality outputs rather than regurgitating common patterns from training data.

## Implications
For practitioners and model developers, the q@Tail(α) diagnostic provides a practical, lower-cost tool to audit and improve creativity-promoting techniques such as prompt engineering, fine-tuning, or sampling strategies, shifting focus from average-case performance to the rare, genuinely novel outputs that matter for creative applications. For the broader AI research community, the finding that tail-region rankings better predict human creativity judgments suggests that current benchmarking practices may systematically undervalue models that excel in long-tail generation, and that evaluation pipelines should be redesigned to weight tail performance more heavily. This has direct consequences for model selection in creative industries such as content generation, design, and storytelling, where the ability to produce outputs outside the common distribution is the core value proposition.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.12998v1)
