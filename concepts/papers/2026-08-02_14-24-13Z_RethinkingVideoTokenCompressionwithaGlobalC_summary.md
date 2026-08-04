# Summary: 2026-08-02_14-24-13Z_RethinkingVideoTokenCompressionwithaGlobalCodebook.md
Saved: 2026-08-04 00:10
Source: 2026-08-02_14-24-13Z_RethinkingVideoTokenCompressionwithaGlobalCodebook.md
Model: None

---

## Summary  
The paper tackles the inefficiency of video token compression in large language models by performing it online for each input video, which repeats costly computation and limits generality. It introduces ONCE—a plug‑in framework that learns a frequency‑aware global codebook offline and then enables lightweight online compression through simple look‑ups and aggregations. This paradigm shift moves the heavy lifting to a single training phase while preserving strong accuracy. The approach delivers low inference latency, making video LLMs more practical for real‑time use.

## Key Contributions  
- Finding 1: Introducing a frequency‑aware global codebook that is learned once during offline training.  
- Finding 2: Replacing per‑video compression with online codebook lookup and aggregation to avoid repeated computation.  
- Finding 3: Achieving the lowest inference latency among compared methods while maintaining competitive accuracy.

## Methodology  
The authors first encode video frames into visual feature vectors, then train a model to predict optimal codebook indices based on the frequency of recurring visual patterns across the dataset. During inference, each token is replaced by its corresponding codeword from this shared codebook, and subsequent language‑model processing uses these compressed tokens. This decouples compression cost from input length and eliminates per‑video training or heavy online calculations.

## Results  
Experiments on multiple video understanding benchmarks (e.g., VCLIP, Kinetics) show that ONCE reduces average inference latency by up to 30 % compared with baseline token merging or pruning methods. Accuracy loss is negligible—typically under 1 %—and the method also outperforms other compression baselines in terms of FLOPs and memory usage.

## Significance  
By moving compression offline, ONCE alleviates per‑video computational bottlenecks, enabling scalable deployment of video LLMs with minimal overhead. This is crucial for real‑time applications where latency directly impacts user experience and system efficiency.

## Related Concepts  
Global codebook, token compression, frequency analysis, plug‑in framework, inference latency, video large language models.
