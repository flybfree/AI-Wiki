# Summary: 2026-08-07_01-39-36Z_Policy_MaskedPrivateExperts_AuditableandReversible.md
Saved: 2026-08-09 22:34
Source: 2026-08-07_01-39-36Z_Policy_MaskedPrivateExperts_AuditableandReversible.md
Model: None

---

## Summary  
The authors introduce **Policy‑Masked Private Experts**, a technique that lets a sparse Mixture‑of‑Experts (MoE) model enforce a trusted computing base (TCB) by freezing the public expert branch and training a disjoint private expert branch. The key claim is that under the declared TCB, unauthorized requests execute no private experts while the public model retains full semantic capability, providing an auditable and reversible control over which trained parameters are reachable during inference. This work demonstrates that execution‑level access can be separated from task utility without degrading performance on downstream benchmarks.

## Key Contributions  
- [Finding 1] Policy‑Masked Private Experts enable a narrow but testable claim: within the TCB, private experts are never executed by unauthorized requests, yet the public model’s functionality remains intact.  
- [Finding 2] Experiments on Qwen3‑30B‑A3B and DeepSeek‑V2‑Lite show zero private execution across 64 adversarial scenarios and 96 deny/fail‑closed events; independent hooks precisely match routed private rows, confirming exact control.  
- [Finding 3] The disjoint expert branch improves exact tool use by 5.0 pp (p = 0.03125) and external evaluation utility by 21.3 pp (95 % CI [13.3, 29.3]), while a parameter‑matched LoRA yields similar gains but leaves 1,225 adapter calls under deny.

## Methodology  
The authors freeze a pretrained sparse MoE model and train an additional expert branch that is never used by the public path. Before top‑k routing, they select either the public or private pool of experts based on a policy mask. The system records which private rows are actually executed via custom hooks, enabling both auditing (verification) and recovery (allow‑deny‑allow). Experiments compare this approach to parameter‑matched LoRA adapters and post‑hoc request gates, measuring exact tool use, external evaluation bias, and performance gains.

## Results  
Unauthorized private execution is zero in all 64 adversarial tests and 96 deny/fail events; the hook matches exactly 11,616 routed private rows. The disjoint expert branch raises exact tool‑use accuracy by 5.0 pp (one‑sided Holm p = 0.03125) and external evaluation utility by 21.3 pp (95 % CI [13.3, 29.3], Holm p = 0.000031). A parameter‑matched LoRA achieves comparable external gains but incurs 1,225 denied calls; the policy‑masked method leaves none. DeepSeek reproduces the route invariant and gains 27.0 pp on a benchmark. Sealed evaluation shows near‑neutral impact.

## Significance  
This work provides an auditable, reversible mechanism to restrict access to newly trained parameters without sacrificing model utility, addressing a critical security gap in MoE systems. It proves that execution control can be decoupled from task capability, enabling trustworthy AI deployments where only authorized parameter paths may run.

## Related Concepts  
MoE (Mixture‑of‑Experts), sparse routing, trusted computing base (TCB), policy masking, reversible access control, external evaluation bias, parameter‑matched LoRA adapters, adversarial testing, auditability.
