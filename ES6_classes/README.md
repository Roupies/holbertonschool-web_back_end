# 0x02. ES6 Classes

This project focuses on ES6 class syntax and object-oriented programming concepts in JavaScript. You'll learn how to define classes, implement inheritance, use getters and setters, and work with advanced class features like static methods and symbols.

## Learning Objectives

At the end of this project, you should be able to explain the following concepts without external help:

- How to define a Class in ES6
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols in ES6
- Getters and setters in classes
- Private attributes and methods
- Abstract classes and method overriding

## Requirements

### General
- All files executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Code should use the `.js` extension
- Code will be tested using Jest Testing Framework
- Code will be analyzed using ESLint with specific rules
- All functions/classes must be exported

### Setup
```bash
# Install NodeJS 12.11.x
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y

# Verify installation
nodejs -v  # Should show v12.11.1
npm -v     # Should show 6.11.3
```

## Tasks

### 0. You Used to Attend a Place Like This
**File:** `0-classroom.js`

Implement a class named `ClassRoom`:
- Constructor accepts one attribute `maxStudentsSize` (Number)
- Store the attribute in an underscore prefixed property

**Usage:**
```javascript
import ClassRoom from "./0-classroom.js";

const room = new ClassRoom(10);
console.log(room._maxStudentsSize); // 10
```

### 1. Let's Make Some Classrooms
**File:** `1-make_classrooms.js`

Implement a function named `initializeRooms`:
- Returns an array of 3 `ClassRoom` objects with sizes 19, 20, and 34

**Usage:**
```javascript
import initializeRooms from './1-make_classrooms.js';

console.log(initializeRooms());
// Array of 3 ClassRoom instances
```

### 2. A Course, Getters, and Setters
**File:** `2-hbtn_course.js`

Implement a class named `HolbertonCourse`:
- Constructor accepts `name` (String), `length` (Number), and `students` (Array of Strings)
- Store each attribute in an underscore prefixed property
- Implement getters and setters for each attribute
- Verify the type of attributes during assignment

**Features:**
- Type validation for all attributes
- Proper getter/setter implementation
- Error handling for invalid types

### 3. Methods, Static Methods, Computed Method Names
**File:** `3-currency.js`

Implement a class named `Currency`:
- Constructor accepts `code` (String) and `name` (String)
- Store each attribute in an underscore prefixed property
- Implement getters and setters for each attribute
- Implement `displayFullCurrency` method that returns the attributes in format: `name (code)`

**Usage:**
```javascript
import Currency from "./3-currency.js";

const dollar = new Currency('$', 'Dollars');
console.log(dollar.displayFullCurrency()); // Dollars ($)
```

### 4. Pricing
**File:** `4-pricing.js`

Implement a class named `Pricing`:
- Constructor accepts `amount` (Number) and `currency` (Currency)
- Store each attribute in an underscore prefixed property
- Implement getters and setters for each attribute
- Implement `displayFullPrice` method that returns: `amount currency_name (currency_code)`
- Implement static method `convertPrice(amount, conversionRate)` that returns amount * conversionRate

**Usage:**
```javascript
import Pricing from './4-pricing.js';
import Currency from './3-currency.js';

const p = new Pricing(100, new Currency("EUR", "Euro"));
console.log(p.displayFullPrice()); // 100 Euro (EUR)
```

### 5. A Building
**File:** `5-building.js`

Implement a class named `Building`:
- Constructor accepts `sqft` (Number)
- Store the attribute in an underscore prefixed property
- Implement getter for the attribute
- Consider this class as an abstract class
- Any class extending from it should implement `evacuationWarningMessage` method
- If a class extends this and doesn't implement the method, throw an error

**Abstract Class Pattern:**
- Enforces method implementation in subclasses
- Demonstrates abstract class concepts in JavaScript

### 6. Inheritance
**File:** `6-sky_high.js`

Implement a class named `SkyHighBuilding` that extends from `Building`:
- Constructor accepts `sqft` (Number) and `floors` (Number)
- Store each attribute in an underscore prefixed property
- Implement getters for each attribute
- Override `evacuationWarningMessage` method to return: `Evacuate slowly the NUMBER_OF_FLOORS floors`

