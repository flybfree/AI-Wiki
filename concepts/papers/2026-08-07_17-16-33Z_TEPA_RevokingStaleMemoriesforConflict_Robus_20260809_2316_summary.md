# Summary: 2026-08-07_17-16-33Z_TEPA_RevokingStaleMemoriesforConflict_RobustLangua.md
Saved: 2026-08-09 23:16
Source: 2026-08-07_17-16-33Z_TEPA_RevokingStaleMemoriesforConflict_RobustLangua.md
Model: None

---

## Summary  
Long‑term memory is essential for language agents to reuse past facts and preferences, but its persistence can introduce “memory pollution” when newer evidence contradicts older entries. TEPA (Revoking Stale Memories) tackles this problem by treating each observation as a keyed precedent that carries an explicit validity state, allowing the system to revoke outdated precedents when fresh data arrives. This mechanism enables agents to maintain a truthful retrieval set while preserving a full audit trail of revoked memories for later re‑promotion. The work demonstrates that revocable evidence is not merely a theoretical improvement but a practical solution that dramatically reduces stale memory errors under real‑world drift conditions.

## Key Contributions  
- [Finding 1] TEPA defines memory as a collection of keyed precedents with an explicit validity flag, turning “active” memories into falsifiable states.  
- [Finding 2] The revocation operation removes stale active precedents from the retrieval set when a contradictory fresh observation is observed under the same key, preventing memory pollution.  
- [Finding 3] Empirical experiments across hidden‑regime drift, real file‑backed executable drift, and preference‑update streams show that TEPA maintains near‑perfect recall (≈0.95) whereas append‑only or last‑write‑wins fall below random performance (≈0.21–0.30).

## Methodology  
The authors model a language agent’s memory as a map where each observation is stored under a unique key and labeled either *active* or *revoked*. When a new observation arrives with the same key, TEPA checks its validity: if the fresh evidence contradicts the active entry, it marks the old entry revoked and inserts the new one as active. Retrieval queries only consider entries whose validity flag is true, while all revoked entries are logged for audit and can be re‑activated later. The system is integrated into a MemoryAgentBench suite to evaluate single‑hop fact consolidation under controlled drift scenarios.

## Results  
Across 50 random seeds of hidden‑regime drift, TEPA achieved a recall score of 0.95, whereas append‑only and last‑write‑wins fell to 0.21 and 0.30 respectively (both below the random baseline). Real file‑backed executable drift produced comparable results: TEPA = 0.95, append‑only = 0.203, no‑memory = 0.298. On the clean MemoryAgentBench SH‑6k benchmark, TEPA’s performance matched a strong last‑write‑wins cache, confirming that current‑key replacement is the decisive operation for fact consolidation. Boundary tests on multi‑hop and very long‑context MemoryAgentBench settings revealed retrieval‑chain and context‑selection bottlenecks beyond simple validity tracking.

## Significance  
Memory pollution threatens agents’ ability to falsify outdated knowledge, erode trust, and hinder auditability. TEPA introduces a lifecycle revocation operation that makes truthfulness an explicit state, enabling agents to discard stale evidence cleanly while retaining a complete history for later re‑promotion. This approach is crucial for any system where factual accuracy must evolve with the world, such as autonomous assistants or scientific reasoning tools.

## Related Concepts  
- Memory pollution: degradation caused by active memories that newer conflicting evidence has superseded.  
- Active vs. stale memory: distinction between entries currently usable and those superseded.  
- Last‑write‑wins / append‑only strategies: traditional conflict resolution methods without explicit validity tracking.  
- Keyed precedents: representation of observations as key‑value pairs with state flags.  
- Retrieval chain: sequence of memory accesses that can be bottlenecked by invalid entries.  
- Context selection: mechanism for choosing which context to retrieve from a long‑term store.
