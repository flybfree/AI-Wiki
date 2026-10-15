---
title: MultiPartyTurnBench: Benchmarking Floor Control in Multi-Party Spoken Dialogue
url: http://arxiv.org/abs/2610.20172v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_13-20-14Z_MultiPartyTurnBench_BenchmarkingFloorControlinMult.md
generated_at: 2026-10-14 21:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MultiPartyTurnBench (MPTB), a benchmark of 240 synthetically generated, channel-separated conversations involving two to five speakers across six interaction types, designed to evaluate how full-duplex speech systems handle floor control in multi-party settings. The benchmark tests two tasks—End-of-Turn detection and Interruption detection—and reveals a stark asymmetry: systems perform well at detecting turn completions but struggle significantly with selective interruption handling, with full-duplex agents performing near chance level on interruption tasks.

## Key Takeaways
- MPTB provides the first unified, controlled evaluation of genuine floor transitions against confusable non-events in multi-party settings, using exact event-conditioned annotations that enable causal evaluation through false-positive-constrained recall and signed latency metrics, addressing a gap left by existing dyadic or end-to-end evaluations.
- A critical asymmetry exists between EOT and INT detection: learned systems achieve 82.5–92.6% EOT recall at manageable false-positive rates of 4.3–11.8%, while INT detection suffers from either missed takeovers or excessive false activations, indicating that recognizing when someone is genuinely interrupting is far harder than recognizing when someone has finished speaking.
- Five full-duplex agents achieve 86.1–95.8% balanced accuracy on turn entry but perform near chance (46.9–54.7%) on selective interruption handling, with Gemini-3.8-Live yielding to 97.7% of backchannels while MiniCPM-o-4.5 yields to only 1.4% of genuine interruptions, demonstrating that current systems cannot reliably distinguish floor-taking speech from non-floor-taking speech.

## Context
Full-duplex speech systems and conversational AI agents are increasingly deployed in multi-party settings such as meetings, classrooms, and collaborative workspaces, where multiple speakers overlap, backchannel, or attempt to take the conversational floor. Prior benchmarks have focused on dyadic turn-taking or holistic agent behavior, leaving a critical gap in understanding how systems handle the nuanced distinction between genuine floor transitions and confusable non-events like backchannels or temporary holds. MPTB fills this gap by providing controlled, multi-party evaluation infrastructure that isolates floor control as a measurable capability.

## Implications
These findings establish selective floor control as a distinct and unresolved challenge that directly impacts the reliability of multi-party voice interaction systems in real-world deployments such as meeting assistants, collaborative AI tools, and social robots. Practitioners building full-duplex conversational agents must move beyond optimizing turn-entry accuracy and invest in training systems to selectively handle interruptions, as current models either over-yield to non-interruptive speech or fail to recognize genuine floor takeovers, undermining user trust and conversational naturalness in multi-party environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20172v1)
