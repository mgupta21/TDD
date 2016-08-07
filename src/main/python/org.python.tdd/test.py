#!/usr/bin/python
__author__ = 'Mayank'


# The first argument of every class method, including __init__, is always a reference to the current instance of the class.
# __init__ is the optional constructor of class

# super class
class TestCase(object):
    def __init__(self, methodName):
        self.methodName = methodName

    def setUp(self):  # no-Opt. empty method (kind of abstract)
        pass

    def tearDown(self):  # no-Opt
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()  # Ensure setup is always run before method run
        try:
            method = getattr(self, self.methodName)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result


class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount = self.runCount + 1

    def testFailed(self):
        self.errorCount = self.errorCount + 1

    def summary(self):
        return "%d run. %d failed" % (self.runCount, self.errorCount)


# sub class
class TestCaseTest(TestCase):
    # Tested in testSetup itself
    # def testRunning(self):
    #     # test = WasRun("testMethod") # Moved to setup
    #     # assert (not test.wasRun)
    #     self.test.run()
    #     assert self.test.wasRun

    # def testSetup(self):
    #     #test = WasRun("testMethod") # Moved to setup
    #     self.test.run()
    #     # assert self.test.wasSetup
    #     assert ("setup testMethod " == self.test.log)

    # Renamed testSetup
    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert ("setup testMethod tearDown " == self.test.log)

    # def setUp(self): # override super class method
    #     self.test = WasRun("testMethod")

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run. 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert ("1 run, 1 failed" == result.summary)

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert ("1 run, 1 failed" == result.summary())


# sub class
class WasRun(TestCase):
    def __init__(self, methodName):
        # self.wasRun = None
        # self.methodName = methodName
        TestCase.__init__(self, methodName)  # same as super(arg);

    def setUp(self):  # override empty method from super
        # self.wasRun = None # Moved from constructor
        # self.wasSetup = 1
        self.log = "setup "  # used to remove all flags

    def testMethod(self):  # Some method to run
        # self.wasRun = 1
        self.log = self.log + "testMethod "

    def testBrokenMethod(self):
        raise Exception

    def tearDown(self):
        self.log = self.log + "tearDown "

        # 1) Moved constant code to super class. 2) Uses attributes only in super class, belongs there
        # def run(self):
        #     method = getattr(self, self.methodName)
        #     method()


# test = WasRun("testMethod")
# print test.wasRun
# test.run()
# print test.wasRun

# TestCaseTest("testRunning").run() # super class constructor takes test method to run as argument
# TestCaseTest("testSetup").run()

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()
TestCaseTest("testFailedResultFormatting").run()
