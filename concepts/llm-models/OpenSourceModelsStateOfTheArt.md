---
title: "Open-Source Models State of the Art — 2026-09-16"
date: 2026-09-16
status: draft
tags: ["wiki", "open-source-models", "foundation-models", "state-of-the-art", "local-use", "gguf", "quantization", "2026-09-16"]
---

# Open-Source Models State of the Art — 2026-09-16

**Source**: [Original Article](https://github.com/flybfree/AI-Wiki/wiki)

This page tracks the current open-weight frontier and the models most relevant for local deployment. The recent signal splits into frontier generalists, local-use quantized checkpoints, and deployment infrastructure that determines whether open weights are usable in practice. The snapshot is refreshed through 2026-09-16.

## Semantic links
- [[concepts/2026-07-27_FoundationModelsStateOfTheArt.md|Foundation Models State of the Art — 2026-08-27]] — 5 title terms overlap, shared tags: foundationmodels, stateoftheart, wiki, 5 topic terms overlap
- [[concepts/2026-06-30_FoundationModelsStateOfTheArt.md|Foundation Models State of the Art — 2026-06-30]] — 5 title terms overlap, shared tags: foundationmodels, stateoftheart, wiki, 5 topic terms overlap
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 2 title terms overlap, 2 topic terms overlap, same area: home

## Snapshot

Open-source model progress now splits into two tracks:

- frontier open-weight generalists
- local-first quantized and fine-tuned models

The practical question is no longer just “what is the strongest open model?” It is also “what model can I run locally, tune for my tasks, and keep updated as the ecosystem moves?”

## Qwen3.8-27B spotlight

[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) is Alibaba's 27B dense, open-weight vision-language model, released under Apache 2.0.[1] It accepts text, images, and video, and targets coding, professional work, research, and long-horizon agent tasks.[1] Its native context window is 262,144 tokens, extendable to 1M with YaRN; the checkpoint also uses multi-token prediction (MTP) and a hybrid layout combining gated DeltaNet linear-attention blocks with gated attention.[1]

The model's practical differentiator is controllable reasoning rather than a separate reasoning checkpoint: thinking is enabled by default, can be disabled, and exposes `reasoning_effort` levels of `xhigh`, `medium`, and `low`.[1] This is useful for agent loops, but the default is not ideal for interactive local use. Simon Willison's independent hands-on report found that the default `xhigh` setting can spend tens of thousands of tokens and turn simple tasks into multi-minute jobs; he recommends starting with low or no reasoning on consumer hardware.[2]

Qwen reports strong results on coding and computer-use evaluations, including 73.0 on Terminal-Bench 2.1, 61.7 on SWE-bench Pro, 84.3 on OSWorld-Verified, and 81.9 on AndroidWorld. These are vendor-reported results using different harnesses and should be treated as directional rather than directly comparable across model cards.[1] The local trade-off is compelling but not free: a Q4_K_M build is about 17 GB, while dense-model memory bandwidth and long reasoning traces can make inference feel slow even when the model fits.[2]

**Best fit:** a local multimodal coding and agent model when Apache licensing, long context, image/video input, and controllable reasoning matter. **Main caveat:** configure context length and reasoning effort explicitly; otherwise local latency and token usage can overwhelm the benefit of the compact 27B footprint.

## Ornith-1.5 spotlight

[Ornith-1.5](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) is a family of open-weight models from Ornith AI focused on coding agents and end-to-end self-improvement.[3] Its training loop jointly improves task generation, scaffold construction, and solution rollouts instead of treating the task set and agent harness as fixed; the model therefore learns both how to solve tasks and how to search for solutions more effectively.[3]

The family spans a 9B dense model, a 35B-A3B mixture-of-experts (MoE) model that activates about 3B parameters per token, and a 397B MoE flagship.[3][4] The 35B-A3B checkpoint is the practical local option: Ornith reports 67.8 on Terminal-Bench 2.1 with Terminus-2, 68.5 with Claude Code, 79 on SWE-bench Verified, and 59.6 on SWE-bench Pro.[3] The flagship reports 86.1 on Terminal-Bench 2.1 and 86 on SWE-bench Verified, but its roughly 800 GB BF16 footprint requires multi-GPU serving.[4]

The results are promising but should be read as model-card claims: Ornith says its results are averaged over five runs, while the benchmarks use different harnesses, context windows, timeouts, and judge models.[3][4] An independent overview describes Ornith-1.5-35B-A3B as a strong coding-agent model, but also recommends starting below the full 262K context on constrained hardware and increasing it only when the workload needs it.[5]

**Best fit:** repository-level coding, terminal automation, and tool-using agents where scaffold quality and long-horizon execution matter. **Main caveat:** the 35B-A3B model is much more local-friendly than the 397B flagship, but neither should be treated as a general multimodal replacement for Qwen3.8; Ornith-1.5's center of gravity is agentic software work.

## Frontier open-weight generalists

| Model | Why it matters | Main caveat |
|---|---|---|
| [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Compact dense multimodal model with long context, controllable reasoning, and strong coding/agent results | Vendor-reported benchmarks; dense local inference can be bandwidth- and latency-bound |
| [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | Balanced multimodal + agentic coding model with a strong open-weight footprint | Heavier deployment than compact local specialists |
| [Gemma 4 26B A4B](https://huggingface.co/google/gemma-4-26B-A4B-it) | Strong open-weight multimodal generalist | Bigger memory footprint than smaller variants |
| [Gemma 4 12B Unified](https://huggingface.co/google/gemma-4-12B) | Best compact multimodal generalist in the Gemma 4 family | Less raw capacity than the 26B MoE model |
| [Kimi K3](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart) | Frontier open-weight model with huge context and agentic coding focus | More of a frontier pressure test than a lightweight local model |
| [Inkling-Small](https://thinkingmachines.ai/news/inkling-small/) | Open-weights MoE with 276B total parameters, 12B active, 1M-token context, and variable thinking effort | Still large and customization-oriented rather than compact |
| [MuseGlimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) | Apache 2.0 30B model optimized for always-on local agents, tool use, coding, multimodal input, and failure recovery | Requires roughly 17–20 GB for the quantized model plus runtime headroom |
| [IFM K2 Horizon](https://ifm.ai/k2/press-release) | Fully open fleet spanning 0.9B to 375B, with weights, code, training data, and methods; includes local-use 32B and 36B-A4B variants | Performance claims are new and largely vendor-reported; the 375B flagship is not consumer-local |
| [Nemotron 3.5 Lightning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/) | Open 30B MoE with 3B active parameters, optimized for fast, high-volume execution inside long-running agents | Execution specialist rather than a broad frontier generalist; benchmark and serving results are NVIDIA-reported |
| [GLM-5.3-Flash](https://huggingface.co/docs/transformers/main/en/model_doc/glm5_next) | Native multimodal 320B MoE with 18B active parameters, hybrid sparse/linear attention, and 1M context | Very large total footprint; official capability claims need independent benchmarking |
| [Qwen4-Exp](https://huggingface.co/docs/transformers/main/en/model_doc/qwen4_exp) | Qwen3.5-derived hybrid model combining gated residual streams, sparse attention, and per-layer embeddings for long-context efficiency | Experimental release; public evidence is currently stronger on architecture than end-user benchmark coverage |
| [Step-3.7-Flash](https://static.stepfun.com/blog/step-3.7-flash/) | 198B sparse MoE vision-language model with native image understanding and multi-token prediction support | Large serving requirement and limited public technical-report detail |
| [Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) | Self-improving coding-agent MoE with about 3B active parameters and strong repository-level results | Coding-focused; reported scores depend on harness and evaluation protocol |
| [Ornith-1.5-397B](https://huggingface.co/ornith-ai/Ornith-1.5-397B) | Flagship self-improving MoE with frontier-level reported coding and agentic scores | Approximately 800 GB in BF16; multi-GPU serving required |
| [Ornith-1.5-9B](https://huggingface.co/ornith-ai/Ornith-1.5-9B) | Smaller dense member for lower-resource coding-agent experiments | Less capacity than the 35B-A3B and 397B variants |
| [Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B) | Purpose-built for agentic coding and repository-level automation | Focused more on coding than broad multimodal use |
| [Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M) | Compact long-context reasoning model built from Claude Mythos / Fable traces | Derived model, not a broad frontier multimodal system |
| [VibeThinker-1.5B](https://huggingface.co/WeiboAI/VibeThinker-1.5B) | Tiny-model math and coding specialist | Experimental and not a general assistant |

### What to watch

- whether open-weight multimodal models keep closing the gap with proprietary frontier systems
- whether agentic coding models keep improving on terminal-heavy and repo-level tasks
- whether long-context compact models remain useful once real tool use and retrieval are layered in
- whether hybrid sparse/linear attention and multi-token prediction translate into repeatable serving gains outside vendor demos
- whether model-hub support arrives quickly enough for new releases to become reproducible local workflows

## Local-use quantized and fine-tuned models

This subsection is for models that matter because they can actually be run, tuned, or adapted locally.

### Current local-use watchlist

| Model / derivative | Local form | Why it matters |
|---|---|---|
| [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Official Transformers checkpoint; [Unsloth GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF) and local runtimes | A 27B Apache-licensed multimodal model that fits in roughly 17 GB at Q4_K_M and can serve local coding/agent workloads |
| [Qwen 3.6 27B GGUF release](../entities/article/2026-04-26_Qwen_3_6_27B_Arrives_with_GGUF_Support_and_Local_M_summary.md) | GGUF + 4-bit quantization | Shows how a flagship open-weight model becomes practical on consumer hardware |
| [Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M) | Dense 9B with 1M context | Very strong candidate for local long-context reasoning and tool use |
| [Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) | MoE checkpoint; about 3B active parameters; Transformers/vLLM/SGLang support | Strong local coding-agent candidate, but start with a smaller context on constrained hardware |
| [Ornith-1.5-9B](https://huggingface.co/ornith-ai/Ornith-1.5-9B) | Dense checkpoint with local/mobile-oriented variants | Lower resource requirement, lower ceiling |
| [Ornith-1.5-397B](https://huggingface.co/ornith-ai/Ornith-1.5-397B) | Multi-GPU MoE serving; FP8/INT4 options | Not a consumer-local model despite sparse activation |
| [Ornith-1.0 family](https://huggingface.co/collections/deepreinforce-ai/ornith-10) | Dense / MoE checkpoints for local deployment | Designed for agentic coding and self-scaffolding workflows |
| [VibeThinker-1.5B](https://huggingface.co/WeiboAI/VibeThinker-1.5B) | Tiny dense checkpoint | Useful for low-cost experiments, edge cases, and fine-tune baselines |
| [MuseGlimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) | Approximately 4-bit quantization; K-Quant-17GB and speculative decoding with DFlash | Targets 24–32 GB consumer hardware and local, responsive agent interaction |
| [IFM K2 Horizon 32B](https://huggingface.co/IFM/K2-Horizon-32B-GGUF) / [MoVA 36B-A4B](https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B-GGUF) | Apache 2.0 local-use checkpoints; MoVA activates about 4B parameters and the fleet shares deployment interfaces across sizes | Verify quantization, context, and runtime support before treating vendor efficiency claims as measured local performance |
| [Nemotron 3.5 Lightning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/) | NVFP4, speculative decoding with DFlash/DSpark, and deployment from RTX PCs/DGX Spark through data centers | Designed for low-latency tool calls, validation, code review, and other high-volume agent execution |
| [GLM-5.3-Flash](https://huggingface.co/docs/transformers/main/en/model_doc/glm5_next) | FP8/MTP-oriented serving path; sparse/linear attention targets lower long-context cost | Not a practical consumer-GPU model despite low active-parameter count |
| [Step-3.7-Flash](https://static.stepfun.com/blog/step-3.7-flash/) | MTP-enabled checkpoint can support speculative decoding; native VLM packaging | Designed primarily for accelerator-backed serving rather than LM Studio-class hardware |

### Local deployment notes

- GGUF support is still one of the biggest signals that a model is becoming locally useful quickly.
- For agentic work, Q4_K_M remains a practical sweet spot; overly aggressive quantization tends to hurt reasoning and tool calling.
- Fine-tuned local models are most interesting when they preserve enough general capability to remain useful outside a single benchmark.
- LM Studio-style workflows are ideal when you want to compare quantization levels and switch models quickly.
- The current conversation is less about raw downloadability and more about whether an open model can be made genuinely useful in a local agent loop with retrieval, tools, and serving optimizations.

## Recent public discussion

- The loudest frontier signal is still Kimi K3: community coverage keeps framing it as an open-weight pressure test against closed frontier models, especially on coding and long-context work. [YouTube coverage](https://www.youtube.com/watch?v=bcyyrnjWSEk)
- Anthropic’s open-weights position and related HN discussion show the argument has shifted from ideology to deployment policy: what should stay closed, and why. [Anthropic](https://www.anthropic.com/news/position-open-weights-models)
- The market debate is now explicitly about economics and regulation too, with HN threads on overregulating open-weight models and on low-cost open-model fine-tunes beating frontier defaults on narrow tasks. [CNBC / HN](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html) · [FermiSense](https://fermisense.com/when-machines-take-the-wheel/)
- A newer signal points to open weights being framed for local agentic use, not just benchmark wins. [Meta HN signal](https://twitter.com/finkd/status/2086754845218726027)
- The August 26 Transformers release is a useful ecosystem signal: model support landed for [Qwen4-Exp](https://huggingface.co/docs/transformers/main/en/model_doc/qwen4_exp), [GLM-5.3-Flash](https://huggingface.co/docs/transformers/main/en/model_doc/glm5_next), and [Step-3.7-Flash](https://huggingface.co/docs/transformers/main/en/model_doc/step3p7), showing that architecture support is becoming part of the competitive cycle rather than an afterthought.
- Meta’s MuseGlimmer release makes that local-agent framing concrete: its Apache 2.0 weights, multimodal tool use, quantized deployment path, and DFlash speculative decoding are aimed at always-on agents running on consumer hardware. [Meta AI Research](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model)
- IFM’s [K2 Horizon release](https://ifm.ai/k2/press-release) expands the local/open-weight story from a single checkpoint to a coordinated fleet: 0.9B and 3.7B for constrained devices, 7B for phones, 32B and 36B-A4B for local or on-premise hosting, and 375B-A23B for enterprise workloads. The important distinction is transparency: IFM released training data, code, methods, and weights rather than weights alone.
- NVIDIA’s Nemotron 3.5 Lightning extends the local-agent framing into a system-of-models architecture: a larger model plans while a fast 30B/3B-active MoE handles repetitive execution, with NeMo Switchyard routing requests across open and proprietary models. [NVIDIA Developer](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/)
- Qwen3.8-27B adds a strong dense-model counterpoint: native multimodality, 262K context, Apache 2.0 licensing, and controllable reasoning in a checkpoint that can be quantized to roughly 17 GB. Independent testing confirms the capability is real but highlights the need to avoid the default `xhigh` reasoning setting for routine local tasks.[1][2]
- Ornith-1.5 shifts the open-weight discussion from self-scaffolding to broader self-improvement: the task generator, agent scaffold, and solution rollouts are optimized together. Its 35B-A3B checkpoint is the deployment-friendly member, while the 397B model is a frontier-scale coding-agent benchmark contender.[3][4]

## Progress log

- **2026-08-10** — Last30days research says the open-weight conversation is now centered on local-agent usefulness, cost/performance, and release policy, with Kimi K3 still the loudest frontier signal.
- **2026-08-10** — Meta releases MuseGlimmer, a 30B Apache 2.0 open-weight model designed for local agent workflows, adding a strong deployment-focused counterpoint to larger frontier releases.
- **2026-08-11** — NVIDIA adds Nemotron 3.5 Lightning, an open 30B MoE with 3B active parameters, plus NeMo Switchyard for model routing; the pair makes high-volume execution a first-class open-weight deployment target.
- **2026-08-26** — Transformers adds support for Qwen4-Exp, GLM-5.3-Flash, and Step-3.7-Flash. The releases reinforce three current SOTA directions: hybrid attention for long-context efficiency, sparse MoE scale with low active compute, and native multimodal models with speculative-decoding hooks.
- **2026-08-27** — Last30days discussion was noisy and thin, but the strongest recurring signal was that open-weight progress is now being judged by licensing, deployment economics, serving efficiency, and ecosystem control—not downloadability alone.
- **2026-09-03** — IFM launches K2 Horizon, a six-model fully open fleet from 0.9B to 375B. Add it to both the frontier open-weight track and the local-use watchlist because the 32B and 36B-A4B variants target local or on-premise deployment, while the release publishes the full training and development artifacts.
- **2026-08-14–16** — Qwen3.8-27B arrives as a 27B Apache 2.0 native multimodal model with 262K native context, 1M YaRN extension, flexible reasoning control, and a strong local Q4_K_M path. Early independent testing finds excellent capability but warns that the default `xhigh` reasoning setting is impractical for many simple local prompts.[1][2]
- **2026-08-18–24** — Ornith-1.5 expands Ornith's self-scaffolding approach into an end-to-end self-improvement loop and releases 9B, 35B-A3B, and 397B open-weight variants. The 35B-A3B checkpoint is the local-use candidate; the 397B flagship targets multi-GPU frontier coding-agent evaluation.[3][4][5]
- **2026-08-04** — Inkling-Small, DeepSeek V4-Flash on a single MI300X, and Shieldstral each point to the same theme: open weights are becoming an operational/deployment story, not just a download story.
- **2026-07-15** — Agents-A1-NVFP4-MTP-GGUF adds a local agentic multimodal MoE derivative to the watchlist, showing how NVFP4/MTP packaging can make a Qwen3.5-35B-A3B-style model practical for local experiments.
- **2026-07-27** — Kimi K3 and Inkling join the open-weight frontier list, expanding the page to cover both big open frontier releases and the models likely to pressure closed-model defaults.
- **2026-07-10** — Qwen 3.6 27B arrives with GGUF support, making a flagship open-weight model viable for local multimodal use.
- **2026-06-30** — The model comparison page highlights current local frontiers like Ornith, Qwythos, VibeThinker, Qwen3.6, and Gemma 4.
- **2026-06-30** — Qwythos-9B-Claude-Mythos-5-1M shows how Claude Mythos / Fable traces can be distilled into a compact long-context reasoning model.
- **2026-06-09** — The open-weight landscape is already split between frontier generalists and task-specialist local models.

## Sources

- [Thinking Machines: Introducing Inkling-Small](../entities/article/2026-08-04_IntroducingInkling-Small_summary.md)
- [DeepSeek V4-Flash on a Single AMD MI300X](../entities/article/2026-08-04_DeepSeekV4FlashonaSingleAMDMI300X_summary.md)
- [Mistral’s Shieldstral 3B open-weights model](../entities/article/2026-08-04_Mistral_sShieldstral_3Bopen-weightsmodelformultimo_summary.md)
- [A Safe Path to Open Weights](../entities/article/2026-08-10_ASafePathtoOpenWeights_summary.md)
- [Model Comparison — Ornith, Qwythos, VibeThinker, Qwen3.6, Gemma 4](../comparisons/2026-06-30_Ornith_Qwythos_VibeThinker_Qwen3_6_Comparison.md)
- [Qwen 3.6 27B Arrives with GGUF Support and Local Multimodal](../entities/article/2026-04-26_Qwen_3_6_27B_Arrives_with_GGUF_Support_and_Local_M_summary.md)
- [Summary: Inkling: Our Open-Weights Model](../entities/article/2026-07-27_Inkling_OurOpen-WeightsModel_summary.md)
- [Summary: Kimi-K3 Releases on HuggingFace 7/27](../entities/article/2026-07-27_Kimi-K3ReleasesonHuggingFace7_27_summary.md)
- [Summary: Meta MuseGlimmer — open weights 30B local coding model](../entities/article/2026-08-10_MetaMuseGlimmer_openweights30Blocalcodingmodel_summary.md) · [Original Meta AI Research article](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model)
- [Summary: NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard](../entities/article/2026-08-11_NvidiaNemotron3_5lightningandNeMoSwitchyard_summary.md) · [NVIDIA Developer article](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/)
- [IFM K2 Horizon press release](https://ifm.ai/k2/press-release) · [IFM K2 Horizon model collection](https://huggingface.co/collections/ifm-ai/k2-horizon)
- [Qwen3.8-27B model card](https://huggingface.co/Qwen/Qwen3.8-27B) · [official GitHub repository](https://github.com/AlibabaCloud-Official/Qwen3.8-27B)
- [Qwen 3.8 27B local hands-on](https://simonwillison.net/2026/Aug/16/qwen-38-27b/)
- [1] [Qwen3.8-27B model card](https://huggingface.co/Qwen/Qwen3.8-27B)
- [2] [Qwen 3.8 27B local hands-on](https://simonwillison.net/2026/Aug/16/qwen-38-27b/)
- [3] [Ornith-1.5-35B-A3B model card](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- [4] [Ornith-1.5-397B model card](https://huggingface.co/ornith-ai/Ornith-1.5-397B)
- [5] [Independent Ornith-1.5-35B-A3B overview](https://www.mindstudio.ai/blog/ornith-1-5-moe-model-release)
- [LLM Release Tracker](2026-07-10_LLMReleaseTracker.md)
- [LLM Model Evolution](2026-06-10_LLMModelEvolution.md)
- [Inference Layer: Quantized Models, GGUF, and Local Use](../self-improving-ai-loops/2026-06-10_Lesson2_InferenceLayer.md)

## Related navigation

- [[AI Research Wiki — Topic Index]]
