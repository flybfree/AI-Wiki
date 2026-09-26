# Summary: 2026-09-24_06-24-16Z_WhereDoesExactly_OnceLive_Model_Harness_andTool_Co.md
Saved: 2026-09-24 21:29
Source: 2026-09-24_06-24-16Z_WhereDoesExactly_OnceLive_Model_Harness_andTool_Co.md
Model: None

---

## Summary  
This paper investigates where exactly-once behavior should be enforced in tool-using large language model (LLM) agents: within the agent’s decision-making model, the harness that orchestrates its actions, or the tool contract defining service interactions. The authors introduce LIMBO, a deterministic sandbox environment with realistic tools and fault models, to empirically test how different components contribute to duplicate side effects when write operations fail or time out. Their analysis reveals that exact-once guarantees are fragile and context-dependent, depending on whether in-flight actions can be detected and on the availability of idempotency keys under various failure modes.

## Key Contributions  
- [Finding 1] Frontier LLM models exhibit near-zero duplication rates (0.5%) when immediate read-backs confirm write completion, but duplicate in up to 74% of episodes when actions cannot be verified due to lost acknowledgments or transport errors.  
- [Finding 2] The tool contract significantly influences duplication: contracts that support idempotency keys reduce duplicates from 28% to 4%, proving that key-based recovery is more effective than waiting alone, especially under heavy-tailed delays.  
- [Finding 3] No verification-only policy can guarantee exactly-once behavior without a bounded in-flight time limit; waiting per episode (e.g., an hour) is insufficient for reliable idempotency across all fault scenarios.

## Methodology  
The authors constructed LIMBO, a six-service sandbox with twelve injected fault modes—including late commits, redelivery, and partial batches—to simulate real-world service failures. Each episode involves a tool-using agent executing actions that may time out or fail, while a ledger tracks committed effects to detect duplicates. The study spans 25,930 episodes across nine recent LLM models, three production harnesses, two contract variants (with and without idempotency keys), and fifteen recovery conditions. Agents are graded on whether they duplicate effects that were already committed.

## Results  
When immediate read-backs confirm write completion, duplication occurs only 0.5% of the time across frontier models, with explanations accounting for 53% of variance. However, when actions cannot be verified—such as during lost acknowledgments or transport errors—the same models duplicate in 56–74% of episodes, and contract design explains 81% of this variation. Waiting per episode reduces duplicates from 28% to 4%, but only because agents use idempotency keys when available; without keys, waiting fails under long delays.

## Significance  
This research clarifies that exactly-once behavior in LLM agent tool interactions is not inherent but emergent and fragile, depending on model capability, harness design, and contract robustness. It highlights the critical role of idempotency keys over passive retry mechanisms and underscores the need for bounded in-flight time assumptions to avoid costly duplicates.

## Related Concepts  
- Idempotency key  
- Exactly-once semantics  
- Tool-use agent  
- In-flight action detection  
- Fault-tolerant systems  
- Deterministic sandbox testing
