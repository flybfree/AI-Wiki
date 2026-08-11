# Summary: 2026-08-08_11-58-56Z_RotaryQuant_Fitting120BMoEModelsonConsumerHardware.md
Saved: 2026-08-10 22:54
Source: 2026-08-08_11-58-56Z_RotaryQuant_Fitting120BMoEModelsonConsumerHardware.md
Model: None

---

## Summary  
Large mixture‑of‑experts (MoE) language models with 26–120 billion parameters exceed the memory capacity of typical consumer devices because they store dense weight matrices, maintain a key‑value (KV) cache that grows linearly with context length, and page many expert sublayers on demand. RotaryQuant tackles these three pressures simultaneously by introducing a three‑axis compression system: mixed‑precision weight quantization, LRU‑based expert offloading, and IsoQuant, a novel KV‑cache compression technique. The fused four‑kernel Metal GPU pipeline executes attention directly on packed 3‑bit tensors without materialising full‑precision KV state, enabling dense models to run within modest memory budgets. Experimental results show that Gemma 4‑26B‑A4B and Qwen3‑30B‑A3B fit into a 16 GB budget while Nemotron‑H 120B fits in 32 GB, delivering interactive speeds of 9–19 tokens per second with negligible perplexity degradation (ΔPPL ≤ +0.0012) and full retrieval accuracy at 32 K context.

## Key Contributions  
- [Finding 1] Mixed‑precision weight quantization assigns 4‑bit, 2‑bit, or 8‑bit bit‑widths to dense layers, routed experts, and the high‑activation shared expert, respectively.  
- [Finding 2] IsoQuant compresses KV cache activations using a Walsh–Hadamard transform followed by block‑diagonal SO(4) rotations, achieving isotropic activation distribution with only 3‑bit scalar quantization and O(d log d) cost versus O(d²).  
- [Finding 3] The fused GPU pipeline directly operates on packed 3‑bit tensors, eliminating the need to materialise full‑precision KV state and enabling true memory‑efficient attention.

## Methodology  
The authors first quantize model weights according to their architectural role, then implement LRU offloading of non‑resident experts to disk when physical RAM is exhausted. For KV cache compression they apply IsoQuant: each head’s activation vector undergoes a Walsh–Hadamard transform to decorrelate values, followed by block‑diagonal SO(4) rotations that make the distribution isotropic, and finally 3‑bit scalar quantization. The resulting compressed activations are stored in a compact format (256 parameters per head versus 16 384 for dense rotation). During inference, a four‑kernel Metal GPU pipeline fuses these operations into a single kernel that reads only the packed 3‑bit tensors, performing attention computation without ever expanding to full precision. This approach is integrated with MoE routing so that each expert’s weights are accessed in their quantized form.

## Results  
RotaryQuant enables the deployment of Gemma 4‑26B‑A4B and Qwen3‑30B‑A3B within a 16 GB memory budget, fitting them on consumer hardware. For Nemotron‑H 120B, the system fits into 32 GB while maintaining interactive performance of 9–19 tokens per second. Benchmarks report perplexity degradation no greater than +0.0012 and retrieval accuracy remains at 100 % for a 32 K context window, demonstrating that compression does not impair model quality.

## Significance  
By compressing both weights and KV state with orthogonal techniques—mixed‑precision quantization, LRU offloading, and IsoQuant—the authors provide the first practical pathway to run massive MoE models on ordinary laptops or mobile devices. This reduces hardware cost dramatically while preserving near‑native language generation quality, opening the door for real‑time conversational AI in resource‑constrained environments.

## Related Concepts  
MoE (Mixture‑of‑Experts), mixed‑precision quantization, LRU offloading, KV cache compression, IsoQuant, Walsh–Hadamard transform, block‑diagonal SO(4) rotations, 3‑bit scalar quantization, fused GPU pipeline, Metal GPU execution model.
