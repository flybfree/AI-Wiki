---

title: What is the Difference Between `new object()` and `new {}` in C#?
date: 2026-04-29
url: https://stackoverflow.com/questions/17586525/what-is-the-difference-between-new-object-and-new-in-c
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://stackoverflow.com/questions/17586525/what-is-the-difference-between-new-object-and-new-in-c
scraped: "2026-04-29 11:00"

---

## Summary

Placeholder summary — please add a concise summary of this article.



# What is the Difference Between `new object()` and `new {}` in C#?

**Source**: [Original Article](https://stackoverflow.com/questions/17586525/what-is-the-difference-between-new-object-and-new-in-c)

## Full Article

Collectives™ on Stack Overflow
Find centralized, trusted content and collaborate around the technologies you use most.
Learn more about Collectives
Stack Internal
Knowledge at work
Bring the best of human thought and AI automation together at your work.
Explore Stack Internal
What is the Difference Between `new object()` and `new {}` in C#?
Ask Question
Asked
12 years, 9 months ago
Modified
4 years, 11 months ago
Viewed
98k times
60
First of all i searched on this and i found the following links on Stack Overflow:
Is there any difference between `new object()` and `new {}` in c#?
Difference between object a = new Dog() vs Dog a = new Dog()
But i'm not
satisfied
with this answer, it's not explained well (i didn't get it well). 
Basically, i want to know the difference between
new object()
and
new {}
.
How, they are treated at compile time and runtime?
Secondaly, i have the following code which i have used for
WebMethods
in my asp.net simple application
[WebMethod]
[ScriptMethod(UseHttpGet = false)]
public static object SaveMenus(MenuManager proParams)
{
    object data = new { }; // here im creating an instance of an 'object' and i have typed it `new {}` but not `new object(){}`.
    try
    {
        MenuManager menu = new MenuManager();    
        menu.Name = proParams.Name;
        menu.Icon = proParams.Icon;
        bool status = menu.MenuSave(menu);
        if (status)
        {
            // however, here i'm returning an anonymous type
            data = new
            {
                status = true,
                message = "Successfully Done!"
            };
        }
    }
    catch (Exception ex)
    {
        data = new { status = false, message = ex.Message.ToString() };
    }
    return data;
}
So, (as you can see in comments in code), How
new object(){}
and
new {}
differences?
Is this even the right way that i have write the code?
Can you suggest a best way for this code?
I know, i can't explain it well and i'm asking alot, but that's the best i have right now.
c#
.net
object
Share
Improve this question
Follow
edited
May 10, 2021 at 6:40
[Dmitrii Bychenko's user avatar]
Dmitrii Bychenko
188k
20
20 gold badges
179
179 silver badges
232
232 bronze badges
asked
Jul 11, 2013 at 6:31
[Idrees Khan's user avatar]
Idrees Khan
7,762
18
18 gold badges
65
65 silver badges
112
112 bronze badges
5
7
Your
new{}
is creating an
anonymous type
CodesInChaos
–
CodesInChaos
2013-07-11 06:34:06 +00:00
Commented
Jul 11, 2013 at 6:34
4
new {} is for anonymous type and new object() is just the constructor of the object class.
Cybermaxs
–
Cybermaxs
2013-07-11 06:34:38 +00:00
Commented
Jul 11, 2013 at 6:34
1
@Cybermaxs-Betclic, i know the result type is an anonymous type of an object but how they are treated by
MSIL
? Will this generate a new
Anonymouse
type separate code by c# compliler?
Idrees Khan
–
Idrees Khan
2013-07-11 06:40:05 +00:00
Commented
Jul 11, 2013 at 6:40
1
That was new info to me. Can I use
new {}
to create instance for all objects types?
Subin Jacob
–
Subin Jacob
2013-07-11 06:47:39 +00:00
Commented
Jul 11, 2013 at 6:47
Note that if you declared it
var a = new { };
and
var o = new object();
, then there is one difference, former is assignable only to another similar anonymous object, while latter being object, it can be assigned to anything.
nawfal
–
nawfal
2014-09-07 10:46:00 +00:00
Commented
Sep 7, 2014 at 10:46
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
64
new {...}
always creates an
anonymous object
, for instance:
Object sample = new {};
  String sampleName = sample.GetType().Name; // <- something like "<>f__AnonymousType0" 
                                             //                    not "Object"
while
new Object()
creates an instance of
Object
class
Object sample = new Object() {};
  String sampleName = sample.GetType().Name; // <- "Object"
since all objects (including anonymous ones) are derived from
Object
you can always type
Object sample = new {};
Share
Improve this answer
Follow
edited
Nov 14, 2018 at 6:52
answered
Jul 11, 2013 at 6:42
[Dmitrii Bychenko's user avatar]
Dmitrii Bychenko
188k
20
20 gold badges
179
179 silver badges
232
232 bronze badges
Sign up to request clarification or add additional context in comments.
2 Comments
Add a comment
Idrees Khan
Idrees Khan
Over a year ago
much better explanation. so, it means, they are treated as an
object
type at runtime and compiler doesn't treat it as
anonymous
type
2013-07-11T06:47:20.2Z+00:00
0
Reply
Copy link
JLRishe
JLRishe
Over a year ago
@DotNetDreamer What do you mean "they are treated as an object type at runtime"? All objects inherit from the
Object
class, but Dimitry's example specifically shows that the anonymous object's actual type is
not
Object.
2013-07-11T07:02:07.29Z+00:00
5
Reply
Copy link
14
To see the difference between
new Object()
and
new {}
and
new Object(){}
... why don't we just find out?
Console.WriteLine(new Object().GetType().ToString());
Console.WriteLine(new Object() { }.GetType().ToString());
Console.WriteLine(new { }.GetType().ToString());
The first two are just different ways of creating an Object and prints
System.Object
.  The third is actually an anonymous type and prints
<>f__AnonymousType0
.
I think you might be getting confused by the different uses of '{}'.  Off the top of my head it can be used for:
Statement blocks.
Object/Collection/Array initialisers.
Anonymous Types
So, in short
object data = new { };
does not create a new object.  It creates a new AnonymousType which, like
all classes, structures, enumerations, and delegates
inherits Object and therefor can be assigned to it.
As mentioned in comments, when returning anonymous types you still have declare and downcast them to Object.  However, they are still different things and have some implementation differences for example:
static void Main(string[] args)
{
    Console.WriteLine(ReturnO(true).ToString());  //"{ }"
    Console.WriteLine(ReturnO(false).ToString());  // "System.Object"

    Console.WriteLine(ReturnO(true).Equals(ReturnO(true)));  //True
    Console.WriteLine(ReturnO(false).Equals(ReturnO(false)));  //False
    Console.WriteLine(ReturnO(false).Equals(ReturnO(true)));  //False

    Console.WriteLine(ReturnO(true).GetHashCode());  //0
    Console.WriteLine(ReturnO(false).GetHashCode());  //37121646

    Console.ReadLine();
}

static object ReturnO(bool anonymous)
{
    if (anonymous) return new { };
    return new object();
}
Share
Improve this answer
Follow
edited
Jul 11, 2013 at 7:23
answered
Jul 11, 2013 at 6:41
[NPSF3000's user avatar]
NPSF3000
2,449
16
16 silver badges
20
20 bronze badges
3 Comments
Add a comment
Idrees Khan
Idrees Khan
Over a year ago
what will be the return of my
webmethod
an
anonymouse
or
object
type ?
2013-07-11T07:08:34.243Z+00:00
0
Reply
Copy link
NPSF3000
NPSF3000
Over a year ago
The return type is object - you can't return anonymous type because... you don't actually know what the type is at compile time.  However returning an anonymous type (downcast to an object) and returning an object may lead to different behaviour - e.g. they implement ToString() differently.
2013-07-11T07:10:04.367Z+00:00
1
Reply
Copy link
Idrees Khan
Idrees Khan
Over a year ago
thank your for the new info. i wish i had more then +1 for you :)
2013-07-11T07:11:22.817Z+00:00
1
Reply
Copy link
Add a comment
8
new{ }
creates an instance of an anonymous type with no members. This is different from creating an instance of
object
. But like almost all types, anonymous types can be assigned to object.
object data = new { };
 Console.WriteLine(data.GetType().Name)
Clearly shows an auto-generated name, not
Object
.
Share
Improve this answer
Follow
answered
Jul 11, 2013 at 6:38
[CodesInChaos's user avatar]
CodesInChaos
109k
26
26 gold badges
224
224 silver badges
268
268 bronze badges
3 Comments
Add a comment
p.s.w.g
p.s.w.g
Over a year ago
"
like almost all types, anonymous types can be assigned to object
" can you name one that can't?
2013-07-11T06:39:24.543Z+00:00
0
Reply
Copy link
CodesInChaos
CodesInChaos
Over a year ago
Obvious example are pointers. I think there are some more, stuff like those weird argument iterators or certain kinds of references that can't be used in C# directly.
2013-07-11T06:40:12.6Z+00:00
5
Reply
Copy link
Mare Infinitus
Mare Infinitus
Over a year ago
pointer in c#, so unsafe... but everything in the "safe" part.
2013-07-11T06:42:05.74Z+00:00
0
Reply
Copy link
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
.net
object
See similar questions with these tags.
The Overflow Blog
Your LLM issues are really data issues
Welcome to the “find out” stage of AI
Featured on Meta
Retiring the beta site
Policy: Generative AI (e.g., ChatGPT) is banned
Linked
65
What is the difference between new Object() and new Object{} in expressions in C#
27
Difference between object a = new Dog() vs Dog a = new Dog()
6
Is there any difference between `new object()` and `new {}` in c#?
0
What does new(new() { Args = args }); mean?
Related
6
New {object} vs {object} = new {object}
6
Is there any difference between `new object()` and `new {}` in c#?
3
Difference between Object() and Object{}
1
What's the difference between new object[] {} and new [] {}?
0
When do we need to create an object with "new" and when can we just declare and assign value to it?
62
Does { } act like ( ) when creating a new object in C#?
1
Creating an object in C# with or without new
0
What is difference between initializing object with new and without new
65
What is the difference between new Object() and new Object{} in expressions in C#
1
Create C# object using Object object = new(); versus var object = new Object();
Hot Network Questions
Why isn't the Neumann value being satisfied for a simple linear PDE?
Recurrence leading to simple closed form for Fishburn numbers
Is panpsychism linguistically disingenuous?
What explanation systems do humans use (not just in philosophy)
Maxing out multcomp of R package marginaleffects
What precedent did the 2 Live Crew case actually set?
In "a landscape in which inner and outer vision were reconciled" is *vision* countable?
How can data science be used for "good" causes?
Are emanations spherical?
Unexpected spacing with negative coordinates in a command for projective coordinates using `expl3`
The Presupposition of the Soul in Plato’s Phaedo
Electrical wiring shared neutral?
Difficulties with Set-Notation in Taxicab Geometry
Who is ‘Blessed’ in Mark 14:61?
Fires spread through centrifugal gravity systems
Why do derivatives of piecewise functions expand brackets versus derivatives of expressions
Is it legal to visit the pre-security (landside) part of an airport without a flight or any business to be there?
How can I model a flattened fish bowl?
Bowling up the slide
Measuring absolute static charge
What were the effects of the spellplague on arcane spellcasters?
Centrifugal Gravity in an existentially empty universe
Why is it a bad idea to delete my Google Scholar as a TT faculty?
Controlled Heisenberg evolution gate
more hot questions
Question feed
lang-cs

## Metadata
- **Source URL**: https://stackoverflow.com/questions/17586525/what-is-the-difference-between-new-object-and-new-in-c
