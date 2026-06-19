---

title: c# - What does new () mean? - Stack Overflow
date: 2026-05-03
url: https://stackoverflow.com/questions/4236854/what-does-new-mean
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://stackoverflow.com/questions/4236854/what-does-new-mean
scraped: "2026-05-03 16:36"

---

## Summary

Placeholder summary — please add a concise summary of this article.



# c# - What does new () mean? - Stack Overflow

**Source**: [Original Article](https://stackoverflow.com/questions/4236854/what-does-new-mean)

## Full Article

Collectives™ on Stack Overflow
Find centralized, trusted content and collaborate around the technologies you use most.
Learn more about Collectives
Stack Internal
Knowledge at work
Bring the best of human thought and AI automation together at your work.
Explore Stack Internal
What does new() mean?
Ask Question
Asked
15 years, 5 months ago
Modified
12 years, 9 months ago
Viewed
12k times
17
There is an
AuthenticationBase
class in WCF RIA Services. The class definition is as follows:
// assume using System.ServiceModel.DomainServices.Server.ApplicationServices

public abstract class AuthenticationBase<T> 
    : DomainService, IAuthentication<T> 
    where T : IUser, new()
What does
new()
mean in this code?
c#
generics
new-operator
Share
Improve this question
Follow
edited
Mar 24, 2012 at 9:17
[Abel's user avatar]
Abel
57.6k
25
25 gold badges
161
161 silver badges
260
260 bronze badges
asked
Nov 21, 2010 at 7:21
[synergetic's user avatar]
synergetic
8,116
11
11 gold badges
69
69 silver badges
110
110 bronze badges
Add a comment
|
3 Answers
3
Sorted by:
Reset to default
Highest score (default)
Trending (recent votes count more)
Date modified (newest first)
Date created (oldest first)
28
It's the
new constraint
.
It specifies that
T
must not be
abstract
and must expose a
public
parameterless
constructor
in order to be used as a
generic type argument
for the
AuthenticationBase<T>
class.
Share
Improve this answer
Follow
edited
Jul 20, 2013 at 0:04
answered
Nov 21, 2010 at 7:24
[Frédéric Hamidi's user avatar]
Frédéric Hamidi
264k
43
43 gold badges
497
497 silver badges
488
488 bronze badges
Sign up to request clarification or add additional context in comments.
1 Comment
Add a comment
Jon Skeet
Jon Skeet
Over a year ago
Teeny weeny correction: a type must have those features in order to be used as a generic type
argument
.
T
is the generic type
parameter
, but the type which is actually used, (e.g.
object
,
int
) is the type argument.
2010-11-21T08:18:20.387Z+00:00
2
Reply
Copy link
7
Using the new() keyword requires a default constructor to be defined for said class. Without the keyword, trying to class new() will not compile.
For instance, the following snippet will not compile. The function will try to return a new instance of the parameter.
public T Foo <T> ()
// Compile error without the next line
// where T: new()
{
    T newInstance = new T();
    return newInstance;
}
This is a generic type constraint. See this
MSDN article
.
Share
Improve this answer
Follow
edited
Nov 21, 2010 at 7:30
answered
Nov 21, 2010 at 7:23
[AK.'s user avatar]
AK.
763
7
7 silver badges
14
14 bronze badges
Comments
Add a comment
5
It means that a type used to fill the generic parameter
T
must have a public and parameterless constructor.  If the type does not implement such a constructor, this will result in a compile-time error.
If the
new()
generic constraint is applied, as in this example, that allows the class or method (the
AuthenticationBase<T>
class in this case) to call
new T();
to construct a new instance of the specified type.  There is no other way, short of reflection (this includes using
System.Activator
, to construct a new object of a generic type.
Share
Improve this answer
Follow
answered
Nov 21, 2010 at 7:24
[cdhowie's user avatar]
cdhowie
173k
25
25 gold badges
305
305 silver badges
326
326 bronze badges
Comments
Add a comment
Your Answer
Draft saved
Draft discarded
Sign up or
log in
Sign up using Google
Sign up using Email and Password
Submit
Post as a guest
Name
Email
Required, but never shown
Post Your Answer
Discard
By clicking “Post Your Answer”, you agree to our
terms of service
and acknowledge you have read our
privacy policy
.
Start asking to get answers
Find the answer to your question by asking.
Ask question
Explore related questions
c#
generics
new-operator
See similar questions with these tags.
The Overflow Blog
Time is a construct but it can still break your software
Dispatches from O'Reilly: Fast Paths and Slow Paths
Featured on Meta
(Almost) One year of Challenges
Linked
4
Inheritance in C#, what does where T: new()  mean?
2
What does new() mean in this case?
2
What does new() mean in this context
1
Base Class Generic Arguments Clarification
0
New() in constructor
405
What does "where T : class, new()" mean?
2
What does "T : new()" mean with generics?
1
Reference - What does this symbol mean in C#?
Related
14
What does new() do in `where T: new()?`
10
What is the purpose of new() while declaration of a generic class?
39
What does 'new' keyword mean when used inside an interface in C#?
4
What is the purpose of new() when defining a generic?
6
What is this new[] a shorthand for?
4
new() in method
2
What does "T : new()" mean with generics?
2
Using the new keyword
2
C# need explanation on new constraint (new T(...))
16
What is new without type in C#?
Hot Network Questions
Is using AI tools (ChatGPT, Claude, etc.) for self-studying mathematics a good idea?
TikZ mark line end with x
Help for exercise 2.4 of Rijke’s Introduction to Homotopy type theory
How to run script as cronjob that requires sudo?
When and where did the 19-inch standard for rack-mount servers originate?
How to download Blender for Intel Macs?
POSIX: Regular Expression: "\(a\(b\)*\)*\2" matches "abab"
In parallel RLC circuit, how will the current through a capacitor change when a source connected in parallel with circuit is removed instantaneously?
Why did a Fedora update break my unicode U.S. flag symbol?
How to plot a curved line a cross the thickness of the beams
X and Z axes swapped between N-panel and 3D View
Handling the MediaWiki rate limit with `WikipediaData` link mapping methods
How to open Microsoft Edge in Windows 11 to a specific Workspace via commandline?
Is this Bartók or Penderecki?
What is Quine referring to here
Were the docking interfaces for Gemini 8 and the Agena Target Vehicle ever mated before launch?
Lords Spiritual: French translation for their robes
Investigating what is possibly an obsolete word meaning 'keep silent'; 'refrain from speaking'
When was the first magical crystal mine?
Coordinates of a vector not taken from the origin
Is there any benefit from writing homomorphisms on the same side as the module/group action?
How would you make Weeping Angels in Mutants and Masterminds 3rd edition?
Preemptive warning for a False Vacuum bubble
Origin of commutator of two operators
more hot questions
Question feed
lang-cs

## Metadata
- **Source URL**: https://stackoverflow.com/questions/4236854/what-does-new-mean
