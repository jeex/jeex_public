from base_test import BaseTest

class RunTest(BaseTest):
	def mandatory_functions(self):
		return ['ask_name', 'say_hello']

	def test_ask_name(self):
		funcname = 'ask_name'
		expected = 'Jacques'
		parameters = tuple()
		comargs = []
		erin = "Jacques"
		testname = f' where user input would be "{erin}"'
		self.input_and_or_output(funcname, testname, expected, parameters, comargs, erin=erin)

	def test_say_hello(self):
		funcname = 'say_hello'
		expected = 'Sjakie'
		parameters = [expected]
		comargs = []
		eruit = expected
		testname = f' where prompt output should be "{eruit}"'
		self.input_and_or_output(funcname, testname, expected, parameters, comargs, eruit=eruit)

