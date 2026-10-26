# Summary: Running Kimi K3 on MI355X at Better Performance per Dollar Than B300
Saved: 2026-10-25
Source: 2026-08-02_RunningKimiK3onMI355XatBetterPerformanceperDollarT.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://www.wafer.ai/blog/kimi-k3-mi355x)

---

## Summary
This article details a benchmarking study by Wafer.ai demonstrating that AMD’s MI355X GPU offers superior performance per dollar compared to NVIDIA’s B300 and B200 configurations when serving the massive open-source model Kimi K3. Despite historical software support challenges for AMD hardware, recent improvements in kernel optimization and day-0 framework support have enabled the MI355X to achieve competitive throughput metrics. The study highlights that while NVIDIA retains a raw speed advantage in aggregate throughput, the significantly lower cost of AMD GPUs makes them a more economically viable option for deploying frontier-scale models with large memory requirements.

## Key Takeaways
- **Cost Efficiency Dominates Raw Speed**: While NVIDIA’s B300 nodes achieve higher aggregate throughput (1,568 tok/s) compared to the MI355X (952 tok/s), the MI355X provides 48 tok/s per dollar-hour versus 33 for the B300. This makes AMD hardware a compelling choice for cost-sensitive deployments where peak performance is less critical than budget efficiency.
- **Memory Capacity Enables Single-Node Deployment**: Kimi K3, with 2.8 trillion parameters, requires over 1.5TB of VRAM before context allocation. The MI355X’s 288GB HBM per GPU allows it to fit the model on a single node (TP8), whereas NVIDIA’s B200 nodes require a complex two-node tensor parallelism setup (TP16) that incurs significant cross-node communication latency penalties.
- **Software Gaps Are Closing**: The article notes that AMD previously suffered from slower kernels and poor day-0 support for inference frameworks. However, the availability of day-0 support for Kimi K3 on ROCm, combined with agent-driven kernel optimization tools like RadixArk’s Dspark, has mitigated these software hurdles, allowing near-out-of-the-box deployment success despite initial scheduler errors.

## Context
The article situates itself within a broader industry shift where open-source models like DeepSeek V4-Pro, GLM5.2, and Kimi K3 are reaching intelligence levels comparable to closed-source proprietary models such as Opus or Fable/Sol. As these models scale in parameter count—Kimi K3 at 2.8T parameters—the hardware requirements for serving them have exceeded the capacity of standard single-node setups using older NVIDIA architectures like the B200. This creates a specific niche for high-memory GPUs, where AMD’s focus on HBM capacity aligns with the needs of these ultra-large models, challenging NVIDIA’s dominance in the inference market by offering comparable hardware specs at significantly lower price points.

## Implications
This development signals a potential shift in AI infrastructure procurement strategies, particularly for organizations prioritizing cost-efficiency over absolute peak performance. By demonstrating that AMD hardware can serve frontier models effectively with better economics per dollar, the article suggests that the "software gap" barrier for non-NVIDIA GPUs is diminishing due to improved tooling and vendor support. This could encourage broader adoption of heterogeneous compute clusters in production environments, reducing reliance on NVIDIA’s ecosystem and fostering competition in the high-end AI hardware market. Furthermore, it highlights the importance of memory capacity as a critical differentiator for serving next-generation large language models, potentially influencing future GPU design priorities across vendors.
