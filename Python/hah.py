constructors:special method which gets executed when object is instantiated
1.allocate the memory with the appropriate structure for the object
2.initialize the member

__init__ is used to define the constructor in python.
constructor will get executed implicitely when the object is instantiated
it will execute once per object with respect to class
If constructor has to be executed ,object must be instantiated
list and tuple is ordered but dictionary is unordered

Passing parameters to methods:Parameters are the necessary values which are passed form the calling
environment into methods.Ehen parameters are passed, it has to be received in the method with 
the flollowing guidelines.The number of parameters(Values)Passed in the number of arguments
define inside method to receive it.The sequence of the parameters passed,is the sequence of
the arguments defined to receive parameters.Parameters can be passed in three styles
1.Static pass
2.Dynamic pass
3.Expression pass

Destructor will executes when the object is deleted or just before the program termination
__del__---special name of the destructor
1.Local scope-any member defined in the method
2.Class scope--static member
3.Object scope--if the object is destroyed that variable also destroyed
4.Global scope--anything defined in the main 
5.External scope--defined in the another program

We can pass key word arguments in python 
Keyword arguments are mechanism to provide the necessary values to any of the argument in
the list without going with sequence. When keyword arugments is to be provided we use the same 
name as provided in the argument list and initialize only the necessary argument in the
list.

ob2=wipro(y=3,x=4)--python and ruby only support this

def Sample(x,y,z)
	print x,y,z
Sample()-------------will gives an error because we are not giving any values
if we initialize x y and z it will return those values
We can initilaize all or any one of them based on the requirment
def Sample(x,y=0,z=0)---it is possible but we have to give non default first and default 
next otherwise it will throws an error.
it wont allows extra values passed rather than defined
eg:Sample(1,2,3,4)--gives an error because we have defined only 3 parameters

Special members in python for class are used to convert a function into a method.This
Process is called type casting. 
two spcial builtin funcitons called static method and class method.
Scope resolution operator
Static members are only accessible with in the static method which means it cant access
instance variables .If it is having self then it is called class method
'this' = 'self' in python
if the method doesn't have self then it will be static
if we implementing any method with an object it is bounded and if we implementing with 
class which is unbounded(static)
converting functions into methods should be done after defining all of the methods in 
the program
Staticmethod--it takes one argument as a function handle and return method handle
Classmethod--it takes one argument as a function handle and return method handle
if we would like to convert 100 of functions into methods it is very tidious task so 
decoratives are addded to mitigate this problem
Decorators are ways to convert the static functions into a dynamic functions
There are two types of decorators
1.Builtin
2.User defined
All decorators are prefixed with "@" and to be defined just before the definiton of 
function
@class method,@static method
Inheritance:Inhertance is a mechnism of OOP to extend the members of one class to
another
The class which extends the member is called Base class/Super class/Parent class
The class which receives the members is called Derived class/Child class/sub class
Inheritance provides code reusability and code clarity
There are 5 styles of inheritance
1.single level inheritance
2.multilevel inheritance
3.multiple inheritance--is resolved in python with method resolution operator
4.hirearchial inheritance
5.hybrid inheritance
IS-A relationship and HAS-A relationship
Objects are always created in the bottom most class in the class hirearchy and access
top most classes.
Overriding
1.Classic style
2.New style
1.Disconnected class
2.loosely connected class
3.Tightly connected class(inherited classes)
Super word is used to represent immediate parent member
1.Classic Style class--top most calss and standalone
2.New style class--inherits the object class
two algorithms useful for Method resolution order
1.Breadth first search(BFS) for new style
2.Depth first search for classic style

class A:
class B(A):
class C(A):
class D(B,C):
DFS------D,B,A,C
BFS------D,B,C,(D-B)A,DC


eg:class A:
display():
class B(A):
display():
class C(B):
super(B,self).display():---------it is directly executing parent display 

