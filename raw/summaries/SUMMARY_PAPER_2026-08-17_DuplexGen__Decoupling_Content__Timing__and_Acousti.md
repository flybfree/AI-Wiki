---
title: DuplexGen: Decoupling Content, Timing, and Acoustics for Synthetic Dialogue Speech
url: http://arxiv.org/abs/2608.16053v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_03-30-52Z_DuplexGen_DecouplingContent_Timing_andAcousticsfor.md
generated_at: 2026-08-17 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DuplexGen, a framework that decouples dialogue content, timing, and acoustics in synthetic conversation generation. By generating the script with an LLM and having two full‑duplex models interact in real time, the system lets conversational dynamics emerge naturally while preserving the original script. The final high‑fidelity TTS re‑renders the interaction without altering its timing, yielding results that closely match real dialogue.

## Key Takeaways
- DuplexGen separates content generation from interactive speech production, allowing each model to listen and respond simultaneously, which creates organic conversation timing rather than rigidly scheduled markers.  
- The framework uses a high‑fidelity text‑to‑speech model only for final re‑rendering, ensuring that the original word timestamps remain unchanged throughout the process.  
- Experimental evaluation on a patient–clinician corpus shows conversational dynamics and interaction events are more faithful to real dialogue than conventional stitching methods.

## Context
Synthetic dialog generation remains limited by approaches that treat timing as a post‑hoc overlay, leading to unnatural pauses or overlaps. This work addresses the need for truly interactive speech synthesis where timing is emergent from mutual listening. The paper contributes a scalable pipeline that could serve as a benchmark for evaluating conversational AI quality.

## Implications
For researchers, DuplexGen provides a clear methodology to test how well models can generate believable dialogue without artificial constraints. For industry practitioners, the decoupled design may reduce development time and improve user experience in voice assistants and virtual agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16053v1)
