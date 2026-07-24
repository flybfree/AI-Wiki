# Summary: 2026-07-20_13-49-51Z_TowardsAgenticAgent_basedModels_Feasibility_Perfor.md
Saved: 2026-07-24 00:24
Source: 2026-07-20_13-49-51Z_TowardsAgenticAgent_basedModels_Feasibility_Perfor.md
Model: None

---

## Summary  
This paper investigates how embedding large‑language‑model (LLM) decision‑making into classic agent‑based models affects their reliability, computational cost, and observable behavior. By extending the Schelling segregation model in Mesa ABMs with a single LLM‑enabled agent that classifies neighbors via tool calls, the authors demonstrate a minimal yet controllable setting where LLM‑driven actions can be evaluated statistically. The work shows that while larger LLMs perform well, smaller ones often fail or become operationally unusable, and that statistical model checking provides quantitative insight into the impact of such hybrid components.

## Key Contributions  
- [Finding 1] Feasibility: a hybrid agent‑based system can be built where ordinary agents follow symbolic rules while one agent delegates classification to an LLM via tool calls.  
- [Finding 2] Performance: smaller LLMs either misclassify neighbors or generate excessive tool calls, rendering the agent ineffective; larger models pass the initial checks.  
- [Finding 3] Statistical model checking: MultiVeStA can estimate classical ABM observables (e.g., segregation fraction) and quantify how LLM integration alters them.

## Methodology  
The authors start with Mesa’s Schelling segregation model, a standard ABM where agents update their location based on the proportion of same‑type neighbors. They integrate MultiVeStA, a statistical model checker for discrete systems, to monitor observable variables. In the hybrid setup, most agents use the classic symbolic rule (e.g., “move if > 50 % of neighbors are of my type”). One agent is programmed to receive natural‑language descriptions of its neighbors and invoke LLM‑based tools that increment counters for similar or different neighbors; these counters feed back into the original happiness calculation. This approach isolates the semantic and operational effects of LLM decisions without altering the rest of the simulation.

## Results  
Experiments with locally served LLMs of varying sizes reveal a clear size threshold: models under ~70 M parameters often produce incorrect classifications or generate hundreds of tool calls per step, causing crashes or slowdowns. Models around 130–250 M parameters complete the required classification within acceptable latency and maintain correct counter updates. Statistical model checking reports that the segregation fraction changes by only a few percent when using the larger LLM agents versus pure symbolic agents, indicating a modest impact on observable behavior.

## Significance  
The study provides a practical framework for assessing how AI‑augmented ABMs behave under formal verification tools. By quantifying performance trade‑offs and reliability metrics, it helps researchers design hybrid systems that retain the interpretability of classic models while leveraging LLM capabilities responsibly.

## Related Concepts  
agent‑based modeling, large language models, statistical model checking (MultiVeStA), tool calls, hybrid agents, Mesa ABM library, Schelling segregation rule, natural‑language interface, counter‑based decision making.
