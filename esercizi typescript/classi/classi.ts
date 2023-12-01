class Person {
    name: string;
    lastname: string;
    age: number;
  
    constructor(name: string, lastname: string, age: number) {
      this.name = name;
      this.lastname = lastname;
      this.age = age;
    }
  
    greet(): string {
      return `Hello, my name is ${this.name} ${this.lastname} and I am ${this.age} years old.`;
    }
}

const persona1 = new Person('Mario', 'Rossi', 19);
const persona2 = new Person('Maria', 'Rosa', 21);
console.log(persona1.greet());
console.log(persona2.greet());

class Student extends Person {
    studentId: string;

    constructor(name: string, lastname: string, age: number, studentId: string) {
        super(name, lastname, age);
        this.studentId = studentId;
    } 
    
    greet(): string {
      return `${super.greet()} My student ID is ${this.studentId}.`;
    }
}

const student1 = new Student('Alice', 'Verdi', 22, 'S12345');
const student2 = new Student('Mattia', 'Verdi', 26, 'S67890');
console.log(student1.greet());