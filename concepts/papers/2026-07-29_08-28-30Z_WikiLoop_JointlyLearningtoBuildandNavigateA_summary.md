# Summary: 2026-07-29_08-28-30Z_WikiLoop_JointlyLearningtoBuildandNavigateAgent_Na.md
Saved: 2026-07-29 20:30
Source: 2026-07-29_08-28-30Z_WikiLoop_JointlyLearningtoBuildandNavigateAgent_Na.md
Model: None

---

## Summary  
WikiLoop proposes a unified framework that simultaneously learns to construct and navigate an agent‑native Wiki—a persistent linked‑page knowledge base—by coupling the two tasks through downstream feedback. The contribution is a role‑conditioned shared policy that lets a Navigator retrieve evidence for queries while a Builder proposes edits whose utility is measured by changes in navigation performance. By training sequentially on role‑specific objectives and then jointly optimizing over homogeneous batches, WikiLoop achieves higher answer correctness than previously reported approaches.

## Key Contributions  
- Jointly learning both construction and navigation within a single shared policy, eliminating the need for separate models or baselines.  
- Introducing a sufficiency‑before‑efficiency objective that penalizes retrieval cost only after full evidence collection, ensuring completeness before efficiency gains are rewarded.  
- Using utility‑driven evaluation: a frozen Navigator scores candidate edits by their impact on downstream navigation and applies a guard penalty to prevent regressions on unrelated queries.

## Methodology  
The authors employ Qwen3.5‑9B as the common backbone for both interfaces. Training proceeds in two stages: first, each role (Navigator and Builder) is optimized individually using its own loss; second, a joint stage merges role‑homogeneous batches to refine a single shared policy. The Navigator follows a retrieval‑cost penalty after evidence completeness, while the Builder’s loss combines utility differences with a guard term that discourages harmful edits.

## Results  
WikiLoop reaches an aggregate Answer Correctness of 62.6 on AuthTrace, exceeding LLM‑Wiki base by 6.3 points and showing the largest gains on multi‑document queries. Controlled experiments confirm that both objectives are learned: the final shared policy retains role‑specific capabilities, improves Navigator performance by 0.4 points relative to specialist baselines, and consolidates construction and querying into one model. Moreover, edits generated in a held‑out evaluation remain useful for navigation, and WikiLoop outperforms LLM‑Wiki on HotpotQA and MuSiQue without dataset‑specific fine‑tuning.

## Significance  
By bridging knowledge construction and querying through downstream feedback, WikiLoop enables agents to maintain a self‑sustaining wiki that continuously improves with use. This approach reduces the need for external data pipelines, lowers retrieval costs, and yields higher overall answer quality—key benefits for scalable AI assistants and long‑term knowledge management.

## Related Concepts  
- Agent‑native Wiki (persistent linked‑page knowledge base)  
- Retrieval‑augmented agents  
- Sufficientity‑before‑efficiency objective  
- Role‑conditioned shared policy  
- Downstream feedback for construction evaluation  
- Joint learning across heterogeneous tasks  
- LLM‑Wiki baseline models (LLM‑Wiki base)  
- HotpotQA and MuSiQue benchmark datasets
