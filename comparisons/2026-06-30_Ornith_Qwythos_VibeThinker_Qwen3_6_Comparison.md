---
title: "Model Comparison — Ornith, Qwythos, VibeThinker, Qwen3.6, Gemma 4, Agents-A1"
date: 2026-06-30
status: draft
tags: ["wiki", "comparison", "foundation-models", "open-weight", "coding", "reasoning", "multimodal", "2026-06-30"]
---

# Model Comparison — Ornith, Qwythos, VibeThinker, Qwen3.6, Gemma 4, Agents-A1

**Source**: [Original Article](https://github.com/flybfree/AI-Wiki/wiki)

This is the benchmark-heavy version of the local/open-weight comparison.
It keeps the task-fit summary, then expands into score tables and model-specific notes.

Important caveat: these models are not directly apples-to-apples. They optimize for different tasks, sizes, and benchmark suites, so the right interpretation is “best for this use case,” not “one universal winner.”

## Quick take

- Best open-source coding agent: [Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)
- Best mid-size open-source coding model: [Ornith-1.0-31B](https://huggingface.co/collections/deepreinforce-ai/ornith-10)
- Best long-context local reasoning model: [Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)
- Best ultra-small math/coding model: [VibeThinker-1.5B](https://huggingface.co/WeiboAI/VibeThinker-1.5B)
- Best balanced open-weight multimodal generalist: [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- Best smaller multimodal generalist: [Gemma 4 12B Unified](https://huggingface.co/google/gemma-4-12B)
- Best larger multimodal MoE generalist: [Gemma 4 26B A4B](https://huggingface.co/google/gemma-4-26B-A4B-it)
- Best experimental local agentic search model: [Agents-A1-NVFP4-MTP-GGUF](https://huggingface.co/s-batman/Agents-A1-NVFP4-MTP-GGUF)

## Comparison table

| Model | Origin | Params / shape | License | Context | Main strength | Main caveat |
|---|---|---:|---|---:|---|---|
| Ornith-1.0-31B | DeepReinforce | 31B dense | MIT | 128K in eval setup | Mid-size agentic coding and software-engineering tasks | Less capacity than the 35B MoE variant |
| Ornith-1.0-35B | DeepReinforce | 35B MoE | MIT | 128K in eval setup | Agentic coding and software-engineering tasks | Heavy model; focused on coding rather than broad multimodal use |
| Qwythos-9B-Claude-Mythos-5-1M | Empero / Qwen-derived | 9B dense | Apache 2.0 | 1,048,576 tokens | Long-context reasoning and tool use | Derived model; not a general frontier multimodal model |
| VibeThinker-1.5B | WeiboAI | 1.5B dense | MIT | Not emphasized as its headline feature | Tiny-model math and coding efficiency | Experimental; best on competitive-style math/coding, not broad assistant work |
| Qwen3.6-35B-A3B | Qwen / Alibaba | 35B total, 3B active | Apache 2.0 | 262,144 native, extensible to 1,010,000 | Balanced multimodal + agentic coding | Larger deployment footprint than the smaller models |
| Gemma 4 26B A4B | Google DeepMind | 26B MoE | Apache 2.0 | 256K | Strong multimodal reasoning and coding | Bigger memory footprint than 12B |
| Gemma 4 12B Unified | Google DeepMind | 12B dense | Apache 2.0 | 256K | Best compact multimodal generalist in Gemma 4 family | Less raw capacity than the 26B MoE model |
| Agents-A1-NVFP4-MTP-GGUF | InternScience / s-batman GGUF | Qwen3.5-35B-A3B MoE derivative | GGUF / local artifact | — | Agentic search, instruction following, scientific reasoning | Experimental local packaging, not a broad generalist |

## Model notes

### Ornith-1.0 family (31B Dense / 35B MoE)

Ornith is the most explicitly code-agent-focused model family in this set. The family spans 9B-Dense, 31B-Dense, 35B-MoE, and 397B-MoE variants, and it is MIT licensed.

What stands out:
- Trained for agentic coding and self-improving scaffolds
- The 31B dense checkpoint gives a smaller-footprint option within the same family
- Officially claims state-of-the-art results among open-source models of comparable size on Terminal-Bench 2.1, SWE-Bench, NL2Repo, and OpenClaw
- The 35B card emphasizes efficient single-GPU deployment

Official benchmark snapshot from the model card:
- Terminal-Bench 2.1 (Terminus-2): 64.2
- Terminal-Bench 2.1 (Claude Code): 62.8
- SWE-bench Verified: 75.6
- SWE-bench Pro: 50.4
- SWE-bench Multilingual: 69.3
- NL2Repo: 34.6
- Claw-eval Avg: 69.8

Best fit:
- Coding agents
- Terminal-heavy workflows
- Repository-level automation
- Self-improving / scaffolded agent experiments

Source:
- [Ornith-1.0 collection](https://huggingface.co/collections/deepreinforce-ai/ornith-10)
- [Ornith-1.0-35B README](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B/raw/main/README.md)
- [Ornith-1.0 blog post](https://deep-reinforce.com/ornith_1_0.html)

### Qwythos-9B-Claude-Mythos-5-1M

Qwythos is a compact 9B reasoning model built on a Qwen3.5-9B base and post-trained on over 500 million tokens of Claude Mythos and Claude Fable traces. It is Apache 2.0 licensed and ships with a 1,048,576-token context window via YaRN rope scaling.

What stands out:
- Extremely long context for a 9B model
- Native function calling / tool-use support
- Strong lift over the base Qwen3.5-9B on the model card’s controlled harness
- Useful in domains where long context matters more than raw multimodal breadth

Headline results from the model card:
- gsm8k flexible: 0.860 vs 0.670 for base
- gsm8k strict: 0.810 vs 0.510 for base
- MMLU: 0.575 vs 0.232 for base
- ARC-Challenge: 0.490 vs 0.470 for base
- GPQA Diamond: 0.580 vs 0.630 for base, so not uniformly better on every hard-reasoning metric

Best fit:
- Long-context document reasoning
- Local tool-using assistants
- Research / codebase review where context length matters more than raw multimodal breadth

Source:
- [Qwythos-9B README](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M/raw/main/README.md)

### VibeThinker-1.5B

VibeThinker is the smallest model here by a wide margin. It is a 1.5B dense model, MIT licensed, and explicitly positioned as an experimental release for competitive-style math and algorithmic coding.

What stands out:
- Very small footprint
- Surprisingly strong math/coding scores for its size
- Low reported training cost in the model card
- Best treated as a specialist model, not a general assistant

Key reported scores:
- AIME24: 80.3
- AIME25: 74.4
- HMMT25: 50.4
- LiveCodeBench v5: 55.9
- LiveCodeBench v6: 51.1

Best fit:
- Competitive math
- Algorithmic coding
- Tiny-model experiments
- Edge / constrained deployment where capability per parameter matters most

Source:
- [VibeThinker-1.5B README](https://huggingface.co/WeiboAI/VibeThinker-1.5B/raw/main/README.md)
- [Technical report](https://huggingface.co/papers/2511.06221)

### Qwen3.6-35B-A3B

Qwen3.6-35B-A3B is the broadest model in this set. It is a 35B-total, 3B-active open-weight multimodal model with 262,144 native context and extensibility up to 1,010,000 tokens.

What stands out:
- Native multimodal / image-text-to-text support
- Strong agentic coding positioning
- Thinking preservation for iterative workflows
- Very broad benchmark coverage in the model card

Official benchmark snapshot from the model card:
- SWE-bench Verified: 73.4
- SWE-bench Multilingual: 67.2
- SWE-bench Pro: 49.5
- Terminal-Bench 2.0: 51.5
- Claw-Eval Avg: 68.7
- NL2Repo: 29.4
- LiveCodeBench v6: 80.4
- AIME26: 92.7

Best fit:
- General-purpose open-weight deployment
- Multimodal work
- Agentic coding and repository reasoning
- Teams that want one model to cover a lot of ground

### Gemma 4 26B A4B

Gemma 4 26B A4B is Google DeepMind’s larger multimodal open-weight model in the Gemma 4 family. The official naming is 26B A4B, not A3B; if you meant a different variant, I can swap it in.

What stands out:
- Multimodal: text + image, with audio supported in the family’s larger context stack
- MoE design: 26B total with about 4B active parameters
- 256K context window
- Strong benchmark scores across language, math, coding, vision, and long-context tasks

Selected model-card scores:
- MMLU Pro: 82.6%
- AIME 2026 no tools: 88.3%
- LiveCodeBench v6: 77.1%
- Codeforces ELO: 1718
- GPQA Diamond: 82.3%
- MMMU Pro: 73.8%
- MATH-Vision: 82.4%
- MRCR v2 8 needle 128k: 44.1%

Best fit:
- Multimodal reasoning
- Coding and STEM tasks
- Long-context assistant work
- Teams that want an open-weight MoE model with strong all-round quality

Source:
- [Gemma 4 26B A4B README](https://huggingface.co/google/gemma-4-26B-A4B-it/raw/main/README.md)
- [Gemma 4 overview](https://ai.google.dev/gemma/docs/core)

### Gemma 4 12B Unified

Gemma 4 12B Unified is the smaller dense multimodal variant in the family. It uses the same unified encoder-free design, with audio, vision, and text handled in one stack.

What stands out:
- Unified multimodal design: text, image, audio, and video inputs
- Dense 12B model with 256K context
- Better deployment economics than the 26B A4B while staying surprisingly strong
- Good choice when you want a local/open model that is still broad rather than tiny-specialized

Selected model-card scores:
- MMLU Pro: 77.2%
- AIME 2026 no tools: 77.5%
- LiveCodeBench v6: 72.0%
- Codeforces ELO: 1659
- GPQA Diamond: 78.8%
- MMMU Pro: 69.1%
- MATH-Vision: 79.7%
- MRCR v2 8 needle 128k: 43.4%

Best fit:
- Local multimodal assistants
- On-device or smaller server deployments
- Reasoning + vision + audio tasks where you do not need the heavier 26B MoE

Source:
- [Gemma 4 12B README](https://huggingface.co/google/gemma-4-12B/raw/main/README.md)
- [Introducing Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)

### Agents-A1-NVFP4-MTP-GGUF

Agents-A1-NVFP4-MTP-GGUF is a local GGUF derivative of InternScience/Agents-A1, described as a Qwen3.5-35B-A3B MoE multimodal derivative with MTP heads grafted from unsloth/Qwen3.6-35B-A3B-MTP-GGUF. The packaging uses llama.cpp NVFP4/MXFP4 routing patches, which makes it interesting as a local agentic model experiment rather than a broad generalist.

What stands out:
- Local GGUF delivery for an agentic multimodal MoE derivative
- MTP support, which can help speculative decoding workflows
- Strong agent-oriented benchmark signal: Seal-0 56.4, HiPhO 46.4, FrontierScience-Olympiad 79.0, FrontierScience-Research 40.0, IFBench 80.6, IFEval 94.8
- Also strong on BrowseComp 75.5, XBench-DS-2510 86.0, GAIA 96.0, SciCode 44.3, HLE with tools 47.6, and MolBench-bind 56.8

Best fit:
- Local agentic search / scientific reasoning experiments
- Tool-using workflows
- Hardware setups that can take advantage of NVFP4/MTP support

Source:
- [s-batman/Agents-A1-NVFP4-MTP-GGUF](https://huggingface.co/s-batman/Agents-A1-NVFP4-MTP-GGUF)
- [Model README](https://huggingface.co/s-batman/Agents-A1-NVFP4-MTP-GGUF/blob/main/README.md)

## Expanded benchmark tables

### Agentic and coding benchmarks

| Model | Terminal-Bench | SWE-bench Verified | SWE-bench Pro | NL2Repo | Claw-Eval Avg | BrowseComp | GAIA | IFEval |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ornith-1.0-35B | 64.2 | 75.6 | 50.4 | 34.6 | 69.8 | — | — | — |
| Qwen3.6-35B-A3B | 51.5 | 73.4 | 49.5 | 29.4 | 68.7 | — | — | — |
| Agents-A1-NVFP4-MTP-GGUF | — | — | — | — | — | 75.5 | 96.0 | 94.8 |

### Reasoning and math benchmarks

| Model | MMLU Pro | AIME | GPQA Diamond | ARC-Challenge | GSM8K | HiPhO |
|---|---:|---:|---:|---:|---:|---:|
| Qwythos-9B-Claude-Mythos-5-1M | — | — | 58.0 | 0.490 | 0.860 / 0.810 | 46.4 |
| Qwen3.6-35B-A3B | — | 92.7 | — | — | — | — |
| Gemma 4 26B A4B | 82.6 | 88.3 | 82.3 | — | — | — |
| Gemma 4 12B Unified | 77.2 | 77.5 | 78.8 | — | — | — |
| VibeThinker-1.5B | — | 80.3 / 74.4 | — | — | — | 50.4 |

### Multimodal and long-context benchmarks

| Model | Context | MMMU Pro | MATH-Vision | MRCR v2 8-needle 128k | LiveCodeBench v6 |
|---|---:|---:|---:|---:|---:|
| Qwythos-9B-Claude-Mythos-5-1M | 1,048,576 | — | — | — | — |
| Qwen3.6-35B-A3B | 262,144 native / 1,010,000 extensible | — | — | — | 80.4 |
| Gemma 4 26B A4B | 256K | 73.8 | 82.4 | 44.1 | 77.1 |
| Gemma 4 12B Unified | 256K | 69.1 | 79.7 | 43.4 | 72.0 |
| Agents-A1-NVFP4-MTP-GGUF | — | — | — | — | — |

### Agent instruction-following and scientific task suite

| Model | Seal-0 | HiPhO | FrontierScience-Olympiad | FrontierScience-Research | IFBench | IFEval | SciCode | HLE w/ tools | MolBench-bind |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Agents-A1-NVFP4-MTP-GGUF | 56.4 | 46.4 | 79.0 | 40.0 | 80.6 | 94.8 | 44.3 | 47.6 | 56.8 |
| Qwythos-9B-Claude-Mythos-5-1M | — | — | — | — | — | — | — | — | — |
| Qwen3.6-35B-A3B | — | — | — | — | — | — | — | — | — |

## Practical ranking by use case

### If you want coding agents
1. Ornith-1.0-35B
2. Qwen3.6-35B-A3B
3. Qwythos-9B for tool-heavy long-context coding
4. Gemma 4 26B A4B
5. VibeThinker-1.5B only for tiny constrained tasks

### If you want long-context reasoning
1. Qwythos-9B-Claude-Mythos-5-1M
2. Qwen3.6-35B-A3B
3. Gemma 4 26B A4B
4. Ornith-1.0-35B
5. VibeThinker-1.5B

### If you want the smallest serious model
1. VibeThinker-1.5B
2. Qwythos-9B
3. Gemma 4 12B Unified
4. Ornith-1.0-35B
5. Qwen3.6-35B-A3B

### If you want broad capability
1. Qwen3.6-35B-A3B
2. Gemma 4 26B A4B
3. Gemma 4 12B Unified
4. Ornith-1.0-35B
5. Qwythos-9B
6. VibeThinker-1.5B

### If you want agentic search / scientific reasoning
1. Agents-A1-NVFP4-MTP-GGUF
2. Qwen3.6-35B-A3B
3. Ornith-1.0-35B

## Bottom line

These models occupy different points on the local/open-weight frontier:

- Ornith is the strongest fit for agentic coding.
- Qwythos is the most interesting long-context reasoning model in a small footprint.
- VibeThinker is the most impressive tiny specialist model.
- Qwen3.6 is the best all-around open-weight multimodal option here.
- Gemma 4 26B A4B is the strongest Gemma option for heavyweight multimodal reasoning.
- Gemma 4 12B Unified is the more compact Gemma option with very strong capability per parameter.
- Agents-A1 adds a useful local agentic-search and scientific-reasoning option.

If you want, I can split this further into a task-first shortlist, a coding-only comparison, and a multimodal-only comparison.
