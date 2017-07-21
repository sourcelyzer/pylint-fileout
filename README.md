# pylint-fileout

This is a plugin to write the output of pylint's parseable format to a text file.

## Installation

```
$ pip install git+git://github.com/sourcelyzer/pylint-fileout.git
```

## Usage

```
$ pylint --load-plugins=pylint_fileout.plugin -f fileout [python module to scan]
```

The report is saved to `reports/pylint/pylint.out`

Pylint does not have any file writing reporter, and tox doesn't support stdout redirection in its `commands` setting. Thus if you want to process pylint messages then you can use this plugin.

## Limitations

The plugin currently can not be configured, thus reports are always in `reports/pylint/pylint.out`. Eventually some form of plugin configuration, most likely with environment variables, will be introduced.
