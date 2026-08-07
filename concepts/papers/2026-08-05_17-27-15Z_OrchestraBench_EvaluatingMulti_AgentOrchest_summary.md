# Summary: 2026-08-05_17-27-15Z_OrchestraBench_EvaluatingMulti_AgentOrchestrationF.md
Saved: 2026-08-06 20:25
Source: 2026-08-05_17-27-15Z_OrchestraBench_EvaluatingMulti_AgentOrchestrationF.md
Model: None

---

## Summary  
OrchestraBench is a benchmark designed to systematically evaluate multi‑agent orchestration failure modes, recovery capabilities, and decomposition quality in enterprise‑style workflows. It introduces two primary metrics—cascade radius and per‑failure‑mode recovery—to diagnose why pipelines break and how they are repaired. The study injects failures into 26 gold‑labelled cases across multiple large language models (Claude, Sonnet, Opus, Haiku) to obtain reproducible diagnostics. By comparing keyword/flag routers with intent‑reasoning routers, the authors demonstrate that only the latter can achieve full diagnostic accuracy.

## Key Contributions  
- [Finding 1] Intent‑reasoning routing outperforms keyword/flag routing on adversarial cases, achieving 100 % oracle‑matched diagnosis.  
- [Finding 2] Cascade radius grows with pipeline depth (mean 0.9 to 4.7 across depths 3‑7), indicating deeper failures propagate farther.  
- [Finding 3] Recovery rates vary by failure mode: tool faults recover fully (1.0), ambiguous delegation partially (0.30), while latent or semantic modes never recover (0.0).

## Methodology  
The authors built OrchestraBench as a controlled, seed‑reproducible harness that injects failures into templated workflows. They measure cascade radius by tracking how many downstream agents are affected and define per‑failure‑mode recovery as the fraction of tasks restored after intervention. Diagnostic quality is assessed via keyword/flag routers versus intent‑reasoning routers, using paired tests and bootstrap confidence intervals.

## Results  
On a 26‑case gold‑labelled diagnostic, the keyword router scored 0 % on adversarial cases while the intent‑reasoning router matched the oracle (100 %). Probe experiments with Claude revealed three failure‑handling tiers: full recovery for tool faults, partial recovery for ambiguous delegation, and zero recovery for latent/semantic modes. Blind retry increased detection latency, confirming that detection and attribution are essential for containment.

## Significance  
OrchestraBench provides the first systematic framework to quantify orchestration failure propagation and repair quality, moving beyond task‑accuracy metrics to diagnose root causes. Its findings guide more robust routing policies and reveal inherent limitations of current diagnostic mechanisms in multi‑agent systems.

## Related Concepts  
- Multi‑agent orchestration  
- Cascade radius  
- Per‑failure‑mode recovery  
- Intent‑reasoning router  
- Bootstrap confidence intervals  
- Latent failure modes
