# DSA and DesignPattern
<hr>

## Creational Patterns

### Factory Method
Use the Factory Method when you don’t know beforehand the exact types and dependencies of the objects your code should work with.

Use the Factory Method when you want to provide users of your library or framework with a way to extend its internal components.

Use the Factory Method when you want to save system resources by reusing existing objects instead of rebuilding them each time.

### Abstract Factory
Use the Abstract Factory when your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you simply want to allow for future extensibility.

The Abstract Factory provides you with an interface for creating objects from each class of the product family. As long as your code creates objects via this interface, you don’t have to worry about creating the wrong variant of a product which doesn’t match the products already created by your app.

### Builder
Use the Builder pattern to get rid of a “telescoping constructor”.

 Use the Builder pattern when you want your code to be able to create different representations of some product (for example, stone and wooden houses).

Use the Builder to construct Composite trees or other complex objects.

### Prototype
Use the Prototype pattern when your code shouldn’t depend on the concrete classes of objects that you need to copy.

Use the pattern when you want to reduce the number of subclasses that only differ in the way they initialize their respective objects.

### Singleton
Use the Singleton pattern when a class in your program should have just a single instance available to all clients; for example, a single database object shared by different parts of the program.

Use the Singleton pattern when you need stricter control over global variables.

## Structural Patterns

### Adapter

Use the Adapter class when you want to use some existing class, but its interface isn't compatible with the rest of your code.

Use the pattern when you want to reuse several existing subclasses that lack some common functionality that can't be added to the superclass.

### Bridge


### Composite
Use the Composite pattern when you have to implement a tree-like object structure.

Use the pattern when you want the client code to treat both simple and complex elements uniformly.

### Decorator


### Facade


### Flyweight


### Proxy


## Behavioral Patterns