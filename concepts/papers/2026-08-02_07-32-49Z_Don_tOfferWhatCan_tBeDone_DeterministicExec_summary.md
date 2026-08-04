# Summary: 2026-08-02_07-32-49Z_Don_tOfferWhatCan_tBeDone_DeterministicExecutabili.md
Saved: 2026-08-03 20:38
Source: 2026-08-02_07-32-49Z_Don_tOfferWhatCan_tBeDone_DeterministicExecutabili.md
Model: None

---

## Summary  
The paper tackles the problem that a production‑grade LLM agent must select from a large library of skills while respecting both semantic relevance and the current account state; otherwise it may offer a skill that is impossible to execute. It introduces a deterministic executability gate that removes any candidate whose internal hard‑stop condition cannot be satisfied under the present account context, ensuring only executable skills reach the LLM’s decision point. This two‑stage pipeline cuts the amount of skill‑description text fed to the model by roughly 90 % while preserving downstream behavior.

## Key Contributions  
- Finding 1: The gate eliminates about 59.4 % of skill‑message pairs that would otherwise be blocked because both the skill and the LLM evaluate the same exit predicate, preventing non‑executable candidates from being considered.  
- Finding 2: By pruning the context, the system reduces skill‑description token consumption to 9.5 % of the full ten‑skill exposure, saving 228.8 million tokens in a production run of 756.6 K messages.  
- Finding 3: Counterfactual replay with all ten skills exposed shows that only 7.8 % (78 out of 1,000) of conversations involve the model selecting a blocked skill, indicating gating does not alter downstream outcomes.

## Methodology  
The authors built a three‑stage pipeline for Helpmate’s customer‑care assistant. First, a recall‑oriented semantic matcher selects messages related to a ten‑skill domain family without consulting account state. Second, a deterministic gate evaluates each candidate skill against the same exit predicates used by the LLM and discards those that cannot complete under the current account state. Finally, the LLM chooses among the remaining candidates. The pipeline was evaluated on 756.6 K user messages across 267.6 K conversations.

## Results  
Semantic matching retained 174,927 messages (≈23.1 % of total). Within that stream, the gate removed 1,039,462 skill‑message pairs (59.4 %). This reduced the skill‑description context by 90.5 % relative to exposing all ten skills per message. In a controlled replay with full exposure, the model selected a production‑blocked skill in only 78 of 1,000 conversations (7.8 %), confirming that gating does not affect model behavior.

## Significance  
Pruning non‑executable skills lowers computational load and memory usage, improves reliability by ensuring the LLM never receives or selects an impossible action, and scales the skill library to millions of entries without performance degradation.

## Related Concepts  
Semantic matching, deterministic gating, exit predicates, account state constraints, token cost reduction, counterfactual testing, LLM skill selection, Helpmate, Wix customer‑care assistant.
