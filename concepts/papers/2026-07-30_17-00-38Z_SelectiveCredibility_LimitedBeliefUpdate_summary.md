# Summary: 2026-07-30_17-00-38Z_SelectiveCredibility_LimitedBeliefUpdate.md
Saved: 2026-07-30 22:21
Source: 2026-07-30_17-00-38Z_SelectiveCredibility_LimitedBeliefUpdate.md
Model: None

---

## Summary  
The paper introduces **selective credibility‑limited belief update**, a new framework that allows an agent to incorporate only part of an epistemic input per source world by first transforming the input into a weaker proxy before applying credibility restrictions. It provides both semantic and axiomatic characterizations of the resulting class of update operators, thereby extending standard belief‑update theory beyond the indivisible‑input assumption. The framework identifies two well‑behaved sub‑classes—consistency‑preserving and maximal consistency‑preserving operators—that capture how agents can selectively accept evidence based on source reliability. By showing that credibility‑limited belief update is a special case of this model and that Katsuno–Mendelzon update emerges when restrictions are removed, the authors demonstrate a unified and strictly more expressive account of belief updating.

## Key Contributions  
- Introduces selective credibility‑limited belief update as a transformation of epistemic inputs into weaker proxies.  
- Provides semantic and axiomatic characterizations of the class of update operators, distinguishing consistency‑preserving from maximal consistency‑preserving sub‑classes.  
- Shows that credibility‑limited belief update is a special case of the framework and Katsuno–Mendelzon update emerges when restrictions are removed.

## Methodology  
The authors begin with conventional belief‑update models where an epistemic input is treated as a single, indivisible proposition. They formalize **credibility limits** that apply per source world, meaning only certain successor worlds are regarded as credible. To respect these limits while still allowing partial information incorporation, they define a **transformation function** that maps each original input to a proxy that is credible only when the original input is consistent. By analyzing this mapping they derive properties of the resulting update operators and identify sub‑classes with specific behavioral guarantees.

## Results  
The framework yields a class of operators where consistency preservation holds whenever the transformed proxy is credible, guaranteeing that agents never adopt false beliefs from inconsistent inputs. A maximal version further requires the proxy to be maximally informative among all credible consequences of the original input, providing the strongest possible belief update under credibility constraints. Theoretical derivations confirm that removing credibility restrictions yields Katsuno–Mendelzon belief update, confirming the generality and expressiveness of the model.

## Significance  
This unified model clarifies how agents can selectively accept parts of evidence based on source reliability, offering a theoretically grounded alternative to treating epistemic inputs as monolithic. It enables more realistic epistemic dynamics in AI by supporting source‑dependent selective acceptance and providing precise conditions under which belief updates remain consistent with credibility limits.

## Related Concepts  
- Belief update  
- Katsuno–Mendelzon belief update  
- Credibility‑limited belief update  
- Consistency preservation  
- Proxy transformation  
- Selective acceptance  
- Epistemic input decomposition