**Inheritance Features:**
- Proper use of `super()` in constructor
- Method overriding
- Extension of parent class functionality

### 7. Airport
**File:** `7-airport.js`

Implement a class named `Airport`:
- Constructor accepts `name` (String) and `code` (String)
- Store each attribute in an underscore prefixed property
- Implement getters for each attribute
- Default string description should return the airport code

**Metaprogramming:**
- Custom `toString()` implementation
- Use of `Symbol.toStringTag`

### 8. Primitive - Holberton Class
**File:** `8-hbtn_class.js`

Implement a class named `HolbertonClass`:
- Constructor accepts `size` (Number) and `location` (String)
- Store each attribute in an underscore prefixed property
- When cast to Number, return the size
- When cast to String, return the location

**Type Conversion:**
- Custom `valueOf()` method for Number conversion
- Custom `toString()` method for String conversion

### 9. Hoisting
**File:** `9-hoisting.js`

Fix the code and make it work:
- Define `HolbertonClass` and `StudentHolberton` classes properly
- Create instances with proper class relationships
- Export a list of students

**Hoisting Concepts:**
- Proper class declaration order
- Class instantiation best practices
- Module exports with classes

### 10. Vroom
**File:** `10-car.js`

Implement a class named `Car`:
- Constructor accepts `brand` (String), `motor` (String), and `color` (String)
- Store each attribute in an underscore prefixed property
- Implement getters and setters for each attribute
- Add method `cloneCar()` that returns a new object of the same class
- Use `Symbol.species` to make cloning work with inheritance

**Advanced Features:**
- Symbol.species for constructor inheritance
- Proper cloning mechanism
- Metaprogramming concepts

## Usage Examples

```javascript
// Basic class usage
import ClassRoom from "./0-classroom.js";
const room = new ClassRoom(10);

// Inheritance example
import SkyHighBuilding from './6-sky_high.js';
const building = new SkyHighBuilding(140, 60);
console.log(building.evacuationWarningMessage());

// Type conversion example
import HolbertonClass from "./8-hbtn_class.js";
const hc = new HolbertonClass(12, "Mezzanine");
console.log(Number(hc)); // 12
console.log(String(hc)); // Mezzanine

// Static method example
import Pricing from './4-pricing.js';
console.log(Pricing.convertPrice(100, 1.2)); // 120
```

## Testing

Run the tests using Jest:
```bash
npm test
```

Run ESLint for code analysis:
```bash
npm run lint
```

## Key ES6 Class Features Covered

1. **Class Declaration**: Basic class syntax with constructor
2. **Getters and Setters**: Property access control and validation
3. **Inheritance**: Extending classes with `extends` and `super`
4. **Static Methods**: Class-level methods not tied to instances
5. **Abstract Classes**: Enforcing method implementation in subclasses
6. **Method Overriding**: Customizing parent class behavior
7. **Type Conversion**: Custom `valueOf()` and `toString()` methods
8. **Symbols**: Using `Symbol.species` and `Symbol.toStringTag`
9. **Private Properties**: Convention using underscore prefixes
10. **Metaprogramming**: Advanced class manipulation techniques

## Object-Oriented Programming Concepts

- **Encapsulation**: Data hiding with private properties
- **Inheritance**: Code reuse through class extension
- **Polymorphism**: Method overriding and type conversion
- **Abstraction**: Abstract classes and interface enforcement

## Best Practices

1. **Use getters/setters** for data validation and encapsulation
2. **Validate input types** in setters to prevent runtime errors
3. **Call `super()`** first in child class constructors
4. **Use underscore prefix** for private properties by convention
5. **Implement abstract methods** when extending abstract classes
6. **Use static methods** for utility functions related to the class
7. **Handle inheritance properly** with Symbol.species for cloning

## Resources

- [Classes - JavaScript MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)
- [Metaprogramming](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming)
- [ES6 Classes in Depth](https://ponyfoo.com/articles/es6-classes-in-depth)

## Author

Educational project for learning ES6 classes and object-oriented programming in JavaScript. 