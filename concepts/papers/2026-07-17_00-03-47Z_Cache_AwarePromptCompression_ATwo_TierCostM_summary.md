# Summary: 2026-07-17_00-03-47Z_Cache_AwarePromptCompression_ATwo_TierCostModelfor.md
Saved: 2026-07-23 23:51
Source: 2026-07-17_00-03-47Z_Cache_AwarePromptCompression_ATwo_TierCostModelfor.md
Model: None

---

## Summary  
This paper investigates the trade‑offs between prompt caching and compression in LLM API usage, showing that naive query‑aware compression can degrade cache hit rates. The authors develop a two‑tier cost model to quantify these effects on Anthropic’s Sonnet 4.6 service. They propose Cache‑Aware Prompt Compression (CAPC), which combines query‑agnostic compression with explicit cache control and a ratio bound. Experiments across multiple production workloads demonstrate CAPC as the most cost‑effective strategy while preserving quality within 0.05 tokens.  

## Key Contributions  
- [Finding 1] The empirical analysis reveals that Sonnet’s cache exhibits a two‑tier structure with a sharp threshold near 3,500 tokens, yielding a hit rate of ~0.83 below this limit across repeated calls.  
- [Finding 2] Query‑aware compression mechanically invalidates the strict prefix cache on every call, causing high cost at high compression ratios (r≥6), whereas CAPC’s ratio bound keeps prefixes in the hot tier.  
- [Finding 3] CAPC achieves the lowest total cost among four strategies—cache‑only, query‑aware compression, vanilla, and CAPC—with mean savings of up to 90% over vanilla while maintaining quality within 0.05 tokens.  

## Methodology  
The authors first characterize Sonnet’s two‑tier cache architecture by measuring hit rates across a series of API calls with varying token lengths and compression ratios (r). They then construct a cost model that combines the discounted rate for cached prefixes (rho) with the token count saved by compression. To evaluate strategies, they implement four variants: (1) cache‑only, (2) query‑aware compression without CAPC, (3) vanilla (no caching), and (4) CAPC which enforces a tier‑preserving ratio bound. Experiments are conducted on LongBench‑v2 benchmark and three real production workloads: an enterprise assistant with a 94k‑token schema prefix, a graphify RAG pipeline using FastAPI/httpx, and the public tau‑bench retail dataset (50 tasks). The model predicts cost savings for each configuration before running experiments to validate predictions.  

## Results  
Across LongBench‑v2, CAPC yields mean token savings of 49% versus cache‑only, 64% versus query‑aware compression, and 90% versus vanilla. In the enterprise assistant workload (r=3), CAPC reduces cost by 51.7%. The graphify RAG pipeline shows a 2.4× speedup on httpx compared to cache‑all and a 9.3× improvement over cache‑only in FastAPI. On tau‑bench, CAPC is the cheapest strategy with reward equal to vanilla (36/50) while query‑aware compression incurs +40.1% cost relative to vanilla, confirming the negative ROI prediction of the crossover model.  

## Significance  
This work provides a practical two‑tier cost framework that bridges theory and production deployment, enabling developers to choose compression strategies without sacrificing cache efficiency. By preventing over‑compression from pushing prefixes into the hot tier, CAPC offers a scalable solution for large language model services where token budgets are tight. The findings also validate earlier negative ROI predictions on public benchmarks, encouraging more conservative compression policies in real systems.  

## Related Concepts  
- Prompt caching (discounted rate for reused token prefixes)  
- Prompt compression (reducing token count via query‑aware methods)  
- Two‑tier cache architecture with a sharp threshold near 3,500 tokens  
- Query‑aware compression and its cache invalidation impact  
- Cache‑aware prompt compression (CAPC) strategy  
- Cost model combining rho and compression ratio  
- Production workloads: LongBench‑v2, enterprise assistant schema, graphify RAG pipeline, tau‑bench retail benchmark
