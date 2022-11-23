# Test Automation Framework BDD - Demo

Run Automation Tests for this API and Web UI Demo.

## Getting Started

### Install

Run `scripts/helper setup` to install all dependencies.

### Usage

Write tests described in business language as features and scenarios in
`*.feature` files.

Write the glue code in `steps/*.py` files mapping actions to steps within
the context of a particular product.

Write modules/classes encapsulating common logic between various systems
under test in `lib/`, so we can share across tests of different products.

Run your tests with `scripts/test [project_name]` (a project being a directory
under `features/`).

## Project Architecture

### Project Design

      System Under Test: features/product
     Feature Under Test:   ↳ features/product/basic_checks.feature
              Glue Code:     ↳ features/product/steps/basic_checks.py
    Implementation Code:       ↳ lib/api/product
    Implementation Code:       ↳ lib/webdriver/product

#### features/*

Contains a directory for each system under test (in business terms, a product).

#### features/**/*

Contains all feature files and step definitions relevant to testing a
particular system or product.

#### features/**/*.feature

These files express scenarios and features we wish to test under a particular
system. The scenarios should ideally by designed in co-ordination with a
product owner to ensure we are testing cases the business values.

These scenarios and features should express journeys in the language of the end
user of the product and relevant business processes. They should be devoid of
implementation details. For example, a scenario which includes testing that
the user can access a particular page in a web application should not detail
precise steps of bootstraping a user into the system.

#### features/**/steps/*

Step definitions are the glue code which bind the expression of intent of a
step to its actual implementation.

The code defined within each step should be co-ordinating various method calls
between objects under `lib/`, to achieve the expressed intent of the step.

These steps should be described what should be done, on a high-level, while
the code in `lib/` contains all the detail, doing all the heavy lifting.

While steps can be re-used across a single product, duplication is less of a
priority than readibility and expressiveness at this layer.

#### lib/*

Contains modules for various APIs we use to talk across services in the
integration environment and emulate user behaviour. While steps define what
we want to do, the logic in `lib/` details exactly how we do it.

Code under `lib/` ought to be flexible enough to be used between products under
test and should not couple itself with a particular test suite
(under `features/`). This is the one area we *should* be aiming for code
re-use.

#### lib/webdriver

Encapsulates all code required to programmatically drive a web browser through
one or more web applications. Step files should be calling these objects in
order to carry out various actions in the browser.

Pages are defined within these directories and can be identified by the
`_page.py` suffix. The design for these classes is based off the [Page Object Model](https://martinfowler.com/bliki/PageObject.html) defined by Martin Fowler.

Where common sets of elements are shared between pages in the browser, we may
define these under a `components` directory with the intention that they are
composed into the Page Object classes.

Aside from the case above, Page Object classes should primarily define methods
described in terms of interacting or reading from the page. Callers should
then use these methods directly and refrain from accessing any underlying
attributes of the class.

### scripts

Contains the various scripts used to setup and run the tests in this project.

Inspired by [Scripts to Rule Them All](https://github.com/github/scripts-to-rule-them-all).


#### scripts/run-taf --podman

Runs the tests under `features/` inside a container completely in headless mode.

i.e. Web UI Test: `scripts/run-taf features/ui_automationintesting_website --podman`

i.e. API Test: `scripts/run-taf features/api_automationintesting --podman`

#### scripts/helper format

- Runs formatter [autopep8](https://pypi.org/project/autopep8/) over the project 
and performs a best-effort to correct any violations.

#### scripts/helper lint

- Runs linter [flake8](https://pypi.org/project/flake8/) over the project.

#### scripts/helper setup

Performs the initial setup for the project to put it into a clean state,
with all dependencies installed.

#### scripts/run-taf --local

Runs all tests defined in `features/`. Additional arguments and flags can be
fed through to the underlying `behave` command.

i.e. Web UI Tests with chrome: `scripts/run-taf -D browser=chrome features/ui_automationintesting_website --local`

i.e. API Test: `scripts/run-taf features/api_automationintesting --local`

#### scripts/helper audit

Runs a audit over pip dependencies.

#### scripts/helper pip-list-outdated

Runs a check to see if there are any outdated pip dependencies.

#### scripts/helper ci-build-checks  

Builds a docker container to run the following:

- Runs a audit over pip dependencies.
- Runs a check to see if there are any outdated pip dependencies.
- Runs linter [flake8](https://pypi.org/project/flake8/) over the project.

## References

* [Behave](https://behave.readthedocs.io)
* [Selenium Python](https://selenium-python.readthedocs.io)
