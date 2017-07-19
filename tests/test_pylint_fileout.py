from pylint_fileout.plugin import FileoutReporter
import random, os, shutil
from pylint.utils import Message
from pylint.interfaces import Confidence

test_message_one = {
    'msg_id': 'C0305',
    'symbol':  'trailing-newlines',
    'msg': 'Trailing newlines',
    'C': 'C',
    'category': 'convention',
    'confidence': Confidence(name='UNDEFINED', description='Warning without any assiociated confidence level.'),
    'abspath': 'somewhere',
    'path': 'pylint_fileout/plugin.py',
    'module': 'pylint_fileout.plugin',
    'obj': '',
    'line': 38,
    'column': 0
}

# test_message_obj = Message('C0305', 'trailing-newlines', (38,0), 'foobar', test_message_one['confidence'])

CWD=None
NEWCWD=None

class TestPylintFileout():

    def setup(self):
        self.cwd = os.getcwd()
        newcwd = os.path.join(os.path.dirname(__file__), 'tmp', str(random.randint(0,1000)))
        os.makedirs(newcwd)

        shutil.copy(os.path.join(os.path.dirname(__file__), 'fixtures', 'code_to_scan.py'), os.path.join(newcwd, 'code_to_scan.py'))

        os.chdir(newcwd)

        self.newcwd = newcwd

    def teardown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.newcwd)
        self.newcwd = None

    def test_fileout_reporter(self):
        from pylint.lint import Run
        args = ['--load-plugins=pylint_fileout.plugin', '-f', 'fileout', 'code_to_scan.py']

        try:
            Run(args)
        except SystemExit:
            pass

        assert os.path.exists(os.path.join(self.newcwd, 'reports', 'pylint', 'pylint.out'))



