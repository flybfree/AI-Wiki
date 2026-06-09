# Summary: 2026-05-05_17-55-25Z_OpenSeeker_v2_PushingtheLimitsofSearchAgentswithIn.md
Saved: 2026-05-07 23:04
Source: 2026-05-05_17-55-25Z_OpenSeeker_v2_PushingtheLimitsofSearchAgentswithIn.md
Model: None

---

## Summary  
This paper introduces OpenSeeker-v2, a search agent trained using only supervised fine-tuning (SFT) with a minimal dataset of 10.6k data points, demonstrating that informative and high-difficulty trajectories can significantly enhance the performance of frontier Large Language Model agents without requiring costly pre-training or reinforcement learning pipelines. The authors achieve state-of-the-art results across four benchmarks using a simple SFT approach, challenging the assumption that advanced search capabilities necessitate resource-intensive training procedures. Their work opens the door for academic teams to develop competitive search agents independently, reducing reliance on industrial-scale infrastructure.  

## Key Contributions  
- [Finding 1] OpenSeeker-v2 achieves state-of-the-art performance (46.0%, 58.1%, 34.6%, and 78.0%) across four benchmarks—BrowseComp, BrowseComp-ZH, Humanity’s Last Exam, and xbench—outperforming the industry-standard Tongyi DeepResearch pipeline that uses CPT+SFT+RL.  
- [Finding 2] The authors demonstrate that scaling knowledge graph size, expanding tool set diversity, and applying strict low-step filtering can create high-quality training trajectories with minimal data, enabling effective SFT without heavy pre-training.  
- [Finding 3] This is the first SOTA search agent within its model scale (30B) and paradigm (ReAct) developed purely by an academic team using only SFT, proving that industrial pipelines are not strictly necessary for frontier performance.  

## Methodology  
The authors constructed a dataset of 10.6k high-difficulty trajectories by modifying three simple data synthesis techniques: increasing knowledge graph size to provide richer contextual information, expanding the tool set to include diverse functionalities (e.g., web search, code execution), and filtering out low-step trajectories that lack meaningful progress. These modifications allowed them to generate a structured, informative dataset suitable for supervised fine-tuning. The model was trained using only SFT on this curated data, avoiding pre-training or reinforcement learning. The ReAct paradigm—where agents alternate between reasoning steps and tool use—was maintained throughout training and evaluation.  

## Results  
OpenSeeker-v2 achieved 46.0% accuracy on BrowseComp (English), 58.1% on BrowseComp-ZH (Chinese), 34.6% on Humanity’s Last Exam, and 78.0% on xbench. These results surpass Tongyi DeepResearch’s performance on all benchmarks, which reached 43.4%, 46.7%, 32.9%, and 75.0%, respectively. The key finding is that SFT with carefully designed informative trajectories can match or exceed the performance of complex pipelines like CPT+SFT+RL when data quality is optimized.  

## Significance  
This paper significantly reduces the barrier to entry for frontier search agent research by proving that academic teams can achieve competitive results without industrial-grade resources. It challenges the prevailing belief that deep search capabilities require massive pre-training and RL, encouraging a shift toward efficient, data-driven fine-tuning approaches. By open-sourcing the model weights and methodology, the authors promote transparency and reproducibility in AI research.  

## Related Concepts  
- Large Language Model (LLM) agents  
- Supervised Fine-Tuning (SFT)  
- Reinforcement Learning (RL)  
- ReAct paradigm  
- Knowledge graph scaling  
- Tool set expansion  
- High-difficulty trajectories  
- SOTA performance benchmarking

[[2026-05-05_17-55-25Z_OpenSeeker_v2_PushingtheLimitsofSearchAgentswithIn.md]]