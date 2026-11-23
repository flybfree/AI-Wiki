---
title: "LLM Release Tracker"
date: 2026-07-10
type: concept
tags: [llm-models, evolution, tracking]
---

# LLM Release Tracker

**Source**: [Sarvam-105B-1711 release](https://www.sarvam.ai/blogs/sarvam-105b-1711) · [AI/ML API comparison article](https://aimlapi.com/blog/top-llm-models-in-2026-the-best-ai-models-for-reasoning-coding-multimodal-tasks) · [Fazm April releases roundup](https://fazm.ai/blog/new-llm-releases-april-2026) · [LLM Model Evolution](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/2026-06-10_LLMModelEvolution.md)

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

**Last reviewed**: 2026-11-22

### Current release verdict

This section is the living summary. Keep it short, opinionated, and current. When a new release lands, replace these bullets with the newest interpretation and move the older interpretation into the log below.

| Model | Current role | Signal |
|---|---|---|
| [**Sarvam-105B-1711**](https://huggingface.co/sarvamai/sarvam-105b-1711) | Apache-2.0 open-weight checkpoint of Sarvam’s existing 105B model for enterprise agents, voice, and Indic-language workloads | Announced Nov 22; 10.3B active, 160K context, 65GB NVFP4 checkpoint for a workstation-class GPU. Sarvam reports a 73.9 eight-benchmark average at $0.15/M blended; all comparisons are publisher-run |
| **Gemini 4 Neon** | Closed-weight mid-tier frontier model for complex coding, knowledge work, science, and higher-frequency agent workflows | Google reports a 1M-token context, API pricing of $3/M input and $15/M output ($0.15/M cached), and #3 on Artificial Analysis Intelligence Index at xhigh; benchmarks and rollout are publisher-reported |
| **GPT-6.2 Astra** | Frontier model for demanding professional, scientific, and long-horizon work | OpenAI says API input/output prices are 20% below GPT-6 Astra ($8/$40 per million; $0.40 cached input); first externally released model at OpenAI's High AI self-improvement threshold; company benchmarks and risk ratings require independent evaluation |
| **GPT-6.2 Sol** | Efficient everyday and multi-step agent model | OpenAI says it is available in ChatGPT Work, Codex, and API; it keeps GPT-6.1 Sol's stated rates ($2/$10 per million; $0.10 cached input); not an open-weight release |
| **Microsoft MAI Ignite 2026 wave** | Seven announced in-house models spanning coding, cybersecurity, image, real-time, transcription, and decision workloads | Includes MAI Code 2/Code 2 Flash and MAI Cyber 2 Flash; Microsoft reports benchmark and cost comparisons, not independent results; no downloadable model weights verified |
| **Gemini 4 Hydrogen** | Closed-weight fast execution model for everyday coding, debugging, agent workflows, and Google Search | Google reports 57% on Terminal-Bench 4.1 vs. 18.2% for Gemini 3.8 Flash; 1M context; API pricing $1.50/M input and $7.50/M output. Orchestrator's Terminal-Bench 4.0 result is near-Carbon success at 24% less quota and 19% faster; all results are company-reported |
| **Perplexity Decider v1.3 / Decider Flash v1.3** | Open-weight typed decision models for classification, routing, scoring, and evidence-span location | Perplexity says both are downloadable on Hugging Face under Apache terms; v1.3 adds `locate`. Bidirectional attention and evaluation results are publisher-described; not general-purpose chat models |
| **SpeakLeash Bielik-One** | Four open-weight 4B–11B decision models returning structured probabilities | Nov 12 family launch; Apache-2.0 model cards and merged-weight/adapter options verified on Hugging Face; specialized decision models, not standard chat assistants |
| **BotPsy-0.8B** | Open-weight, on-device tool-use model for low- to medium-difficulty personal workflows | Tether reports it beats tested ≤1.2B peers across six benchmarks and tops its broader comparison set on five of six; Apache-2.0 weights are available on Hugging Face |
| **Qwen4-Max** | Alibaba-hosted multimodal flagship for coding, professional work, reasoning, and agent tasks | QwenCloud’s model-release record dates the hosted `qwen4-max` listing to Nov 16 after the Nov 11 Token Plan preview; 1M context and native vision; no downloadable Qwen4-Max weights verified |
| [**Tencent Hy4 flash**](https://huggingface.co/tencent/Hy4-flash) | Open-weight, 224B total / 12B active multimodal MoE for cost-sensitive agent and office workflows | Weights appeared Nov 17 CST under Tencent Hy License 1.0; the hosted model launched Nov 16 and supports 1M context. Check the license’s commercial-service terms before hosting |
| [**Tencent Hy4 full weights**](https://huggingface.co/tencent/Hy4) | Open-heavyweight multimodal checkpoint for server-scale use | Weights for Hy4, Hy4-FP8, and Hy4 base were posted at 03:52 UTC Nov 20 (21:52 CST Nov 19) under Tencent Hy License 1.0, not Apache 2.0. The card lists 770B backbone / 49B active text parameters and 1M context; qualifying large MaaS providers need separate written terms |
| [**Inkling 2 Mini**](https://thinkingmachines.ai/model-card/inkling-2-mini/) | Apache-2.0 open-weight multimodal local model | Released Nov 20; 26.4B total, 3.4B unique active and 5.4B effective active with loops; 1M context and roughly 20GB checkpoint. Thinking Machines' model card and benchmark claims are publisher evidence |
| [**Ayb 0.5**](https://huggingface.co/blog/Metric-AI/ayb-05-intro) | Armenian-language open-weight model family | Metric AI Lab lists 0.8B, 4B, and 9B variants released Nov 20; the Ayb-0.5-9B card uses CC BY-NC 4.0, so do not treat it as unrestricted commercial weights |
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
- **Gemini 4 Neon remains the newest verified closed-frontier release (Nov 18); Sarvam-105B-1711 is the newest target-day open-weight checkpoint (Nov 22).** Sarvam updates an existing 105B model with agent, instruction-following, and Indic-language post-training; its price/performance claims are publisher-reported. Inkling 2 Mini and Ayb 0.5 remain Nov 20 releases, and Tencent Hy4 full weights arrived late Nov 19 CST under a custom license.
- **GPT-6.2 Astra/Sol and Microsoft's seven-model Ignite wave remain the prior day's closed/hosted launches.** No same-day downloadable open-weight checkpoint and license were verified on Nov 18; do not count an API or product feature as an open-weight release.
- **Qwen4-Max and Tencent Hy4 flash were hosted releases on Nov 16.** Tencent published Hy4 flash weights on Nov 17 CST under Tencent Hy License 1.0; the later full Hy4 weights release is tracked below as a Nov 19 CST event.
- **Hy4 flash moved from hosted launch to downloadable weights on Nov 17 CST.** Tencent's 224B total / 12B active multimodal checkpoint uses the Tencent Hy License 1.0; its full 770B Hy4 weights followed late Nov 19 CST.
- **Inkling 2 Mini and Ayb 0.5 add two different open-weight options on Nov 20.** Inkling is an Apache-2.0 looped multimodal model with a roughly 20GB checkpoint; Ayb 0.5 targets Armenian and English, with CC BY-NC 4.0 terms listed for its 9B model card. Keep vendor benchmarks attributed and check the exact Ayb checkpoint license.
- **Tencent Hy4 weights appeared late Nov 19 CST, not Nov 20 CST.** The 770B multimodal model is downloadable under Tencent Hy License 1.0, which adds terms for large model-as-a-service providers; do not label it Apache 2.0 or count it as a Nov 20 local-day release.
- **No Nov 20 closed-frontier general model release was verified.** The API changelog dates GPT-Live-1.1 to Nov 19, and model catalogs that list Pixtral Large 2502 on Nov 20 reflect a router listing of Mistral's older, deprecated model rather than a new Mistral launch.
- **Gemini 4 Hydrogen adds a fast closed-model tier on Nov 12.** Google positions it for execution and Search, with Orchestrator routing work between Hydrogen and Carbon; pricing and performance should be benchmarked on equal-success production tasks.
- **Typed decision models are a distinct open-weight track.** Perplexity Decider v1.3/Flash v1.3 and SpeakLeash Bielik-One target calibrated choices and extraction rather than free-form chat; test calibration, abstention, and workload fit before using outputs to trigger actions.

### Open questions / contradictions

- **Claude Opus 4.7 context size is source-dependent.** One roundup reports 200K context, while the later comparison article describes 1M context. Treat the exact figure as source-sensitive until upstream docs converge.
- **Seedream architecture and openness are not established by the launch post.** Do not classify it as a diffusion architecture or open-weight release without a first-party model card or license.
- **No November 9 diffusion-language checkpoint was confirmed** in the targeted official-source check. Google's Gemini Diffusion remains described as an experimental demo, not a new dated release.

## Chronological Release Log

### 2026-11-22 - Sarvam-105B-1711 open-weight checkpoint

- **Sources**: [Sarvam announcement](https://www.sarvam.ai/blogs/sarvam-105b-1711) · [NVFP4 model card](https://huggingface.co/sarvamai/sarvam-105b-1711) · [BF16 weights](https://huggingface.co/sarvamai/sarvam-105b-1711-bf16)
- **Model**: New checkpoint/post-training of the existing 105B mixture-of-experts model; the card lists 10.3B active parameters. It targets tool use, instruction following, enterprise agents, voice, and Indian languages.
- **Availability and license**: Apache-2.0 weights are on Hugging Face; BF16 and 65GB NVFP4 versions are available. Sarvam reports a 160K context and on-premises use on one workstation-class GPU.
- **Claims and follow-up**: Sarvam reports 73.9 average across eight conversational-agent tests at $0.15/M blended pricing, but its comparisons are publisher-run. Independently evaluate the exact model, price mix, language set, runtime, hardware memory, and end-to-end agent success before ranking it against closed or open peers.

### 2026-11-20 - open-weight local releases; Tencent Hy4 date-qualified

- **Sources**: [Thinking Machines — Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/) · [Inkling 2 Mini model card](https://thinkingmachines.ai/model-card/inkling-2-mini/) · [Metric AI Lab — Ayb 0.5](https://huggingface.co/blog/Metric-AI/ayb-05-intro) · [Ayb-0.5-9B model card](https://huggingface.co/Metric-AI/Ayb-0.5-9B) · [Tencent Hy4 weights](https://huggingface.co/tencent/Hy4)
- **Models**: Inkling 2 Mini (26.4B total / 3.4B unique active, Apache 2.0) and Ayb 0.5 (0.8B/4B/9B Armenian-English family; CC BY-NC 4.0 listed for the 9B card). Tencent Hy4 weights were posted at 03:52 UTC Nov 20, which is 21:52 CST Nov 19; they are adjacent-day context, under Tencent Hy License 1.0 rather than Apache 2.0.
- **Why it matters**: Open-weight access spans a local multimodal model, language-specific checkpoints, and a cluster-scale flagship with commercial-service thresholds. These are different deployment and licensing choices, not one “open” tier.
- **Current take / follow-up**: Benchmark claims remain publisher-reported. Verify local runtime support, memory, per-checkpoint licenses, and Tencent's Section 10 requirements before deployment; no new Nov 20 closed-frontier release or diffusion language model was verified.

### 2026-11-18 - Google Gemini 4 Neon

- **Source**: [Google — Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) · [Gemini 4 Neon model card](https://deepmind.google/models/model-cards/gemini-4-neon/)
- **Model**: Gemini 4 Neon, a closed/hosted model for complex software engineering, knowledge work, science, and production-grade agent workflows.
- **Availability and pricing**: Google announced rollout on Nov 18 through the Gemini API/AI Studio, Gemini for business, Antigravity, and Gemini app for eligible paid tiers. Google lists a 1M-token context and API pricing of $3/M input, $0.15/M cached input, and $15/M output.
- **Claims**: Google reports 61 and #3 on the Artificial Analysis Intelligence Index at xhigh and strong results on selected agent, coding, and science tasks. Treat the vendor's benchmark selection and comparisons as claims pending matched independent evaluation.
- **Follow-up**: Compare Neon with Astra and other models using equal task success, latency, retries, review effort, and complete task cost. No downloadable weights or license were verified; keep it out of the open-weight inventory.

### 2026-11-17 - OpenAI GPT-6.2 Astra and Sol

- **Source**: [OpenAI release](https://openai.com/index/introducing-gpt-6-2-astra-sol) · [GPT-6.2 system card](https://deploymentsafety.openai.com/gpt-6-2-astra-sol)
- **Models**: GPT-6.2 Astra and GPT-6.2 Sol; OpenAI also announced the legal-work configuration Astra for Law.
- **Availability**: OpenAI says Astra and Sol are available through ChatGPT Work, Codex, and the API for eligible paid/enterprise/education access. Astra's stated API prices are $8/M input, $0.40/M cached input, and $40/M output; Sol carries GPT-6.1 Sol's $2/$0.10/$10 rates.
- **Why it matters**: OpenAI positions Astra for demanding professional/scientific tasks and Sol for efficient everyday and multi-step agent workflows. The company says Astra is its first externally released model at the High AI self-improvement threshold and that both models meet its Critical cybersecurity threshold.
- **Current take / follow-up**: Evaluate with matched harnesses, real task success, review effort, and full cost. Treat benchmarks and risk-control effectiveness as vendor-reported until independently replicated; test access gates, containment, and monitor performance.

### 2026-11-17 - Microsoft MAI model wave at Ignite

- **Source**: [Microsoft AI — seven new models](https://microsoft.ai/news/microsoft-ignite-2026/) · [MAI Code 2 and Code 2 Flash](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/)
- **Models**: Seven announced in-house models across coding, cybersecurity, image, real-time, transcription, and decision workloads, including MAI Code 2, MAI Code 2 Flash, and MAI Cyber 2 Flash.
- **Why it matters**: Microsoft is pitching narrower, lower-cost task models as alternatives to general frontier systems. Its coding quality and price comparisons are publisher-reported and should not be treated as independent benchmarks.
- **Current take / follow-up**: Keep this in the closed/hosted track; no public downloadable weights or license were verified. Test which models are actually available in the target service and compare end-to-end task costs.

### 2026-11-16 - Tencent Hy4 flash hosted release

- **Sources**: [Tencent announcement](https://www.tencent.com/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows) · [Tencent Cloud model details](https://cloud.tencent.com/tokenhub/hy4-flash-en)
- **Model**: Hy4 flash, a multimodal Tencent Hy model announced November 16, 2026.
- **Availability**: Tencent reports 224B total parameters (including 64B Engram parameters), 12B active parameters, multimodal inputs, and up to 1M context. It lists hosted API pricing and says it plans to open-source the model later. The checked release and model-detail pages did not provide downloadable weights, a public repository, or a license, so this is a hosted launch—not a verified open-weight release.
- **Why it matters**: The design targets lower-cost everyday agent and office workloads. Tencent reports the costs and performance comparisons; independent reproduction is not established by the announcement.
- **Follow-up**: Recheck for an official repository, model card, license, and downloadable checkpoints before moving Hy4 flash into the open-weight inventory.

### 2026-11-16 - Qwen4-Max hosted release

- **Sources**: [Alibaba Qwen — Qwen4-Max](https://qwen.ai/blog?id=qwen4-max) · [QwenCloud model-release record](https://docs.qwencloud.com/changelog/models?date=2026-11-16) · [QwenCloud latest-model documentation](https://docs.qwencloud.com/developer-guides/getting-started/latest-model?date=2026-11-16)
- **Model**: Qwen4-Max (`qwen4-max`), a hosted multimodal flagship for reasoning, coding, and agent tasks.
- **Availability**: The official model changelog dates the hosted `qwen4-max` listing to November 16. It follows the Token Plan-only `qwen4-max-preview` period that began November 11. Current documentation describes text, image, and video input, tool calling, and a one-million-token context. No public downloadable Qwen4-Max weights were verified; keep this release out of the open-weight count.
- **Why it matters**: This documents the dated hosted `qwen4-max` endpoint and resolves the official-date boundary noted in the November 15 local briefing. It is a closed-weight release, not evidence that the Qwen4 family’s promised smaller open models have shipped.
- **Follow-up**: Check regional API availability and pricing in the live QwenCloud console; track smaller Qwen4 models only after official weight repositories and licenses are published.

### 2026-11-12 - Gemini 4 Hydrogen targets fast execution

- **Source**: [Google — Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Google Search rollout](https://blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade/)
- **Model**: Gemini 4 Hydrogen
- **Availability**: Google says it is available through Google AI Studio, Gemini API, Gemini for business, Gemini app, Search, and paid Google AI Pro/Ultra access in Antigravity. Its stated context window is 1 million tokens; API pricing is $1.50/M input and $7.50/M output.
- **Why it matters**: This is a fast coding/agent execution tier rather than a replacement for Google's deeper-reasoning Carbon and Argon models. Google reports 57% on Terminal-Bench 4.1 versus 18.2% for Gemini 3.8 Flash. Its Antigravity Orchestrator reportedly approaches Carbon task success on Terminal-Bench 4.0 with 24% less quota and 19% faster completion.
- **Claims and follow-up**: Results and performance comparisons are from Google and use different benchmark versions. Verify independent task success, failure recovery, latency, and cost; test Search answer quality and link discovery separately.

### 2026-11-12 - open-weight typed decision models

- **Sources**: [Perplexity — Decider v1.3](https://www.perplexity.ai/hub/blog/perplexity-decider) · [SpeakLeash — Bielik-One launch schedule](https://www.bielik.ai/en/blog/launching-bielik-11b-v31-dflash-and-the-bielik-one-family) · [Bielik-One 11B v3.1-r1 card and weights](https://huggingface.co/speakleash/Bielik-One-11B-v3.1-r1)
- **Models**: Perplexity Decider v1.3 and Decider Flash v1.3; Bielik-One 4B, 7B, and 11B decision models.
- **Availability**: Perplexity says its weights are downloadable under Apache terms on Hugging Face and are also served through OpenRouter and the Decisions API. SpeakLeash scheduled Bielik-One for Nov 12; Hugging Face model cards list Apache-2.0 weights with merged and adapter options.
- **Why it matters**: These are typed decision components that return probabilities or located spans, making classification, routing, evaluation, and extraction first-class model workloads alongside text generation.
- **Claims and follow-up**: Perplexity's benchmark comparisons are publisher-reported. Evaluate calibration, abstention, false-positive/false-negative costs, model-card completeness, and the exact license/runtime for the selected checkpoint.

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
