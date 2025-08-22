# 0x00. ES6 Basics

This project covers the fundamental concepts of ECMAScript 6 (ES6), the major update to JavaScript released in 2015. Through practical exercises, you'll learn about new features that make JavaScript more powerful and expressive.

## Learning Objectives

At the end of this project, you should be able to explain the following concepts without external help:

- What ES6 is and its significance
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables (`let` and `const`)
- Arrow functions and function parameters default to them
- Rest and spread function parameters
- String templating in ES6 (template literals)
- Object creation and their properties in ES6
- Iterators and for-of loops

## Requirements

### General
- All files executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Code should use the `.js` extension
- Code will be tested using the Jest Testing Framework
- Code will be analyzed using ESLint with specific rules
- All functions must be exported

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

### 0. Const or let?
**File:** `0-constants.js`

Modify the variables to use `const` and `let` appropriately:
- Use `const` when the value won't be reassigned
- Use `let` when the value might change

**Functions:**
- `taskFirst()` - Returns a string using const
- `taskNext()` - Returns a string using let and concatenation

### 1. Block Scope
**File:** `1-block-scoped.js`

Demonstrates block scoping with `const` and `let`:
- Variables declared inside a block don't affect outer scope
- Returns an array showing the outer scope values

**Function:**
- `taskBlock(trueOrFalse)` - Shows block scoping behavior

### 2. Arrow Functions
**File:** `2-arrow.js`

Convert a standard function to use ES6 arrow function syntax:
- Arrow functions maintain lexical `this` binding
- Useful for callbacks and event handlers

**Function:**
- `getNeighborhoodsList()` - Constructor function with arrow method

### 3. Parameter Defaults
**File:** `3-default-parameter.js`

Use ES6 default parameter syntax:
- Simplifies function definitions
- Provides fallback values when arguments are undefined

**Function:**
- `getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19)` - Sum with defaults

### 4. Rest Parameter Syntax
**File:** `4-rest-parameter.js`

Use the rest parameter (`...args`) to handle variable arguments:
- Collects remaining arguments into an array
- Replaces the need for the `arguments` object

**Function:**
- `returnHowManyArguments(...args)` - Counts arguments using rest syntax

### 5. The Wonders of Spread Syntax
**File:** `5-spread-operator.js`

Use spread syntax to concatenate arrays and strings:
- Expands iterables into individual elements
- Useful for array concatenation and function calls

**Function:**
- `concatArrays(array1, array2, string)` - Concatenates using spread

### 6. Take Advantage of Template Literals
**File:** `6-string-interpolation.js`

Use template literals for string interpolation:
- Embed expressions within strings using `${}`
- Supports multi-line strings
- More readable than string concatenation

**Function:**
- `getSanFranciscoDescription()` - Returns formatted description using template literals

### 7. Object Property Value Shorthand Syntax
**File:** `7-getBudgetObject.js`

Use ES6 shorthand property syntax:
- When property name matches variable name
- Reduces redundant code

**Function:**
- `getBudgetObject(income, gdp, capita)` - Returns object using shorthand

### 8. Computed Property Names
**File:** `8-getBudgetCurrentYear.js`

Use computed property names in object literals:
- Dynamic property names using `[expression]`
- Useful for creating objects with variable keys

**Function:**
- `getBudgetForCurrentYear(income, gdp, capita)` - Creates object with computed keys

### 9. ES6 Method Properties
**File:** `9-getFullBudget.js`

Use ES6 method shorthand in object literals:
- Define methods without the `function` keyword
- Cleaner syntax for object methods

**Function:**
- `getFullBudgetObject(income, gdp, capita)` - Object with method properties

### 10. For...of Loops
**File:** `10-loops.js`

Use the for...of loop instead of for...in:
- Iterates over iterable objects (arrays, strings, etc.)
- More intuitive than traditional for loops
- Provides direct access to values

**Function:**
- `appendToEachArrayValue(array, appendString)` - Modifies array using for...of

### 11. Iterator
**File:** `11-createEmployeesObject.js`

Create objects using ES6 features:
- Dynamic property assignment
- Computed property names

**Function:**
- `createEmployeesObject(departmentName, employees)` - Creates department object

### 12. Let's Create a Report Object
**File:** `12-createReportObject.js`

Create a report object with methods:
- Combine multiple ES6 features
- Object spread syntax
- Method shorthand

**Function:**
- `createReportObject(employeesList)` - Creates comprehensive report

## Usage Examples

```javascript
// Task 0: Constants and variables
import { taskFirst, taskNext } from './0-constants.js';
console.log(`${taskFirst()} ${taskNext()}`);

// Task 1: Block scope
import taskBlock from './1-block-scoped.js';
console.log(taskBlock(true));  // [false, true]
console.log(taskBlock(false)); // [false, true]

// Task 2: Arrow functions
import getNeighborhoodsList from './2-arrow.js';
const neighborhoodsList = new getNeighborhoodsList();
console.log(neighborhoodsList.addNeighborhood('Noe Valley'));

// Task 3: Default parameters
import getSumOfHoods from './3-default-parameter.js';
console.log(getSumOfHoods(34));      // 142 (34 + 89 + 19)
console.log(getSumOfHoods(34, 3));   // 56  (34 + 3 + 19)
console.log(getSumOfHoods(34, 3, 4)); // 41  (34 + 3 + 4)
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

## Key ES6 Features Covered

1. **Block Scoping**: `let` and `const` provide block-level scope
2. **Arrow Functions**: Concise function syntax with lexical `this`
3. **Default Parameters**: Function parameters with default values
4. **Rest Parameters**: Collect remaining arguments into an array
5. **Spread Syntax**: Expand iterables into individual elements
6. **Template Literals**: String interpolation with embedded expressions
7. **Object Shorthand**: Concise object property and method syntax
8. **Computed Properties**: Dynamic object property names
9. **For...of Loops**: Iterate over iterable objects
10. **Destructuring**: Extract values from arrays and objects

## Resources

- [ECMAScript 6 - ECMAScript 2015](https://www.w3schools.com/js/js_es6.asp)
- [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [Rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
- [Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)

## Author

Educational project for learning ES6 fundamentals and modern JavaScript development practices. 