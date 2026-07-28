---
title: "Foundation Models State of the Art — 2026-07-27"
date: 2026-07-27
status: draft
tags: ["wiki", "foundation-models", "state-of-the-art", "leaderboard", "comparison", "2026-07-27"]
---

# Foundation Models State of the Art — 2026-07-27

**Source**: [Original Article](https://github.com/flybfree/AI-Wiki/wiki)

This is the updated frontier foundation-model snapshot. It supersedes the 2026-06-30 baseline with the biggest additions since then: **Claude Opus 5** and OpenAI’s **GPT-5.6** family (**Sol**, **Terra**, **Luna**).

## Research sources

- [OpenAI: GPT-5.6](https://openai.com/index/gpt-5-6/)
- [OpenAI: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)
- [OpenAI API: GPT-5.6 Luna](https://developers.openai.com/api/docs/models/gpt-5.6-luna)
- [Anthropic: Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)
- [Anthropic: Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [OpenAI: Health in ChatGPT](https://openai.com/index/health-in-chatgpt/)
- [Google: Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)
- [xAI: Grok 4](https://x.ai/news/grok-4)
- [Meta: The Llama 4 herd](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [Google: Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)
- [DeepSeek V4 Preview](https://api-docs.deepseek.com/news/news260424)
- [Qwen3: Think Deeper, Act Faster](https://qwenlm.github.io/blog/qwen3/)
- [GLM-5.2](https://z.ai/blog/glm-5.2)
- [Kimi K2.6 quickstart](https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart)

## Executive summary

The frontier is still fragmented rather than dominated by one universal winner:

- **OpenAI’s GPT-5.6 family** is the biggest new proprietary release since the 2026-06-30 snapshot.
- **Claude Opus 5** is the clearest new Anthropic flagship and is now the model to watch for long-horizon coding and knowledge work.
- The model race is increasingly **tiered**: one flagship, one balanced model, and one low-cost / high-throughput model.
- Open-weight leaders still matter because the best choice depends on the job: reasoning, coding, multimodal work, self-hosting, or cost control.

## 1) American proprietary frontier models

### OpenAI — GPT-5.6 family: Sol, Terra, and Luna

OpenAI’s newest family is the most important addition since the last snapshot.

- **Sol** is the flagship model for complex reasoning, coding, and long-horizon agentic work.
- **Terra** is the balanced everyday model with stronger cost/performance tradeoffs.
- **Luna** is the cheapest and fastest tier for high-volume, low-latency workloads.

Why it matters:
- OpenAI is now shipping a **family strategy** instead of a single monolithic flagship
- Sol gives a clear top-end choice for hard work
- Luna makes the low-cost tier explicit instead of hiding it behind a generic “mini” label

Current impression:
- **Sol** is the model to watch when you want frontier capability
- **Terra** is the pragmatic default for many product workloads
- **Luna** is the cost-sensitive routing option

Sources:
- [GPT-5.6](https://openai.com/index/gpt-5-6/)
- [Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)
- [GPT-5.6 Luna model docs](https://developers.openai.com/api/docs/models/gpt-5.6-luna)

### Anthropic — Claude Opus 5

Claude Opus 5 is the major Anthropic release since the last snapshot.

- Anthropic says Opus 5 is a thoughtful, proactive model that comes close to **Claude Fable 5** at **half the price**.
- Anthropic also says it is the new state of the art on coding and knowledge-work evaluations in its framing.
- The safety split still matters: Opus 5 remains behind **Claude Mythos 5** on cybersecurity tasks.

Why it matters:
- It is the clearest new public benchmark for Anthropic’s flagship tier
- It is especially relevant for software engineering, agentic workflows, and careful long-horizon work
- It shows the current tradeoff: better everyday utility without collapsing the safety/cyber gap

Current impression:
- **Opus 5** is the main public Anthropic model to track now
- **Fable 5** still reads like the more precision-oriented sibling
- **Mythos 5** still anchors the harder safety/cyber tier

Source:
- [Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)

### Google — Gemini 3.1 Pro

Google remains a major frontier player, especially in multimodal understanding and product integration.

Why it matters:
- Strong multimodal and long-context capabilities
- Deep integration into Google’s consumer and developer products
- Competitive reasoning and science/research performance

Current impression:
- Gemini 3.1 Pro remains one of the strongest closed models for multimodal work
- Google’s advantage is still platform integration as much as raw model quality

Sources:
- [Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)
- [Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/)

### xAI — Grok 4

xAI’s Grok line is still focused on real-time search, tool use, and fast product iteration.

Why it matters:
- Native tool use
- Real-time search integration
- Strong product focus on immediacy and current information

Current impression:
- Not always the benchmark leader, but still a frontier contender
- Relevant when current-event awareness and tool-assisted interaction matter

Source:
- [Grok 4](https://x.ai/news/grok-4)

## 2) American open-weight / open-source-style frontier models

### Meta — Llama 4 Scout and Maverick

Meta’s Llama 4 release pushed open-weight models further into native multimodality and MoE territory.

Why it matters:
- Open-weight natively multimodal models
- Mixture-of-experts architecture
- Large context support

Current impression:
- One of the most important open-weight western releases
- Best when you need open deployment, customization, or on-prem control

Source:
- [The Llama 4 herd](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

### Google — Gemma 4 26B A4B and Gemma 4 12B Unified

Gemma 4 is Google’s open-weight multimodal family.

Why it matters:
- Multimodal text, image, and audio support across the family
- 26B A4B MoE variant is the heavyweight open-weight option
- 12B Unified is the compact encoder-free multimodal option
- Strong long-context and reasoning benchmarks for an open family

Current impression:
- Gemma 4 26B A4B is one of the strongest open-weight multimodal models available
- Gemma 4 12B Unified gives a strong capability-per-parameter tradeoff

Sources:
- [Gemma 4 12B blog post](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)
- [Gemma 4 model overview](https://ai.google.dev/gemma/docs/core)

## 3) Chinese proprietary frontier models

### Baidu — ERNIE 5.0 / 5.1

Baidu’s ERNIE line remains a serious Chinese proprietary competitor, especially in multimodal and leaderboard performance.

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

Kimi’s platform emphasizes long context, tool calling, code generation, and visual reasoning.

Why it matters:
- Very large model family
- 256K context on the API platform
- Strong coding and agent-style workflows

Current impression:
- Important Chinese proprietary contender for coding and long-context tasks
- Especially relevant for document-heavy or tool-heavy workloads

Sources:
- [Kimi K2.6 quickstart](https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart)
- [Kimi API Platform](https://platform.kimi.ai/)

### Tencent Hunyuan

Tencent Hunyuan remains a meaningful frontier effort, especially in multimodal understanding and model research.

Why it matters:
- Active model research and product ecosystem
- Ongoing work in language, vision, translation, and world-model style directions
- Public pages emphasize code, document understanding, and agent ability

Current impression:
- Less standardized in public benchmark chatter than OpenAI / Anthropic / Google, but still important
- Worth tracking because Tencent keeps shipping practical upgrades

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

## 5) What changed since 2026-06-30

The biggest deltas are:

- **OpenAI GPT-5.6 Sol** now defines the flagship closed-model slot more clearly than the older single-model framing.
- **Terra** and **Luna** make OpenAI’s cost/performance tiers much more explicit.
- **Claude Opus 5** is a major step up in Anthropic’s public Opus tier and is the model to watch for coding and knowledge work.
- The market is increasingly choosing between **flagship**, **balanced**, and **cost-efficient** model tiers rather than one universal best model.

## 6) Practical guidance

If you want the best model for a specific job, I would treat the frontier like this:

- Best general closed-model reasoning: **GPT-5.6 Sol** or **Claude Opus 5**
- Best closed-model multimodal work: **Gemini 3.1 Pro**
- Best coding-heavy closed model: **GPT-5.6 Sol** or **Claude Opus 5**
- Best low-cost closed model routing: **GPT-5.6 Luna**
- Best open-weight generalist: **Qwen3**, **DeepSeek V4**, or **GLM-5.2** depending on the task
- Best open-weight coding / agent work: **GLM-5.2** or **DeepSeek V4 Pro Max**
- Best model for self-hosting control: **Llama 4**, **Qwen3**, **DeepSeek V4**, or **GLM-5.2**
- Best Chinese proprietary platform model to watch: **ERNIE 5.1** and **Kimi K2.6**

## 7) Bottom line

As of 2026-07-27, foundation-model SOTA is no longer a single throne.

Instead, the frontier is a cluster:
- American proprietary leaders still dominate the premium closed-model tier
- Chinese labs remain competitive across both proprietary and open-weight releases
- Open-weight models are strong enough that the best choice is usually task-specific, not brand-specific

For a living wiki, this page should be updated again when the next major family lands.

## Related wiki pages

- [LLMs & Foundation Models Hub](2026-06-09_LLMsAndFoundationModelsHub.md)
- [LLM Model Evolution](llm-models/2026-06-10_LLMModelEvolution.md)
- [LLM Release Tracker](llm-models/2026-07-10_LLMReleaseTracker.md)
- [AI Industry Trends](ai-trends/2026-06-10_AIIndustryTrends.md)
- [AI Benchmarks](ai-benchmarks/2026-06-10_AIBenchmarks.md)
