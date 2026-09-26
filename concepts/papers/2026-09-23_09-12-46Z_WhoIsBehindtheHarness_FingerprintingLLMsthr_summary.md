# Summary: 2026-09-23_09-12-46Z_WhoIsBehindtheHarness_FingerprintingLLMsthroughAge.md
Saved: 2026-09-25 00:25
Source: 2026-09-23_09-12-46Z_WhoIsBehindtheHarness_FingerprintingLLMsthroughAge.md
Model: None

---

## Summary  
This paper introduces LIDAR (LLM Identification from Decisions and Actions at Runtime), a novel active black-box fingerprinting method for identifying the underlying large language model (LLM) behind coding-agent harnesses. While existing fingerprints rely on direct text or token distributions, which are obscured in agentic environments where system instructions mediate model behavior, LIDAR leverages observable execution decisions to distinguish models without access to weights or logs. The goal is to provide a reliable, runtime-based identity verification that captures how LLMs make choices during code modification tasks such as post-edit verification and failure recovery. By analyzing behavioral trajectories across multiple controlled probe pairs, LIDAR generates both instance-level and distribution-level features to create a probabilistic identifier.

## Key Contributions  
- [Finding 1] LIDAR achieves high Top-1 accuracy and MRR in identifying LLMs from their execution behavior across diverse models and harnesses.  
- [Finding 2] The method successfully distinguishes model identities based on behavioral patterns such as post-edit verification, transient-failure recovery, and specification-test conflict resolution under controlled changes.  
- [Finding 3] LIDAR outperforms four existing fingerprinting and API-auditing baselines, demonstrating superior performance in both accuracy and recall.

## Methodology  
LIDAR operates as an active black-box system that monitors the execution of coding-agent harnesses through three carefully designed probe pairs. Each pair exposes a specific decision-making scenario: post-edit verification (whether the agent confirms changes), transient-failure recovery (how it recovers from errors), and specification-test conflict resolution (how it handles conflicting requirements). The authors run these probes on 36 models across seven families and two harnesses, recording detailed behavioral trajectories. These trajectories are transformed into instance-level features (specific decision outcomes) and distribution-level features (statistical properties of decisions across runs). A lightweight probabilistic identifier then compares the resulting feature vectors to a clean reference model’s behavior. The method requires no access to model weights, logits, or internal provider logic.

## Results  
Across all experiments, LIDAR achieves high Top-1 accuracy and MRR, significantly outperforming four existing baselines in both detection rate and recall. Ablation studies confirm that each of the two feature levels (instance and distribution), all three probe pairs, and their controlled variants are essential to the model’s success. The method is effective across different LLM families and harness architectures, suggesting broad applicability.

## Significance  
This work matters because it shifts LLM fingerprinting from static text analysis to dynamic behavioral observation, enabling more robust identity verification in real-world agentic workflows. By focusing on decision-making under controlled conditions, LIDAR provides evidence of model identity that cannot be inferred from final outputs alone. This is crucial for security and compliance, where knowing *which* model made a decision matters as much as the decision itself.

## Related Concepts  
- Large Language Models (LLMs)  
- Coding-agent harnesses  
- Active black-box fingerprinting  
- Behavioral trajectory analysis  
- Top-1 accuracy and MRR  
- Instance-level vs. distribution-level features  
- Probabilistic identification  
- A/B testing for model comparison
