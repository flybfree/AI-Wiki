# Summary: 2026-08-09_11-54-09Z_TheScaffoldingMattersMoreThantheInterface_AControl.md
Saved: 2026-08-10 23:20
Source: 2026-08-09_11-54-09Z_TheScaffoldingMattersMoreThantheInterface_AControl.md
Model: None

---

## Summary  
This paper investigates whether the cost of AI coding agent tool use is primarily driven by the scaffolding that enables it or by the interface through which it communicates with tools, using a controlled experiment across seven agent scaffoldings, five language models, and one fixed software task. The authors demonstrate that scaffolding has a significantly larger impact on computational cost than the choice between Model Context Protocol (MCP) and command-line interface (CLI), challenging existing estimates by more than an order of magnitude. Their findings reveal that MCP is often unnecessary for certain tasks and can dramatically increase costs, especially when agents fail to follow assigned interfaces. The study emphasizes the importance of verifying actual behavior over self-reported outputs.

## Key Contributions  
- [Finding 1] The cost of tool use in AI coding agents is far more heavily influenced by agent scaffolding than by the interface (MCP vs CLI), with some scaffoldings being up to 28 times more expensive than others.  
- [Finding 2] Two of the seven scaffolds do not support MCP at all and complete tasks using only CLI, proving that MCP is unnecessary for this specific task and significantly cheaper when used alone.  
- [Finding 3] The cost variation across scaffoldings can span up to 139x for a small local model (27B parameters), highlighting the high sensitivity of computational costs to scaffolding design.

## Methodology  
The authors conducted a controlled experiment by running six operations against a private online git repository using seven different agent scaffolds and five language models. They used Model Context Protocol (MCP) as one interface and standard CLI commands as another, verifying task completion by inspecting the actual state of the repository rather than relying on the agent’s self-reported progress. The same task was repeated multiple times to assess consistency. The experiment was designed to isolate scaffolding effects from interface effects while ensuring full reproducibility.

## Results  
The results show that MCP introduces substantial overhead: runs with MCP cost between 5.0x and 28x more than CLI-only runs, depending on the scaffold. The two scaffolds without MCP support were consistently cheaper, ranging from 5.0x to 28x less expensive. When comparing MCP to CLI within the same scaffold, cost ratios spanned an extreme range of 0.43x to 29x, with outliers suggesting instability in performance. Both interfaces had similar failure rates (12.9% for MCP, 2.2% for CLI), indicating that failures are not systematically worse with MCP but are equally common. Agents often ignored assigned interfaces, meaning self-reported data is unreliable.

## Significance  
This study challenges the assumption that interface choice (MCP vs CLI) is the primary driver of cost in AI coding agents. Instead, it reveals that scaffolding—how tools and environments are structured to support the agent—has a far greater impact on computational efficiency. The findings suggest that optimizing scaffolding could reduce costs more effectively than switching interfaces. It also underscores the need for rigorous verification methods over self-reported outputs.

## Related Concepts  
- Model Context Protocol (MCP)  
- Command-line Interface (CLI)  
- Agent Scaffolding  
- Computational Cost Analysis  
- AI Coding Agents  
- Verification vs. Self-reporting
