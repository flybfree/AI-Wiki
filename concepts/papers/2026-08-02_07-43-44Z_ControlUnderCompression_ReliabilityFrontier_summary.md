# Summary: 2026-08-02_07-43-44Z_ControlUnderCompression_ReliabilityFrontiersforToo.md
Saved: 2026-08-03 20:39
Source: 2026-08-02_07-43-44Z_ControlUnderCompression_ReliabilityFrontiersforToo.md
Model: None

---

## Summary  
Tool‑using language‑model agents rely on persistent system‑side instructions that define tools, arguments, policies and execution protocols; these are called ACCs (Agent Control Contexts). While compressing ACCs can lower input cost, existing prompt‑compression studies have not demonstrated whether the resulting control remains operationally reliable. The authors introduce **CompressAgent**, a comprehensive benchmark that evaluates nine independently constructed ACCs across multiple task families and model identifiers under six retained‑context budgets, revealing a nonlinear, method‑dependent reliability frontier.

## Key Contributions  
- [Finding 1] Reliability of compressed ACCs follows a sharp, non‑linear decline as the retained context budget drops from 75 % to 35 %, with generic rewriting and section‑based compression remaining near the full‑context baseline (≈92.7 % and 92.4 %) but falling below 40 % at lower budgets.  
- [Finding 2] The reliability frontier varies dramatically across ACCs, making a single universal compressor ranking unsuitable; some ACCs become fragile even at modest retention levels.  
- [Finding 3] Failure modes are dominated by tool‑execution and action‑parsing errors rather than prompt‑level misunderstandings, indicating that compression primarily breaks the runtime pipeline.

## Methodology  
The authors built an environment‑verified benchmark called **CompressAgent**. It comprises nine distinct ACCs organized into three task families, each tested with six retained‑context budgets (10 %, 25 %, 35 %, 50 %, 75 %, 90 %). The study runs 15,525 experiments using six Qwen API model identifiers to capture model‑specific behavior. By measuring success rates on executable outcomes, the authors quantify how compression impacts reliability in a controlled setting.

## Results  
At 75 % retained context, generic rewriting achieved 92.7 % and section‑based compression 92.4 % success, only ~1.3 % below the full‑context baseline of 93.8 %. When retention falls to 35 %, performance collapses: generic rewriting drops to 47.0 %, section‑based to 39.0 %, and a third method (obligation‑aware) to 19.9 %. Further reductions below 35 % push many methods into the sub‑20 % range, where executable protocols become fragile. The failure analysis consistently shows tool‑execution and action‑parsing errors as the primary cause of compression‑induced failures.

## Significance  
These findings recast ACC compression from a token‑reduction problem to a runtime reliability issue that must be evaluated through observable execution outcomes. Because reliability varies non‑linearly with retention and differs across ACCs, universal compressor rankings are inappropriate; instead, per‑context qualification is required. The work highlights the need for systematic testing of compression methods in executable environments rather than relying solely on prompt‑level metrics.

## Related Concepts  
- Tool‑using language‑model agents  
- Agent Control Contexts (ACCs)  
- Prompt compression / context retention budgets  
- Reliability frontier  
- Tool execution errors  
- Action parsing failures
