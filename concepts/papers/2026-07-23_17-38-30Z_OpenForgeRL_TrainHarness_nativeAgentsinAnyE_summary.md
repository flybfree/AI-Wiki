# Summary: 2026-07-23_17-38-30Z_OpenForgeRL_TrainHarness_nativeAgentsinAnyEnvironm.md
Saved: 2026-07-24 03:03
Source: 2026-07-23_17-38-30Z_OpenForgeRL_TrainHarness_nativeAgentsinAnyEnvironm.md
Model: None

---

## Summary  
OpenForgeRL introduces a framework that enables end‑to‑end training of agents built on complex inference harnesses such as Claude Code and OpenClaw in any arbitrary environment. By decoupling the harness’s inference from the RL training loop, the authors create a lightweight proxy and a Kubernetes‑based orchestrator that record model calls as data for standard RL codebases like veRL. This approach allows researchers to train, study, and improve agents directly within their real deployment harnesses without requiring custom infrastructure. The framework is validated across multiple harness types and environments, demonstrating superior performance over open baselines.

## Key Contributions  
- [Finding 1] OpenForgeRL provides a universal proxy‑orchestrator pipeline that can train any harness‑based agent in any environment at scale.  
- [Finding 2] The framework achieves state‑of‑the‑art results on benchmark suites (ClawEval, QwenClawBench, OSWorld‑Verified) surpassing comparable open baselines and matching larger models.  
- [Finding 3] Empirical analysis reveals that harness choice and RL shaping affect agent reliability, with RL improving self‑verification and multi‑step planning but leaving error recovery weak.

## Methodology  
The authors built OpenForgeRL by wrapping the harness’s inference engine in a thin proxy service that logs every model call with context and output. Each rollout is executed inside an isolated Kubernetes container, allowing the logged data to be streamed into a conventional RL trainer (e.g., veRL). The orchestrator manages stateful multi‑process execution while keeping training independent of the harness’s internal dynamics.

## Results  
OpenForgeClaw reaches 31.7 pass³ and 55.9 pass@3 on ClawEval, 33.7 on QwenClawBench; OpenForgeGUI scores 37.7 (OSWorld‑Verified), 63.0 (Online‑Mind2Web), 72.3 (WebVoyager). These results exceed open baselines of similar size across all tasks and match or surpass larger models in GUI settings.

## Significance  
By decoupling training from inference, OpenForgeRL democratizes the training of harness‑based agents, enabling rapid experimentation and systematic study within real deployment environments. The framework’s scalability and modular design reduce engineering overhead, fostering research that can directly inform production agent development.

## Related Concepts  
- Inference harnesses (Claude Code, Codex, OpenClaw)  
- RL codebases such as veRL  
- Kubernetes orchestration for distributed training  
- Proxy services for logging model calls
