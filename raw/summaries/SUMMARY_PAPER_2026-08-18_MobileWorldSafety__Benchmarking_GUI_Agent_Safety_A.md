---
title: MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps
url: http://arxiv.org/abs/2608.17659v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_11-33-22Z_MobileWorldSafety_BenchmarkingGUIAgentSafetyAgains.md
generated_at: 2026-08-18 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MobileWorldSafety, a benchmark of 142 risk tasks on real Android apps to test GUI agents against environmental injection attacks. It evaluates six agents and finds attack success rates between 40.4% and 66.9%, showing high vulnerability. The framework distinguishes safety failures from capability failures using rule-based verification and LLM judging.

## Key Takeaways
- MobileWorldSafety provides a systematic evaluation of GUI agent safety under real-world environmental injection attacks, moving beyond existing benchmarks that ignore everyday mobile contexts.
- All tested agents remain highly vulnerable, with attack success rates ranging from 40.4% to 66.9%, indicating frequent manipulation without user awareness.
- The two-stage pipeline separates unambiguous rule-based verification from ambiguous LLM adjudication, enabling objective and reproducible safety assessment.

## Context
Mobile GUI agents powered by large language models are entering early deployment, yet their interaction with untrusted environmental content poses novel security risks. Current research lacks standardized benchmarks that capture these everyday attack vectors on mobile devices, leaving safety concerns understudied.

## Implications
This benchmark will guide developers in designing safer autonomous agents and inform policy makers about the need for robust safeguards in AI-driven mobile applications. Practitioners can use MobileWorldSafety to quantify vulnerabilities and prioritize mitigation strategies before real-world rollout.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17659v1)
