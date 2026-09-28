# 🏋️ Gym Management System

A simple **Gym Management System** built with Python using Object-Oriented Programming (OOP).

The system allows gym administrators to manage members, trainers, memberships, payments, and attendance through a simple **Tkinter GUI**.

The project also uses **JSON file handling** to save and load data.

---

## 📌 Project Overview

The Gym Management System is designed to manage the main operations of a gym.

The system provides functionality for:

- Managing gym members
- Managing trainers
- Managing memberships
- Managing payments
- Managing attendance
- Searching for records
- Filtering memberships
- Validating business rules
- Saving and loading data using JSON
- Displaying real-time dashboard statistics
- Providing a graphical user interface using Tkinter

---

## ✨ Features

### 👤 Members

The system supports:

- Add member
- Search member
- Update member
- Delete member

Member information includes:

- ID
- Name
- Email
- Phone

---

### 🏋️ Trainers

The system supports:

- Add trainer
- Search trainer
- Update trainer
- Delete trainer

Trainer information includes:

- ID
- Name
- Phone
- Specialty

Available specialties:

- Fitness
- Cardio
- Bodybuilding

---

### 📅 Memberships

The system supports:

- Add membership
- Search membership
- Update membership
- Delete membership
- Filter memberships

Membership types:

- Monthly
- Quarterly
- Yearly

Memberships can also be filtered by:

- All
- Active
- Expired

---

### 💰 Payments

The system supports:

- Add payment
- Search payment
- Update payment
- Delete payment

Each payment contains:

- ID
- Member
- Amount
- Payment date

The payment amount must be greater than zero.

---

### 📝 Attendance

The system supports:

- Add attendance
- Search attendance
- Update attendance
- Delete attendance

Attendance contains:

- ID
- Member
- Attendance date

A member can only attend the gym if they have an active membership.

---

# 🧠 OOP Concepts Used

This project demonstrates the main Object-Oriented Programming concepts required for the project.

## 1. Classes and Objects

The project contains multiple classes such as:

- `Person`
- `Member`
- `Trainer`
- `Membership`
- `Payment`
- `Attendance`
- `Gym`
- `FileManager`

Objects are created from these classes to represent real entities in the gym system.

---

## 2. Constructor

Each class uses the `__init__()` constructor to initialize its attributes.

Example:

```python
class Member(Person):

    def __init__(self, id, phone, name, email):
        super().__init__(id, phone, name)
        self.email = email
```

---

## 3. Encapsulation

Encapsulation is demonstrated using private attributes.

For example, the `Gym` class stores payments using:

```python
self.__payments = []
```

The payment list can be accessed through a property:

```python
@property
def payments(self):
    return self.__payments
```

The `Person` class also uses a private ID:

```python
self.__id = id
```

---

## 4. Inheritance

`Member` and `Trainer` inherit from the abstract `Person` class.

```text
        Person
        /    \
    Member  Trainer
```

This allows both classes to reuse common attributes such as:

- ID
- Name
- Phone

---

## 5. Abstraction

The `Person` class is an abstract class.

It inherits from `ABC` and contains an abstract method:

```python
@abstractmethod
def get_role(self):
    pass
```

This means that child classes must provide their own implementation of `get_role()`.

---

## 6. Polymorphism

Both `Member` and `Trainer` implement the same method:

```python
get_role()
```

But each class provides its own implementation.

For example:

```python
Member.get_role()
```

returns:

```text
i am member
```

while:

```python
Trainer.get_role()
```

returns:

```text
I am trainer
```

This demonstrates method overriding and polymorphism.

---

## 7. Composition

The project uses composition between several classes.

For example:

- `Membership` contains a `Member`
- `Payment` contains a `Member`
- `Attendance` contains a `Member`
- `Gym` contains collections of members, trainers, memberships, payments, and attendance records

Example:

```python
membership.member
```

refers to a `Member` object.

---

## 8. Type Hints

Type hints are used in the project to make the expected types of parameters clearer.

Example:

```python
def add_member(self, member: Member):
    self.members.append(member)
```

Another example:

```python
def add_payment(self, payment: Payment):
    self.__payments.append(payment)
```

---

# ⚙️ Business Rules

The system contains several business rules to prevent invalid operations.

### Membership Rule

A member cannot have more than one active membership.

If a member already has an active membership, the system raises an exception.

```text
You already active
```

---

### Attendance Rule

A member cannot attend the gym if their membership is expired.

