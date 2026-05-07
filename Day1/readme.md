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


Privacy level summary
_name → “internal by convention”
__name → “internally renamed (harder to access)”
__name__ → reserved for Python special methods (__init__, __str__)


05/07/2026
Polymorphism - many forms
Python can call same method name from different classes with different types but Python can still map to w

FULL CHEAT SHEET — DAYS 1–4

Everything in one place

Define a class      class MyClass:
Constructor         def __init__(self, x): self.x = x
Encapsulation       Prefix private attrs with _ (e.g. self._status)
Child class         class Child(Parent):
Call parent init    super().__init__(args) — always first line
Override method     Redefine same method name in child class
Polymorphism        Same method name across classes → loop and call once
Duck typing         Any object with the right method works — no inheritance needed
ABC import          from abc import ABC, abstractmethod
Make abstract       @abstractmethod above method + pass as body
ABC parent          class PrintJob(ABC):
ABC error           TypeError if subclass skips an abstract method

