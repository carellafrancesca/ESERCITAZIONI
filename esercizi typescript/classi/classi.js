var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Person = /** @class */ (function () {
    function Person(name, lastname, age) {
        this.name = name;
        this.lastname = lastname;
        this.age = age;
    }
    Person.prototype.greet = function () {
        return "Hello, my name is ".concat(this.name, " ").concat(this.lastname, " and I am ").concat(this.age, " years old.");
    };
    return Person;
}());
var persona1 = new Person('Mario', 'Rossi', 19);
var persona2 = new Person('Maria', 'Rosa', 21);
console.log(persona1.greet());
console.log(persona2.greet());
var Student = /** @class */ (function (_super) {
    __extends(Student, _super);
    function Student(name, lastname, age, studentId) {
        var _this = _super.call(this, name, lastname, age) || this;
        _this.studentId = studentId;
        return _this;
    }
    Student.prototype.greet = function () {
        return "".concat(_super.prototype.greet.call(this), " My student ID is ").concat(this.studentId, ".");
    };
    return Student;
}(Person));
var student1 = new Student('Alice', 'Verdi', 22, 'S12345');
var student2 = new Student('Mattia', 'Verdi', 26, 'S67890');
console.log(student1.greet());
