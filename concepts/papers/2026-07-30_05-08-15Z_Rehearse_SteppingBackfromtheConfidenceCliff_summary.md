# Summary: 2026-07-30_05-08-15Z_Rehearse_SteppingBackfromtheConfidenceCliffinSelf_.md
Saved: 2026-07-30 20:26
Source: 2026-07-30_05-08-15Z_Rehearse_SteppingBackfromtheConfidenceCliffinSelf_.md
Model: None

---

## Summary  
The paper investigates the “confidence cliff” observed in autoregressive self‑improving machine‑learning agents, where their ability to judge promising modifications deteriorates as loops progress. It quantifies this decline using two public AutoSOTA logs and a controlled benchmark of 39 tasks with 296 modification pairs. The authors introduce Rehearse, a lightweight skill that curates ideas, compares them before execution, runs the most promising one, and judges later using only similar past attempts and outcomes to mitigate the cliff.

## Key Contributions  
- Finding 1: The fraction of helpful modifications drops from 70 % in the first two iterations to 43 % by iteration 6+ across public AutoSOTA logs.  
- Finding 2: An LLM judge without history achieves 79.5 % accuracy on same‑baseline pairs where strict consensus returns a verdict, but this selective accuracy falls from 82.8 % to 56.9 % later in the loop.  
- Finding 3: Rehearse’s focused outcome memory raises late selective accuracy to 83.5%, improving endpoint performance across three tasks.

## Methodology  
The authors analyze AutoSOTA logs and a controlled benchmark, measuring judge accuracy before each training run. They implement Rehearse as a loop skill that proposes several ideas, compares them using rationales, selects the most promising based on early consensus, executes it, and judges later using only similar past attempts and outcomes.

## Results  
Over 4,000 budgeted training runs across nanochat, image classification, and time‑series forecasting, Rehearse improves endpoint performance under the same budget. The selective accuracy metric rises from 56.9 % to 83.5%, confirming that focused outcome memory mitigates the confidence cliff.

## Significance  
This work reveals a systematic degradation in autoregressive agent reliability that can hinder progress despite unchanged training budgets, offering a practical mitigation strategy (Rehearse) and highlighting the need for better confidence management in self‑improving systems.

## Related Concepts  
- Autoresearch  
- Confidence cliff  
- Selective accuracy  
- Outcome memory  
- Self‑improving ML agents