The system checks the membership status before adding attendance.

---

### Payment Rule

Payment amount must be greater than zero.

For example:

```text
Amount = 0
```

is rejected.

---

### Membership Date Rule

The membership start date cannot be after the end date.

For example:

```text
Start Date: 20/09/2026
End Date: 10/09/2026
```

is invalid.

---

### Trainer Specialty Rule

The trainer specialty must be one of:

```text
fitness
cardio
bodybuilding
```

---

# 💾 File Handling

The project uses a JSON file to store the gym data.

The file is:

```text
gym_data.json
```

The system can:

- Save data
- Load data
- Convert objects into dictionaries
- Convert dictionaries back into objects

---

## Saving Data

Objects are converted into dictionaries using `to_dict()`.

Example:

```python
gym.to_dict()
```

The resulting dictionary is saved using `FileManager`.

---

## Loading Data

When the program starts, data is loaded from:

```text
gym_data.json
```

The `from_dict()` methods recreate the required objects.

For example:

```python
Member.from_dict(member_data)
```

---

# 📊 Dashboard

The application contains a dashboard displaying real data from the system.

The dashboard shows:

- Total Members
- Total Trainers
- Active Memberships
- Expired Memberships
- Total Payments
- Total Attendance

The dashboard is updated after adding or deleting records.

---

# 🖥️ Graphical User Interface

The project uses **Tkinter** to provide a graphical user interface.

The main window contains access to:

- Members
- Trainers
- Memberships
- Payments
- Attendance
- Save Data

Each section provides the required operations for managing its data.

The GUI also displays error and success messages using Tkinter message boxes.

---

# 📂 Project Structure

```text
Gym Management System/
│
├── main.py
├── gui.py
│
├── GYM.py
├── Member.py
├── Person.py
├── Trainer.py
├── Membership.py
├── Payment.py
├── Attendance.py
│
├── FileManager.py
├── gym_data.json
│
└── tests.py
```

---

# ▶️ How to Run

## 1. Clone or download the project

Download the project files to your computer.

---

## 2. Make sure Python is installed

The project requires Python 3.

You can check your Python version using:

```bash
python --version
```

---

## 3. Run the application

Open the project folder in a terminal and run:

```bash
python main.py
```

The Gym Management System GUI will open.

---

# 🧪 Testing

The project includes test scenarios covering different types of operations.

The tests cover:

### Successful Operations

- Adding a member
- Adding a trainer
- Adding a payment

### Invalid Inputs

- Invalid trainer specialty
- Invalid membership type
- Payment amount less than or equal to zero

### Business Rule Violations

- Creating another active membership for a member
- Attendance with an expired membership

### Edge Cases

- Searching for a non-existing member
- Working with an empty gym

---

# 🛡️ Exception Handling

Custom exceptions are used to handle different problems in the system.

Examples include:

```python
class action_status(Exception):
    pass
```

and:

```python
class not_found(Exception):
    pass
```

These exceptions are used when operations cannot be completed successfully.

The GUI catches exceptions and displays the error message to the user.

---

# 🔄 CRUD Operations

CRUD stands for:

- **Create**
- **Read**
- **Update**
- **Delete**

The system provides CRUD functionality for the main entities:

| Entity     | Create | Read/Search | Update | Delete |
| ---------- | ------ | ----------- | ------ | ------ |
| Member     | ✅     | ✅          | ✅     | ✅     |
| Trainer    | ✅     | ✅          | ✅     | ✅     |
| Membership | ✅     | ✅          | ✅     | ✅     |
| Payment    | ✅     | ✅          | ✅     | ✅     |
| Attendance | ✅     | ✅          | ✅     | ✅     |

Memberships also support filtering by status.

---

# 🎯 Project Goals

The main goals of this project are to demonstrate:

- Object-Oriented Programming
- Class relationships
- Inheritance
- Abstraction
- Polymorphism
- Encapsulation
- Composition
- Exception handling
- Type hints
- File handling
- JSON persistence
- CRUD operations
- Searching and filtering
- Business rule validation
- GUI development

---

# 👨‍💻 Technologies Used

- **Python 3**
- **Tkinter**
- **JSON**
- **Object-Oriented Programming**

---

# 📌 Notes

The application automatically loads the existing data when it starts.

Data can be saved using the **Save Data** button.

The application also saves the current data before closing.

All main operations are handled by the `Gym` class, while the GUI is responsible for displaying information and receiving user input.

```

```
