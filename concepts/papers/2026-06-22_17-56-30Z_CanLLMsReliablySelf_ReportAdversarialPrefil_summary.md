# Summary: 2026-06-22_17-56-30Z_CanLLMsReliablySelf_ReportAdversarialPrefills_andH.md
Saved: 2026-06-23 00:01
Source: 2026-06-22_17-56-30Z_CanLLMsReliablySelf_ReportAdversarialPrefills_andH.md
Model: None

---


## Summary  
The paper investigates whether large language models can reliably detect that their own outputs have been compromised by adversarial prefill attacks and, if so, how such detection occurs. Across a diverse set of open‑weight LLMs and safety benchmarks, the authors find that no model consistently flags its own vulnerable responses, with only about 27 % claiming intent on prefilled inputs versus natural ones. Their analysis reveals that introspective signals arise mainly from safety‑oriented reasoning and are fragile to weight orthogonalization and probing techniques. The work also shows that fine‑tuning methods can amplify the gap between claimed intention and actual tampering, highlighting a tension between self‑report reliability and attack success.

## Key Contributions  
- [Finding 1] No open‑weight LLM reliably distinguishes its own adversarial prefill from benign outputs; average claim rate on prefilled responses is ~27 %.  
- [Finding 2] Introspective signals are primarily driven by safety‑related reasoning and collapse when model weights are orthogonalized against the refusal direction.  
- [Finding 3] LoRA fine‑tuning (SFT, GRPO, DPO) widens the intention‑probe gap across models from 8B to 27B, though the effect varies by method.

## Methodology  
The authors evaluate ten open‑weight instruction‑tuned LLMs ranging from 3 B to 70 B on four safety benchmarks. They generate both natural and adversarial prefilled responses, then probe each model’s self‑report of whether it recognized the tampering. To isolate causal factors, they orthogonalize weights against the refusal direction and test three LoRA fine‑tuning paradigms (SFT, GRPO, DPO) on eight representative models.

## Results  
Across all models, claim rates on prefilled vs. natural outputs differ by only ~5 %, indicating near‑identical behavior. Orthogonalization eliminates this gap entirely, suggesting that the observed signal is not unique to refusal reasoning but may be a side effect of weight alignment. Fine‑tuning with SFT, GRPO, or DPO increases the gap from 8B to 27B models by up to 15 percentage points on average. Critically, these methods raise the success rate of adversarial prefill attacks by ~30 % in most cases, implying that self‑report reliability can be compromised rather than enhanced.

## Significance  
The findings underscore a critical gap between LLM introspection and real‑world safety: models cannot trust their own assessments when faced with adversarial inputs. By showing that fine‑tuning amplifies both the false confidence in self‑reports and the efficacy of attacks, the work warns developers to treat model introspection as unreliable without rigorous validation.

## Related Concepts  
- Large language models (LLMs)  
- Adversarial prefill attacks  
- Introspective capability  
- Safety benchmarks  
- LoRA fine‑tuning (SFT, GRPO, DPO)  
- Weight orthogonalization  
- Probe‑dependent responses
