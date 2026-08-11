# Summary: 2026-08-09_11-54-09Z_TheScaffoldingMattersMoreThantheInterface_AControl.md
Saved: 2026-08-10 23:21
Source: 2026-08-09_11-54-09Z_TheScaffoldingMattersMoreThantheInterface_AControl.md
Model: None

---

## Summary  
The paper investigates whether the cost of interacting with AI coding agents is driven primarily by the scaffolding that enables tool access rather than the interface (MCP vs CLI) used. It conducts a controlled experiment comparing seven different agent scaffoldings across five language models on a single software task: six operations against a private git repository. By verifying repository state rather than trusting self‑reports, the authors isolate the effect of scaffolding on cost and reliability.  

## Key Contributions  
- [Finding 1] The dominant cost driver is the scaffolding; two scaffoldings lacking MCP support are 5–28× cheaper than those with MCP, even when using only CLI.  
- [Finding 2] Cost varies dramatically across scaffolds: for a small local model, expenses range from 0.43× to 29× between paired runs, showing high variability.  
- [Finding 3] Failure rates are similar on both interfaces (12.9% vs 2.2%), indicating that interface choice does not reduce errors but may inflate monetary waste.  

## Methodology  
The authors defined a fixed task requiring six git operations in a private repository. They deployed five language models (including a 27‑billion‑parameter local model) under seven distinct agent scaffoldings, each exposing either an MCP server or a plain CLI. All runs were logged and the final repository state was inspected to confirm completion. The experiment measured monetary cost per operation and compared MCP vs CLI usage across scaffolds.  

## Results  
Cost estimates for MCP‑enabled runs ranged from 0.43× to 29× higher than comparable CLI runs, with outliers on both ends. Two scaffoldings without MCP completed the task using only CLI at a fraction of the cost. The small local model showed the greatest variability (139× across scaffolds). Failure rates were comparable between interfaces.  

## Significance  
These findings challenge the assumption that interface choice is the primary cost factor, highlighting instead that scaffolding architecture has a far larger impact on resource consumption and reliability. They also demonstrate that reported cost differences are often unreliable due to unverified agent behavior, urging rigorous verification in AI tool evaluation.  

## Related Concepts  
- Model Context Protocol (MCP)  
- Command‑line Interface (CLI)  
- Agent scaffolding  
- Cost of computation  
- Failure rate  
- Open‑source benchmarking
