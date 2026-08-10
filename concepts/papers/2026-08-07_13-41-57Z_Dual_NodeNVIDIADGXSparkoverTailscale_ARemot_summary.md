# Summary: 2026-08-07_13-41-57Z_Dual_NodeNVIDIADGXSparkoverTailscale_ARemote_Acces.md
Saved: 2026-08-09 22:58
Source: 2026-08-07_13-41-57Z_Dual_NodeNVIDIADGXSparkoverTailscale_ARemote_Acces.md
Model: None

---

## Summary  
The paper demonstrates a proof‑of‑concept remote‑access testbed that enables distributed NanoChat pretraining across two NVIDIA DGX Spark nodes equipped with GB10 Grace Blackwell chips, communicating via a Tailscale mesh VPN and a 200 Gb/s QSFP56 fiber link. By running PyTorch torchrun with DDP and NCCL, the authors achieve a global batch of 131,072 tokens per step while sustaining an average step time of ~69 seconds (≈1,890 tokens/s). The same infrastructure also supports a cybersecurity fine‑tuning experiment using CISA advisories and evaluates its impact on specialized vs. general knowledge. This work shows that modest local hardware can host both research‑grade LLM training and practical CTI fine‑tuning workloads.

## Key Contributions  
- [Finding 1] Distributed NanoChat pretraining is feasible on two DGX Spark systems with 128 GB unified memory, delivering ~1,890 tokens per second using a dedicated high‑speed fiber link.  
- [Finding 2] Fine‑tuning the model on CISA cybersecurity advisories improves CTI‑specific performance (score rises from 2.06 to 2.29) but causes a slight regression in general‑knowledge scores, indicating domain‑focused adaptation.  
- [Finding 3] The same dual‑node setup can simultaneously host a 400‑level AI course and a CompTIA Security+ query engine, showcasing the platform’s versatility beyond research.

## Methodology  
The authors configured two GB10 DGX Spark nodes each with a single process (depth‑20 NanoChat model), local batch size of 32 per node, and a 2,048‑token context. Training employed PyTorch torchrun with DDP and NCCL, binding the processes to the dedicated QSFP56 link while Tailscale provided secure mesh VPN connectivity. Container orchestration ensured reproducible environment setup; checkpointing was performed every few steps to mitigate loss. A step‑zero bug causing NCCL timeouts was identified, diagnosed, and patched before final run.

## Results  
The experiment processed approximately 653 million tokens over four days, yielding a throughput of ~1,890 tokens per second. The CTI fine‑tuning evaluation used an Ollama‑hosted LLM judge to compare baseline vs. CTI‑augmented checkpoints on 17 questions; the overall score improved modestly from 2.06 to 2.29 on a 0–10 scale, with notable gains in CTI categories and minor losses in general knowledge.

## Significance  
This study proves that remote multi‑node LLM training and specialized fine‑tuning can be performed with relatively inexpensive hardware, offering a scalable template for labs, classrooms, and production‑grade security AI services. The reproducibility runbook and scripts make the setup accessible to other researchers, bridging gaps between academic experimentation and real‑world cybersecurity applications.

## Related Concepts  
distributed training (torchrun DDP NCCL), Tailscale VPN mesh networking, GB10 Grace Blackwell system‑on‑chip, QSFP56 high‑speed fiber link, NanoChat model architecture, fine‑tuning for cybersecurity, CTI categories, Ollama LLM judge, checkpointing, reproducibility runbook.
