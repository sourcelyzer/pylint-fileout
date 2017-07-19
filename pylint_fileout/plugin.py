from __future__ import absolute_import, print_function
import os
import sys
from pylint.reporters.text import ParseableTextReporter
from pylint.interfaces import IReporter

class FileoutReporter(ParseableTextReporter):

    __implements__ = IReporter
    name = 'fileout'
    extension = 'txt'

    def __init__(self, output=None, reports_dir='reports/pylint'):
        ParseableTextReporter.__init__(self, output)
        self._messages = []
        self.reports_dir = reports_dir

    def write_message(self, msg):
        self._messages.append(msg.format(self._template))
        ParseableTextReporter.write_message(self, msg)

    def _display(self, layout):
        ParseableTextReporter._display(self, layout)

        if not os.path.exists(self.reports_dir):
            os.makedirs(self.reports_dir)

        report_file = os.path.join(self.reports_dir, 'pylint.out')

        with open(report_file, 'w') as f:
            for msg in self._messages:
                f.write(msg + os.linesep)


def register(linter):
    linter.register_reporter(FileoutReporter)

