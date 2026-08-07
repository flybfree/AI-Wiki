# Summary: 2026-08-06_09-10-25Z_WhenDoPrompt_SideAgentPlaybooksTransfer_Accuracy_C.md
Saved: 2026-08-06 20:34
Source: 2026-08-06_09-10-25Z_WhenDoPrompt_SideAgentPlaybooksTransfer_Accuracy_C.md
Model: None

---

## Summary  
This paper investigates the conditions under which prompt‑side agent playbooks can be transferred from a source to a target environment without retraining, focusing on accuracy, computational cost, and runtime behavior. The authors introduce a frozen‑playbook transfer protocol that relies on distill‑validate‑transfer cycles and evaluate it across three benchmark suites: ALFWorld, TAU2‑Bench, and XBench‑DeepSearch. Their analysis shows that transferred playbooks can be beneficial only under specific decoding strategies and when the target’s cost‑runtime constraints align with those of the source; otherwise they may introduce errors or inflate expenses. The study concludes that frozen transfer is a conditional cold‑start option rather than a universal reuse strategy.

## Key Contributions  
- Finding 1: Transfer improves ALFWorld performance under greedy decoding and matches five fixed demonstrations in one near‑budget comparison, indicating selective utility of prompt‑side playbooks.  
- Finding 2: On TAU2‑Bench, aggregate contrast yields a modest matched‑domain advantage, yet Holm correction isolates only one of 135 route‑level effects, revealing heterogeneous compatibility issues.  
- Finding 3: XBench‑DeepSearch demonstrates that preserving first‑try heuristics can lead to repeated queries and delayed stopping after context‑runtime shifts, causing cost inflation.

## Methodology  
The authors adopt a shared distill‑validate‑transfer protocol where playbooks are frozen at the source, then validated against target tasks before deployment. They compare transferred playbooks with those derived directly from target demonstrations across multiple benchmarks, measuring accuracy, total query cost, and runtime duration. The evaluation includes greedy decoding, fixed demonstration baselines, and aggregate contrast to quantify domain‑specific benefits.

## Results  
Empirically, transferred playbooks achieve comparable or higher accuracy on ALFWorld when the source’s greedy policy aligns with the target’s token budget. In TAU2‑Bench, the average advantage is small (≈0.8 %), and only one of 135 route effects survives Holm correction, suggesting limited global benefit. XBench‑DeepSearch shows that while initial heuristics are retained, context‑runtime mismatches cause query repetitions and cost spikes, offsetting any early gains.

## Significance  
Understanding when prompt‑side playbooks transfer is valuable informs the design of modular AI agents that can reuse knowledge without costly retraining. The findings guide practitioners to treat frozen transfer as a conditional cold‑start option rather than a default strategy, promoting more efficient and reliable agent deployment across heterogeneous environments.

## Related Concepts  
- Prompt‑side playbooks: reusable instruction sets for language agents.  
- Distill‑validate‑transfer protocol: a framework for safe knowledge propagation.  
- Frozen transfer: static playbook reuse without retraining.  
- Greedy decoding, fixed demonstrations, aggregate contrast, Holm correction: evaluation techniques used to assess domain compatibility.
