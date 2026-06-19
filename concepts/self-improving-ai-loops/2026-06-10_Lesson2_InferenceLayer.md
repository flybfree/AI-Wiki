---
title: "Lesson 2 — Inference Layer: Self-Hosted LLMs"
created: 2026-06-10
module: Self Improving AI Loops
lesson: 2
tags: [inference, self-hosted, ollama, vllm, llama-cpp, model-selection, gguf]
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 2: Inference Layer — Self-Hosted LLMs



**Source**: [Original Article](https://github.com/ggerganov/llama.cpp.git)
## Core Idea

The inference layer is where your models live and serve requests. For self-hosted self-improving loops, you need a local model server that provides an OpenAI-compatible API — this lets you run agents against local models in dev and swap to cloud models in prod without changing agent code.

## Model Server Options

### LM Studio — Preferred Dev Tool
**Best for:** Development, prototyping, single-GPU setups, GUI-first workflow
**Self-hosted:** Yes, desktop application

```bash
# Download from https://lmstudio.ai
# Open app → search/download model → start local API server
# API runs automatically at http://localhost:1234
```

**Pros:**
- Visual model browser and download — no CLI needed
- Built-in API server (OpenAI-compatible)
- GGUF model format support
- One-click model switching
- Great for dev and local testing

**Cons:**
- Single-machine only
- Not designed for production throughput
- Limited concurrency controls

### Ollama — Quick CLI Alternative
**Best for:** Headless servers, Docker workflows, CLI-first developers
**Self-hosted:** Yes, one command

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3.3
# API runs at http://localhost:11434
```

**Pros:**
- Zero config, model pulls automatically
- Growing library of open-weight models
- OpenAI-compatible API out of the box
- Great for headless/Docker deployments

**Cons:**
- CLI-only (no GUI)
- Not designed for high-throughput production
- Limited concurrency controls

### vLLM — Production Throughput
**Definition:** A high-performance inference engine with PagedAttention for efficient memory management.
**Best for:** Production serving, concurrent requests, multi-GPU setups
**Self-hosted:** Yes, Docker-based

```bash
docker run --gpus all -p 8000:8000 vllm/vllm-openai:latest \
  --model meta-llama/Llama-4-Scout-256B \
  --tensor-parallel-size 8 \
  --max-model-len 32768
```

**Pros:**
- PagedAttention — 24x higher throughput than baseline
- Tensor parallelism across multiple GPUs
- OpenAI-compatible API
- Speculative decoding support
- Production-grade batching

**Cons:**
- Requires GPU expertise to configure
- No GUI — CLI and API only
- Memory intensive

### LM Studio — Desktop GUI
**Best for:** Developers who want a GUI, single-machine development
**Self-hosted:** Yes, desktop application

**Pros:**
- Visual model browser and download
- Built-in API server
- GGUF model format support
- No Docker or CLI needed

**Cons:**
- Single-machine only
- Not designed for production
- Limited concurrency

### TGI (Text Generation Inference) — Hugging Face
**Best for:** Production inference with quantized models, Hugging Face ecosystem
**Self-hosted:** Yes, Docker-based

```bash
docker run --gpus all -p 8080:80 \
  ghcr.io/huggingface/text-generation-inference:latest \
  --model-id mistralai/Mistral-Small-3.1-24B-Instruct-2506
```

**Pros:**
- Built for quantized models (GGUF, AWQ, GPTQ)
- Docker-based, easy deployment
- Hugging Face ecosystem integration
- Handles batching automatically

**Cons:**
- Smaller community than vLLM
- Less flexible configuration
- Primarily for text generation (not agentic tool calling)

### llama.cpp — CPU-GPU Hybrid Inference
**Definition:** A highly optimized C++ implementation of the Transformer architecture for local inference. Supports GGUF, GGML, AWQ, GPTQ, and FP16 models with fine-grained control over GPU/CPU memory split.

**Best for:** Systems with limited VRAM, mixed CPU-GPU workloads, users who want maximum control over quantization and memory management.

```bash
# Install (if not already installed)
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp && cmake -B build && cmake --build build --target server -j$(nproc)

# Start the OpenAI-compatible server
llama-server \
  --model /path/to/model.gguf \
  --host 127.0.0.1 --port 8080 \
  --ngl 999 \
  --ctx-size 8192 \
  --threads $(nproc) \
  --log-disable
```

Verify: `curl http://localhost:8080/v1/models` should return the model list.

**Key features:**
- **CPU offloading:** Control exactly how many layers go to GPU (`--ngl`) vs CPU — offload as many as VRAM allows, rest runs on CPU
- **Quantization support:** Native GGUF format with Q4_K_M, Q5_K_M, Q8_0, and more — minimal quality loss at 4-bit
- **KV cache quantization:** Reduce memory usage with Q4_K or Q8_0 KV cache at small perplexity cost
- **Speculative decoding:** Faster token generation via `--speculative` draft models
- **OpenAI-compatible API:** Same API shape as Ollama/LM Studio — swap without changing agent code
- **ROPE scaling:** Extend context window with `--rope-scaling yarn` or `:extended` on compatible models
- **Numactl binding:** Multi-socket server support: `numactl --cpunodebind=0 --membind=0 llama-server ...`

**GGUF quantization guide:**
| Quant | Size (7B) | Quality | Speed | When to Use |
|-------|-----------|---------|-------|-------------|
| Q4_K_M | ~4.0 GB | 95-97% of FP16 | Fast | Default for agentic work, tool-calling |
| Q5_K_M | ~4.8 GB | 97-99% of FP16 | Fast | When marginal quality matters |
| Q8_0 | ~7.3 GB | 99%+ of FP16 | Medium | When VRAM permits full offload |
| IQ4_XS | ~3.4 GB | 93-95% of FP16 | Fast | Non-knowledge-intensive tasks |

**Recommendation:** Q4_K_M is the sweet spot for agentic work. Avoid IQ2_XS / IQ3_XXS — too aggressive, hurts tool-calling and reasoning.

**Memory management tips:**
- `--mlock` pins model to RAM (prevents swap thrashing on Linux)
- `--cache-reuse 256` persists KV cache across requests (reduces re-computation)
- `--tensor-split 0.5,0.5` distributes across multiple GPUs

**Pros:**
- Best VRAM efficiency of any local option — partial GPU offload works well
- Extremely fast inference on CPU when GPU memory is insufficient
- Granular quantization control for fitting any model on any hardware
- Active development, large GGUF model ecosystem
- OpenAI-compatible API — drop-in replacement for Ollama/LM Studio

**Cons:**
- CLI-only, no GUI — requires comfort with configuration flags
- No automatic model download — you must source GGUF files yourself
- Steeper learning curve for quantization and memory tuning
- No built-in concurrency management for multi-user setups

## Model Picks for Agentic Work (2026)

### Llama 4 Scout (256B)
**Best for:** Best reasoning, complex agentic tasks
**Hardware:** 8x A100/H100 or cloud GPU clusters
**Agentic capability:** Highest — strong tool calling, planning, reasoning
**Self-hosted cost:** ~$20-40/hour on cloud GPUs, or $80k+ for on-prem hardware

### Gemma 4 (12B-27B)
**Best for:** Strong coding, fits on a single GPU with quantization
**Hardware:** Single A10/A100 with 4-bit quantization
**Agentic capability:** Very good for coding tasks, solid tool calling
**Self-hosted cost:** ~$0.50/hour on a single A10

### Mistral Small 3.1 (24B)
**Best for:** Best balance of reasoning and cost for local use
**Hardware:** Single A100 or 2x RTX 4090
**Agentic capability:** Strong reasoning, good for Ralph loops
**Self-hosted cost:** ~$1-2/hour on cloud, or free on your own GPU

### Phi-4 Mini (3.8B)
**Best for:** Edge/local, surprisingly capable for tool calling
**Hardware:** Runs on CPU, no GPU needed
**Agentic capability:** Good for simple tool calling, weaker on complex reasoning
**Self-hosted cost:** Free on any machine

### DeepSeek-R1 Distilled
**Best for:** Open reasoning model, strong for Ralph loops
**Hardware:** 7B-70B variants available
**Agentic capability:** Strong reasoning with distilled training
**Self-hosted cost:** 7B variant runs on single GPU

## Quantization Trade-offs

**Definition:** Quantization reduces model precision (e.g., from 16-bit floats to 4-bit integers) to fit models on smaller hardware, at the cost of some accuracy.

| Quantization | GPU Memory | Quality Loss | Use Case |
|-------------|-----------|-------------|----------|
| FP16 (no quant) | 512GB+ for 256B | None | Research, best accuracy |
| 8-bit | 256GB+ | Minimal | Production with good GPUs |
| 4-bit (AWQ/GPTQ) | 64-128GB | Noticeable but manageable | Single GPU, dev |
| GGUF (Q4_K_M) | 32-64GB | Moderate | Consumer GPUs, local dev |

**Key insight from Raj Shukla:** The model stays the same — the memory in file systems and markdown files is where the real magic lives. You don't need the biggest model; you need the right feedback loops.

## Forge: Reliability Layer for Self-Hosted Models

**Forge** (by Texas Instruments) is a Python reliability layer for self-hosted LLM tool calling.

**The problem:** For most of 2025 and early 2026, the conventional wisdom on local agents was: "nice for chat, useless for tool calling."

**Forge's solution:** Adds a reliability layer on top of local models that fixes tool-calling accuracy. For most TI engineers who tried it, the model quality gap closed enough for production agentic work.

```python
# Example: Forge wraps your local model
from forge import ToolCallingLayer

layer = ToolCallingLayer(model="ollama/llama3.3")
result = layer.call("extract email from this text", tools=[email_parser])
```

## When to Self-Host vs. Use Cloud APIs

| Factor | Self-Host | Cloud API |
|--------|-----------|-----------|
| **Privacy** | Full control, data never leaves your server | Data goes to provider |
| **Cost** | High upfront (GPU hardware), low marginal | Pay per token, scales with usage |
| **Model version brittleness** | You control upgrades, no surprise breaks | Provider updates break your prompts |
| **Maintenance** | You manage GPU drivers, updates, scaling | Provider handles everything |
| **Best for** | Sensitive data, high-volume stable workloads, learning the stack | Prototyping, variable workloads, accessing frontier models |

**Practical approach:** Use **LiteLLM** (next lesson) to abstract the model layer. Dev on local Ollama, prod on cloud Claude — same agent code.

## Key Takeaway

Start with Ollama for dev. Move to vLLM when you need production throughput. Pick your model based on your hardware, not benchmarks — a 24B model with good feedback loops beats a 256B model with no verification.

## Related Concepts
- [[Self-Improving AI Loops]]
- [[Harness Engineering]]
- [[Model Version Brittleness]]
