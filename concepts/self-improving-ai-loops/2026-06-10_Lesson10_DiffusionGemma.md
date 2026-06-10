---
title: "Lesson 10 — DiffusionGemma: Block-Autoregressive Text Generation"
created: 2026-06-10
module: Self Improving AI Loops
lesson: 10
tags: [diffusiongemma, google-deepmind, text-diffusion, moe, inference-speed]
---

# Lesson 10: DiffusionGemma — Block-Autoregressive Text Generation

## Concept: Why Diffusion for Text?

Traditional LLMs act like typewriters — generating one token at a time, left to right. This is efficient in cloud servers that batch thousands of requests, but wasteful locally: a single user's GPU sits idle waiting for each "keystroke."

DiffusionGemma reverses this. Instead of predicting words sequentially, it **drafts an entire 256-token block simultaneously** using discrete diffusion. The result: **up to 4x faster text generation on GPUs** for local, low-concurrency workloads.

This is not a replacement for autoregressive models — it's a complementary approach optimized for the **local inference** use case that agent loops and interactive workflows depend on.

---

## Architecture Overview

### Key Specs

| Parameter | Value |
|-----------|-------|
| Total Parameters | 25.2B |
| Active Parameters | 3.8B (MoE: 8 of 128 experts) |
| Layers | 30 |
| Context Length | Up to 256K tokens |
| Canvas Length | 256 tokens |
| Vocabulary Size | 262K |
| Supported Modalities | Text, Image |
| Vision Encoder | ~550M parameters |
| License | Apache 2.0 |

### Encoder-Decoder Design

DiffusionGemma uses a **bidirectional encoder-decoder architecture** optimized for inference speed:

1. **Encoder** (prefill): Processes the prompt and generates the KV cache
2. **Decoder**: Applies bidirectional attention over the generation canvas, accessing cached context via cross-attention

During inference, the model uses **multi-canvas sampling**:
- The decoder iteratively denoises a full block of 256 tokens
- Once a canvas is denoised, it's processed by the encoder and appended to the KV cache
- The model then generates the next canvas

This block-autoregressive approach enables **15-20 tokens per forward pass**, unlocking per-user generation speeds exceeding **1,100 tokens per second** on H100 hardware (FP8, low batch size).

---

## How Diffusion Sampling Works

### The Process

DiffusionGemma treats text generation like image generation:

1. **Start** with a canvas of random noise (noisy token IDs)
2. **Iteratively denoise** by predicting which tokens are "confident" and keeping them, renoising the rest
3. **Adaptive stopping** terminates early when the model is confident and stable

### Entropy-Bounded Denoising (Recommended Sampler)

```
Max denoising steps: 48
Temperature schedule: Linear decay from 0.8 → 0.4
Entropy bound: 0.1
Adaptive stopping: Enabled
  - Average canvas entropy < 0.005
  - Highest-probability tokens stable for 2 consecutive steps
```

At each step, the sampler selects the lowest-entropy tokens whose mutual information bound stays below the entropy bound. Non-selected tokens are fully renoised before the next step.

### Adaptive Inference Time Computation

Simpler prompts and structured tasks require fewer denoising steps. The model dynamically adjusts tokens-per-second based on task complexity — no manual tuning needed.

---

## Benchmark Comparison: DiffusionGemma vs Gemma 4

| Benchmark | DiffusionGemma 26B | Gemma 4 26B |
|-----------|-------------------|-------------|
| MMLU Pro | 77.6% | 82.6% |
| AIME 2026 no tools | 69.1% | 88.3% |
| LiveCodeBench v6 | 69.1% | 77.1% |
| Codeforces ELO | 1429 | 1718 |
| GPQA Diamond | 73.2% | 82.3% |
| MMMU Pro (vision) | 54.3% | 73.8% |
| MATH-Vision | 70.5% | 82.4% |

**Key takeaway**: DiffusionGemma trades ~5-10 points on accuracy benchmarks for up to 4x generation speed. It's designed for **speed-critical, interactive workflows** where latency matters more than squeezing out every percentage point.

---

## Multimodal Capabilities

DiffusionGemma is a **vision-language model** — it processes interleaved text, image, and video inputs to generate text output:

- **Image understanding**: Object detection, document/PDF parsing, screen/UI understanding, chart comprehension, OCR (including multilingual), handwriting recognition
- **Video understanding**: Analyzes and describes video content (up to 60 seconds at 1 frame/second)
- **Variable image resolution**: Configurable visual token budget (70, 140, 280, 560, 1120 tokens) — lower for classification/captioning, higher for OCR/document parsing
- **Interleaved multimodal input**: Mix images, video, and text within a single prompt

