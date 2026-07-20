---

title: What is the 'new' keyword in JavaScript? - Stack Overflow
date: 2026-05-03
url: https://stackoverflow.com/questions/1646698/what-is-the-new-keyword-in-javascript
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://stackoverflow.com/questions/1646698/what-is-the-new-keyword-in-javascript
scraped: "2026-05-03 16:36"

---

## Summary

Explains how JavaScript's `new` keyword constructs objects and what happens under the hood.



# What is the 'new' keyword in JavaScript? - Stack Overflow

**Source**: [Original Article](https://stackoverflow.com/questions/1646698/what-is-the-new-keyword-in-javascript)

## Full Article

Collectives™ on Stack Overflow
Find centralized, trusted content and collaborate around the technologies you use most.
Learn more about Collectives
Stack Internal
Knowledge at work
Bring the best of human thought and AI automation together at your work.
Explore Stack Internal
What is the 'new' keyword in JavaScript?
Ask Question
Asked
16 years, 6 months ago
Modified
1 year, 9 months ago
Viewed
385k times
1931
The
new
keyword in JavaScript can be quite confusing when it is first encountered, as people tend to think that JavaScript is not an object-oriented programming language.
What is it?
What problems does it solve?
When is it appropriate and when not?
javascript
new-operator
Share
Improve this question
Follow
edited
Jul 25, 2015 at 13:42
[Bergi's user avatar]
Bergi
672k
162
162 gold badges
1k
1k silver badges
1.5k
1.5k bronze badges
asked
Oct 29, 2009 at 21:32
[Alon Gubkin's user avatar]
Alon Gubkin
57.2k
58
58 gold badges
200
200 silver badges
293
293 bronze badges
2
15
Also, related thread -
stackoverflow.com/questions/383402/…
Chetan S
–
Chetan S
2009-10-29 22:04:46 +00:00
Commented
Oct 29, 2009 at 22:04
2
read these examples first folks,
developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/…
MartianMartian
–
MartianMartian
2018-12-30 17:00:39 +00:00
Commented
Dec 30, 2018 at 17:00
Add a comment
|
18 Answers
18
Sorted by:
Reset to default
Highest score (default)
Trending (recent votes count more)
Date modified (newest first)
Date created (oldest first)
2305
It does 5 things:
It creates a new object.  The type of this object is simply
object
.
It sets this new object's internal, inaccessible,
[[prototype]]
(i.e.
__proto__
) property to be the constructor function's external, accessible,
prototype
object (every function object automatically has a
prototype
property).
It makes the
this
variable point to the newly created object.
It executes the constructor function, using the newly created object whenever
this
is mentioned.
It returns the newly created object, unless the constructor function returns a non-
null
object reference. In this case, that object reference is returned instead.
Note:
constructor function
refers to the function after the
new
keyword, as in
new ConstructorFunction(arg1, arg2)
Once this is done, if an undefined property of the new object is requested, the script will check the object's
[[prototype]]
object for the property instead. This is how you can get something similar to traditional class inheritance in JavaScript.
The most difficult part about this is point number 2.  Every object (including functions) has this internal property called
[[prototype]]
. It can
only
be set at object creation time, either with
new
, with
Object.create
, or based on the literal (functions default to
Function.prototype
, numbers to
Number.prototype
, etc.). It can only be read with
Object.getPrototypeOf(someObject)
. There is
no
other way to get or set this value.
Functions, in addition to the hidden
[[prototype]]
property, also have a property called
prototype
, and it is this that you can access, and modify, to provide inherited properties and methods for the objects you make.
Here is an example:
ObjMaker = function() { this.a = 'first'; };
// `ObjMaker` is just a function, there's nothing special about it
// that makes it a constructor.

ObjMaker.prototype.b = 'second';
// like all functions, ObjMaker has an accessible `prototype` property that 
// we can alter. I just added a property called 'b' to it. Like 
// all objects, ObjMaker also has an inaccessible `[[prototype]]` property
// that we can't do anything with

obj1 = new ObjMaker();
// 3 things just happened.
// A new, empty object was created called `obj1`.  At first `obj1` 
// was just `{}`. The `[[prototype]]` property of `obj1` was then set to the current
// object value of the `ObjMaker.prototype` (if `ObjMaker.prototype` is later
// assigned a new object value, `obj1`'s `[[prototype]]` will not change, but you
// can alter the properties of `ObjMaker.prototype` to add to both the
// `prototype` and `[[prototype]]`). The `ObjMaker` function was executed, with
// `obj1` in place of `this`... so `obj1.a` was set to 'first'.

obj1.a;
// returns 'first'
obj1.b;
// `obj1` doesn't have a property called 'b', so JavaScript checks 
// its `[[prototype]]`. Its `[[prototype]]` is the same as `ObjMaker.prototype`
// `ObjMaker.prototype` has a property called 'b' with value 'second'
// returns 'second'
It's like class inheritance because now, any objects you make using
new ObjMaker()
will also appear to have inherited the 'b' property.
If you want something like a subclass, then you do this:
SubObjMaker = function () {};
SubObjMaker.prototype = new ObjMaker(); // note: this pattern is deprecated!
// Because we used 'new', the [[prototype]] property of SubObjMaker.prototype
// is now set to the object value of ObjMaker.prototype.
// The modern way to do this is with Object.create(), which was added in ECMAScript 5:
// SubObjMaker.prototype = Object.create(ObjMaker.prototype);

SubObjMaker.prototype.c = 'third';  
obj2 = new SubObjMaker();
// [[prototype]] property of obj2 is now set to SubObjMaker.prototype
// Remember that the [[prototype]] property of SubObjMaker.prototype
// is ObjMaker.prototype. So now obj2 has a prototype chain!
// obj2 ---> SubObjMaker.prototype ---> ObjMaker.prototype

obj2.c;
// returns 'third', from SubObjMaker.prototype

obj2.b;
// returns 'second', from ObjMaker.prototype

obj2.a;
// returns 'first', from SubObjMaker.prototype, because SubObjMaker.prototype 
// was created with the ObjMaker function, which assigned a for us
I read a ton of rubbish on this subject before finally finding
this page
, where this is explained very well with nice diagrams.
Share
Improve this answer
Follow
edited
Feb 12, 2023 at 3:56
community wiki
29 revs, 24 users 49%
Daniel Howard
Sign up to request clarification or add additional context in comments.
30 Comments
Add a comment
Blub
Blub
Over a year ago
Just wanted to add: There is in fact a way to access the internal [[prototype]], by __proto__. This is however non-standard, and only supported by relatively new browsers (and not all of them). There is a standardized way coming up, namely Object.getPrototypeOf(obj), but it is Ecmascript3.1, and is itself only supported on new browers - again. It is generally recommended to not use that property though, stuff gets complicated real fast inside there.
2011-04-14T14:55:40.85Z+00:00
53
Reply
Copy link
Jim Blackler
Jim Blackler
Over a year ago
Question: what happens differently if
ObjMaker
is defined as a function that returns a value?
2012-02-27T19:05:32.9Z+00:00
12
Reply
Copy link
Engineer
Engineer
Over a year ago
@LonelyPixel
new
exists
so that you don't have to
write factory methods to construct/copy functions/objects. It means, "Copy this, making it just like its parent 'class'; do so efficiently and correctly; and store inheritance info that is accessible only to me, JS, internally". To do so, it modifies the otherwise inaccessible internal
prototype
of the new object to opaquely encapsulate the inherited members, mimicking classical OO inheritance chains (which aren't runtime modifiable). You can simulate this without
new
, but inheritance will be runtime modifiable. Good? Bad? Up to you.
2012-10-23T22:36:20.337Z+00:00
15
Reply
Copy link
charlie roberts
charlie roberts
Over a year ago
a small point to add: a call to a constructor, when preceded by the new keyword, automatically returns the created object; there is no need to explicitly return it from within the constructor.
2013-06-06T02:04:18.243Z+00:00
12
Reply
Copy link
Tom Pažourek
Tom Pažourek
Over a year ago
There is a note that says
Notice that this pattern is deprecated!
. What is the correct up-to-date pattern to set the prototype of a class?
2014-02-17T12:18:41.793Z+00:00
7
Reply
Copy link
Add a comment
|
Show 25 more comments
457
Suppose you have this function:
var Foo = function(){
  this.A = 1;
  this.B = 2;
};
If you call this as a stand-alone function like so:
Foo();
Executing this function will add two properties to the
window
object (
A
and
B
). It adds it to the
window
because
window
is the object that called the function when you execute it like that, and
this
in a function is the object that called the function. In JavaScript at least.
Now, call it like this with
new
:
var bar = new Foo();
When you add
new
to a function call, a new object is created (just
var bar = new Object()
) and the
this
within the function points to the new
Object
you just created, instead of to the object that called the function. So
bar
is now an object with the properties
A
and
B
. Any function can be a constructor; it just doesn't always make sense.
Share
Improve this answer
Follow
edited
Nov 29, 2022 at 11:21
[Peter Mortensen's user avatar]
Peter Mortensen
31.1k
22
22 gold badges
111
111 silver badges
134
134 bronze badges
answered
Oct 29, 2009 at 22:22
[JulianR's user avatar]
JulianR
16.6k
5
5 gold badges
59
59 silver badges
85
85 bronze badges
9 Comments
Add a comment
MaksymB
MaksymB
Over a year ago
Depends on execution context. In my case (Qt scripting) it's just a global object.
2013-01-21T13:24:27.217Z+00:00
8
Reply
Copy link
Jürgen Paul
Jürgen Paul
Over a year ago
will this cause more memory usage?
2013-07-24T19:20:44.42Z+00:00
4
Reply
Copy link
Dávid Horváth
Dávid Horváth
Over a year ago
because window is the object that called the function
- must be: because window is the object that
contains
the function.
2016-07-23T13:22:05.963Z+00:00
3
Reply
Copy link
Dávid Horváth
Dávid Horváth
Over a year ago
@Taurus In a web browser a non-method function will be a method of
window
implicitly. Even in a closure, even if anonymus. However, in the example it is a simple method invocation on window:
Foo();
=>
[default context].Foo();
=>
window.Foo();
.  In this expression
window
is the
context
(not only the
caller
, which does not matter).
2017-09-11T11:47:02.003Z+00:00
3
Reply
Copy link
Dávid Horváth
Dávid Horváth
Over a year ago
@Taurus Basicly yes. However in ECMA 6 and 7 things are more complex (see lambdas, classes, etc).
2017-09-11T12:00:32.5Z+00:00
2
Reply
Copy link
Add a comment
|
Show 4 more comments
180
In addition to
Daniel Howard's answer
, here is what
new
does (or at least seems to do):
function New(func) {
    var res = {};
    if (func.prototype !== null) {
        res.__proto__ = func.prototype;
    }
    var ret = func.apply(res, Array.prototype.slice.call(arguments, 1));
    if ((typeof ret === "object" || typeof ret === "function") && ret !== null) {
        return ret;
    }
    return res;
}
While
var obj = New(A, 1, 2);
is equivalent to
var obj = new A(1, 2);
Share
Improve this answer
Follow
edited
Nov 29, 2022 at 11:24
[Peter Mortensen's user avatar]
Peter Mortensen
31.1k
22
22 gold badges
111
111 silver badges
134
134 bronze badges
answered
Jun 20, 2013 at 23:46
[basilikum's user avatar]
basilikum
10.5k
5
5 gold badges
51
51 silver badges
58
58 bronze badges
5 Comments
Add a comment
damphat
damphat
Over a year ago
I found that javascript is easier to understand than english :v
2013-10-20T10:11:10.083Z+00:00
79
Reply
Copy link
Tom Pažourek
Tom Pažourek
Over a year ago
Excellent answer. I have one tiny question: How can it be possible for
func.prototype
to be
null
? Could you please elaborate a bit on that?
2014-04-02T11:12:10.18Z+00:00
1
Reply
Copy link
basilikum
basilikum
Over a year ago
@tomp you could override the prototype property, by simply writing
A.prototype = null;
In that case
new A()
will result in on object,  thats internal prototype points to the
Object
object:
jsfiddle.net/Mk42Z
2014-04-28T18:19:32.473Z+00:00
7
Reply
Copy link
Oriol
Oriol
Over a year ago
The typeof check might be wrong because a host object could produce something different than "object" or "function". To test if something is an object, I prefer
Object(ret) === ret
.
2015-10-08T21:40:25.373Z+00:00
3
Reply
Copy link
basilikum
basilikum
Over a year ago
@Oriol thank you for the comment. It is true what you say and any actual test should be done in more robust way. However, I think for this conceptual answer, the
typeof
test just makes it easier to understand what is going on behind the scenes.
2015-10-08T21:53:27.713Z+00:00
3
Reply
Copy link
Add a comment
141
For beginners to understand it better
Try out the following code in the browser console.
function Foo() {
    return this;
}

var a = Foo();       // Returns the 'window' object
var b = new Foo();   // Returns an empty object of foo

a instanceof Window;  // True
a instanceof Foo;     // False

b instanceof Window;  // False
b instanceof Foo;     // True
Now you can read the
community wiki answer
:)
Share
Improve this answer
Follow
edited
Nov 29, 2022 at 11:35
[Peter Mortensen's user avatar]
Peter Mortensen
31.1k
22
22 gold badges
111
111 silver badges
134
134 bronze badges
answered
May 27, 2015 at 9:23
[Anulal S's user avatar]
Anulal S
6,645
5
5 gold badges
29
29 silver badges
34
34 bronze badges
2 Comments
Add a comment
Nelu
Nelu
Over a year ago
Good answer. Also - leaving out
return this;
yields the same output.
2017-02-02T21:26:52.69Z+00:00
8
Reply
Copy link
Mikko Rantalainen
Mikko Rantalainen
Over a year ago
And the explanation for why
return this;
doesn't change the behavior is that the operator
new
is magical in creating the new object and executing the constructor and
if
the return value of the constructor is
undefined
(no return clause or just
return;
) or
null
(special case:
return null;
) then the newly created object (
this
inside the constructor) will be used as the value of
new
operator, otherwise the value of
new
is the returned value. I don't know the rationale for this behavior but I'd guess "due historical reasons".
2022-09-30T07:39:28.443Z+00:00
0
Reply
Copy link
41
so it's probably not for creating
  instances of object
It's used exactly for that. You define a function constructor like so:
function Person(name) {
    this.name = name;
}

var john = new Person('John');
However the extra benefit that ECMAScript has is you can extend with the
.prototype
property, so we can do something like...
Person.prototype.getName = function() { return this.name; }
All objects created from this constructor will now have a
getName
because of the prototype chain that they have access to.
Share
Improve this answer
Follow
edited
Jan 6, 2016 at 8:49
[Adrian Thompson Phillips's user avatar]
Adrian Thompson Phillips
7,218
7
7 gold badges
44
44 silver badges
72
72 bronze badges
answered
Oct 29, 2009 at 21:34
[meder omuraliev's user avatar]
meder omuraliev
187k
76
76 gold badges
402
402 silver badges
444
444 bronze badges
3 Comments
Add a comment
meder omuraliev
meder omuraliev
Over a year ago
function constructors are used like classes, there is no
class
keyword but you can pretty much do the same thing.
2009-10-29T21:37:07.77Z+00:00
8
Reply
Copy link
Greg
Greg
Over a year ago
There kindof is a class keyword - class is reserved for future use
2009-10-29T21:41:09.59Z+00:00
2
Reply
Copy link
Greg
Greg
Over a year ago
Incidentally that's why you use .className not .class to set a CSS class
2009-10-29T21:41:47.097Z+00:00
12
Reply
Copy link
Add a comment
31
JavaScript
is
an object-oriented programming language and it's used exactly for creating instances. It's
prototype-based
, rather than
class-based
, but that does not mean that it is not object-oriented.
Share
Improve this answer
Follow
edited
Nov 29, 2022 at 11:55
[Peter Mortensen's user avatar]
Peter Mortensen
31.1k
22
22 gold badges
111
111 silver badges
134
134 bronze badges
answered
Oct 29, 2009 at 21:36
[Michael's user avatar]
Michael
9,128
3
3 gold badges
42
42 silver badges
56
56 bronze badges
1 Comment
Add a comment
JustAMartin
JustAMartin
Over a year ago
I like to say that JavaScript seems to be even more object-oriented than all those class-based languages. In JavaScript everything you write immediately becomes an object, but in class-based languages you first write declarations and only later you create specific instances (objects) of classes. And JavaScript prototype seems to vaguely remind all that VTABLE stuff for class-based languages.
2013-10-07T07:33:29.28Z+00:00
9
Reply
Copy link
27
Summary:
The
new
keyword is used in JavaScript to create a object from a constructor function. The
new
keyword has to be placed before the constructor function call and will do the following things:
Creates a new object
Sets the prototype of this object to the constructor function's prototype property
Binds the
this
keyword to the newly created object and executes the constructor function
Returns the newly created object
Example:
function Dog (age) {
  this.age = age;
}

const doggie = new Dog(12);

console.log(doggie);
console.log(Object.getPrototypeOf(doggie) === Dog.prototype) // true
What exactly happens:
const doggie
says: We need memory for declaring a variable.
The assignment operator
=
says: We are going to initialize this variable with the expression after the
=
The expression is
new Dog(12)
. The JavaScript engine sees the
new
keyword, creates a new object and sets the prototype to
Dog.prototype
The constructor function is executed with the
this
value set to the new object. In this step is where the age is assigned to the new created doggie object.
The newly created object is returned and assigned to the variable doggie.
Share
Improve this answer
Follow
edited
Dec 8, 2022 at 20:32
[Peter Mortensen's user avatar]
Peter Mortensen
31.1k
22
22 gold badges
111
111 silver badges
134
134 bronze badges
answered
Aug 31, 2018 at 8:22
[Willem van der Veen's user avatar]
Willem van der Veen
37.2k
19
19 gold badges
209
209 silver badges
179
179 bronze badges
Comments
Add a comment
21
Please take a look at my observation on
case III
below. It is about what happens when you have an explicit
return
statement in a function which you are
new
ing up. Have a look at the below cases:
Case I
:
var Foo = function(){
  this.A = 1;
  this.B = 2;
};
console.log(Foo()); //prints undefined
console.log(window.A); //prints 1
Above is a plain case of calling the anonymous function pointed by variable
Foo
. When you call this function it returns
undefined
. Since there isn’t any explicit return statement, the JavaScript interpreter forcefully inserts a
return undefined;
statement at the end of the function. So the above code sample is equivalent to:
var Foo = function(){
  this.A = 1;
  this.B = 2;
  return undefined;
};
console.log(Foo()); //prints undefined
console.log(window.A); //prints 1
When
Foo
function is invoked
window
is the default invocation object (contextual
this
) which gets new
A
and
B
properties.
Case II
:
var Foo = function(){
  this.A = 1;
  this.B = 2;
};
var bar = new Foo();
console.log(bar()); //illegal isn't pointing to a function but an object
console.log(bar.A); //prints 1
Here the JavaScript interpreter, seeing the
new
keyword, creates a new object which acts as the invocation object (contextual
this
) of anonymous function pointed by
Foo
. In this case
A
and
B
become properties on the newly created object (in place of window object). Since you don't have any explicit return statement, JavaScript interpreter forcefully inserts a return statement to return the new object created due to usage of
new
keyword.
Case III
:
var Foo = function(){
  this.A = 1;
  this.B = 2;
  return {C:20,D:30};
};
var bar = new Foo();
console.log(bar.C);//prints 20
console.log(bar.A); //prints undefined. bar is not pointing to the object which got created due to new keyword.
Here again, the JavaScript interpreter, seeing the
new
keyword, creates a new object which acts as the invocation object (contextual
this
) of anonymous function pointed by
Foo
. Again,
A
and
B
become properties on the newly created object. But this time you have an explicit return statement so JavaScript interpreter will
not
do anything of its own.
The thing to note in
case III
is that the object being created due to
new
keyword got lost from your radar.
bar
is actually pointing to a completely different object which is not the one which JavaScript interpreter created due to the
new
keyword.
Quoting David Flanagan from
JavaScript: The Definitive Guide
(6th Edition), Chapter 4, Page # 62:
When an object creation expression is evaluated, JavaScript first
creates a new empty object, just like the one created by the object
initializer {}. Next, it invokes the specified function with the
specified arguments, passing the new object as the value of the this
keyword. The function can then use this to initialize the properties
of the newly created object. Functions written for use as constructors
do not return a value, and the value of the object creation expression
is the newly created and initialized object. If a constructor does
return an object value, that value becomes the value of the object
creation expression and the newly created object is discarded.
Additional information:
The functions used in the code snippet of the above cases have special names in the JavaScript world as below:
Case #
Name
Case I
Constructor function
Case II
Constructor function
Case III
Factory function
You can read about the difference between constructor functions and factory functions in
this thread
.
Code smell in case III
- Factory functions should
not
be used with the
new
keyword which I've shown in the code snippet above. I've done so deliberately only to explain the concept.
Share
Improve this answer
Follow
edited
Nov 30, 2022 at 5:44
answered
Oct 5, 2017 at 2:28
[RBT's user avatar]
RBT
26.4k
24
24 gold badges
178
178 silver badges
268
268 bronze badges
1 Comment
Add a comment
appu
appu
Over a year ago
your case 3, is a gr8 observation
2019-06-16T16:51:55.413Z+00:00
2
Reply
Copy link
13
JavaScript is a dynamic programming language which supports the object-oriented programming paradigm, and it is used for creating new instances of objects.
Classes are not necessary for objects. JavaScript is a
prototype-based
language.
Share
Improve this answer
Follow
edited
Nov 29, 2022 at 11:55
[Peter Mortensen's user avatar]
Peter Mortensen
31.1k
22
22 gold badges
111
111 silver badges
134
134 bronze badges
answered
Oct 29, 2009 at 21:37
[Greg's user avatar]
Greg
323k
55
55 gold badges
378
378 silver badges
338
338 bronze badges
Comments
Add a comment
10
The
new
keyword changes the context under which the function is being run and returns a pointer to that context.
When you don't use the
new
keyword, the context under which function
Vehicle()
runs is the same context from which you are calling the
Vehicle
function. The
this
keyword will refer to the same context. When you use
new Vehicle()
, a new context is created so the keyword
this
inside the function refers to the new context. What you get in return is the newly created context.
Share
Improve this answer
Follow
answered
Nov 27, 2017 at 13:13
[Juzer Ali's user avatar]
Juzer Ali
4,217
3
3 gold badges
40
40 silver badges
64
64 bronze badges
1 Comment
Add a comment
appu
appu
Over a year ago
That's a very insightful answer in terms of scope. Gr8 addition to the answer.
2019-06-16T16:53:41.113Z+00:00
0
Reply
Copy link
7
Sometimes code is easier than words:
var func1 = function (x) { this.x = x; }                   // Used with 'new' only
var func2 = function (x) { var z={}; z.x = x; return z; }  // Used both ways
func1.prototype.y = 11;
func2.prototype.y = 12;

A1 = new func1(1);  // Has A1.x  AND  A1.y
A2 =     func1(1);  // Undefined ('this' refers to 'window')
B1 = new func2(2);  // Has B1.x  ONLY
B2 =     func2(2);  // Has B2.x  ONLY
For me, as long as I do not prototype, I use the style of func2 as it gives me a bit more flexibility inside and outside the function.
Share
Improve this answer
Follow
edited
Nov 29, 2022 at 11:34
[Peter Mortensen's user avatar]
Peter Mortensen
31.1k
22
22 gold badges
111
111 silver badges
134
134 bronze badges
answered
May 16, 2015 at 7:21
[rsbkk's user avatar]
rsbkk
243
3
3 silver badges
2
2 bronze badges
2 Comments
Add a comment
sunny_dev
sunny_dev
Over a year ago
B1 = new func2(2);
<- Why this will not have
B1.y
?
2015-11-17T09:37:24.477Z+00:00
3
Reply
Copy link
Eagle
Eagle
Over a year ago
@sunny_dev I'm not a JS expert, but probably because
func2
is returning directly a value (z object), instead of working/returning with internal values (this)
2016-12-19T09:05:45.393Z+00:00
0
Reply
Copy link
4
Every function has a prototype object that’s automatically set as the prototype of the objects created with that function.
You guys can check easily:
const a = { name: "something" };
console.log(a.prototype); // 'undefined' because it is not directly accessible

const b = function () {
    console.log("somethign");
};

console.log(b.prototype); // Returns b {}
But every function and objects has the
__proto__
property which points to the prototype of that object or function.
__proto__
and
prototype
are two different terms. I think we can make this comment: "Every object is linked to a prototype via the
proto
" Bu

## Metadata
- **Source URL**: https://stackoverflow.com/questions/1646698/what-is-the-new-keyword-in-javascript
