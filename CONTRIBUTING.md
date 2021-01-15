# Contributing
First off, thanks for contributing to this project, we appreciate all efforts made to help this project!

## Code of Conduct
before you contribute please have a look at [our Code-of-Conduct](CODE_OF_CONDUCT.md)

- [Contributing](#contributing)
  - [Code of Conduct](#code-of-conduct)
  - [Features, bugs and other issues](#features-bugs-and-other-issues)
    - [Duplicate](#duplicate)
  - [Contributing code](#contributing-code)
    - [Coding conventions](#coding-conventions)
    - [Branching](#branching)
    - [Pull request](#pull-request)
    - [Commit template](#commit-template)
    - [Testing](#testing)
      - [Assets](#assets)


## Features, bugs and other issues
If you would like to report a bug, or request a feature [Open an issue](https://github.com/ilionx/qlabs-limitlessgaming/issues/new/choose), and select the appropriate template 
### Duplicate
please beware to not open a duplicate issue, please first search for the issue, of you didn't find any issue that like yours, feel free to open a new one.

## Contributing code
If you would like to start contributing to the code, select an open issue, Start coding and [open a pull-request ](https://github.com/ilionx/qlabs-limitlessgaming/compare) 
### Coding conventions
We'll use the [standard python coding conventions](https://www.python.org/dev/peps/pep-0008/), these could automatically be checked with `Pylint`, or `Flake8` and even formatted with `autopep8` or `Black` --> Alt + Shift + F is the standard shortcut for auto-formatting a whole document in Visual Studio Code
### Branching
The branching strategy is quite simple, for each new pull request we'll use subject matter branches  
as an example, for a bug fix we'll use the new branch `Limitless-gaming-bugfix-<issue number>` same with features, `Limitless-gaming-feature-<issue number>`. this way if someone want's to start working on a open issue, they can see what code is already present, if it is present.
### Pull request
There is a [pull request template](.github/PULL_REQUEST_TEMPLATE.md), this will ensure consistent and complete pull requests.
If something isn't clear or a PR is taking to long to review, please let us know ASAP.
### Commit template
There is also a small [commit template](docs/.commit-template), to use the commit template execute the following command:  
`git config commit.template ./docs/.commit-template`, for more info have a look into [the file itself](docs/.commit-template)  
please also try not to bulk commit files (commit a large set of files which you have worked on)  
please try committing them as smaller logical groups.
### Testing
We'll use the standard [python unittest module](https://docs.python.org/3/library/unittest.html), it very well documented, and pretty easy in use. for a simple example have a look at [the example test](docs/tests/Example_test.py), the name of a test should always follow the following format -> `*_test.py`, e.g. `example_test.py` or `main_test.py`.  
For more info about how to write and execute test see [How-to-test](docs/How-to-test.md)
#### Assets
if a test needs a input, or stream try to simulate it with a file. please provide the file in the assets folder, with the corresponding test