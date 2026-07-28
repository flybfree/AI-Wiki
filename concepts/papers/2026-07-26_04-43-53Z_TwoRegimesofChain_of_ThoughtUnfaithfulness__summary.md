# Summary: 2026-07-26_04-43-53Z_TwoRegimesofChain_of_ThoughtUnfaithfulness_Behavio.md
Saved: 2026-07-27 22:41
Source: 2026-07-26_04-43-53Z_TwoRegimesofChain_of_ThoughtUnfaithfulness_Behavio.md
Model: None

---

## Summary  
The paper investigates chain‑of‑thought (CoT) explanations and their faithfulness, focusing on how well behavioral detectors can identify unfaithful CoT across model outputs. It discovers that detection signals collapse when models generate incorrect answers, producing only oracle‑level performance (AUROC 0.696). The problem is split into two regimes: moderate separation for correct answers versus near‑chance performance for wrong ones on all benchmark signals. Linear probes reveal distinct behavior patterns in different model families and answer regimes.

## Key Contributions  
- [Finding 1] Behavioral detection signals are ineffective at detecting unfaithfulness when models produce wrong answers, outperforming only by an oracle diagnostic (AUROC 0.696).  
- [Finding 2] The task stratifies into two regimes: on correct answers, signals moderately separate faithful from post‑hoc reasoning (AUC ≈ 0.64–0.67); on incorrect answers, no tested signal beats chance (AUC ≈ 0.5) across all models and benchmark signals.  
- [Finding 3] Linear probes decode the behaviorally blind regime in Llama‑3.1‑8B and the correct‑answer regime in Qwen‑2.5‑7B; there is no shared, positively aligned direction between regimes, and answer‑first trace transformations transfer to neither annotated regime.

## Methodology  
The authors audited behavioral detection of unfaithful CoT against human annotations from FaithCoT‑Bench. They compared the AUROC of various purpose‑built signals, stratified by answer correctness, performed linear probing on Llama‑3.1‑8B and Qwen‑2.5‑7B to see which regimes each probe captures, tested trace transformations (answer‑first traces and hint‑induced unverbalized flips), and independently verified the benchmark’s label semantics.

## Results  
Answer incorrectness alone yields an AUROC of 0.696, which exceeds every purpose‑built signal. On correct answers, signals achieve AUCs around 0.64–0.67, separating faithful from post‑hoc reasoning. On incorrect answers, all signals fall at or below chance (AUC ≈ 0.5). Linear probes show opposite alignments: Llama‑3.1‑8B captures the behaviorally blind regime, while Qwen‑2.5‑7B captures the correct‑answer regime; no positive direction is shared. Answer‑first trace transformations transfer to neither annotated regime, and hint‑induced flips affect model and source in a dependent manner.

## Significance  
The study demonstrates that current CoT oversight methods are only reliable for detecting unfaithfulness when models answer correctly, highlighting a critical gap in deployable detection pipelines. It underscores the need for model‑specific detectors or alternative strategies, and it resolves a previously reported documentation‑data mismatch in FaithCoT‑Bench.

## Related Concepts  
Chain‑of‑thought explanations, faithfulness, behavioral detection, AUROC, FaithCoT‑Bench, linear probing, regimes (correct vs. incorrect answer), trace transformations, oracle diagnostics.
