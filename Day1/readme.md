04/05/2026
Learned about child and parent
How to declare child class:

def child(parent):


05/05/2026
Inheritance lets a child class automatically get everything the parent class has — attributes, methods, all of it — without rewriting any of it.

The three things to remember as a beginner:That's really it for a beginner. The three rules cover 90% of what you'll actually use:

1. Put the parent in parentheses — `class Child(Parent):`
2. Call `super().__init__()` first whenever you write your own `__init__`
3. Override a method by just redefining it with the same name



