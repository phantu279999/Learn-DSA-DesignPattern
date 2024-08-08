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
Use the Bridge pattern when you want to divide and organize a monolithic class that has several variants of some functionality (for example, if the class can work with various database servers).

Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.

Use the Bridge if you need to be able to switch implementations at runtime.


### Composite
Use the Composite pattern when you have to implement a tree-like object structure.

Use the pattern when you want the client code to treat both simple and complex elements uniformly.

### Decorator
Use the Decorator pattern when you need to be able to assign extra behaviors to objects at runtime without breaking the code that uses these objects.

Use the pattern when it’s awkward or not possible to extend an object’s behavior using inheritance.

### Facade
Use the Facade pattern when you need to have a limited but straightforward interface to a complex subsystem

Use the Facade when you want to structure a subsystem into layers.

### Flyweight
Use the Flyweight pattern only when your program must support a huge number of objects which barely fit into available RAM.

### Proxy
Lazy initialization (virtual proxy). This is when you have a heavyweight service object that wastes system resources by being always up, even though you only need it from time to time.

Access control (protection proxy). This is when you want only specific clients to be able to use the service object; for instance, when your objects are crucial parts of an operating system and clients are various launched applications (including malicious ones).

Local execution of a remote service (remote proxy). This is when the service object is located on a remote server.

Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.

Caching request results (caching proxy). This is when you need to cache results of client requests and manage the life cycle of this cache, especially if results are quite large.

Smart reference. This is when you need to be able to dismiss a heavyweight object once there are no clients that use it

## Behavioral Patterns

### Chain of Responsibility
Use the Chain of Responsibility pattern when your program is expected to process different kinds of requests in various ways, but the exact types of requests and their sequences are unknown beforehand.

Use the pattern when it’s essential to execute several handlers in a particular order.

Use the CoR pattern when the set of handlers and their order are supposed to change at runtime.

### Command
Use the Command pattern when you want to parametrize objects with operations.

Use the Command pattern when you want to queue operations, schedule their execution, or execute them remotely.

Use the Command pattern when you want to implement reversible operations.

### Iterator
Use the Iterator pattern when your collection has a complex data structure under the hood, but you want to hide its complexity from clients (either for convenience or security reasons).

Use the pattern to reduce duplication of the traversal code across your app.

Use the Iterator when you want your code to be able to traverse different data structures or when types of these structures are unknown beforehand.

### Mediator
Use the Mediator pattern when it’s hard to change some of the classes because they are tightly coupled to a bunch of other classes.

Use the pattern when you can’t reuse a component in a different program because it’s too dependent on other components.

Use the Mediator when you find yourself creating tons of component subclasses just to reuse some basic behavior in various contexts.

### Memento
Use the Memento pattern when you want to produce snapshots of the object’s state to be able to restore a previous state of the object.

Use the pattern when direct access to the object’s fields/getters/setters violates its encapsulation.

### Observer
Use the Observer pattern when changes to the state of one object may require changing other objects, and the actual set of objects is unknown beforehand or changes dynamically.

Use the pattern when some objects in your app must observe others, but only for a limited time or in specific cases.

### State
Use the State pattern when you have an object that behaves differently depending on its current state, the number of states is enormous, and the state-specific code changes frequently.

Use the pattern when you have a class polluted with massive conditionals that alter how the class behaves according to the current values of the class’s fields.

Use State when you have a lot of duplicate code across similar states and transitions of a condition-based state machine.

### Strategy
Use the Strategy pattern when you want to use different variants of an algorithm within an object and be able to switch from one algorithm to another during runtime.

Use the Strategy when you have a lot of similar classes that only differ in the way they execute some behavior.

Use the pattern to isolate the business logic of a class from the implementation details of algorithms that may not be as important in the context of that logic.

Use the pattern when your class has a massive conditional statement that switches between different variants of the same algorithm.

### Template Method
Use the Template Method pattern when you want to let clients extend only particular steps of an algorithm, but not the whole algorithm or its structure.

Use the pattern when you have several classes that contain almost identical algorithms with some minor differences. As a result, you might need to modify all classes when the algorithm changes.

### Visitor
Use the Visitor when you need to perform an operation on all elements of a complex object structure (for example, an object tree).

Use the Visitor to clean up the business logic of auxiliary behaviors.

Use the pattern when a behavior makes sense only in some classes of a class hierarchy, but not in others.

