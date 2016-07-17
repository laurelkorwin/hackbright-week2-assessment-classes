"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Abstraction: You can hide away the "how" of why things work, and interact easily
                with your classes/instances
   Encapsulation: You put all the data related to a "thing" or class/instance together,
                and close to the "thing".
   Polymorphism: Your objects are structured in such a way that you can interact with
                them in the same way, and their components are interchangeable.

2. What is a class?
    A class is an object that represents a particular "type" of thing, that stores information
    and methods available to that thing.

3. What is an instance attribute?
    An instance attribute is an attribute that is applicable only to a specific instance of a class.
    For example, if you had a class "OlympicSwimmers" and an instance "michael_phelps", the name variable
    for Michael Phelps would be an instance attribute, because it applies only to him - not to all swimmers.
    Similarly, if I made a class for my family ("KorwinFamily") and an instance for myself, I could set an
    instance attribute for likes_spin_classes = True for myself, because it applies only to me and not to
    any other of my family members.

4. What is a method?
    A method is a function that is available to a particular class. Specifically, you can call a method on
    an instance of that class to get it to do or return whatever the function indicates. For example, if you
    had a class for Hackbrighters, an instance of that class for Laurel and a method def code(): return "I <3 CODING",
    you could call the code method as follows: laurel.code() and it would return "I <3 CODING."

5. What is an instance in object orientation?
    An instance is an individual occurrence of a particular class. See above example - class, OlympicSwimmers, instance
    michael_phelps.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute is something that is shared for all members of a class, where an instance attribute is different for
   varied instances of that class. For example, class Hackbrighters - a class attribute could be likes_to_code = True,
   because hopefully we all do!! An instance attribute for class Hackbrighters could be favorite_lecture_snack, because
   that will vary for each of us.


"""

"""Part 2 - 3 Classes & Class Methods"""


class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        user_answer = raw_input(self.question + " ")
        if user_answer == self.answer:
            return True
        else:
            return False


class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, answer):
        new_question = Question(question, answer)
        self.questions.append(new_question)

    def administer(self):
        self.score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                self.score += 1
        return self.score


class Quiz(Exam):

    def administer(self):
        self.score = {"True": 0, "False": 0}
        for question in self.questions:
            if question.ask_and_evaluate():
                self.score["True"] += 1
            else:
                self.score["False"] += 1

        self.score_percentage = float(self.score["True"]) / (self.score["True"] + self.score["False"])

        if self.score_percentage > 0.5:
            return True
        else:
            return False


def take_test(exam, student):
    student.score = exam.administer()

    return student.score


def example():
    sample_exam = Exam("Sample")

    sample_exam.add_question("Who's the President of the US?", "Barack Obama")
    sample_exam.add_question("What year is it?", "2016")
    sample_exam.add_question("What city are we in?", "San Francisco")

    sample_student = Student("Suzie", "Sample", "1 Main St SF CA")

    sample_score = take_test(sample_exam, sample_student)

    return "{}, your sample score is {}".format(sample_student.first_name, sample_score)
