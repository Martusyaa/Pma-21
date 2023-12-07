from abc import ABC, abstractmethod

class ResearchGuidelineFactory(ABC):

    @abstractmethod
    def create_steps(self):
        pass

class UniversityAFactory(ResearchGuidelineFactory):

    def create_steps(self):
        return UniversityASteps()


class UniversityBFactory(ResearchGuidelineFactory):

    def create_steps(self):
        return UniversityBSteps()

class ResearchGuidelineSteps(ABC):

    def templateMethod(self):
        self.step1()
        self.step2()
        self.step3()
        self.step4()

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass

    @abstractmethod
    def step4(self):
        pass

class UniversityASteps(ResearchGuidelineSteps):

    def step2(self):
        print("Step 2 - Applied by University A")

    def step3(self):
        print("Step 3 - Applied by University A")

class UniversityBSteps(ResearchGuidelineSteps):

    def step1(self):
        print("Step 1 - Applied by University B")

    def step3(self):
        print("Step 3 - Applied by University B")

    def step4(self):
        print("Step 4 - Applied by University B")


factory_a = UniversityAFactory()
steps_a = factory_a.create_steps()
steps_a.templateMethod()

factory_b = UniversityBFactory()
steps_b = factory_b.create_steps()
steps_b.templateMethod()