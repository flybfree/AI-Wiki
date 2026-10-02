---
title: KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards
url: http://arxiv.org/abs/2610.02206v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_17-59-55Z_KaliBench_AFine_GrainedBenchmarkforCybersecurityTo.md
generated_at: 2026-10-01 21:56
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces KaliBench, a fine-grained benchmark designed to evaluate Large Language Models' ability to translate natural language into executable command-line interfaces for cybersecurity tools on Kali Linux. The authors address the critical gap in existing evaluations by focusing on precise CLI syntax and tool invocation rather than just knowledge or end-to-end agentic tasks. Their results reveal that no open-weight model achieves more than 42% exact-command accuracy, but supervised fine-tuning and reinforcement learning using deterministic verifiable rewards can bridge this performance gap effectively.

## Key Takeaways
- KaliBench comprises a comprehensive dataset of 8,504 query-command pairs covering 1,642 tools across 23 capability dimensions and five security phases, constructed via a manuscript-grounded pipeline that ensures deterministic canonicalization and alias-aware evaluation for reproducible assessment.
- The benchmark employs a rigorous multi-stage verification pipeline integrating LLM-based validation, sandboxed terminal execution, and human-in-the-loop refinement to guarantee semantic correctness and practical executability, enabling the development of runtime-free verifiable rewards for model training.
- Evaluation across 24 configurations shows that no open-weight model exceeds 42% exact-command accuracy in unrestricted settings, highlighting significant challenges in CLI tool use

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02206v1)
