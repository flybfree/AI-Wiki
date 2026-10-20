---
title: Tandem: Serving Hybrid Linear-Attention GUI Agents on Mobile NPUs
url: http://arxiv.org/abs/2610.26660v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_16-18-16Z_Tandem_ServingHybridLinear_AttentionGUIAgentsonMob.md
generated_at: 2026-10-20 00:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Tandem is a runtime system designed to optimize the execution of hybrid linear-attention GUI agents on mobile neural processing units (NPUs), specifically targeting the latency and energy overheads that accumulate across repeated agent actions on smartphones. The system addresses three core inefficiencies in existing NPU serving stacks—suboptimal checkpoint policies for reusable prompt prefixes, speculative decoding overhead that displaces work from the NPU matrix unit, and unnecessary power consumption between request bursts—and achieves a 30% per-step latency reduction for text-based screen descriptions, a 16% reduction for screenshot inputs, a 33% energy reduction per text step, and a dramatic standby power drop from 0.76 W to 0.22 W on a Snapdragon 8 Elite.

## Key Takeaways
- Tandem introduces a divergence-aware checkpointing strategy that saves recurrent state precisely at the positions where consecutive agent prompts diverge, rather than relying on chat-continuation checkpoint policies that miss reusable prefixes. Because GUI agent requests retain instructions but rewrite recent history, this targeted state-saving allows later requests to reuse previously processed context, significantly reducing redundant prefill computation across sequential actions.
- The system restructures speculative decoding so that most prefill computation stays on the NPU's matrix unit, while rollback states are produced through a short per-token tail rather than full speculative decoding passes. Its verification kernel reads each weight block only once for all proposed tokens, preventing the overhead that would otherwise outweigh decoding savings on the short action outputs typical of GUI agents.
- Between request bursts, Tandem releases NPU power votes without unloading the model from memory, cutting standby power from 0.76 W to 0.22 W. This keeps the model resident for fast wake-up while eliminating the idle power drain that a loaded model would otherwise impose on the device battery.

## Context
On-device GUI agents represent a growing frontier in mobile AI, enabling smartphones to autonomously navigate apps by reading screen content and issuing actions without sending data to cloud servers. Hybrid linear-attention architectures such as Mamba and RWKV variants are attractive for this setting because they reduce KV-cache memory demands, but existing serving runtimes like llama.cpp were designed for chat workloads and do not exploit the structural regularities of agent interaction patterns. This paper sits at the intersection of efficient transformer serving, mobile hardware scheduling, and agentic AI, addressing a gap where model architecture advances outpace the runtime infrastructure needed to deploy them on constrained mobile NPUs.

## Implications
For mobile AI practitioners and device OEMs, Tandem demonstrates that meaningful latency and energy savings are achievable without changing model weights or hardware, purely through runtime-level scheduling and memory-management innovations. The 30% latency and 33% energy reductions make multi-step GUI automation more viable on battery-constrained devices, while the standby-power reduction addresses a practical deployment concern that has previously discouraged keeping models resident on NPUs. For the broader field, the divergence-aware checkpointing and matrix-unit-preserving speculative decoding techniques offer transferable patterns for any agentic workload on heterogeneous mobile accelerators, potentially accelerating the shift from cloud-dependent to fully on-device autonomous agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26660v1)
