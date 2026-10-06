---
title: Programmatic Search Agents: Extending Agentic Search Beyond Query Reformulation
published: 2026-10-05T16:52:57Z
authors: Jiaming Qian, Huiyan Yang, Mandi Liu, Jie Liu, Wenkai Shen, Pengyang Zhou, Jing Jin, Jin Ma, Dezhi Ye, Chaochao Chen
url: http://arxiv.org/abs/2610.06689v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Programmatic Search Agents: Extending Agentic Search Beyond Query Reformulation

## Abstract
Search agents adapt their queries, yet fixed search interfaces leave candidate processing and evidence presentation outside the agent's direct control. Our trajectory analysis shows that supporting passages can be retrieved yet never delivered to the agent; a same-page oracle intervention shows that changing the returned evidence can reduce subsequent search. We introduce Programmatic Search Agent (PSA), which makes a local executable computation over candidates the unit of a search action. PSA unifies a persistent candidate workspace, flexible primitive composition, and selective evidence presentation. It incrementally generates program cells that reuse candidates, execute dependent operations, and select what the agent inspects next. The runtime resolves specified data dependencies within each cell, while the agent adapts its search strategy across cells as new evidence arrives. We compare PSA with the Query-based Agent and Tool-based Agent on InfoSeek-Eval and BrowseComp-Plus using five policy backbones without task-specific training. All three interfaces share the search substrate, and the Tool-based Agent also shares PSA's primitives and persistent workspace. Relative to the Query-based Agent, PSA improves macro-averaged task success by 4.00 and 7.56 percentage points on the two benchmarks, respectively; within-backbone reductions in final-step tokens average 28.3% and 33.9%. These results support extending agent control beyond query reformulation to the processing and presentation of retrieved evidence. Code will be released subject to approval.

## Metadata
- **Published**: 2026-10-05T16:52:57Z
- **Authors**: Jiaming Qian, Huiyan Yang, Mandi Liu, Jie Liu, Wenkai Shen, Pengyang Zhou, Jing Jin, Jin Ma, Dezhi Ye, Chaochao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06689v1)