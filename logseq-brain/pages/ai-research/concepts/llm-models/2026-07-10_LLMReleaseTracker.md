---
title: "LLM Release Tracker"
date: 2026-07-10
type: concept
tags: [llm-models, evolution, tracking]
---

# LLM Release Tracker

**Source**: [AI/ML API comparison article](https://aimlapi.com/blog/top-llm-models-in-2026-the-best-ai-models-for-reasoning-coding-multimodal-tasks) · [Fazm April releases roundup](https://fazm.ai/blog/new-llm-releases-april-2026) · [LLM Model Evolution](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/2026-06-10_LLMModelEvolution.md)

> A living one-stop shop for the latest model releases, with the newest update pinned at the top and older snapshots moved downward into a chronological record.

## Semantic links
- [LLM Release Tracker Archive](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/2026-07-10_LLMReleaseTracker-archive.md) — 3 title terms overlap, shared tags: evolution, llmmodels
- [LLM Model Evolution](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/2026-06-10_LLMModelEvolution.md) — 1 title term overlap, shared tags: evolution, llmmodels
- [LLM Models Hub](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/llm-models-hub.md) — 1 title term overlap, shared tags: llmmodels

## How this page works

This page is designed as an **update-first tracker**:

1. The **Current Snapshot** at the top always reflects the latest available information.
2. When new model news arrives, update the snapshot in place.
3. Move the previous snapshot into the **Chronological Release Log** below.
4. Keep the record cumulative so the page becomes a history of model-release momentum, not just a static list.

## Current Snapshot

**Last reviewed**: 2026-11-12

### Current release verdict

This section is the living summary. Keep it short, opinionated, and current. When a new release lands, replace these bullets with the newest interpretation and move the older interpretation into the log below.

| Model | Current role | Signal |
|---|---|---|
| **Gemini 4 Hydrogen** | Closed-weight fast execution model for everyday coding, debugging, agent workflows, and Google Search | Google reports 57% on Terminal-Bench 4.1 vs. 18.2% for Gemini 3.8 Flash; 1M context; API pricing $1.50/M input and $7.50/M output. Orchestrator's Terminal-Bench 4.0 result is near-Carbon success at 24% less quota and 19% faster; all results are company-reported |
| **BotPsy-0.8B** | Open-weight, on-device tool-use model for low- to medium-difficulty personal workflows | Tether reports it beats tested ≤1.2B peers across six benchmarks and tops its broader comparison set on five of six; Apache-2.0 weights are available on Hugging Face |
| **Qwen4-Max Preview** | Alibaba-hosted multimodal frontier preview for coding and agent work | Preview opened at 20:00 CST Nov 10 via Token Plan and named Qwen products; no open weights or official benchmark results announced |
| **Gemini 4 Carbon** | Google’s broader-availability model for long-horizon engineering, cybersecurity, and scientific reasoning | General availability announced Nov 10; company reports benchmark leadership on selected tasks; API introductory pricing runs through Nov 30 |
| **Claude Fable 5.2** | Anthropic's broadly available model for difficult technical work | Anthropic reports up to 30% faster output than Fable 5.1; $8/M input, $40/M output |
| **Claude Mythos 5.2** | Restricted high-capability sibling for approved cybersecurity and biomedical work | Same underlying model as Fable 5.2; access through Anthropic verification programs |
| **Meta Muse Ember** | Lower-cost model for repeated agent execution, tool calls, and coding subtasks | 1M-token context; $0.10/M input, $0.50/M output; Meta reports 37.8% on AutomationBench-AA |
| **Meituan LongCat-2.5** | Open-weight, native multimodal heavyweight for long-horizon agent tasks | Weights released Nov 9 under MIT; 1.6T total / ~48B active per Meituan; Hugging Face marks custom code and the documented NPU path uses SGLang-FluentLLM |
| **ByteDance Seedream 5.5** | Visual creation and iterative image editing | Nov 9 platform rollout; ByteDance claims stable edits across 100 rounds and native RGBA; release post does not state weights, license, or architecture |
| **Inkling 2 Small** | Closed-weight Tinker release pending external safety testing | Announced Nov 5; Thinking Machines says Apache 2.0 weights will follow after external red-teaming; do not count the promised checkpoint as open weights yet |
| **GPT-5.5** | Safest all-around agentic and multimodal default | 1M context, broad tool ecosystem, reliable across task types |
| **Claude Opus 4.7** | Best for code review and repository reasoning | 87.6% SWE-Bench Verified, strongest engineering signal |
| **Gemini 3.5 Flash** | Best speed-first frontier option | Roughly 4x faster than Gemini 3.1 Pro, strong multimodal throughput |
| **DeepSeek V4 Pro** | Best value pick for coding and agentic tasks | MIT-licensed, very low API pricing, open-weight availability |
| **Qwen 3.7 Max** | Strong open-hosted option for agentic coding | Large context window and competitive benchmark claims |
| **Llama 4 Scout** | Best long-context self-hosting candidate | 10M context, open weights, privacy-friendly deployment |
| **Kimi K3** | Frontier open-weight pressure test | 1M context, agentic coding focus, huge open-weight scale |
| **Inkling** | Broad open-weights generalist | Multimodal, customizable, and positioned as a practical foundation model |
| **IFM K2 Horizon** | Fully open model fleet from edge to enterprise | Six sizes from 0.9B to 375B; weights, code, training data, and methods released together |

### Current read

- **Frontier capability now has distinct access tiers.** Anthropic says Fable 5.2 is broadly available while Mythos 5.2 is gated through cybersecurity and life-sciences verification programs.
- **Agent execution has a dedicated low-cost tier.** Meta positions Muse Ember for repeated tool calls, coding subtasks, routing, and document work rather than as a general replacement for its highest-capability model.
- **Benchmark comparisons are workload-specific.** Vendor and benchmark-publisher results should be tested against the buyer's own harness, tools, and success criteria.
- **The latest confirmed model releases span distinct deployment tiers.** BotPsy adds an open, sub-billion-parameter local-agent candidate; Qwen4-Max is a time-limited hosted preview rather than a weight release; Gemini 4 Carbon widened from limited cyber-defender access to broader paid developer, enterprise, scientist, and consumer access on Nov 10.
- **Gemini 4 Hydrogen adds a fast closed-model tier on Nov 12.** Google positions it for execution and Search, with Orchestrator routing work between Hydrogen and Carbon; pricing and performance should be benchmarked on equal-success production tasks.

### Open questions / contradictions

- **Claude Opus 4.7 context size is source-dependent.** One roundup reports 200K context, while the later comparison article describes 1M context. Treat the exact figure as source-sensitive until upstream docs converge.
- **Seedream architecture and openness are not established by the launch post.** Do not classify it as a diffusion architecture or open-weight release without a first-party model card or license.
- **No November 9 diffusion-language checkpoint was confirmed** in the targeted official-source check. Google's Gemini Diffusion remains described as an experimental demo, not a new dated release.

## Chronological Release Log

### 2026-11-12 - Gemini 4 Hydrogen targets fast execution

- **Source**: [Google — Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Google Search rollout](https://blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade/)
- **Model**: Gemini 4 Hydrogen
- **Availability**: Google says it is available through Google AI Studio, Gemini API, Gemini for business, Gemini app, Search, and paid Google AI Pro/Ultra access in Antigravity. Its stated context window is 1 million tokens; API pricing is $1.50/M input and $7.50/M output.
- **Why it matters**: This is a fast coding/agent execution tier rather than a replacement for Google's deeper-reasoning Carbon and Argon models. Google reports 57% on Terminal-Bench 4.1 versus 18.2% for Gemini 3.8 Flash. Its Antigravity Orchestrator reportedly approaches Carbon task success on Terminal-Bench 4.0 with 24% less quota and 19% faster completion.
- **Claims and follow-up**: Results and performance comparisons are from Google and use different benchmark versions. Verify independent task success, failure recovery, latency, and cost; test Search answer quality and link discovery separately.

### 2026-11-11 - BotPsy targets on-device tool use

- **Source**: [Tether AI Research on Hugging Face](https://huggingface.co/blog/qvac/botpsy) · [QVAC release note](https://qvac.tether.io/blog/on-device-ai-agent-botpsy) · [BotPsy-0.8B weights](https://huggingface.co/qvac/BotPsy-0.8B)
- **Model**: BotPsy-0.8B, based on Qwen3.5-0.8B
- **Availability**: Hugging Face lists Apache-2.0 weights, with safetensors and GGUF variants; the publisher frames use for research and education.
- **Why it matters**: The model targets device-resident tool use rather than frontier chat. Tether reports roughly doubled scores over its base on several tests, beats the tested ≤1.2B peers on all six benchmarks, and tops its broader comparison set on five of six.
- **Claims and follow-up**: Results are publisher-reported. The article identifies multi-step information retrieval, accumulated instructions, lower-resource languages, and high-stakes use as limitations; verify license scope and runtime behavior before deployment.

### 2026-11-10 - Qwen4-Max opens a hosted preview

- **Source**: [Alibaba Qwen announcement](https://x.com/Alibaba_Qwen/status/2120335993643684315) · [Alibaba Cloud Model Studio documentation](https://www.alibabacloud.com/help/en/model-studio/qwen4-max-preview)
- **Model**: Qwen4-Max Preview (`qwen4-max-preview`)
- **Availability**: The official post was timestamped 2026-11-11 02:01 UTC (2026-11-10 20:01 CST); documentation sets the preview start at 10:00 China time, also 20:00 CST on November 10. Access is through Token Plan and named Alibaba applications; the preview is scheduled to end November 25 China time.
- **Why it matters**: This is the first Qwen4 model available to try, but it is a hosted preview, not an open-weight release. Documentation describes text, image and video input and a 1M-token context.
- **Follow-up**: No official benchmark results or downloadable Qwen4 weights were announced with this preview; verify whether a durable general-availability offering follows.

### 2026-11-10 - Gemini 4 Carbon expands to broader access

- **Source**: [Google — Gemini 4 Carbon is now available](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) · [Developer availability](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-4-carbon-developers/)
- **Model**: Gemini 4 Carbon
- **Availability**: Google announced access for paid Gemini API developers and enterprises, scientists, and eligible Google AI Ultra users across its listed surfaces; this broadens the earlier Fairwind cyber-defender rollout.
- **Why it matters**: The update shifts the model from a restricted defender preview into broader paid access, while maintaining differentiated access by product and subscription.
- **Claims and follow-up**: Google’s selected benchmark and cost-per-task results are company-reported; compare against the buyer’s own agent harness and verified task success. Introductory API pricing is stated to run through November 30, 2026.

### 2026-11-09 - closed model tiers, open heavyweight weights, and visual creation

- **Source**: [Anthropic — Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [Meta AI Research — Muse Ember](https://research.meta.ai/blog/muse-ember) · [Meituan LongCat weights post](https://x.com/Meituan_LongCat/status/2119793531393040462) · [LongCat-2.5 model card](https://huggingface.co/meituan-longcat/LongCat-2.5) · [ByteDance Seedream 5.5](https://seed.bytedance.com/en/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5)
- **Models**: Claude Fable 5.2, Claude Mythos 5.2, Meta Muse Ember, Meituan LongCat-2.5 weights, ByteDance Seedream 5.5
- **Why it matters**: The day spans restricted/broad frontier access, low-cost hosted agent execution, an MIT-licensed open heavyweight, and a commercial visual-creation model.
- **Current take**: Compare by workflow and access tier, not one benchmark order. LongCat is open-weight but cluster-scale and custom-stack-oriented; Seedream's architecture and license remain unstated in its launch post.
- **Follow-up**: Reproduce capability and cost claims, test LongCat serving/custom-code requirements, verify Seedream's availability and license, and track Inkling 2 Small's weights only after its promised external testing is complete.

### Log format

Use one dated block per release wave. If multiple articles land on the same day, append another bullet under the same date instead of creating a new shape.

```md
### YYYY-MM-DD - {release wave label}

- **Source**: [Publisher](https://example.com/source)
- **Models**: model A, model B, model C
- **Why it matters**: one or two lines on the practical impact
- **Current take**: how the snapshot above should change
- **Follow-up**: any contradiction, pricing change, or open question
```

### 2026-07-10 - Latest comparison snapshot

- **Source**: [AI/ML API Blog comparison](https://aimlapi.com/blog/top-llm-models-in-2026-the-best-ai-models-for-reasoning-coding-multimodal-tasks)
- **Models**: GPT-5.5, Claude Opus 4.7, Gemini 3.5 Flash, DeepSeek V4 Pro, DeepSeek V4 Flash, Qwen 3.7 Max, Llama 4 Scout, Llama 4 Maverick
- **Why it matters**: it splits the market into safe generalists, repo-reasoners, speed-first models, value coding models, and self-hosting picks.
- **Current take**: GPT-5.5 stays the safest all-around agentic default; Claude Opus 4.7 stays the best for code review; Gemini 3.5 Flash wins on throughput.
- **Follow-up**: Open-weight models now belong in the main shortlist, not a separate "interesting" bucket.

### 2026-09-03 - IFM K2 Horizon fully open fleet

- **Source**: [IFM K2 Horizon press release](https://ifm.ai/k2/press-release) · [MBZUAI announcement](https://mbzuai.ac.ae/news/mbzuais-institute-of-foundation-models-launches-k2-horizon-the-worlds-largest-fully-open-ai-models-in-history/)
- **Models**: K2 Horizon 0.9B, 3.7B, 7B, 32B, MoVA 36B-A4B, and 375B-A23B
- **Why it matters**: IFM released weights, code, training data, methodologies, and deployment tooling across a single fleet, extending open model transparency beyond weights-only releases.
- **Current take**: The 32B and MoVA 36B-A4B variants belong in the practical local and on-premise shortlist; the 375B flagship is an enterprise-scale open-weight pressure test.
- **Follow-up**: Verify independent benchmarks, quantized checkpoints, and actual local throughput before ranking K2 Horizon against Qwen, Gemma, or MuseGlimmer.

### 2026-06-11 - Spring 2026 release wave

- **Source**: [Fazm roundup](https://fazm.ai/blog/new-llm-releases-april-2026)
- **Models**: GPT-5.5, Claude Opus 4.7, Gemma 4, GLM-5.1, Qwen 3.6-Plus, Llama 4 Scout, Llama 4 Maverick, Arcee Trinity
- **Why it matters**: the April wave showed that frontier APIs and open-weight releases were both moving fast.
- **Current take**: the top of the market is a two-horse race, while open models are good enough for serious self-hosted use.
- **Follow-up**: preserve this entry as the historical baseline; don't rewrite it when newer models ship.

### 2026-06-10 - Baseline model-evolution snapshot

- **Source**: [LLM Model Evolution](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/2026-06-10_LLMModelEvolution.md)
- **Models**: Llama 4 Scout, Gemma 4, Mistral Small 3.1, Phi-4 Mini, DiffusionGemma 26B-A4B-it, Harness-1
- **Why it matters**: this page started as the broader evolution view for model capabilities, benchmarks, and release dates.
- **Current take**: keep this older concept page as the background layer; the tracker should carry the newest release wave.
- **Follow-up**: if the tracker becomes too long, move older dated blocks into an archive page instead of deleting them.

## Practical shortlist

- **Need difficult technical work with broad availability**: evaluate Claude Fable 5.2 against task-specific alternatives; Anthropic reports 30% faster output than 5.1.
- **Need approved cyber or biomedical research access**: Claude Mythos 5.2 is gated through Anthropic's verification programs.
- **Need low-cost repeated agent steps**: evaluate Meta Muse Ember for tool calls, routing, coding subtasks, and large-document work.
- **Need open weights or self-hosting**: compare the [open-model shortlist](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/OpenSourceModelsStateOfTheArt.md), including BotPsy for small local-agent workflows and LongCat-2.5 for cluster-scale multimodal use; verify each model’s license and serving requirements.
- **Before switching**: measure end-to-end task success, latency, token cost, permissions, and recoverability in the production harness.

## Update protocol

When a new model release lands:

1. Update the **Current release verdict** bullets first.
2. Prepend a new dated block under **Chronological Release Log**.
3. Keep older dated blocks below the newest block, unchanged unless a source correction is needed.
4. Use the fixed log template above so appending a new article is mostly copy, paste, and replace.
5. If the log gets too long, archive old dated blocks into a sibling page and link to it from here.

## Automation helper

Use the small generator script when you have a new article file or URL:

```bash
python3 tools/llm_release_block.py path/to/new-article.md --summary path/to/summary.md
python3 tools/llm_release_block.py https://example.com/new-model-article
python3 tools/append_latest_llm_release.py
```

The last command does the full loop: it finds the newest model article, generates the dated block, and inserts it at the top of the tracker log. The other two commands are still useful when you want to target a specific article manually.

## Append-only helper

Copy this block when adding the next release wave:

```md
### YYYY-MM-DD - {release wave label}

- **Source**: [Publisher](https://example.com/source)
- **Models**: model A, model B, model C
- **Why it matters**: 
- **Current take**: 
- **Follow-up**: 
```

## Source pages to watch

- [LLM Model Evolution](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/2026-06-10_LLMModelEvolution.md)
- [Harness-1](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/2026-06-10_Harness1.md)
- [Best LLM Models 2026 Compared: Reasoning, Coding, Multimodal & Price](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/entities/article/2026-07-10_BestLLMModels2026Compared_Reasoning_Coding_Multimo_summary.md)
- [New LLM Releases April 2026: Every Major Model Launch This Month](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/entities/article/2026-06-11_NewLLMReleasesApril2026_EveryMajorModelLaunchThisM_summary.md)
- [LLM Release Tracker archive](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/2026-07-10_LLMReleaseTracker-archive.md)

## Related navigation

- [AI Research Wiki — Topic Index](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/wiki-topic-index.md)
