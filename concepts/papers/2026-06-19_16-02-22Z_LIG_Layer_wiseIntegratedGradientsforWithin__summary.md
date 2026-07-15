title: "Summary: 2026-06-19_16-02-22Z_LIG_Layer_wiseIntegratedGradientsforWithin_LayerFl.md"
# Summary: 2026-06-19_16-02-22Z_LIG_Layer_wiseIntegratedGradientsforWithin_LayerFl.md
Saved: 2026-06-22 21:01
Source: 2026-06-19_16-02-22Z_LIG_Layer_wiseIntegratedGradientsforWithin_LayerFl.md
Model: None

---


## Summary  
The paper introduces LIG (Layer‑wise Integrated Gradients), a new XAI framework that analyses the flow of information within individual Transformer layers by treating each layer as a dynamic graph whose nodes are token representations and per‑head attention outputs. By applying set‑to‑set Integrated Gradients at the module boundaries—Multi‑Head Attention (ATT) and MLP—the authors extend traditional scalarized IG to map token sets, using an L2 scalarization that composes contributions in a Layer‑wise Relevance Propagation style. Their work demonstrates both agreement between module‑wise composition and layer‑whole attribution under the L2 criterion and reveals within‑layer information flow when separate ATT and MLP contributions are traced.  

## Key Contributions  
- [Finding 1] LIG extends Integrated Gradients from scalar‑objective to set‑to‑set maps via an L2 scalarization, enabling token‑to‑token attribution at each nonlinear module boundary.  
- [Finding 2] Experiments on BERT‑base and PTB show that configurations preserving within‑layer consistency use the target token’s embedding as the ATT baseline and either the ATT output at a=0 or Zero as the MLP baseline, achieving maximal agreement between layer‑wide and module‑wise attributions.  
- [Finding 3] LIG provides a diagnostic XAI tool that operates at module‑boundary granularity without requiring model retraining or per‑operation interpreter design.  

## Methodology  
The authors view each Transformer layer as a graph where nodes represent token embeddings and the outputs of Multi‑Head Attention (ATT) and MLP modules. LIG computes Integrated Gradients by mapping input token sets to output token sets at the ATT and MLP boundaries, applying an L2 scalarization that balances contributions across the set. This composition mimics Layer‑wise Relevance Propagation: each boundary’s IG contribution is conserved, allowing within‑layer flow analysis without altering the original model. The method aggregates these per‑boundary gradients to produce a layer‑wide attribution while also isolating individual module effects for diagnostic purposes.  

## Results  
On BERT‑base and PTB datasets, LIG reveals that models with high within‑layer consistency—those where the target token’s embedding serves as the ATT baseline and either the ATT output at a=0 or Zero is used for MLP—exhibit minimal disagreement between layer‑wide and module‑wise attributions. The method also isolates how information propagates through ATT versus MLP, providing quantitative traces of each contribution. These findings confirm that LIG’s set‑to‑set IG with L2 scalarization faithfully captures internal dynamics without model modification.  

## Significance  
LIG offers a practical XAI tool for probing the internal workings of Transformers at a granularity that aligns with their architectural boundaries, enabling researchers to understand and diagnose attention versus feed‑forward interactions without costly retraining or custom interpreters. By leveraging set‑to‑set IG and L2 scalarization, it bridges the gap between standard scalarized IG and the combinatorial nature of multi‑head models, fostering transparency in a widely used architecture.  

## Related Concepts  
- Integrated Gradients (IG) – a gradient‑based XAI method for attributing predictions to inputs.  
- Layer‑wise Relevance Propagation (LRP) – a technique that conserves attention across layers.  
- Set‑to‑set maps – mappings between sets of token representations, used here at module boundaries.  
- L2 scalarization – an optimization strategy that balances contributions from multiple outputs.  
- Dynamic graph representation – viewing a Transformer layer as a graph with nodes and edges representing attention and feed‑forward connections.
