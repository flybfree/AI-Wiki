# Summary: 2026-08-10_01-32-34Z_Multi_agentdiscoveryofpracticalquantumLDPCcodes.md
Saved: 2026-08-10 23:32
Source: 2026-08-10_01-32-34Z_Multi_agentdiscoveryofpracticalquantumLDPCcodes.md
Model: None

---

## Summary  
The paper proposes a multi‑agent discovery framework aimed at finding practical finite‑length quantum low‑density parity‑check (qLDPC) codes that meet hardware constraints such as block length ≤ 400 and weight ≤ 10. By integrating specialist proposal, persistent memory, long‑horizon evolution of executable programs, and deterministic evaluation in a closed loop, the framework explores a search space built from coset‑orbit balanced‑product constructions. The agents generate candidate codes that include bicycle and lifted‑product families as well as non‑normal subgroup actions. This structured agentic search yields concrete finite‑length candidates with competitive rate–distance performance for all considered weight classes.

## Key Contributions  
- Finding 1: Discovery of a [[288, 16, 18]] code at weight 7 and a [[288, 18, 18]] code at weight 9, both achieving leading rate–distance performance.  
- Finding 2: Identification of structurally distinct high‑performing constructions, including a [[336, 12, ≤24]] candidate and a [[368, 18, 16]] code, realized as balanced‑product codes with non‑normal subgroup actions.  
- Finding 3: Demonstration that the discovered codes exhibit low logical failure rates under depolarizing noise when decoded via a common BP‑OSD protocol.

## Methodology  
The authors built an artificial‑intelligence driven multi‑agent system where each agent specializes in proposing new code parameters or reviewing existing proposals. Agents retain persistent scientific memory, allowing long‑term tracking of candidate performance across generations. Programs are executable and evaluated deterministically within a closed loop, restricting the search to binary CSS codes that satisfy the practical constraints. The framework systematically samples cosine‑orbit balanced‑product constructions, ensuring coverage of both normal and non‑normal subgroup actions.

## Results  
The multi‑agent pipeline produced a set of finite‑length qLDPC candidates covering all weight classes up to 10. For each class it identified codes with either the best known rate–distance or competitive performance. The most notable instances are [[288, 16, 18]] (w=7), [[288, 18, 18]] (w=9) and [[234, 28, 18]] (w=10). Additional candidates include a [[336, 12, ≤24]] code and a [[368, 18, 16]] code. Decoding experiments with BP‑OSD under depolarizing noise show logical failure rates well below random guessing levels.

## Significance  
These results provide hardware‑relevant finite‑length qLDPC candidates that can be directly tested in experimental platforms, reducing the gap between theory and practice. The structured agentic search methodology demonstrates how AI‑driven scientific discovery can efficiently explore combinatorial design spaces, offering a scalable approach for future code optimization.

## Related Concepts  
qLDPC codes, low‑density parity‑check codes, CSS codes, balanced‑product constructions (bicycle, lifted‑product), coset‑orbit actions, non‑normal subgroup actions, multi‑agent AI frameworks, persistent memory, closed‑loop search, BP‑OSD decoding, depolarizing noise.
