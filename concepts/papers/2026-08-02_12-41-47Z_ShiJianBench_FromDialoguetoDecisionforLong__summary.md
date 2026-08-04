# Summary: 2026-08-02_12-41-47Z_ShiJianBench_FromDialoguetoDecisionforLong_Horizon.md
Saved: 2026-08-03 23:27
Source: 2026-08-02_12-41-47Z_ShiJianBench_FromDialoguetoDecisionforLong_Horizon.md
Model: None

---

## Summary  
The paper introduces ShiJianBench, an offline evaluation framework that tracks how conversational investment advisors shape long‑horizon investor behavior under realistic market feedback. By simulating thousands of matched investor trajectories and measuring outcomes on three complementary axes—investor side, service side, and content side—the authors demonstrate a clear gap between high‑quality responses and effective long‑term intervention. Their work provides the first systematic audit of advisor language’s downstream impact, moving evaluation from isolated dialogue quality to holistic decision pathways.

## Key Contributions  
- Finding 1: A calibrated multi‑agent investor simulator with evolving state variables, motive‑driven deliberation, long‑term memory, and dialogue‑grounded updates is built to mimic real user behavior.  
- Finding 2: The framework evaluates advisor policies using separate investor‑side, service‑side, and content‑side metrics under a hard compliance gate, revealing distinct performance dimensions.  
- Finding 3: Experiments on Chinese fund‑market traces (2021–2026) show that the top LLM advisors excel at personalized content yet only a subset deliver superior long‑horizon investment outcomes.

## Methodology  
The authors approached the problem by constructing an offline, matched‑trajectory simulator calibrated against behavioral data from 7,199 real users. Advisor policies are injected into this system and observed for their influence on investor decisions as market conditions evolve. The evaluation is performed under a fixed historical feedback loop, allowing separation of content quality (service side), user engagement (investor side), and compliance with investment advice (content side). This design isolates the long‑horizon pathway from short‑term response metrics.

## Results  
Experiments reveal that while the leading advisor group produces substantially higher‑quality personalized content, only a minority achieve competitive investor‑side trajectory outcomes. The service‑side metric (conversation relevance) is high across all top advisors, yet the investor‑side metric (long‑term portfolio performance) remains weak for many. This systematic distinction confirms that producing a high‑quality response does not guarantee effective long‑horizon intervention.

## Significance  
ShiJianBench shifts investment advisor evaluation from isolated dialogue quality to a comprehensive assessment of real‑world decision impact, informing more robust regulatory and design standards. By exposing the gap between content excellence and behavioral outcomes, it guides developers toward advisors that truly align with investor goals over time.

## Related Concepts  
- Conversational AI  
- Multi‑agent simulation  
- Long‑horizon evaluation  
- Investor behavior modeling  
- Market feedback loops  
- LLM performance metrics