---

## Thinking Mode (Reasoning)

DiffusionGemma supports Gemma 4-style thinking mode:

```python
# Enable thinking
system_prompt = "<|think|>\nYou are a helpful assistant."

# The model outputs:
# <|channel>thought\n[Internal reasoning]<channel|>[Final answer]
```

To disable thinking, remove the `<|think|>` token. In multi-turn conversations, **do not include previous hidden thoughts** in the history — only the final assistant response.

---

## Running DiffusionGemma Locally

### Option 1: Transformers (Recommended for Development)

```python
from transformers import DiffusionGemmaForBlockDiffusion, AutoProcessor

MODEL_ID = "google/diffusiongemma-26B-A4B-it"

processor = AutoProcessor.from_pretrained(MODEL_ID)
model = DiffusionGemmaForBlockDiffusion.from_pretrained(
    MODEL_ID,
    dtype="auto",
    device_map="auto",
)

# Generate
message = [{"role": "user", "content": "Why is the sky blue?"}]
input_ids = processor.apply_chat_template(
    message, tokenize=True, add_generation_prompt=True, return_dict=True
).to(model.device)

output = model.generate(**input_ids, max_new_tokens=512)
text = processor.decode(output[0], skip_special_tokens=False)
```

### Option 2: LM Studio (GUI-First Workflow)

DiffusionGemma is available through LM Studio for visual model browsing and one-click switching. Load the GGUF quantized version from the Hugging Face Hub.

### Option 3: Unsloth GGUF Quant (Low VRAM)

```bash
# Dynamic 4-bit quant — needs ~18GB RAM
pip install huggingface_hub hf_transfer
huggingface-cli download unsloth/diffusiongemma-26B-A4B-it-GGUF \
    diffusiongemma-26B-A4B-it-UD-Q4_K_XL.gguf
```

### Option 4: llama.cpp (CPU/GPU)

Requires a specific PR on llama.cpp for DiffusionGemma support (PR #24423). Build with:

```bash
cmake -DGGML_CUDA=ON ..
make
```

Download the UD-Q4_K_XL quant (18GB RAM) or Q8_0 (36GB RAM).

---

## Trade-offs: When to Use DiffusionGemma

### Best For
- **Local, low-concurrency inference** (single user, single GPU)
- **Interactive workflows**: inline editing, rapid iteration, real-time code generation
- **Speed-critical tasks**: agent loops where latency compounds across iterations
- **Non-linear text structures**: perfectly closing complex markdown, generating and rendering code

### Not Ideal For
- **High-QPS cloud serving**: autoregressive models batch more efficiently at scale
- **Maximum accuracy**: Gemma 4 autoregressive models still outperform on benchmarks (~5-10 point gap)
- **Apple Silicon Macs**: unified memory architecture is memory-bandwidth-bound, not compute-bound, so DiffusionGemma's parallel decoding offers diminishing returns

---

## Fine-Tuning

DiffusionGemma can be fine-tuned via Unsloth for specialized tasks. Example: Unsloth fine-tuned DiffusionGemma to play **Sudoku** — a task autoregressive models struggle with because each token depends on future tokens. DiffusionGemma's bidirectional attention makes this much easier.

---

## DiffusionGemma in Self-Improving AI Loops

### Where It Fits in the Stack

```
DiffusionGemma (local inference)
    ↓
LiteLLM (abstraction layer)
    ↓
SmolAgents / LangGraph (loop engine)
    ↓
DeepEval (verification)
    ↓
Mozilla cq (knowledge memory)
```

### Advantages for Agent Loops

1. **Speed**: 4x faster generation reduces the inner loop latency — critical when agents iterate hundreds of times
2. **Bidirectional attention**: Better at non-linear tasks like closing markdown, generating structured output, and code completion
3. **Multimodal**: Can process images/screenshots directly — useful for UI automation and visual debugging
4. **MoE efficiency**: 3.8B active parameters out of 25.2B total — lower memory footprint for local deployment

### Caveats

- The accuracy trade-off (~5-10 points) may matter for complex reasoning tasks in agent loops
- Best on NVIDIA GPUs (H100+), not Apple Silicon
- Requires specific llama.cpp PR for GGUF support

---

## Resources

- **Model card**: https://huggingface.co/google/diffusiongemma-26B-A4B-it
- **Launch blog**: https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/
- **Official docs**: https://ai.google.dev/gemma/docs/diffusiongemma
- **Unsloth GGUF**: https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF
- **llama.cpp support**: https://github.com/ggml-org/llama.cpp/pull/24423
- **License**: Apache 2.0
