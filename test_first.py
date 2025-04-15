import sys
class RunTest:
	btc = None
	def __init__(self, thismod, btc, e_path, experiment, verbose):
		# runs the whole testing cycle
		self.thismod = thismod
		e_mod = experiment.replace('.py', '')
		if not btc.load_module_for_testing(e_path, e_mod):
			print(f"Module {experiment} cannot be found or tested")
			sys.exit(1)
		btc.verbose = verbose
		btc.set_methods_in_runtest(self)
		ef = [
			'plus',
			'minus',
			'sul',
			'fromargs',
			'frominput',
			'tooutput',
			'bodexit',
		]
		if not btc.exist_functions(ef):
			return

		self.btc = btc
		self.btc.run_all_tests()

	def test_plus(self):
		funcname = 'plus'
		testname = ''
		expected = 5
		parameters = (2, 3)
		comargs = []
		self.btc.assert_params_comargs(funcname, testname, expected, parameters, comargs)

	def test_sul(self):
		funcname = 'sul'
		testname = ''
		expected = 3
		parameters = (3, 1)
		comargs = []
		self.btc.assert_params_comargs(funcname, testname, expected, parameters, comargs)

	def test_sul_nul(self):
		funcname = 'sul'
		testname = ''
		expected = 'ZeroDivisionError'
		parameters = (3, 0)
		comargs = []
		# self.btc.assert_params_comargs(funcname, testname, expected, parameters, comargs)
		self.btc.raise_error(funcname, testname, expected, parameters, comargs)

	def test_fromargs_ok(self):
		funcname = 'fromargs'
		testname = ''
		expected = 15
		parameters = tuple()
		comargs = ['3', '5']
		self.btc.assert_params_comargs(funcname, testname, expected, parameters, comargs)

	def test_fromargs_nul(self):
		funcname = 'fromargs'
		testname = ' with not enough command line arguments'
		expected = 'IndexError'
		parameters = tuple()
		comargs = ['3']
		self.btc.raise_error(funcname, testname, expected, parameters, comargs)

	def test_frominput(self):
		funcname = 'frominput'
		expected = 'BOEF'
		parameters = tuple()
		comargs = []
		erin = "Boef"
		testname = f' where user input would be "{erin}"'
		self.btc.input_and_or_output(funcname, testname, expected, parameters, comargs, erin=erin)

	def test_tooutput(self):
		funcname = 'tooutput'
		expected = 'prutje'
		parameters = tuple()
		comargs = []
		eruit = expected
		testname = f' where prompt output should be "{eruit}"'
		self.btc.input_and_or_output(funcname, testname, expected, parameters, comargs, eruit=eruit)

	def test_must_exit(self):
		funcname = 'bodexit'
		expected = 1
		parameters = ('dusss',)
		comargs = []
		testname = f' should exit with message "{expected}"'
		self.btc.sys_exit(funcname, testname, expected, parameters, comargs)
