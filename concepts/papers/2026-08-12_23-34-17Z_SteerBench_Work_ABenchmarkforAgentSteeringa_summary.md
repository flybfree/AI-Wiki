# Summary: 2026-08-12_23-34-17Z_SteerBench_Work_ABenchmarkforAgentSteeringatAction.md
Saved: 2026-08-13 21:31
Source: 2026-08-12_23-34-17Z_SteerBench_Work_ABenchmarkforAgentSteeringatAction.md
Model: None

---

## Summary  
SteerBench‑Work is a benchmark designed to evaluate the ability of large language model agents to make correct “steering” decisions at the boundaries between human‑reviewed and autonomous actions in diverse workplace domains such as developer operations, finance, legal, medical, HR, and security. The authors introduce an incident‑anchored dataset that pairs real public incidents with evidence‑reversed mirrors, providing a balanced set of steer‑proceed vs. hold labels to test both error directions equally. Their work shows that steering errors are highly directional: models frequently over‑hold authorized actions while rarely allowing unsafe ones, and performance degrades sharply on risk‑resolved commits when evidence is reversed. The study also reveals that higher‑capability models tend to be overly cautious at commit boundaries, suggesting a gap between general reasoning ability and precise boundary calibration.

## Key Contributions  
- [Finding 1] SteerBench‑Work provides an incident‑anchored, bidirectional benchmark with paired evidence‑reversed mirrors and near‑evenly split steer labels across multiple high‑stakes domains.  
- [Finding 2] Empirical analysis reveals that model failures are overwhelmingly one‑sided: models hold cleared work on ~28 % of opportunities and allow unsafe work on only ~1 %, indicating a systematic over‑refusal bias.  
- [Finding 3] The hardest cases involve risk‑resolved commits; models score markedly worse (63.8 %) on evidence‑reversed mirrors than on the original incidents, highlighting vulnerability to evidence manipulation.

## Methodology  
The authors constructed SteerBench‑Work by curating 106 scenarios from public workplace incidents, each annotated with a primary steer decision and its mirrored version where the evidence is reversed. Scenarios span developer operations, customer service, finance, legal, medical, HR, and security. A model receives the proposed action and available evidence, outputs a gate decision (proceed/hold), and is evaluated on whether it respects the correct boundary label. The benchmark includes calibration controls to ensure balanced error rates.

## Results  
Across 30 model conditions, the majority of failures occur in the “hold” direction, with models incorrectly holding authorized work on 28.1 % of opportunities while only 1.0 % involve allowing unsafe work. Performance on risk‑resolved commits drops to 98.5 % for original incidents but falls sharply to 63.8 % when evidence is reversed, underscoring the importance of accurate evidence handling.

## Significance  
SteerBench‑Work bridges a critical gap between general LLM reasoning and precise action‑boundary calibration, offering a standardized evaluation that can guide safer autonomous agents in high‑risk environments. By exposing systematic over‑refusal and sensitivity to evidence reversal, it informs model design and deployment strategies aimed at balancing safety with efficiency.

## Related Concepts  
- Agent steering / boundary decision making  
- Evidence‑reversed mirrors  
- Risk‑resolved commits  
- Calibration vs. general capability  
- One‑sided error bias
