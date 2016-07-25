#!/usr/bin/python
__author__ = 'Mayank'


class TestCase(object):
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class TestCaseTest(TestCase):
    def testRunning(self):
        test.run()
        assert (self.test.wasRun)

    def testSetUp(self):
        test.run()
        assert (self.test.wasSetup)

    def setUp(self):
        self.test = WasRun("testMethod")


class WasRun(TestCase):
    def __init__(self, name):
        # self.wasRun = None
        # self.name = name
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

    def testMethod(self):
        self.wasRun = 1


        # def run(self):
        #     method = getattr(self, self.name)
        #     method()


# test = WasRun("testMethod")
# print test.wasRun
# test.run()
# print test.wasRun

TestCaseTest("testRunning").run()
