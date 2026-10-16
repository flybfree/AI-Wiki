---
title: Decoding What iOS Location Services Send to Apple: An LLM Is an Unreliable Analyst but a Useful Toolmaker
url: http://arxiv.org/abs/2610.21597v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_09-43-26Z_DecodingWhatiOSLocationServicesSendtoApple_AnLLMIs.md
generated_at: 2026-10-15 22:17
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether frontier large language models (Claude Opus 4.8 and Codex GPT Sol 5.6) can reliably reverse-engineer the protobuf message schemas that iOS location services send to Apple's servers. The central finding is that while direct LLM-generated schemas contain substantial and hard-to-detect errors, LLMs can be effectively repurposed as toolmakers: the author uses Claude to write a Python tool called Extractor that reliably recovers protobuf schemas from Apple binaries, validated against known-answer test cases, previously published schemas, and real network measurements from a jailbroken iPhone 8 running iOS 16.7.11.

## Key Takeaways
- Direct use of frontier LLMs to reconstruct protobuf schemas from compiled binaries produces schemas with substantial errors in the great majority of cases. These errors are particularly dangerous because the generated schemas are internally consistent, making them difficult to detect without ground-truth validation, which renders direct AI output unsuitable for forensic and privacy analysis of mobile network traffic.
- LLMs are far more effective as toolmakers than as direct analysts. The author prompts Claude to write a Python tool (Extractor) that programmatically recovers protobuf schemas from Apple binaries. Because the tool's output can be independently validated against binaries compiled from schemas with known answers, previously published schemas, and actual network measurements, the tool achieves reliability that direct LLM inference does not.
- The Extractor tool is demonstrated in practice by decoding and analyzing the location services network traffic of a jailbroken iPhone 8 (iOS 16.7.11), showing that the validated tool pipeline can produce actionable insights about what data Apple's location services actually collect and transmit from a real device.

## Context
Reverse engineering proprietary mobile software protocols is a labor-intensive task critical for privacy research, regulatory compliance, and security auditing. As frontier LLMs become increasingly capable of code generation and binary analysis, researchers and practitioners are eager to leverage them to accelerate protocol reverse engineering. This paper provides a rigorous empirical evaluation of that hope, demonstrating both the promise and the significant pitfalls of using LLMs in a domain where subtle structural errors in a schema can lead to incorrect conclusions about data collection practices. It contributes to the broader discussion about when AI assistance is trustworthy and when it introduces hidden failure modes that are invisible to the user.

## Implications
For privacy researchers, regulators, and security auditors who rely on understanding what data mobile operating systems transmit to their vendors, this paper establishes a clear boundary: LLMs should not be treated as authoritative sources for protocol schemas, but they can dramatically accelerate the tooling pipeline when outputs are subjected to rigorous validation. For the AI research community, the finding that internally consistent but incorrect outputs are hard to detect underscores the need for validation-first workflows when deploying LLMs in structured-data extraction tasks. Practitioners building privacy tools for mobile platforms can adopt the Extractor-style approach—using an LLM to generate a validated analysis tool rather than trusting its direct inferences—to achieve both speed and reliability in protocol decoding.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21597v1)
