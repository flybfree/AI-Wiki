# Summary: 2026-08-09_04-46-58Z_VectraYX_Vision_1B_ASub_2BSpanish_LATAMCybersecuri.md
Saved: 2026-08-10 23:12
Source: 2026-08-09_04-46-58Z_VectraYX_Vision_1B_ASub_2BSpanish_LATAMCybersecuri.md
Model: None

---

## Summary  
VectraYX‑Vision‑1B is a sub‑2 billion‑parameter vision‑language model built for Spanish/LATAM cybersecurity imagery, combining a frozen SigLIP‑so400m encoder with a 1.04 B decoder via an MLP to produce natural‑language answers in Spanish. The model uniquely supports structured visual reasoning through <|think|> tokens and native tool invocation via the Model Context Protocol (<|tool_call|>) while exporting to llama.cpp’s LLaVA mmproj format for air‑gapped deployment. A preliminary evaluation shows near‑zero grounding performance (B6 score ≈ 0.08) despite fully functional pipelines, indicating that the current supervised fine‑tuning (400–1900 steps, ~16 M tokens) is insufficient and that a checkpoint‑loader bug masquerades as training collapse.

## Key Contributions  
- [Finding 1] The first sub‑2B VLM for Spanish/LATAM cybersecurity UI that emits structured reasoning via <|think|> and invokes tools through the Model Context Protocol.  
- [Finding 2] Identification of a checkpoint‑loader bug (unstripped llm. prefix) causing training collapse, with remediation strategies including longer SFT (≥60 % replay) and lower learning rates.  
- [Finding 3] A three‑variant ablation matrix (V0: NoPE every‑4, V1: all‑RoPE, V2: NoPE+learned 2D) to investigate whether periodic no‑positional‑encoding layers benefit or harm attention over the 729‑token visual block.

## Methodology  
The authors freeze the encoder’s weights and attach a decoder of 1.04 B parameters through an MLP, training it with supervised fine‑tuning (SFT) that runs 400–1900 steps (~16 M tokens). The model is instructed to generate answers in Spanish, produce <|think|> blocks for reasoning, and call tools using <|tool_call|>. Training data comprises 14,596 QA pairs spanning ten cybersecurity domains (IDA, Ghidra, Wireshark, Nmap, Metasploit, Volatility). The fine‑tuned checkpoint is exported to llama.cpp’s LLaVA mmproj format for CPU‑only inference.

## Results  
Preliminary grounding results yield a B6 score of 0.08 tool‑identification, far below expectations. Wall‑time measurements and GGUF efficiency on CPU are reported alongside the ablation matrix findings: V0 shows modest improvement in attention stability, while V1 and V2 exhibit no significant gain or loss, suggesting NoPE may be neutral for this block size. The authors provide B1–B5 text‑backbone models, text controls, preliminary B6/B7 scores, and release all checkpoints (jsantillana/vectrayx‑1b, jsantillana/vectrayx‑vision‑1b, jsantillana/vectrayx‑vision‑1b‑checks).

## Significance  
This work fills a critical gap for low‑resource Spanish/LATAM cybersecurity analysis by delivering an ultra‑compact VLM that can operate offline and in native Spanish. It also advances the research on NoPE usage within visual blocks, offering a systematic approach to fine‑tuning SFT depth and replay rates. The open‑source release encourages reproducibility and further exploration of sub‑2B models for domain‑specific vision tasks.

## Related Concepts  
Vision‑language model, Sub‑2B model, Structured reasoning tokens (<|think|>, <|tool_call|>), Model Context Protocol (MCP), LLaVA mmproj format, NoPE (no positional encoding), SFT training, grounding performance, checkpoint‑loader bug, MLP decoder architecture.
