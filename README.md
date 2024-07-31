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

### Prototype

### Singleton
