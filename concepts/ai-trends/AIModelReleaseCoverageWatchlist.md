---
title: "AI Model Release Coverage Watchlist"
type: reference
status: active
updated: "2026-11-13"
tags: [ai-intelligence, model-releases, frontier-models, open-weights, quality-control]
---

# AI Model Release Coverage Watchlist

This is a quality-control list for daily AI Intelligence briefings. Each high-signal release should be explicitly classified as **covered**, **deferred**, or **excluded with a reason**. A release should not disappear merely because a newer model in the same family arrives.

## Active watchlist

- [Grok 4.7](https://x.ai/news/grok-4-7) — frontier general model; released September 21, 2026. Check capabilities, agentic coding, context, pricing, and independent evaluation.
- [MiMo-V2.5](https://mimo.mi.com/docs/en-US/news/latest/v2.5-open-sourced) — open multimodal/reasoning family. Track separately from the later MiMo-V2.6 training and telemetry story.
- [Jev / System One Models](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — typed probabilistic decision model; not a conventional chat-model release.
- [YuE2](https://map-yue2.github.io/) — open music-generation model using an editable symbolic plan before rendering a song.
- [IFM K2 Horizon](https://ifm.ai/blog/k2) — fully open foundation-model fleet from 0.9B to 375B parameters.
- [Meituan LongCat-2.5](https://huggingface.co/meituan-longcat/LongCat-2.5) — Nov 9 heavyweight multimodal weights release; MIT license, custom code, and NPU-optimized serving path.
- [ByteDance Seedream 5.5](https://seed.bytedance.com/en/seedream5_5) — Nov 9 visual-generation/editing release; verify architecture, weights, and license only from a first-party card.
- [Inkling 2 Small](https://thinkingmachines.ai/news/inkling-2-small/) — announced Nov 5; Tinker-only closed weights until the promised Apache 2.0 release clears external testing.
- [Perplexity Decider v1.3 and Decider Flash v1.3](https://www.perplexity.ai/hub/blog/perplexity-decider) — released Nov 12; open-weight typed decision models with Apache terms, including the new `locate` extraction mode. Covered in the Nov 12 briefing and release tracker.
- [SpeakLeash Bielik-One](https://www.bielik.ai/en/blog/launching-bielik-11b-v31-dflash-and-the-bielik-one-family) — four open-weight decision models scheduled for Nov 12; Apache-2.0 Hugging Face cards and merged/adapter artifacts. Covered in the Nov 12 briefing and open-model snapshot.

## Additional labs to monitor

- **OpenAI** — GPT-6 Astra and adjacent agent/product releases
- **Anthropic** — Claude Fable/Mythos and safety-restricted frontier tracks
- **Google DeepMind / Google AI** — Gemini, Flash/Cyber variants, specialist foundation models
- **Meta AI** — Muse and other consumer/agent models
- **xAI** — Grok frontier and persistent-agent releases
- **DeepSeek** — open and API-efficient model families
- **Qwen / Alibaba** — language, vision, image, and local-deployment models
- **Z.ai** — GLM releases and domestic-infrastructure signals
- **Mistral AI** — sovereign open-weight and enterprise models
- **Thinking Machines Lab** — Inkling and task-specialized RL systems
- **Xiaomi MiMo** — open multimodal and reasoning models
- **Moonshot AI / Kimi** — large open-weight and long-context models
- **NVIDIA AI** — Nemotron and deployment-oriented foundation models
- **Cohere, AI21 Labs, Microsoft AI, Hugging Face, and MiniMax** — enterprise, open-weight, and ecosystem releases

## Additional model families now tracked

- **GPT-6 Astra** — frontier general/agentic model
- **Claude Fable 5.1 / Mythos 5.1** — broad and restricted frontier tracks
- **Gemini 3.8 Flash / Flash Cyber** — efficient general and cyber-specialized tracks
- **DeepSeek V4.1-Flash** — efficient open multimodal model
- **GLM-5.3-Flash** — open-weight and infrastructure-sovereignty signal
- **Qwen-Image-2.1** — open image generation and editing
- **Meta Muse / Muse Spark 1.3** — consumer agent track
- **Kimi K3** — open-weight frontier model
- **Inkling / Inkling-Small** — staged open-weight release track
- **Inkling 2 Small** — distinct second-generation model, still closed-weight on Tinker pending external red-teaming as of Nov 9
- **Perplexity Decider v1.3 / Decider Flash v1.3** — Apache-licensed open-weight typed decisions and span location, released Nov 12
- **SpeakLeash Bielik-One** — Apache-2.0 family of four open-weight decision models, launched Nov 12
- **Meituan LongCat-2.5** — open-weight native multimodal agent model; released weights Nov 9 under MIT
- **ByteDance Seedream 5.5** — multimodal image-generation and editing model; Nov 9 platform rollout

## Coverage rules

1. **Model releases are first-class intelligence signals.** They must appear in the executive summary or a named model-release section when material.
2. **Track model families, not only the newest version.** MiMo-V2.5 remains a distinct release even when MiMo-V2.6 becomes the current focus.
3. **Cover diverse modalities and architectures.** General language, reasoning, agentic, decision, vision, audio, music, robotics, and multimodal releases qualify when material. Check diffusion-based language and multimodal systems alongside autoregressive models; do not infer a model's architecture from an image-generation label.
4. **Use first-party sources first.** Add benchmark, system-card, pricing, weights, license, and runtime links when available.
5. **State evidence quality.** Separate vendor claims, independent evaluations, community adoption, and verified deployment evidence.
6. **Record omissions explicitly.** If a release is not covered, the briefing must say whether it was missed, deferred for verification, or excluded as low-signal.

## Briefing QA command

From the wiki root:

```bash
python3 scripts/check_model_release_coverage.py --days 10
```

The check is intentionally a gate, not a replacement for judgment. A missing match requires review before publication; it does not automatically mean the model belongs in the final narrative.
