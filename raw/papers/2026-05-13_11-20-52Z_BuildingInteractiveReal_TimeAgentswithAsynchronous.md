---
title: Building Interactive Real-Time Agents with Asynchronous I/O and Speculative Tool Calling
published: 2026-05-13T11:20:52Z
authors: Coleman Hooper, Minwoo Kang, Suhong Moon, Nicholas Lee, Eric Wen, John Wawrzynek, Michael W. Mahoney, Yakun Sophia Shao, Amir Gholami, Kurt Keutzer
url: http://arxiv.org/abs/2605.13360v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Building Interactive Real-Time Agents with Asynchronous I/O and Speculative Tool Calling

## Abstract
There is a growing demand for agentic AI technologies for a range of downstream applications like customer service and personal assistants. For applications where the agent needs to interact with a person, real-time low-latency responsiveness is required; for example, with voice-controlled applications, under 1 second of latency is typically required for the interaction to feel seamless. However, if we want the LLM to reason and execute an agentic workflow with tool calling, this can add can add several seconds or more of latency, which is prohibitive for real-time latency-sensitive applications. In our work, we aim to enable real-time interaction even for agents with complex multi-turn tool calling. We propose Asynchronous I/O, which decouples the core agent reason-and-act thread from waiting for additional information from either the user or environment, thereby allowing for overlapping agentic processing while waiting on external delays. We also propose Speculative Tool Calling as a method to manage task execution when the agent is still unsure if it has received the full information or if additional user information may later be provided. For strong cloud models, our method can be applied out-of-the-box to existing real-time cloud APIs, providing 1.3-1.7$\times$ speedups with minor accuracy loss. To enable real-time interaction with small edge-scale models, we also present a clock-based training methodology that adapts the model to handle streaming inputs and asynchronous responses, and demonstrate a synthetic data generation strategy for SFT. Altogether, this approach provides 1.6-2.2$\times$ speedups with the Qwen2.5-3B-Instruct and Llama-3.2-3B-Instruct models across multiple tool calling benchmarks.

## Metadata
- **Published**: 2026-05-13T11:20:52Z
- **Authors**: Coleman Hooper, Minwoo Kang, Suhong Moon, Nicholas Lee, Eric Wen, John Wawrzynek, Michael W. Mahoney, Yakun Sophia Shao, Amir Gholami, Kurt Keutzer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.13360v1)