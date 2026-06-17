---
title: "TurboQuant"
type: concept
tags: [quantization, vector-quantization, KV-cache, compression, Google, ICLR-2026, local-AI]
sources:
  - paper: "TurboQuant: Online Vector Quantization with Polar Codes" (Zandieh, Daliri, Hadian, Mirrokni, Google, ICLR 2026)
  - github: "https://github.com/TheTom/llama-cpp-turboquant"
  - github: "https://github.com/RyanCodrai/turbovec"
  - arxiv: "https://arxiv.org/abs/2506.xxxxx"
---

# TurboQuant

**TurboQuant** is an online vector quantization algorithm developed by Google researchers (Amir Zandieh, Majid Daliri, Majid Hadian, Vahab Mirrokni) that compresses high-dimensional Euclidean vectors while preserving their geometric structure. Proposed in 2025 and published at ICLR 2026, it uses Walsh-Hadamard-rotated polar codebook quantization for KV cache in large language models.

**Source**: [TurboQuant - Wikipedia](https://en.wikipedia.org/wiki/TurboQuant)

## How It Works

Most vector quantization methods compress by rounding values down. TurboQuant asks a harder question: can you shrink vectors without breaking their geometry?

- **Walsh-Hadamard rotation** — rotates the input vector before quantization, spreading information more uniformly across dimensions
- **Polar codebook** — uses polar codes (a class of error-correcting codes) to build the quantization codebook, enabling online (streaming) updates
- **Result** — 4.6x KV cache compression at ~1% perplexity loss in the original paper; later implementations report 6x compression with near-zero quality loss

## Key Benchmarks

| Metric | Result | Source |
|--------|--------|--------|
| KV cache compression | 4.6x at ~1% PPL loss | Google ICLR 2026 paper |
| KV cache compression | 6x with near-zero quality loss | Google Research blog |
| Memory usage (Gemma-4-31B, 256K context) | 27GB vs 44GB on AMD RDNA4 | r/OpenSourceAI benchmark |
| Speedup | 8x faster inference | FutureSketchLab YouTube |
| Compression accuracy | 5x compression, 99.5% accuracy | Tonbi's AI Garage test |

## Open-Source Implementations

- **[llama-cpp-turboquant](https://github.com/TheTom/llama-cpp-turboquant)** by TheTom — TurboQuant+ for C/C++ local LLM inference, inspired by Google's ICLR 2026 paper. Patches submitted upstream to llama.cpp.
- **[turbovec](https://github.com/RyanCodrai/turbovec)** by RyanCodrai — Rust implementation with Python bindings for vector search, implementing Google's TurboQuant algorithm.
- **Qdrant** — integrated TurboQuant for vector compression in their search engine.

## Community Response

TurboQuant generated significant attention across the local AI community:

- **YouTube** — 946K+ total views across 8 videos. Tim Carambat (Anything LLM founder) called it "going to revolutionize running a model on your device" (221K views). Multiple creators tested and validated the compression numbers.
- **Reddit** — Active benchmarking on AMD RDNA4 hardware. Users confirmed no crashes on consumer GPUs (2x 9070 XT), with patches being submitted upstream.
- **Market impact** — Memory chip stocks (Micron, Western Digital, SanDisk) dropped 7%+ within 24 hours of the announcement, suggesting the market viewed it as a potential disruption to hardware demand.

## Why It Matters

TurboQuant addresses a fundamental bottleneck in local AI: **context length vs. memory**. Traditional approaches reduce model size but lose quality. TurboQuant reduces KV cache memory (the bottleneck for long-context inference) while preserving the geometric relationships between vectors that make retrieval and reasoning work.

The practical implication: a 7B model that previously could only handle 8K tokens can now handle 32K+ on the same hardware, effectively multiplying the useful context window without buying more VRAM.

## Related Concepts

- [[Quantization]] — the broader category of reducing model precision
- [[KV Cache]] — the key-value cache that TurboQuant compresses
- [[Local LLM Inference]] — the primary use case for TurboQuant
- [[Walsh-Hadamard Transform]] — the mathematical basis for the rotation step
- [[Polar Codes]] — the error-correcting code family used for the quantization codebook
- [[Google AI Research]] — the lab that developed TurboQuant
