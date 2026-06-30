---
title: "Foundation Models State of the Art — 2026-06-30"
date: 2026-06-30
status: draft
tags: ["wiki", "foundation-models", "state-of-the-art", "leaderboard", "comparison", "2026-06-30"]
---

# Foundation Models State of the Art — 2026-06-30

**Source**: [Original Article](https://github.com/flybfree/AI-Wiki/wiki)

This is a dated snapshot of the frontier foundation-model landscape. The date is part of the page title so future updates can create a new page instead of duplicating this one.

## Research sources

- [OpenAI: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [Anthropic: Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)
- [Anthropic: Introducing Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6)
- [Google: Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)
- [xAI: Grok 4](https://x.ai/news/grok-4)
- [Meta: The Llama 4 herd](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [Google: Introducing Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)
- [Google: Gemma 4 model overview](https://ai.google.dev/gemma/docs/core)
- [DeepSeek V4 Preview](https://api-docs.deepseek.com/news/news260424)
- [Qwen3: Think Deeper, Act Faster](https://qwenlm.github.io/blog/qwen3/)
- [GLM-5.2](https://z.ai/blog/glm-5.2)
- [Kimi K2.6 quickstart](https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart)
- [ERNIE 5.0 / 5.1](https://ernie.baidu.com/blog/posts/ernie5.0/)
- [Tencent Hunyuan](https://hunyuan.tencent.com/)
- [Artificial Analysis model leaderboard](https://artificialanalysis.ai/leaderboards/models)
- [BenchLM benchmark snapshots](https://benchlm.ai/benchmarks/artificialAnalysis)
- [LMArena text leaderboard](https://lmarena.ai/leaderboard/text)
- [LLM Stats open LLM leaderboard](https://llm-stats.com/leaderboards/open-llm-leaderboard)

## Executive summary

The current frontier is fragmented rather than dominated by a single universal winner:

- The strongest proprietary models are still mostly American: OpenAI, Anthropic, Google, and xAI.
- Chinese labs are now genuinely frontier-competitive, especially in open-weight / open-source-style releases and in cost-performance.
- Open-weight models have closed the gap enough that the best choice now depends heavily on the task: reasoning, coding, long-context work, multimodal understanding, or self-hosting economics.
- Google’s Gemma 4 family deserves special mention: the 26B A4B MoE model is a strong open-weight multimodal heavyweight, and the 12B Unified model is a very capable compact multimodal option.
- Benchmarks disagree by category, so “state of the art” should be read as “best on this task under this evaluation,” not “best at everything.”

## 1) American proprietary frontier models

### OpenAI — GPT-5.5 family

OpenAI positions GPT-5.5 as a model for complex real-world work: coding, research, analysis, and document/spreadsheet workflows.

Why it matters:
- Strong all-around generalist behavior
- Excellent coding and structured work performance
- Good product integration across ChatGPT and the API

Current impression:
- One of the top general-purpose proprietary models
- Often near the top for coding-oriented leaderboards
- Still a first-choice closed model when you want broad capability plus strong tool use

Sources:
- [Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [GPT-5.5 System Card](https://openai.com/index/gpt-5-5-system-card/)

### Anthropic — Claude Opus 4.8 and Claude Sonnet 4.6

Anthropic’s current flagship line is very strong on reasoning, coding, agent planning, and long-form knowledge work.

Why it matters:
- Claude Opus 4.8 is a top-tier reasoning model
- Claude Sonnet 4.6 is the workhorse option for coding and agents
- Anthropic keeps pushing long-context and practical workflows

Current impression:
- Opus is one of the best models for hard reasoning and careful responses
- Sonnet is one of the best “daily driver” models for production use
- Anthropic is especially strong when you need reliable stepwise thinking and agentic workflows

Sources:
- [Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)
- [Introducing Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6)
- [What’s new in Claude Opus 4.8](https://docs.anthropic.com/en/docs/about-claude/models/whats-new-claude-4-8)

### Google — Gemini 3.1 Pro

Google’s Gemini 3 family remains a major frontier player, especially in multimodal understanding and broad consumer/developer integration.

Why it matters:
- Strong multimodal and long-context capabilities
- Deep integration into Google’s consumer and developer products
- Competitive reasoning and science/research performance

Current impression:
- Gemini 3.1 Pro is a top closed model for multimodal work and difficult tasks
- Often lands in the top tier for reasoning and knowledge benchmarks
- Google’s advantage is platform integration as much as raw model quality

Sources:
- [Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)
- [Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/)

### xAI — Grok 4

xAI’s Grok line is optimized for real-time search, native tool use, and fast product iteration.

Why it matters:
- Native tool use
- Real-time search integration
- Strong product focus on immediacy and current information

Current impression:
- Not always the benchmark leader, but still a frontier contender
- Particularly relevant if you want current-event awareness and tool-assisted interaction

Source:
- [Grok 4](https://x.ai/news/grok-4)

## 2) American open-weight / open-source-style frontier models

### Meta — Llama 4 Scout and Maverick

Meta’s Llama 4 release is important because it pushed open-weight models further into native multimodality and MoE territory.

Why it matters:
- Open-weight natively multimodal models
- Mixture-of-experts architecture
- Large context support

Current impression:
- One of the most important open-weight western releases
- Best when you need open deployment, customization, or on-prem control
- Not necessarily the absolute best on every benchmark, but still a central reference point

Source:
- [The Llama 4 herd](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

### Google — Gemma 4 26B A4B and Gemma 4 12B Unified

Gemma 4 is Google’s open-weight multimodal family, and the 26B A4B and 12B Unified variants are especially relevant for current SOTA comparisons.

Why it matters:
- Multimodal text, image, and audio support across the family
- 26B A4B MoE variant is the heavyweight open-weight option
- 12B Unified is the compact encoder-free multimodal option
- Strong long-context and reasoning benchmarks for an open family

Current impression:
- Gemma 4 26B A4B is one of the strongest open-weight multimodal models available
- Gemma 4 12B Unified gives a strong capability-per-parameter tradeoff
- Google’s advantage here is not just quality but deployment flexibility across devices and servers

Selected benchmark snapshot from the model cards:
- Gemma 4 26B A4B: MMLU Pro 82.6%, AIME 2026 no tools 88.3%, LiveCodeBench v6 77.1%, MMMU Pro 73.8%, MRCR v2 8 needle 128k 44.1%
- Gemma 4 12B Unified: MMLU Pro 77.2%, AIME 2026 no tools 77.5%, LiveCodeBench v6 72.0%, MMMU Pro 69.1%, MRCR v2 8 needle 128k 43.4%

Sources:
- [Gemma 4 12B blog post](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)
- [Gemma 4 model overview](https://ai.google.dev/gemma/docs/core)
- [Gemma 4 26B A4B README](https://huggingface.co/google/gemma-4-26B-A4B-it/raw/main/README.md)
- [Gemma 4 12B README](https://huggingface.co/google/gemma-4-12B/raw/main/README.md)

## 3) Chinese proprietary frontier models

### Baidu — ERNIE 5.0 / 5.1

Baidu’s ERNIE line is a serious Chinese proprietary competitor, especially in multimodal and leaderboard performance.

Why it matters:
- ERNIE 5.0 is a very large unified multimodal foundation model
- ERNIE 5.1 focuses on better performance with fewer parameters
- Baidu explicitly tracks leaderboard gains and practical usability

Current impression:
- One of the strongest Chinese proprietary foundation-model families
- Important in the China frontier race, especially for multimodal and productized usage

Sources:
- [ERNIE 5.0](https://ernie.baidu.com/blog/posts/ernie5.0/)
- [ERNIE 5.1 release](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/)

### Moonshot AI — Kimi K2.6 / K2.7 Code

Kimi’s current platform emphasizes long context, tool calling, code generation, and visual reasoning.

Why it matters:
- Very large model family
- 256K context on the API platform
- Strong coding and agent-style workflows

Current impression:
- One of the important Chinese proprietary contenders for coding and long-context tasks
- Particularly relevant if your workload is tool-heavy or document-heavy

Sources:
- [Kimi K2.6 quickstart](https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart)
- [Kimi API Platform](https://platform.kimi.ai/)

### Tencent Hunyuan

Tencent Hunyuan is still a meaningful frontier effort, especially in multimodal understanding and model research.

Why it matters:
- Active model research and product ecosystem
- Ongoing work in language, vision, translation, and world-model style directions
- Public pages emphasize code, document understanding, and agent ability in 2026 updates

Current impression:
- Less standardized in public benchmark chatter than OpenAI/Anthropic/Google, but still an important Chinese platform
- Worth tracking because Tencent keeps shipping practical model upgrades

Sources:
- [Tencent Hunyuan](https://hunyuan.tencent.com/)
- [Tencent Hunyuan model square](https://hunyuan.tencent.com/modelSquare/home/list)

## 4) Chinese open-weight / open-source-style frontier models

### DeepSeek — V4 Preview / V4 Pro / V4 Flash

DeepSeek remains one of the most important open-weight Chinese frontier families.

Why it matters:
- Preview release was explicitly open-sourced
- Strong agentic capabilities
- Strong cost/performance story
- Competitive on coding and general reasoning

Current impression:
- One of the best open-weight options for serious production use
- Often shows up near the top of open-source leaderboards
- Especially attractive when you care about self-hosting economics and model quality together

Sources:
- [DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424)
- [DeepSeek V4 technical documentation](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)
- [DeepSeek homepage](https://www.deepseek.com/en)

### Qwen3 family

Qwen3 is one of the most important open-weight model families globally.

Why it matters:
- Open-weight MoE and dense variants
- Apache 2.0 licensing for the release family
- Broad performance across reasoning and coding

Current impression:
- A top choice for open deployment and customization
- Very relevant to both English and Chinese workloads
- Often among the strongest open-weight contenders across public leaderboards

Source:
- [Qwen3: Think Deeper, Act Faster](https://qwenlm.github.io/blog/qwen3/)

### Z.ai GLM-5.2

GLM-5.2 is a major Chinese open-source/open-weight contender for long-horizon agentic tasks.

Why it matters:
- Strong coding and system-engineering focus
- Large context support
- Designed for long-horizon agentic work

Current impression:
- One of the strongest open-source large models by current leaderboard snapshots
- Important if you need high-end open-weight agent behavior

Sources:
- [GLM-5.2](https://z.ai/blog/glm-5.2)
- [GLM-5 overview](https://docs.z.ai/guides/llm/glm-5)

## 5) What the benchmarks say

This is where the “best model” question gets interesting. Different benchmarks point to different winners.

### Reasoning / hard exam style tasks

A current public snapshot from BenchLM reports:
- Claude Opus 4.8 at 45.7% on AA-HLE
- Gemini 3.1 Pro at 44.7%
- GPT-5.5 at 44.3%

Interpretation:
- The top closed models are very close to one another on hard reasoning
- Small score differences often matter less than prompt style, context length, or product behavior

Source:
- [BenchLM Artificial Analysis Intelligence Index](https://benchlm.ai/benchmarks/artificialAnalysis)

### Coding / software engineering tasks

BenchLM’s public coding snapshot reports:
- GPT-5.5 at 74.9%
- Gemini 3.1 Pro at 68.8%
- GLM-5.2 at 68.8%

Interpretation:
- Coding is one of the places where open-weight Chinese models are genuinely close to frontier closed models
- GPT-5.5 still looks extremely strong
- GLM-5.2 is a standout open-source contender for engineering work

Source:
- [BenchLM AA Coding Index](https://benchlm.ai/benchmarks/aaCodingIndex)

### Open-weight leaderboard snapshot

Artificial Analysis’ open-source rankings describe:
- GLM-5.2 (max) and MiniMax-M3 as the highest-intelligence large open-source models
- DeepSeek V4 Pro (Max) and Kimi K2.6 as the next strongest group

Interpretation:
- Open-weight systems are no longer “far behind” in the way they were a year or two ago
- The strongest open-weight models are now competitive enough for serious production use

Source:
- [Artificial Analysis open-source models](https://artificialanalysis.ai/models/open-source/large)

### SWE-bench and code-agent performance

LLM Stats’ open leaderboard snapshot says:
- DeepSeek-V4-Pro-Max is the top-ranked open-source model on SWE-Bench Verified, with a score of 0.806

Interpretation:
- Open-source code models are now credible front-runners for engineering-heavy workflows
- For coding agents, open-weight is often a real alternative rather than a fallback

Source:
- [LLM Stats open LLM leaderboard](https://llm-stats.com/leaderboards/open-llm-leaderboard)

## 6) Practical guidance

If you want the best model for a specific job, I would treat the frontier like this:

- Best general closed-model reasoning: Claude Opus 4.8 or GPT-5.5
- Best closed-model multimodal work: Gemini 3.1 Pro
- Best coding-heavy closed model: GPT-5.5, with Claude Sonnet 4.6 as a strong second choice
- Best open-weight generalist: Qwen3, DeepSeek V4, or GLM-5.2 depending on the task
- Best open-weight coding/agent work: GLM-5.2 or DeepSeek V4 Pro Max
- Best model for self-hosting control: Llama 4, Qwen3, DeepSeek V4, or GLM-5.2
- Best Chinese proprietary platform model to watch: ERNIE 5.1 and Kimi K2.6

## 7) Bottom line

As of 2026-06-30, foundation-model SOTA is no longer a single throne.

Instead, the frontier is a cluster:
- American proprietary leaders still dominate the premium closed-model tier
- Chinese labs are now competitive across both proprietary and open-weight releases
- Open-weight models are strong enough that the best choice is usually task-specific, not brand-specific

For a living wiki, this page should be updated on a new date when the leaderboard shifts again.

## Related wiki pages

- [[concepts/2026-06-09_LLMsAndFoundationModelsHub.md|LLMs & Foundation Models Hub]]
- [[concepts/llm-models/2026-06-10_LLMModelEvolution.md|LLM Model Evolution]]
- [[concepts/2026-06-09_AIIndustryAndNewsHub.md|AI Industry & News Hub]]
- [[concepts/2026-06-09_AIResearchPapersHub.md|AI Research Papers Hub]]
