---
title: "Open-Source Models State of the Art — 2026-10-28"
date: 2026-10-28
status: draft
tags: ["wiki", "open-source-models", "foundation-models", "state-of-the-art", "local-use", "gguf", "quantization", "2026-10-28"]
---

# Open-Source Models State of the Art — 2026-10-28

**Source**: [Original Article](https://github.com/flybfree/AI-Wiki/wiki)

This page tracks the current open-weight frontier and the models most relevant for local deployment. The snapshot is refreshed through 2026-10-28 and adds Qwen3.8-Flash-Next, Liquid AI's LFM3 family, Google's latest open Gemma releases, and NVIDIA's latest Nemotron releases. It distinguishes open-source artifacts, open weights under model-specific terms, and proprietary models; sparse activation reduces compute per token but does not erase total-weight storage requirements.

## Semantic links
- [[concepts/2026-07-27_FoundationModelsStateOfTheArt.md|Foundation Models State of the Art — 2026-08-27]] — 5 title terms overlap, shared tags: foundationmodels, stateoftheart, wiki, 5 topic terms overlap
- [[concepts/2026-06-30_FoundationModelsStateOfTheArt.md|Foundation Models State of the Art — 2026-06-30]] — 5 title terms overlap, shared tags: foundationmodels, stateoftheart, wiki, 5 topic terms overlap
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 2 title terms overlap, 2 topic terms overlap, same area: home

## Snapshot

Open-source model progress now splits into two tracks:

- frontier open-weight generalists
- local-first quantized and fine-tuned models

The practical question is no longer just “what is the strongest open model?” It is also “what model can I run locally, tune for my tasks, and keep updated as the ecosystem moves?”

## Two-tier local model reference table

This table is a discovery-oriented shortlist, not a catalog limited to models already installed on the author's endpoints. It uses practical local inference as the organizing principle.

**Sizing assumptions:** estimates usually assume 4-bit quantization and cover model weights only; rows with a published package note that instead. Add runtime overhead and KV-cache memory, especially for long context. Mixture-of-experts models reduce active compute, but their total weights still affect loading requirements. Nemotron Bolt 74B's 24GB package uses 2-bit expert weights plus mixed-precision layers, not a generic 4-bit estimate. “Open-source” means materially open code, weights, data, or training artifacts; “open-weight” means the weights are available while other parts of the training stack or license may be restricted.

### Tier 1 — practical within 32 GB

| Model | Openness | Approx. 4-bit memory / package | Capability profile | Discovery value |
|---|---|---:|---|---|
| [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Open-weight, Apache 2.0 | 15–20 GB | Dense multimodal reasoning, coding, image/video input, tools, agents | Strong broad replacement candidate for local generalist workloads |
| [LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) | Open-weight, LFM Open License 1.0 | About 0.8 GB raw 4-bit weights | 1.7B text model, 256K context, native tool use; part of a six-model multimodal family | Compact local-agent and fine-tuning candidate; check each modality's runtime support |
| [LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) | Open-weight, LFM Open License 1.0 | About 12 GB raw 4-bit weights | 24B total / 2B active MoE, 131K context | Higher-capacity local agent candidate; add runtime and KV-cache headroom |
| [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) | Open-weight, Apache 2.0 | 16–20 GB | MoE general reasoning, coding, multilingual work, agents | High capability per active parameter; fast-MoE candidate |
| [Nemotron 3.5 Lightning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/) | Open-weight | 16–20 GB | Fast tool calls, validation, code review, long-running execution | Specialist alternative for high-volume agent loops |
| [Nemotron 3.5 Bolt 74B-A9B 24GB](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB) | Open-weight, OpenMDW-1.1 | 24 GB packed IQ2_XXS/mixed precision | 74B total / 9B active hybrid Mamba-2–Transformer LatentMoE VLM; images, video, tools; 256K context | 24GB model package; RTX Spark/llama.cpp and DGX Spark/vLLM paths; HF vLLM recipe also lists A100, H100-80GB, and Blackwell |
| [Nemotron 3.5 Bolt E4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB) | Open-weight, OpenMDW-1.1 | 6.18 GB Q4_K_M GGUF; NVIDIA targets ~4 GB runtime memory | 8B total / 4B effective, text-only, 64K context; multi-turn tool use, instruction following, device/voice assistants | Small edge/conversational agent; memory depends on workload and runtime |
| [Mistral Small 3.2 24B](https://huggingface.co/mistralai) | Open-weight, Apache 2.0 | 13–17 GB | General chat, coding, reasoning, multilingual tasks | Permissive general-purpose baseline |
| [Devstral Small 2 24B](https://huggingface.co/mistralai) | Open-weight | 13–17 GB | Repository-level coding, tools, software-engineering agents | Coding-first alternative to generalist models |
| [Gemma 3 27B](https://huggingface.co/google/gemma-3-27b-it) | Open-weight, Google terms | 14–18 GB | Multimodal chat, summarization, reasoning, multilingual work | Strong image-capable local generalist |
| [Gemma 4 12B Unified](https://huggingface.co/google/gemma-4-12B) | Open-weight, Apache 2.0 | About 6 GB raw 4-bit weights | 11.95B dense; text, image, and audio input; 256K context | Compact multimodal generalist; official card supports 140+ languages |
| [Nemotron 3.5 ASR Streaming 0.6B](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) | Open-weight, OpenMDW-1.1 | 600M checkpoint; package/runtime varies | Streaming speech recognition across 40 language-locales, with adjustable chunk sizes | Small specialist for low-latency speech; not a general chat model |
| [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B) | Open-weight | 18–22 GB | Math, coding, deep reasoning, analysis | Reasoning-focused comparison candidate |
| [OLMo 2 32B](https://huggingface.co/allenai/OLMo-2-0325-32B) | More fully open, Apache 2.0 | 18–22 GB | General text generation, research, fine-tuning | Best transparency-oriented option in this size range |
| [Ministral 3 8B/14B](https://huggingface.co/mistralai) | Open-weight | 5–11 GB | Fast assistants, multilingual work, reasoning variants | Low-memory and high-concurrency candidates |
| [Qwen3-Coder 30B class](https://huggingface.co/Qwen) | Open-weight | 16–22 GB | Code generation, repository understanding, tool use | Specialized coding-agent discovery path |

### Tier 2 — requires more than 32 GB

| Model | Openness | Approx. 4-bit memory / package | Capability profile | Discovery value |
|---|---|---:|---|---|
| [Llama 3.1 70B](https://huggingface.co/meta-llama/Llama-3.1-70B) | Open-weight, Meta license | 40–50 GB | General reasoning, coding, RAG, multilingual work | Mature large-model ecosystem |
| [Qwen2.5-72B](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) | Open-weight | 40–50 GB | General chat, coding, multilingual reasoning | Large dense comparison baseline |
| [Mistral Small 4 119B A6B](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) | Open-source-style, Apache 2.0 | 65–75 GB | Reasoning, coding, vision, tools, 256K context | Large MoE with relatively low active compute |
| [GLM-5.2](https://huggingface.co/zai-org/GLM-5.2) | Open-weight, MIT | Well above 32 GB | Long-horizon coding, reasoning, agent tasks | Frontier Chinese open-weight candidate |
| [Kimi K3](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart) | Open-weight | Well above 32 GB | Long-context reasoning, coding, agents | Frontier pressure test rather than compact local model |
| [MiniMax M2](https://huggingface.co/MiniMaxAI/MiniMax-M2) | Open-weight, modified MIT | Well above 32 GB | Coding, tools, agent orchestration, long context | Large MoE agent candidate |
| [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) | Open-weight, Apache 2.0 | 125–150 GB | Frontier reasoning, coding, multilingual work, agents | Multi-GPU frontier benchmark candidate |
| [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | Open-weight, Qwen Community License 1.0 | Well above 32 GB in full weights | 125B language model / 6B active, plus 51B n-gram embeddings and 4B MTP; vision input; 262K native context, extensible to 1M | Experimental Qwen4-architecture preview; active-parameter count is not a local-memory estimate |
| [Nemotron 3.5 Super VL 120B-A12B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4) | Open-weight, OpenMDW-1.1 | 75.1 GB NVFP4 package | 120B total / 12B active hybrid Mamba-2–Transformer MoE; text, images, video; up to 1M context | Large multimodal agent model; NVIDIA's documented NVFP4 recipe targets DGX Spark |
| [Nemotron 3.5 Transcribe 30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) | Open-weight, OpenMDW-1.1 | GPU-oriented; BF16, FP8, and NVFP4 checkpoints | 34B total / about 4.3B active including audio encoder; 40-language transcription, translation, diarization, and audio Q&A | Open speech specialist; not a compact local model |
| [Inkling-Small](https://thinkingmachines.ai/news/inkling-small/) | Open-weights | Very large | 276B total, 12B active, 1M context, variable thinking | Important frontier open-weight release, not consumer-local |
| [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | Open-weight, MIT | Hundreds of GB | Frontier reasoning, math, coding, research | Server-class reasoning reference |
| [Llama 3.1 405B](https://huggingface.co/meta-llama/Llama-3.1-405B) | Open-weight, Meta license | 220–250 GB | Large-scale general reasoning and coding | Multi-GPU server reference |

### Capability-oriented shortlist

| Need | Models to investigate first |
|---|---|
| Fast local assistant | Ministral 3 8B, Gemma 3 12B, Qwen3 8B |
| Fast local conversational/device agent | Nemotron 3.5 Bolt E4B; optimized for multi-turn tool use and low-memory edge workloads |
| Best broad model under 32 GB | Qwen3.8-27B, Mistral Small 3.2 24B |
| Local multimodal agent (24 GB checkpoint) | Nemotron 3.5 Bolt 74B-A9B 24GB; NVIDIA’s 2-bit/mixed-precision pack, images/video, tool use; check runtime GPU headroom |
| Coding agents | Devstral Small 2, Qwen3-Coder, GLM-5.2 |
| Deep reasoning | DeepSeek-R1-Distill-Qwen-32B, Qwen3.8-27B, Nemotron 3.5 Lightning |
| Multimodal work | Qwen3.8-27B, Gemma 3 27B, Mistral Small 3.1 |
| Local text agent under 2B | LFM3-1.7B; NVIDIA Nemotron 3.5 ASR Streaming 0.6B for speech-only workloads |
| On-device multimodal retrieval | EmbeddingGemma 2 740M; embedding model, not a generative assistant |
| Frontier long-context multimodal agents | Qwen3.8-Flash-Next; Nemotron 3.5 Super VL; both require accelerator-class memory |
| Training transparency | OLMo 2 |
| Large-scale frontier testing | Qwen3-235B-A22B, Kimi K3, GLM-5.2, DeepSeek-R1 |

The shortlist is intentionally broader than the currently installed models. It should be used to identify candidates for controlled endpoint probes and generation-speed benchmarks, not as a claim that every model will load successfully in every runtime.

## Qwen3.8-27B spotlight

[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) is Alibaba's 27B dense, open-weight vision-language model, released under Apache 2.0.[1] It accepts text, images, and video, and targets coding, professional work, research, and long-horizon agent tasks.[1] Its native context window is 262,144 tokens, extendable to 1M with YaRN; the checkpoint also uses multi-token prediction (MTP) and a hybrid layout combining gated DeltaNet linear-attention blocks with gated attention.[1]

The model's practical differentiator is controllable reasoning rather than a separate reasoning checkpoint: thinking is enabled by default, can be disabled, and exposes `reasoning_effort` levels of `xhigh`, `medium`, and `low`.[1] This is useful for agent loops, but the default is not ideal for interactive local use. Simon Willison's independent hands-on report found that the default `xhigh` setting can spend tens of thousands of tokens and turn simple tasks into multi-minute jobs; he recommends starting with low or no reasoning on consumer hardware.[2]

Qwen reports strong results on coding and computer-use evaluations, including 73.0 on Terminal-Bench 2.1, 61.7 on SWE-bench Pro, 84.3 on OSWorld-Verified, and 81.9 on AndroidWorld. These are vendor-reported results using different harnesses and should be treated as directional rather than directly comparable across model cards.[1] The local trade-off is compelling but not free: a Q4_K_M build is about 17 GB, while dense-model memory bandwidth and long reasoning traces can make inference feel slow even when the model fits.[2]

**Best fit:** a local multimodal coding and agent model when Apache licensing, long context, image/video input, and controllable reasoning matter. **Main caveat:** configure context length and reasoning effort explicitly; otherwise local latency and token usage can overwhelm the benefit of the compact 27B footprint.

## Qwen3.8-Flash-Next spotlight

[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) is Qwen's first open-weight release of an experimental architecture preview described as underpinning Qwen4. The model card specifies a 125B language model with 6B active parameters, plus 51B n-gram embedding parameters and a 4B multi-token-prediction (MTP) module. It is a causal language model with a vision encoder, accepts text, images, and video, and supports 262,144 tokens natively with extension up to 1M. Its architecture combines Gated DeltaNet with Qwen Sparse Attention (QSA), gated residuals, and n-gram embeddings.

The weights use the [Qwen Community License 1.0](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/main/LICENSE), not Apache 2.0. Do not conflate this checkpoint with the managed [Qwen3.8-Flash service](https://www.qwencloud.com/models/qwen3.8-flash): Qwen describes that as a production version with 1M context by default and built-in tools. The open checkpoint remains a very large model despite its 6B active count, because the full language weights, n-gram table, and MTP module affect memory and storage.

NVIDIA publishes a third-party [NVFP4 conversion](https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4). It is not an NVIDIA-developed base model: its terms combine NVIDIA's Open Model License with the underlying Qwen Community License. NVIDIA reports the mixed-precision checkpoint is about 2.7× smaller than the BF16 source; serving and MTP support require current, explicitly versioned vLLM support. Treat its benchmarks as vendor/model-card claims and its deployment target as accelerator-backed rather than consumer-local.

**Best fit:** long-context, multimodal agent research on accelerator-backed systems. **Main caveat:** sparse activation improves compute efficiency, not the model's total memory footprint; the open-weight preview and managed production API are separate products.

## Liquid Foundation Models: LFM3 and LFM2.5

Liquid AI's [LFM3 release](https://www.liquid.ai/blog/lfm3) (October 27, 2026) is a six-model, roughly 2B-class family spanning text, vision, audio, omni, and decision specializations. Liquid describes the models as open-weight under its [LFM Open License 1.0](https://docs.liquid.ai/lfm/models/complete-library). The text model, [LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B), has a 256K context window, native tool calling, and is sized at about 1 GB at 4-bit quantization. Liquid's tri-hybrid architecture combines gated short convolutions, sliding-window attention, and global attention; the company reports 22T pretraining tokens and a tool-use-focused post-training stage.

| Family member | Role | Practical note |
|---|---|---|
| [LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) | Text, local agents, tool use | 256K context; official GGUF, MLX, and ONNX exports are listed in the model library |
| [LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) | Vision-language | Image understanding; context and runtime support differ from the text model |
| [LFM3-Audio-2B](https://huggingface.co/LiquidAI/LFM3-Audio-2B) | Audio | Speech recognition, synthesis, voice chat, audio understanding, and tool calling |
| [LFM3-Omni-2B](https://huggingface.co/LiquidAI/LFM3-Omni-2B) | Omni-modal | Text, image, video, and audio input; text or speech output |
| [d1-2B](https://huggingface.co/LiquidAI/d1-2B) / [d1-omni-2B](https://huggingface.co/LiquidAI/d1-omni-2B) | Decision models | Typed classification, routing, and scoring built from LFM3 backbones |

The broader [LFM2.5 family](https://docs.liquid.ai/lfm/models/complete-library) remains relevant for local deployment: it includes 1.2B instruction/thinking variants, a 2.6B agent model, an 8B-A1B MoE, and [LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) (24B total / 2B active, 131K context). Liquid reports the 2.6B model at 220 tokens/second in under 2.5 GB in its target configuration; treat that as a vendor measurement, not a portable guarantee. Runtime and modality support vary by checkpoint, so use the [official model library](https://docs.liquid.ai/lfm/models/complete-library) rather than assuming the entire family shares the text model's deployment path.

**Best fit:** small, fine-tunable local specialists, particularly where device-side latency or privacy matters. **Main caveat:** benchmark results and speed figures are vendor-reported; verify the precise model, quantization, and runtime for each workload.

## Ornith-1.5 spotlight

[Ornith-1.5](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) is a family of open-weight models from Ornith AI focused on coding agents and end-to-end self-improvement.[3] Its training loop jointly improves task generation, scaffold construction, and solution rollouts instead of treating the task set and agent harness as fixed; the model therefore learns both how to solve tasks and how to search for solutions more effectively.[3]

The family spans a 9B dense model, a 35B-A3B mixture-of-experts (MoE) model that activates about 3B parameters per token, and a 397B MoE flagship.[3][4] The 35B-A3B checkpoint is the practical local option: Ornith reports 67.8 on Terminal-Bench 2.1 with Terminus-2, 68.5 with Claude Code, 79 on SWE-bench Verified, and 59.6 on SWE-bench Pro.[3] The flagship reports 86.1 on Terminal-Bench 2.1 and 86 on SWE-bench Verified, but its roughly 800 GB BF16 footprint requires multi-GPU serving.[4]

The results are promising but should be read as model-card claims: Ornith says its results are averaged over five runs, while the benchmarks use different harnesses, context windows, timeouts, and judge models.[3][4] An independent overview describes Ornith-1.5-35B-A3B as a strong coding-agent model, but also recommends starting below the full 262K context on constrained hardware and increasing it only when the workload needs it.[5]

**Best fit:** repository-level coding, terminal automation, and tool-using agents where scaffold quality and long-horizon execution matter. **Main caveat:** the 35B-A3B model is much more local-friendly than the 397B flagship, but neither should be treated as a general multimodal replacement for Qwen3.8; Ornith-1.5's center of gravity is agentic software work.

## Nemotron 3.5 Bolt spotlight

NVIDIA’s Nemotron 3.5 Bolt release is a *two-model local family*, not one checkpoint. **Bolt 74B-A9B 24GB** is a vision-language model with 74B total parameters and 9B active per token. It uses a hybrid Mamba-2/Transformer LatentMoE backbone with a C-RADIO v4-H vision encoder, accepts text, images, and video, supports up to 256K context, and is packed to a 24GB model target using IQ2_XXS expert weights plus mixed precision for other layers.[6][7] NVIDIA positions it for local tool-using agents, browsing, and terminal work; the published benchmark and speed claims are vendor-reported. The 24GB figure is a checkpoint target, not a universal runtime guarantee: NVIDIA documents RTX Spark with llama.cpp and DGX Spark with vLLM; the Hugging Face card also lists A100, H100-80GB, and Blackwell for its vLLM recipe.

**Bolt E4B 4GB** is the smaller edge model: 8B total parameters and 4B effective, post-trained from Gemma 4 E4B. It is text-only, has 64K context, and focuses on concise conversation, multi-turn tool use, instruction following, and grounding for voice/device assistants and embedded interfaces.[8][9] The Q4_K_M GGUF is 6.18GB on disk; NVIDIA targets roughly 4GB of runtime memory in its described workloads, so the “4GB” label is not the download size.[8][9]

Both are open-weight releases under NVIDIA’s OpenMDW-1.1 terms, not Apache/MIT-licensed checkpoints. Treat capability comparisons as vendor evidence until independently reproduced.[7][9]

## Recent NVIDIA open-model releases

NVIDIA's [Nemotron 3.5 Super and Lightning release](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/) (October 14, 2026) adds **Nemotron 3.5 Super VL 120B-A12B**: 120B total parameters, 12B active, a hybrid Mamba-2/Transformer MoE, text/image/video input, and up to 1M context. Its [NVFP4 checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4) is 75.1 GB; NVIDIA's documented one-GPU quick-start is for DGX Spark, so this is not a consumer-local 12B model despite sparse activation. The weights use OpenMDW-1.1.

On October 28, NVIDIA released [Nemotron 3.5 Transcribe 30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B), an open-weight audio model for transcription, speaker attribution, translation, and audio question-answering. Its model card describes 34B total parameters and about 4.3B active including the audio encoder, 40-language transcription, translation between 31 languages and English, 13-language speaker attribution, recordings up to an hour, and a 65,536-token context. It is offered in BF16, FP8, and NVFP4 under OpenMDW-1.1. NVIDIA's accompanying [Granary v2 dataset and curation pipeline](https://huggingface.co/datasets/nvidia/Granary-v2) reports 463,062 hours across 48 languages; check the individual source-data terms before reuse.

For low-latency speech rather than the larger promptable model, [Nemotron 3.5 ASR Streaming 0.6B](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) is a separate 600M-parameter streaming checkpoint with configurable chunk sizes and 40 language-locales. Do not conflate it with the 30B-A4B Transcribe model.

## Google open-model updates

Google's [Gemma release log](https://ai.google.dev/gemma/docs/releases) lists **EmbeddingGemma 2 740M** (October 6, 2026) as its newest open Gemma release, following **Gemma 4 12B Unified** (June 3). EmbeddingGemma 2 is an Apache 2.0, 740M-parameter multimodal embedding model that maps text, code, images, video, and audio into one 768-dimensional vector space; it is for retrieval, search, classification, and clustering, not text generation. See the [model card](https://huggingface.co/google/embeddinggemma-2) and [launch post](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/).

[Gemma 4 12B Unified](https://huggingface.co/google/gemma-4-12B) is an 11.95B dense, Apache 2.0 open-weight model with text, image, and audio input, 256K context, and multilingual support. The "Unified" architecture removes dedicated vision/audio encoders and projects raw modalities into the language model's embedding space; see Google's [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4). Google's October 28 [Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) announcement describes a closed-access frontier release; no public open-weight checkpoint was identified, so it is excluded from this open-weight tracker.

## Frontier open-weight generalists

| Model | Why it matters | Main caveat |
|---|---|---|
| [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Compact dense multimodal model with long context, controllable reasoning, and strong coding/agent results | Vendor-reported benchmarks; dense local inference can be bandwidth- and latency-bound |
| [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | Experimental sparse, multimodal long-context architecture preview; 6B active parameters | Large total model and Qwen Community License; not a consumer-local checkpoint |
| [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | Balanced multimodal + agentic coding model with a strong open-weight footprint | Heavier deployment than compact local specialists |
| [Gemma 4 26B A4B](https://huggingface.co/google/gemma-4-26B-A4B-it) | Strong open-weight multimodal generalist | Bigger memory footprint than smaller variants |
| [Gemma 4 12B Unified](https://huggingface.co/google/gemma-4-12B) | Best compact multimodal generalist in the Gemma 4 family | Less raw capacity than the 26B MoE model |
| [Nemotron 3.5 Super VL 120B-A12B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4) | Open 120B/12B-active multimodal agent with 1M context | NVFP4 package is 75.1 GB; accelerator-backed deployment |
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
| [Qwen3.8-Flash-Next NVFP4](https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4) | NVIDIA mixed-precision NVFP4 conversion; Qwen base model uses the Qwen Community License | Accelerator-oriented compression of a very large checkpoint; vLLM version and MTP support are specific requirements |
| [LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) | Text model; about 1 GB at 4-bit; 256K context; native tool use | Strong compact local-agent candidate; Liquid reports results on its own agent benchmarks |
| [LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) / [LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) | Small dense agent and 24B/2B-active MoE options; official GGUF/MLX/ONNX exports vary by model | Confirm context, memory, and runtime on the exact variant |
| [EmbeddingGemma 2 740M](https://huggingface.co/google/embeddinggemma-2) | Apache 2.0 multimodal 768D embeddings for text, code, image, video, and audio | Retrieval/embedding model, not a generative chat model |
| [Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M) | Dense 9B with 1M context | Very strong candidate for local long-context reasoning and tool use |
| [Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) | MoE checkpoint; about 3B active parameters; Transformers/vLLM/SGLang support | Strong local coding-agent candidate, but start with a smaller context on constrained hardware |
| [Ornith-1.5-9B](https://huggingface.co/ornith-ai/Ornith-1.5-9B) | Dense checkpoint with local/mobile-oriented variants | Lower resource requirement, lower ceiling |
| [Ornith-1.5-397B](https://huggingface.co/ornith-ai/Ornith-1.5-397B) | Multi-GPU MoE serving; FP8/INT4 options | Not a consumer-local model despite sparse activation |
| [Ornith-1.0 family](https://huggingface.co/collections/deepreinforce-ai/ornith-10) | Dense / MoE checkpoints for local deployment | Designed for agentic coding and self-scaffolding workflows |
| [VibeThinker-1.5B](https://huggingface.co/WeiboAI/VibeThinker-1.5B) | Tiny dense checkpoint | Useful for low-cost experiments, edge cases, and fine-tune baselines |
| [MuseGlimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) | Approximately 4-bit quantization; K-Quant-17GB and speculative decoding with DFlash | Targets 24–32 GB consumer hardware and local, responsive agent interaction |
| [IFM K2 Horizon 32B](https://huggingface.co/IFM/K2-Horizon-32B-GGUF) / [MoVA 36B-A4B](https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B-GGUF) | Apache 2.0 local-use checkpoints; MoVA activates about 4B parameters and the fleet shares deployment interfaces across sizes | Verify quantization, context, and runtime support before treating vendor efficiency claims as measured local performance |
| [Nemotron 3.5 Lightning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/) | NVFP4, speculative decoding with DFlash/DSpark, and deployment from RTX PCs/DGX Spark through data centers | Designed for low-latency tool calls, validation, code review, and other high-volume agent execution |
| [Nemotron 3.5 Bolt 74B-A9B 24GB](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB) | NVIDIA’s IQ2_XXS / mixed-precision 24GB checkpoint; GGUF for llama.cpp and vLLM path for DGX Spark | 74B total / 9B active multimodal agent; verify exact GPU, context, and runtime support before assuming the 24GB target |
| [Nemotron 3.5 Bolt E4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB) | 8B total / 4B effective; Q4_K_M GGUF and companion DFlash drafter | Text-only low-memory conversational/tool-use model; NVIDIA reports 3.5–4.3GB VRAM in its tested workloads |
| [Nemotron 3.5 ASR Streaming 0.6B](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) | 600M streaming ASR checkpoint, OpenMDW-1.1 | Small speech-only deployment path; chunk size trades latency against accuracy |
| [Nemotron 3.5 Transcribe 30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) | BF16 / FP8 / NVFP4, 34B total / about 4.3B active | GPU-focused multilingual transcription and diarization; not a low-memory local model |
| [GLM-5.3-Flash](https://huggingface.co/docs/transformers/main/en/model_doc/glm5_next) | FP8/MTP-oriented serving path; sparse/linear attention targets lower long-context cost | Not a practical consumer-GPU model despite low active-parameter count |
| [Step-3.7-Flash](https://static.stepfun.com/blog/step-3.7-flash/) | MTP-enabled checkpoint can support speculative decoding; native VLM packaging | Designed primarily for accelerator-backed serving rather than LM Studio-class hardware |

### Local deployment notes

- GGUF support is still one of the biggest signals that a model is becoming locally useful quickly.
- For agentic work, Q4_K_M remains a practical sweet spot; overly aggressive quantization tends to hurt reasoning and tool calling.
- Fine-tuned local models are most interesting when they preserve enough general capability to remain useful outside a single benchmark.
- LM Studio-style workflows are ideal when you want to compare quantization levels and switch models quickly.
- The current conversation is less about raw downloadability and more about whether an open model can be made genuinely useful in a local agent loop with retrieval, tools, and serving optimizations.

## Earlier public discussion (historical)

These discussion notes are retained from earlier 2026 research passes; they are not a fresh social-usage survey.

- The loudest frontier signal is still Kimi K3: community coverage keeps framing it as an open-weight pressure test against closed frontier models, especially on coding and long-context work. [YouTube coverage](https://www.youtube.com/watch?v=bcyyrnjWSEk)
- Anthropic’s open-weights position and related HN discussion show the argument has shifted from ideology to deployment policy: what should stay closed, and why. [Anthropic](https://www.anthropic.com/news/position-open-weights-models)
- The market debate is now explicitly about economics and regulation too, with HN threads on overregulating open-weight models and on low-cost open-model fine-tunes beating frontier defaults on narrow tasks. [CNBC / HN](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html) · [FermiSense](https://fermisense.com/when-machines-take-the-wheel/)
- A newer signal points to open weights being framed for local agentic use, not just benchmark wins. [Meta HN signal](https://twitter.com/finkd/status/2086754845218726027)
- The August 26 Transformers release is a useful ecosystem signal: model support landed for [Qwen4-Exp](https://huggingface.co/docs/transformers/main/en/model_doc/qwen4_exp), [GLM-5.3-Flash](https://huggingface.co/docs/transformers/main/en/model_doc/glm5_next), and [Step-3.7-Flash](https://huggingface.co/docs/transformers/main/en/model_doc/step3p7), showing that architecture support is becoming part of the competitive cycle rather than an afterthought.
- Meta’s MuseGlimmer release makes that local-agent framing concrete: its Apache 2.0 weights, multimodal tool use, quantized deployment path, and DFlash speculative decoding are aimed at always-on agents running on consumer hardware. [Meta AI Research](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model)
- IFM’s [K2 Horizon release](https://ifm.ai/k2/press-release) expands the local/open-weight story from a single checkpoint to a coordinated fleet: 0.9B and 3.7B for constrained devices, 7B for phones, 32B and 36B-A4B for local or on-premise hosting, and 375B-A23B for enterprise workloads. The important distinction is transparency: IFM released training data, code, methods, and weights rather than weights alone.
- NVIDIA’s Nemotron 3.5 Lightning extends the local-agent framing into a system-of-models architecture: a larger model plans while a fast 30B/3B-active MoE handles repetitive execution, with NeMo Switchyard routing requests across open and proprietary models. [NVIDIA Developer](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/)
- NVIDIA released Nemotron 3.5 Bolt 74B-A9B on Oct 15 and the smaller E4B variant on Oct 23, extending the local-agent track in two directions: the 74B-A9B 24GB IQ2_XXS VLM targets multimodal local agents, while the 8B/4B-effective E4B model targets compact text-based voice/device agents. NVIDIA’s hardware and benchmark figures are vendor-reported; both checkpoints use OpenMDW-1.1 rather than Apache/MIT licensing. [74B-A9B release](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Bolt-24GB/) · [E4B release](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/)
- Qwen3.8-27B adds a strong dense-model counterpoint: native multimodality, 262K context, Apache 2.0 licensing, and controllable reasoning in a checkpoint that can be quantized to roughly 17 GB. Independent testing confirms the capability is real but highlights the need to avoid the default `xhigh` reasoning setting for routine local tasks.[1][2]
- Ornith-1.5 shifts the open-weight discussion from self-scaffolding to broader self-improvement: the task generator, agent scaffold, and solution rollouts are optimized together. Its 35B-A3B checkpoint is the deployment-friendly member, while the 397B model is a frontier-scale coding-agent benchmark contender.[3][4]

## Progress log

- **2026-10-28** — Added Qwen3.8-Flash-Next and NVIDIA's NVFP4 conversion; Liquid AI's LFM3 and LFM2.5 families; Google's Gemma 4 12B Unified and EmbeddingGemma 2; and NVIDIA Nemotron 3.5 Super VL, Transcribe, and Granary v2. Corrected the open-weight/license distinctions (Qwen Community License, LFM Open License 1.0, Gemma 4 Apache 2.0, NVIDIA OpenMDW-1.1). Official model cards and release pages were verified; this is a primary-source update rather than a fresh social-usage survey, so no community-derived ranking claims are made.
- **2026-10-25** — Added both Nemotron 3.5 Bolt variants to the local-model comparison: 74B-A9B 24GB for multimodal tool-using agents and E4B for low-memory text/voice-device assistants; separated vendor memory targets from checkpoint file size and noted OpenMDW-1.1 licensing.
- **2026-09-28** — Rebuilt the reference section as a discovery-oriented two-tier table: practical sub-32 GB candidates and larger multi-GPU candidates, with separate openness, memory, capability, and discovery-value columns.

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

- [Thinking Machines: Introducing Inkling-Small](../../entities/article/2026-08-04_IntroducingInkling-Small_summary.md)
- [DeepSeek V4-Flash on a Single AMD MI300X](../../entities/article/2026-08-04_DeepSeekV4FlashonaSingleAMDMI300X_summary.md)
- [Mistral’s Shieldstral 3B open-weights model](../../entities/article/2026-08-04_Mistral_sShieldstral_3Bopen-weightsmodelformultimo_summary.md)
- [A Safe Path to Open Weights](../../entities/article/2026-10-11_ASafePathtoOpenWeights_summary.md)
- [Model Comparison — Ornith, Qwythos, VibeThinker, Qwen3.6, Gemma 4](../../comparisons/2026-06-30_Ornith_Qwythos_VibeThinker_Qwen3_6_Comparison.md)
- [Summary: Inkling: Our Open-Weights Model](../../entities/article/2026-07-27_Inkling_OurOpen-WeightsModel_summary.md)
- [Summary: Kimi-K3 Releases on HuggingFace 7/27](../../entities/article/2026-07-27_Kimi-K3ReleasesonHuggingFace7_27_summary.md)
- [Summary: Meta MuseGlimmer — open weights 30B local coding model](../../entities/article/2026-08-10_MetaMuseGlimmer_openweights30Blocalcodingmodel_summary.md) · [Original Meta AI Research article](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model)
- [Summary: NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard](../../entities/article/2026-08-11_NvidiaNemotron3_5lightningandNeMoSwitchyard_summary.md) · [NVIDIA Developer article](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/)
- [IFM K2 Horizon press release](https://ifm.ai/k2/press-release) · [IFM K2 Horizon model collection](https://huggingface.co/collections/ifm-ai/k2-horizon)
- [Qwen3.8-27B model card](https://huggingface.co/Qwen/Qwen3.8-27B) · [official GitHub repository](https://github.com/AlibabaCloud-Official/Qwen3.8-27B)
- [Qwen 3.8 27B local hands-on](https://simonwillison.net/2026/Aug/16/qwen-38-27b/)
- [1] [Qwen3.8-27B model card](https://huggingface.co/Qwen/Qwen3.8-27B)
- [2] [Qwen 3.8 27B local hands-on](https://simonwillison.net/2026/Aug/16/qwen-38-27b/)
- [3] [Ornith-1.5-35B-A3B model card](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- [4] [Ornith-1.5-397B model card](https://huggingface.co/ornith-ai/Ornith-1.5-397B)
- [5] [Independent Ornith-1.5-35B-A3B overview](https://www.mindstudio.ai/blog/ornith-1-5-moe-model-release)
- [6] [NVIDIA Nemotron 3.5 Bolt 74B-A9B 24GB release](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Bolt-24GB/)
- [7] [74B-A9B Hugging Face model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB) · [GGUF checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF)
- [8] [NVIDIA Nemotron 3.5 Bolt E4B 4GB release](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/)
- [9] [E4B BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) · [Q4_K_M GGUF checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB)
- [Qwen3.8-Flash-Next model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) · [NVIDIA NVFP4 conversion](https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4)
- [Liquid AI LFM3 announcement](https://www.liquid.ai/blog/lfm3) · [Complete LFM model library](https://docs.liquid.ai/lfm/models/complete-library) · [LFM2.5-24B-A2B release](https://www.liquid.ai/blog/lfm2-5-24b-a2b) · [LFM2.5-2.6B release](https://www.liquid.ai/blog/lfm2-5-2-6b)
- [Google Gemma release log](https://ai.google.dev/gemma/docs/releases) · [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4) · [EmbeddingGemma 2 model card](https://huggingface.co/google/embeddinggemma-2) · [EmbeddingGemma 2 launch post](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)
- [NVIDIA Nemotron 3.5 Super and Lightning](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/) · [Super VL NVFP4 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4)
- [NVIDIA Nemotron 3.5 Transcribe and Granary v2](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary) · [Transcribe model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) · [Granary v2 dataset](https://huggingface.co/datasets/nvidia/Granary-v2) · [600M streaming ASR model](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)
- [Gemini 4 Carbon announcement — proprietary, not an open-weight entry](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)
- [LLM Release Tracker](2026-07-10_LLMReleaseTracker.md)
- [LLM Model Evolution](2026-06-10_LLMModelEvolution.md)
- [Inference Layer: Quantized Models, GGUF, and Local Use](../self-improving-ai-loops/2026-06-10_Lesson2_InferenceLayer.md)

## Related navigation

- [[AI Research Wiki — Topic Index]]
