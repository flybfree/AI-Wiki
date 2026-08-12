---
title: Tim Gowers: What sort of maths are LLMs good at?
date: 2026-08-12
url: https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/
source_feed: Hacker News
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-08-12 06:10
---

# Tim Gowers: What sort of maths are LLMs good at?

## Full Article

Gowers's Weblog
Mathematics related discussions
«
Thoughts about the Leiden Declaration
What sort of maths are LLMs good at?
For the sake of anyone who might read this blog post in the distant future (a month from now, say), let me mention that I am writing it a few days after OpenAI announced that it had solved ten major problems in mathematics and theoretical computer science, including the first construction of a non-sofic group, and a proof that the multicolour Ramsey number
[R(3,3,...,3)]
(where there are
[k]
3’s) grows superexponentially in
[k]
. The first was, to judge from various talks I have been to, one of the most important unsolved problems in group theory, and the second was a major open problem in Ramsey theory that I didn’t necessarily expect to see solved in my lifetime, though of course such expectations now have to be revised. The reason I want to be clear about the timing is that I shall be discussing the current capabilities of LLMs in the full expectation that those will continue to change rapidly. So it is likely that in not too long from now, if there is anything interesting in what I write, it will be interesting mainly as a record of what the situation looked like in early August 2026.
These results, and the other eight on the list, are extraordinarily impressive, but it still doesn’t seem to be the case that LLMs are better than all humans at all aspects of mathematics. If they were, then their big speed advantage over us would mean that there would be much more of a flood of results. So it is natural to wonder about what kinds of problems LLMs are good at, and about where there is still room for improvement. I don’t pretend to have a good answer to this question, where a good answer would be a crisp classification that would fit the current examples well, but it is an interesting exercise to try to rule out some bad answers, and to try to identify potential answers that aren’t obviously contradicted by the evidence.
Are LLMs particularly good at finding counterexamples?
A first remark here is that LLMs are not just good at finding counterexamples: they can find proofs of difficult statements as well. However, it is notable that the most famous problems they have solved have almost all been with counterexamples rather than proofs. That is true of the two problems mentioned above, and also of the Jacobian conjecture and the unit distance conjecture.
If one wants to theorize that LLMs are particularly good at finding counterexamples, then there are two things it would be good to do to make the theory more convincing. The first may sound unproblematic: it is to decide when solving a problem counts as finding a counterexample. Once that is sorted out, the second is to come up with a potential explanation of why LLMs would be particularly well suited to solving problems of that particular kind.
What does it mean to find a counterexample?
Why am I suggesting that it is not completely obvious what it means to find a counterexample? Surely, one might suggest, all it means is that you have a statement of the form “Every object of such and such a type has such and such a property,” and you exhibit an object of the given type that does not have the given property.
However, this doesn’t always work. Consider a famous result of Vinogradov, which states that every sufficiently large positive integer is a sum of three primes. The negation of this statement is (or is equivalent to) the statement that for every positive integer
[N]
there exists an integer
[n\geq N]
such that
[n]
is not a sum of three primes. In other words, it states that every positive integer
[N]
has a certain property. Seen in this light, Vinogradov found an example of a positive integer
[N]
that does
not
have the given property. Do we want to say that Vinogradov found a counterexample? Clearly not — the result should obviously be classified as a theorem and not a counterexample.
Thus, we cannot just naively say that LLMs are particularly good at negating universally quantified statements: there has to be something about the
nature
of the universal quantification. With the three-primes example, it is clear that Vinogradov did not think,  “How am I going to find
[N]
with this property?” Rather, what he thought would have been more like, “I’ve got an integer
[n]
that is very large. How am I going to show that it is a sum of three primes?” In other words, all his focus would have been on the universally quantified
[n]
, with the existentially quantified
[N]
being a sort of afterthought once the details of the proof have been worked out.
In general, many interesting results, when they are stated formally, begin with an alternation of two or three (or more) quantifiers. The question then becomes to determine which is the first “interesting” quantified variable in some sense. Here’s another example to illustrate the point, from the theory of finite-dimensional normed spaces. I’ll give a few mathematical details for those curious, but if you don’t care about those, then you can skip the next three paragraphs and should get the gist of what I am saying about this example.
Let
[X]
and
[Y]
be two
[n]
-dimensional normed spaces and let
[T]
be a linear map from
[X]
to
[Y]
. We say that
[T]
is a
[C]
–
isomorphism
if there exists
[\lambda>0]
such that
[\lambda|x|\leq|Tx|\leq C\lambda|x|]
for every
[x\in X]
. By rescaling we can always take
[\lambda]
to be 1, in which case we have that
[|x|\leq|Tx|\leq C|x|]
for every
[x\in X]
. If
[C=1]
, then this tells us that
[T]
is an isometry. In general, the
Banach-Mazur distance
[d(X,Y)]
between
[X]
and
[Y]
is defined to be the smallest
[C]
such that there exists a
[C]
-isomorphism from
[X]
to
[Y]
. It is easy to see that the logarithm of the Banach-Mazur distance is a metric on the set of isometry classes of
[n]
-dimensional normed spaces. A less easy fact, but still not too hard, is that the resulting metric space is compact: in fact, it is known as the Banach-Mazur compactum.
It is natural to wonder what the diameter of the Banach-Mazur compactum is, and here things get interesting. A result of Fritz John states that every
[n]
-dimensional space
[X]
has distance at most
[\sqrt n]
from
[\ell_2^n]
. (The idea of the proof is as follows: pick inside the unit ball of
[X]
an
[n]
-dimensional ellipsoid of maximal volume; that is the unit ball of a normed space
[Y]
that is isometric to
[\ell_2^n]
; it can be shown that the identity map is a
[\sqrt n]
-isomorphism between
[X]
and
[Y]
.) From Fritz John’s theorem and the (multiplicative) triangle inequality, it follows that
[d(X,Y)\leq n]
for any two
[n]
-dimensional normed spaces. That is, the diameter of the Banach-Mazur compactum is at most
[n]
. But might it be substantially less than that?
An indication that the answer is not obvious comes from looking at the spaces
[\ell_1^n]
and
[\ell_\infty^n]
. The identity map between these two spaces is an
[n]
-isomorphism, but one can do much better by mapping the standard basis vectors not to themselves but to vertices of the unit cube, with the vertices chosen to be as orthogonal as possible. In particular, if there exists an
[n\times n]
Hadamard matrix, then the corresponding linear map is a
[\sqrt n]
-isomorphism. One can push this observation and deduce that for any
[p,q\in[1,\infty]]
the Banach-Mazur distance between
[\ell_p^n]
and
[\ell_q^n]
is
[O(\sqrt n)]
. It is also easy to show that
[d(\ell_1^n,\ell_2^n)=\sqrt n]
, so
[\ell_p]
-spaces hardly improve on the easy lower bound, and do not improve on it at all in dimensions
[n]
for which an
[n\times n]
Hadamard matrix exists.
In 1981, Gluskin famously solved the problem by determining the correct asymptotics for the diameter of the Banach-Mazur compactum. Informally, what he showed was that the diameter is within a constant of the upper bound that follows immediately from Fritz John’s theorem. If we make the quantification explicit, then the statement we end up with is
[\exists c>0\ \forall n\ \exists X,Y\in K_n\ d(X,Y)\geq cn]
,
where I have written
[K_n]
for the set of all
[n]
-dimensional normed spaces. (If you want to argue that it is not a set, then let me specify in addition that the underlying vector space is
[\mathbb R^n]
.) In words, there is a positive constant
[c]
such that for every positive integer
[n]
there are
[n]
-dimensional normed spaces
[X]
and
[Y]
such that the Banach-Mazur distance between
[X]
and
[Y]
is at least
[cn]
.
I can’t continue without very briefly describing the beautiful and highly influential idea Gluskin had for solving this problem. He took
[X]
and
[Y]
to be normed spaces whose unit balls were random symmetric convex sets defined as follows: take the standard basis vectors and a handful of other random unit vectors, as well as the negatives of all these vectors, and take the convex hull. Gluskin then showed that if two normed spaces are chosen from this distribution, then with high probability their Banach-Mazur distance is at least
[cn]
.
But back to the main point, which is that the logical form of the above statement is very similar to the logical form of Vinogradov’s theorem, which is
[\exists N\ \forall n\geq N\ \exists p_1,p_2,p_3\in P\ \ p_1+p_2+p_3=n]
where I have written
[P]
for the set of primes. And yet, Vinogradov’s result is unquestionably a theorem, while Gluskin’s result is unquestionably a counterexample, or at least an example.
What is the important difference between the two statements? It seems to be that in Vinogradov’s three-primes theorem the number
[n]
plays a more essential role in the statement that is to be proved about the various quantified variables. In Vinogradov’s theorem, that statement is
[n=p_1+p_2+p_3]
, whereas for Gluskin’s theorem the statement to be proved is
[\dim X = \dim Y = n]
and
[d(X,Y)\geq cn]
,
which we can write equivalently as
[\dim X = \dim Y = n]
and
[d(X,Y)\geq c\dim X]
.
In the case of Vinogradov’s theorem, the whole challenge is to get those three primes to add up to
[n]
, whereas for Gluskin it is not remotely challenging to get the dimensions of
[X]
and
[Y]
to equal
[n]
: the challenge is to get
[X]
and
[Y]
to be very far from each other, relative to their common dimension.
There is a further complication to bear in mind here, which is that via the process known as Skolemization, a universally quantified statement of the form
[\forall x\in X\ \exists y\in Y\ \ P(x,y)]
can be converted into an existentially quantifed statement
[\exists f:X\to Y\ \forall x\in X\ \ P(x,f(x))]
. (For this to be an equivalence one needs the axiom of choice, but it is certainly a sufficient condition.) This is not just a piece of logical trickery, but it often reflects quite accurately how we think about some problems. For instance, it is more natural to think of Gluskin’s example as a recipe for constructing (or at least proving the existence of) a pair of suitable normed spaces for any given dimension
[n]
, or in other words to construct a suitable function from
[\mathbb N]
to pairs of normed spaces by giving its value at each
[n]
, than it is to think of it as a statement that says that every positive integer $n$ has a certain complicated property.
Yet another complication is that some universally quantified statements follow naturally from existentially quantified statements, or may even be equivalent to them. For example, the theorem that a 2-dimensional torus is not homeomorphic to a 2-dimensional sphere is an existentially quantified statement (every map from the torus to the sphere fails to be a homeomorphism), but the natural way to prove it is to prove the existential statement that there is an invariant that distinguishes the two spaces. For an example of where a universal statement is equivalent to an existential statement, consider a statement of the form that a vector
[x\in\mathbb R^n]
does not belong to the convex hull of a certain compact set
[A]
. The statement that no convex combination of elements of
[A]
is equal to
[x]
is equivalent to the existence of a linear functional
[\phi:\mathbb R^n\to\mathbb R]
and a
[\lambda\in\mathbb R]
such that
[\phi(x)>\lambda]
and
[\phi(a)\leq\lambda]
for every
[a\in A]
. In both these cases it feels natural to regard the result as a theorem that is proved via an existential statement, perhaps because it is the theorem that is ultimately what interests us. But using “what interests us” as a criterion to determine what counts as a counterexample seems a little vague, and seems to be a difficult criterion to use if we want to explain convincingly why AI should be good at finding counterexamples.
A more general argument against the notion that there is something about existential statements that is particularly suited to AI is that the need to establish existential statements pervades almost all of mathematical research, regardless of the nature of the headline result being aimed for. For example, if I want to prove a statement by induction, I may well look for a strengthening of the statement that serves better as an inductive hypothesis. Or if I want to prove that every object of type
[T]
with property
[P]
also has property
[Q]
, then I may well look for a property
[R]
that follows from
[P]
and can be used to prove
[R]
. These are more metamathematical existence problems, but the distinction can be somewhat blurred, and more importantly, when trying to prove a statement
[S]
, it is often the case that the main question in our minds is less, “Why is
[S]
true?” and more, “What could a proof of
[S]
be like?” To give an example, I feel I understand pretty well why Goldbach’s conjecture is true — a highly plausible probabilistic model of the primes implies it and agrees closely with computational data — but if I were making a serious attempt to prove it, that understanding, which many mathematicians have had for a century or so, would be of limited help. Rather, my main task would be to try to find proof techniques that were powerful enough to make these heuristic ideas rigorous.
What is the difference between an example and a counterexample?
Logically, every statement of the form
[\exists x\ P(x)]
is a counterexample to the universally quantified statement
[\forall x\ \neg P(x)]
. However, we do not describe all existential statements as counterexamples. For example, if I were to say, “The
[\ell_p]
-spaces with
[1\leq p<\infty]
are all separable, as is
[c_0]
, but
[\ell_\infty]
is not separable,” I would not describe the second part of that assertion as a counterexample to the claim that all Banach spaces are separable. Rather, I would present it as probably the most basic example of a non-separable space. The important point seems to be that there was no particular reason to think that all Banach spaces would be separable, and finding an example of a non-separable space is not very difficult.
I think the first point is more important here: we are more inclined to call an object a counterexample if the existence of that object disproves a statement that we had quite good reason to believe. It often happens that after repeated unsuccessful attempts to prove a statement, mathematicians begin to feel that it has no particular reason to be true, even if it seems to be hard to come up with a counterexample to it. In such a situation, if a counterexample is eventually found, it may have lost something of its “counter” feel. My impression is that the construction of a non-sofic group comes into this category. There have been several proposals in the literature for how one might construct such a group, and I don’t think there were many (or even any?) experts who strongly believed that all groups were sofic. So it feels more natural to say, “OpenAI came up with the first example of a non-sofic group” than to say, “OpenAI found a counterexample to the soficity conjecture” (despite the fact that that section of their paper is entitled “A counterexample to the soficity conjecture”).
Likewise, it seems to me that the new lower bound for multicolour Ramsey numbers is more of an example than a counterexample. I think quite a lot of people believed that the bound should be exponential, so for them it was a counterexample, but others, myself included, were more neutral about it. As a matter of fact, I have worked on the problem in the past (a long time ago) in an equivalent formulation, which asks how many triangle-free graphs on
[n]
vertices you need if you want their union to be the complete graph
[K_n]
. If you take bipartite graphs, then it’s easy to see that you need
[\log_2n]
of them, but that bound can be improved if instead you observe that a complete 5-partite graph can be written as a union of two triangle-free subgraphs, and therefore it is possible to write the complete graph as a union of
[2\log_5n]
triangle-free graphs. It is then tempting to try to do better, with triangle-free graphs that are less dense but that make up for it with unbounded chromatic number — a necessary condition if one wishes to use a sublogarithmic number of graphs, which is equivalent to showing a superexponential lower bound for
[R(3,3,\dots,3)]
. All this is to say that when I worked on the problem, my efforts were concentrated on what turned out to be the right direction, so for me OpenAI found an example of what I (weakly) expected, rather than a counterexample.
Where does this leave us?
I would like to find a coherent explanation of the conjunction of the following facts.
The most notable mathematical results proved by LLMs have tended to be ones that we would classify as examples or counterexamples, where counterexamples are, broadly speaking, existence statements that disprove statements that we expected to be true.
Many statements can be formulated as existence statements when we would usually think of them as universal statements, and vice versa, so what we consider to be an example depends on the mathematical context of a statement as well as its logical form.
LLMs are pretty good at proving universal statements as well: it’s just that the strongest statements they have proved that we would think of as theorems have mainly not been at the level of the strongest statements that we would think of as counterexamples.
Given these facts, it seems likely that what LLMs are good at is something else, which happens to have as a consequence that they are good at the kind of existence problem that we would normally classify as asking to find a non-trivial example.
Let us consider two things that we can be confident that LLMs are good at. One of them is knowing a lot of mathematics: if a problem can be solved by means of a relatively standard argument, it is highly likely that an LLM will be able to find and use that argument. The other is the ability that an LLM has simply by virtue of being a computer: it can work at huge speed (compared with humans at least) and can therefore afford to make a large number of unsuccessful attempts at a problem before it finds a solution.
Without even looking at what LLMs have actually managed to solve, one might guess that these two features would lead to their having a somewhat different style from human mathematicians. Very roughly, LLMs would have the edge when there is more of a probabilistic element to the proof-finding process: they would be good at problems for which the best method is to try a lot of ideas, not necessarily particularly novel, until at some point you get lucky. Humans on the other hand would be better (for the moment) at finding more “surprising” and “conceptual” arguments, where the appropriate method is to dig deeper and deeper into a problem until the solution reveals itself. (It is hard to say exactly what this means, but I hope that any experienced researcher reading this will know what I am talking about.)
This raises two questions: does the guess above correspond at all to the reality that we are observing, and is there any reason to suppose that what I have tentatively described as the “LLM style” of doing mathematics would lead naturally to LLMs discovering several counterexamples (or just examples) to long-standing conjectures, even if that was by no means all they could do?
I don’t pretend to have a scientific answer to either question, but the reactions of experts to several of the remarkable solutions that ChatGPT has found do lend some support to the idea that LLMs work in more of a try-lots-of-things-till-you-get-lucky way. People often seem to react by saying something like, “Initially I was amazed that the problem had been solved, but on closer inspection I realized that the approach was actually not all that novel, and one that with the right small hint a suitably expert human could have found quite easily.”
For the second question — whether the LLM style is well suited to finding (counter)examples — I think matters are less clear, because there are many ways of searching for a counterexample, and some of them fit better than others the style I have described. Here are a few general methods. (I don’t claim that the list is exhaustive.)
Look for an off-the-shelf example
. Here one has a stock of fairly standard examples and one simply tries them out one after another to see whether any of them fails to satisfy the given statement. For example, Ryan O’Donnell ends his wonderful book on the analysis of Boolean functions with some tips, one of which is, “If you have a conjecture about Boolean functions, test it on dictators, majority, parity, tribes (and maybe recursive majority of 3). If it’s true for these functions, it’s probably true.”
Build an example from basic examples and standard construction methods.
For an algebraic problem, for instance, one might start with some standard examples, but then take products or quotients or limits.
Make heavy use of metavariables.
The word “metavariable” comes from computer science, and in particular from automatic theorem proving, and refers to the practice that in mathematics would correspond to writing, “where
[x]
is to be chosen later,” (in which case
[x]
is the metavariable). In a paper we usually do this only in fairly simple situations such as when we need to choose a number
[\epsilon>0]
that is small enough for later arguments to work. But when we search for an example of an object
[x]
that satisfies some property
[Q]
(which may well be a conjunction of simpler properties
[Q_1,\dots,Q_k]
), it is often not a good strategy to specify
[x]
completely and only then to check whether it satisfies
[Q]
. Instead, it can be more fruitful to do almost the opposite: we start by saying virtually nothing about
[x]
and simply launch into proving that it satisfies
[Q]
. In the course of doing so, we find that we need
[x]
to satisfy a property
[P_1]
. If we are lucky we can describe in a nice way a very general class of objects
[x]
that satisfy
[P_1]
. For instance, we may be able to find a parametrized class: we identify some function
[f]
and show that
[f(y)]
satisfies
[P_1]
for every
[y]
of a certain type. The problem is then reduced to finding
[y]
such that $Q(f(y))$ holds, which is a more specific version of the original problem. There may be many iterations of this process, or a mixture of this process and other processes, before an example is eventually found.
Try to prove the opposite.
If one wishes to find
[x]
such that
[Q(x)]
, it can be surprisingly helpful to start by attempting to prove the statement
[\forall x\ \neg Q(x)]
. The reason this can be helpful is that using our standard methods of attempting to prove something, we may end up identifying a key lemma that would suffice: that is, we may find an intermediate property
[R]
that implies
[\neg Q]
in a non-trivial way and thus reduce the problem
[\forall x\ \neg Q(x)]
to
[\forall x\ R(x)]
. Turning things round again, it may well then be that finding a counterexample to
[R]
is easier than finding a counterexample to
[\neg Q]
(that is, an example that satisfies
[Q]
). Of course, there is no guarantee that a counterexample to
[R]
will be an example of
[Q]
, but sometimes we are lucky and it is. More often, we can use the idea of the previous method, noting that it is at least a necessary condition of an example of
[Q]
that it should not be an example of
[R]
, so one can try to describe a general class of objects that fail
[R]
and in that way reduce the problem.
Successive approximation.
Sometimes, when we are searching for an example of
[x]
such that
[Q(x)]
, we write down a moderately plausible guess
[x_0]
not because we think it has a chance of working (if we did, then we would be using the first strategy), but because we hope that if
[x_0]
does not satisfy
[Q]
, then we will be able to diagnose what went wrong and specify a new guess
[x_1]
that does not have that defect. Again, this strategy can either be iterated or combined with one or more of the other strategies.
Just-do-it proofs.
Sometimes we need
[x]
to satisfy infinitely many properties
[Q_1,Q_2,\dots]
, each of which is, individually, quite easy to sa

## Metadata
- **Source**: [Original Article](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/)
