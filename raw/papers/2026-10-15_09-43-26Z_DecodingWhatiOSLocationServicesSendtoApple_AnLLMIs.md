---
title: Decoding What iOS Location Services Send to Apple: An LLM Is an Unreliable Analyst but a Useful Toolmaker
published: 2026-10-15T09:43:26Z
authors: Douglas Leith
url: http://arxiv.org/abs/2610.21597v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decoding What iOS Location Services Send to Apple: An LLM Is an Unreliable Analyst but a Useful Toolmaker

## Abstract
Reverse engineering the data formats used by mobile software is skilled and slow, and using AI to assist with it is attractive. We evaluate this for the protobuf messages that an iPhone sends to Apple's location services. Working from Apple's binaries, we use two frontier models (Claude Opus 4.8, Codex GPT Sol 5.6) to reconstruct the schemas of protobufs observed in network traffic. The great majority of the schemas contain substantial errors, and these are hard to detect because the schemas are internally consistent. Direct AI use is therefore unsuitable for forensic and privacy analysis. AI can, however, write reliable analysis tools when their output can be validated. We use Claude to write a Python tool, Extractor, that reliably recovers protobuf schemas from Apple binaries. We validate it against binaries compiled from schemas with known answers, previously published schemas, and network measurements. We demonstrate the use of Extractor to decode and analyse the location services network traffic of a jailbroken iPhone 8 (iOS 16.7.11).

## Metadata
- **Published**: 2026-10-15T09:43:26Z
- **Authors**: Douglas Leith
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21597v1)