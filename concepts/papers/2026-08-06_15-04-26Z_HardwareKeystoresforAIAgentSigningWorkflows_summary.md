# Summary: 2026-08-06_15-04-26Z_HardwareKeystoresforAIAgentSigningWorkflows_AZero_.md
Saved: 2026-08-06 20:46
Source: 2026-08-06_15-04-26Z_HardwareKeystoresforAIAgentSigningWorkflows_AZero_.md
Model: None

---

## Summary  
AI agents that perform cryptographic signing (e.g., Git commits, API authentication) currently expose private keys in software‑resident locations such as plaintext files or environment variables, making them vulnerable to exfiltration. This paper replaces that risk by anchoring keys inside hardware keystores accessible only through a vendor‑neutral PKCS#11 interface and wraps the solution in a five‑layer Zero‑Trust enforcement stack. The authors demonstrate that this architecture eliminates successful injection attacks while preserving normal operation.

## Key Contributions  
- Hardware confinement of private keys removes plaintext exposure entirely, ensuring confidentiality at rest and in use.  
- A comprehensive zero‑trust stack (SAGA session identity, scope bounds Smax, semantic validation RAV, taint tracking) enforces content‑aware authorisation beyond simple access control.  
- Experimental results show a 0 % attack success rate across benign task scenarios with a Wilson 95 % CI upper bound of 2.0 %, while baseline models achieve an average Attack Success Rate of 19.3 %.

## Methodology  
The authors substitute software‑resident key storage with hardware keystores (HSM, TPM, smart card) that expose keys only via the PKCS#11 interface. They implement a five‑layer enforcement architecture: Session Identity (SAGA), Scope Bounds (Smax), Semantic Validation (RAV), Taint Tracking, and the Hardware Execution Boundary. To validate the design they employ 12 injection scenarios derived from AgentDojo’s ImportantInstructionsAttack template, running four LLM models—gpt‑oss‑120b, Qwen2.5‑72B, DeepSeek‑V4‑Flash—in baseline mode (n = 192 combined test cases). The system is evaluated for both successful attacks and false positives.

## Results  
In the unprotected baseline, the Attack Success Rate averages 19.3 % (14.3 % and 25.4 % per model). When the hardware‑keystore + zero‑trust stack is applied, the ASR drops to 0 %, with a Wilson confidence interval upper bound of 2.0 %. No false positives were observed across four benign task scenarios, confirming that legitimate operations remain unaffected.

## Significance  
This work mitigates a critical vulnerability where AI agents could leak private keys via email injection, enabling unauthorized cryptographic actions. By combining hardware‑based key isolation with a multi‑layer zero‑trust enforcement model, the authors provide a practical pathway to enforce both confidentiality and authorisation in AI workflows.

## Related Concepts  
PKCS#11 interface, hardware keystores (HSM, TPM, smart card), Zero‑Trust architecture, SAGA session identity, scope bounds (Smax), semantic validation (RAV), taint tracking, injection attacks, LLM model testing.
