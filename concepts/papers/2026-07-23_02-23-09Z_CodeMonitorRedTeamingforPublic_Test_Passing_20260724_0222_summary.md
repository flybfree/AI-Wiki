# Summary: 2026-07-23_02-23-09Z_CodeMonitorRedTeamingforPublic_Test_PassingCode.md
Saved: 2026-07-24 02:22
Source: 2026-07-23_02-23-09Z_CodeMonitorRedTeamingforPublic_Test_PassingCode.md
Model: None

---

## Summary  
The paper addresses the gap between passing public tests and true correctness of LLM‑generated code, showing that many generated programs still contain hidden bugs. To test this gap, it introduces **Code Monitor Red Teaming**, a protocol that varies generator pressure, verifier scaffolding, and model strength to evaluate weaker LLM verifiers on residual defects. Experiments across function‑level, data‑science, and workflow code reveal that 23 081 of the 43 677 programs that pass public tests fail hidden tests, indicating a substantial blind spot in current verification pipelines.

## Key Contributions  
- **Code Monitor Red Teaming protocol**: A systematic method that manipulates generator pressure, verifier scaffolding, and model capability to expose weaknesses in weaker LLM verifiers.  
- **Empirical finding on residual bugs**: Among the 43 677 programs passing public tests, 23 081 still contain hidden defects, achieving a 5 % false‑positive rate for weak verifiers that detect them.  
- **Robustness stress test**: Adversarial public‑test overfit reduces verifier AUROC and raises miss rates, highlighting the need for robustness checks beyond simple pass/fail metrics.

## Methodology  
The authors built **CodeMonitorBench**, a benchmark spanning three code domains (function‑level, data‑science, workflow). They generated 71 000 candidate programs, filtered those that passed public tests (43 677), and then applied weak LLM verifiers with different scaffolding levels. A stress test introduced adversarial pressure on the public tests to observe degradation in verifier performance. The evaluation measured false‑positive rates, AUROC, and miss rates across cells.

## Results  
- **Pass/fail split**: 43 677 programs pass public tests; 23 081 of these fail hidden tests.  
- **Weak verifier behavior**: Verifiers improve with richer scaffolding and stronger model families but still miss most bugs, yielding a 5 % false‑positive rate.  
- **GLM‑5.1 recovery**: Under the same evidence boundary, GLM‑5.1 recovers part of the gap between public pass and hidden failure detection.  
- **Inferability audit**: Remaining misses are a mix of verifier failures and limitations imposed by M1 evidence limits.

## Significance  
The work demonstrates that passing public tests does not guarantee safety, and that weaker LLM verifiers can still uncover many hidden bugs if properly configured. It also shows that adversarial pressure on test suites can degrade verification robustness, underscoring the importance of comprehensive monitoring strategies beyond simple pass/fail checks.

## Related Concepts  
- LLM‑generated code  
- Red teaming (adversarial testing)  
- Hidden bugs in software  
- Public‑test passing as a gate  
- Verifier scaffolding and model strength  
- AUROC, false‑positive rate, miss rates  
- Evidence boundary and inferability audit  
- M1 evidence limits
