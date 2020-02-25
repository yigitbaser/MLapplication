# MLTemplate
Template for ML repository

# CHECKLIST
- Update a code
- Update a documentation in TEMPLATE_DESCRIPTION.md if needed.
- Update a documentation in README.md if needed.
- **Run tests, mypy, pylint.**

# Personalization

When developing you will need to use files or modules that are specific to your working environment
and thus this section describes the different personal files.

All files in this section are excluded from the repository by .gitignore.

## Config File for the Repository

Upon the location at which you have cloned the repository, each member of the team may have it in 
different folders and thus it is important that each one of us has our own configuration file.

This personal configuration file is named *config.ini and it is not synced with the
depository. In the configuration file section (below) you can find more information regarding this
important file.

## Config File for Make command

# Technologies

- [Sphingx for documentation](www.sphinx-doc.org)
- [jupytext](https://github.com/mwouts/jupytext/)
- Virtualenv (my notes)

# Folder and File Structure

## Folders

- *data*
    - *external*
        - Data from external sources. Dictionaries, synonyms, ...
    - *interim* 
        - Intermediate format between raw and processed. Not raw and also not ready yet.
    - *processed* 
        - Final data after whole preprocessing, merging, cleaning, transformation, enrichment, feature engineering etc.  
    - *raw* 
        - For raw data storage. This directory should be read only. 
    - *Note*: **This one should not be merged.**
    - *Note*: In pycharm mark it as a excluded folder.
- *docs*
    - For a documentation. Please use [Sphingx](www.sphinx-doc.org) for this.
    - *Note*: In pycharm mark it as a excluded folder.
- *models*
    - Storage for created models in binaries, pickles, ...
    - Intermediate results.
    - From long term perspective should be stored somewhere else.
    - Model names/folder should contain some metadata information - date of execution, data, size, ... see reporting.
- *notebooks*
    - *raw* - Just a playground.
    - *final* - For final notebooks.
    - Please use naming convention with NN-NNNameOfTheNotebook. First number with respect to project phase, second order.
    - Commit only *.py files from [jupytext](https://github.com/mwouts/jupytext/) package.
    - Please see section *Notebooks*
- *pipelines*
    - Code for creating the whole pipelines.
- *references*
    - Manuals, explanatory materials.
- *reports*
    - Generated analysis (html, pdf, LaTex, docx, ...)
    - *figures*
        - Figures for reporting.
- *src*
    - For storing source code with folders for respective tasks.
    - *Check*
        - *\_\_init__.py*
        - Code for data checkers.
    - *Data*
        - *\_\_init__.py*
        - Code for reading and writing data.
    - *Exception*
        - *\_\_init__.py*
        - Code for custom exceptions.
    - *Modelling*
        - *\_\_init__.py*
        - Code for models.
    - *Reporting*
        - *\_\_init__.py*
        - Code used for reports creation.
        - *Note*: Date and time, size, data, ...
    - *Transformation*
        - *\_\_init__.py*
        - Code for data transformations.
    - *Utils*
        - *\_\_init__.py*
        - Code used across the whole project.
    - *Visualization*
        - *\_\_init__.py*
        - Code for plots creation.
    - *\_\_init__.py*
    - *GlobalConstanst.py*
        - File for storing global constants like attributes names. Please use capitals for these (eg. ATR_DATE).        
    - *Note*: In pycharm mark it as a source folder.
 - *tests*
    - For storing tests to file. The structure of this repository is similar to src, but the folders start with *t_**. 
    Please store respective files 
      in respective folders.
      
## Files

- *.gitignore*
    - Excludes some files and folder. The base is standard git-based file with some additional feature. 
    For more information see the file. 
- *config.ini*
    - Personal configuration file for python config parser. **This one should not be merged.**
- *config_template.ini*
    - General configuration file for python config parser.
- *Makefile*
    - For _make_ orders.
- *pytest.ini*
    - For usage with pytest.
- *README.md*
    - The overview..
- *requirements.txt*
    - Requirements for libraries for environment. Generated with `pip freeze > requirements.txt`
- *setup.py*
    - For pip installability via `pip install -e`
    
# Configuration Files

There are supposed to be two configuration files in the repository there. The one synced with the 
depository - *config_template.ini* and personal *config.ini, which is not synced with the
depositry. 

The *config.ini* is excluded in .gitignore.

Please when you download the repo, make your own copy of *config_template.ini* and name it *config.ini*

If you do updates of structure in the local *config.ini* file, please update the *config_template.ini*
as well.

**Don't upload your local settings to config_template.ini!**
    
# Notebooks

Jupytext saves Jupyter Notebooks as:
- Markdown and R Markdown documents.
- Scripts in many languages.

The main advantages are:
- Can be added to a repository.
- Changes to the notebook can be done in an IDE.

How to use Jupytext:
- Add entry to the notebook metadata (see below).
- Open the Python script and modify the code in PyCharm.
- Refresh Jupyter Notebook in the browser.

See the [user guide](https://jupytext.readthedocs.io/en/latest/introduction.html#) for more information.

Notebook settings for Jupytext handling - Edit/Edit Notebook Metadata/

{   
    **"jupytext": {"formats": "ipynb,py:light"},**  
    "kernelspec": {   
        "name": "python3",   
        "display_name": "Python 3",   
        "language": "python"   
  },  
  ...
  
# Notebooks Template

- *TemplateParameterizedNotebook*
    - Template for running parameterized notebooks.
  
# Virtualenv

**TODO** - creat a make 

Anaconda prompt - to project folder
- Create `virtualenv .venv`
- Activate `.venv\Scripts\activate` 
    - or
    - `cd .venv`
    - `cd Scripts`
    - `activate`
- Deactivate `deactivate`

Project folder with virtual environment activated.
- `pip install -r requirements.txt`
- `pip list`

Collecting requirements
- `pip freeze > requirements.txt`

Other commands
- `which python`

# Devops

## Mypy

*TODO* - adjust for new make commands.

Is a static type checker for Python. Execution time is reduced because types are checked before running.

To run mypy:
- `mypy --strict your_code.py --config-file mypy.ini`
- See makefile for commands

**We decided to exlude following situations. For more information see the description bellow.**
- Pytest fixtures *Untyped decorator makes function "test_density" untyped :* in files *test_**. 
Exclude in following style:
    - `@pytest.mark.parametrize("df, type_of_normalisation", # type:ignore`
- Pytest fixture *Class cannot subclass 'BaseTransformator' (has type 'Any')*. 
Exclude in following style in the child class:
    - `class DWMYDFTransformator(BaseTransformator): # type:ignore`
    
A [mypy configuration file](https://mypy.readthedocs.io/en/latest/config_file.html) allows you to modify the setting for
 mypy.

Examples of static typing:
- Variable 
    - `x: str = "test"`
- Function
    - `def stringify(num: int) -> str:`
    - `return str(num)`

See the [cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html#variables) for more annotation examples
 and options.
 
 *Tip: If you don't know which type should a callable be, write reveal_type(callable) in the code 
 and run mypy. The PS prompt will specify the type that you should use.*
 
 It is possible to ignore errors in 3 different ways:
 * On a line of code: By adding `# type:ignore` on that line
 * On a .py file: By adding `# type:ignore` to the beginning of file
 * On config file: By disabling the regarding setting of mypy such as `ignore_missing_imports=False`. However,
 this is not encouraged because it can suppress all the errors that can be helpful when debugging and also 
 they could be caused by another reason than you want to ignore but gives the same error.
 
 Two types of error are ignored by adding `# type:ignore` to the regarding line of code
 * Untyped decorator makes function "test_density" untyped : This is caused by the missing annotation 
  while using pytest fixtures or parametrization. It is not possible to use static typing for these therefore,
  they cause a missing annotation when mypy is used. For example:
  `@pytest.mark.parametrize("transformation_type", [FP, P])  # type:ignore`
  * Class cannot subclass 'BaseTransformator' (has type 'Any') : This is possibly caused because of inheritance. 
  of a different class in a different directory. Additional information is gathered by using `disallow_any_unimported = true`
   which gives "Base type BaseTransformator becomes "Any" due to an unfollowed import". Refer 
   [follow imports by mypy](https://mypy.readthedocs.io/en/latest/running_mypy.html#follow-imports). 
   However, real reason is not found. Several possible solutions that didn't solve the issue applied which 
  are as follows:
    - Replace usage of Any with other built-in types
    - Moving the inherited class into the same file
    - Changing parameters from Any to other known ones
    - Changing the number of parameters in the abstract file compatible with the overwritten file 
    - Disabling some of the error checking using config file such as `follow_imports=False`, 
    `follow_imports_for_stubs=False,True`, `disallow_untyped_defs=True,False` 
    - Disabling all the inheritances in both existing file and inherited files
    - Related material can be found in following links: [1](https://github.com/python/typeshed/issues/1544), 
    [2](https://github.com/python/typeshed/pull/1492), [3](https://github.com/python/typeshed/issues/1446), 
    [4](https://github.com/python/mypy/issues/4180), 
    [5](https://stackoverflow.com/questions/49888155/class-cannot-subclass-qobject-has-type-any-using-mypy)
    
    This issue is solved by adding `# type:ignore` to corresponding lines of code. For example:
    `class DWMYDFTransformator(BaseTransformator): # type:ignore`
    
     
        
       

## Pylint

**We decided to exlude following situations. For more information see the description bellow.**
- Invalid-name - is handleded by regular expression, please see .pylintrc.
- Duplicate code. There are separate makes for that. Excluded from the main one.
- Parameters differ from overridden methods fit, fit_predict, predict. Because of problem in Base classes.  
`   # pylint: disable=arguments-differ`  
`    def fit(...`  
`    ...`  
`    def fit_predict(...`  
`    ...`  
`    def predict(...`  
`    ...`  
`    return ...`  
`   # pylint: enable=arguments-differ`

    

*TODO* - put simple one file commands here for mypy and pylint.
*TODO* - adjust for new make commands.

Is a static code analysis tool that:
- looks for programming errors
- helps enforcing a coding standard
- sniffs for code smells 
- offers simple refactoring suggestions

To run Pylint:
- `pylint your_code.py --rcfile .pylintrc`

It can also be executed within Python: 
- `import pylint.lint`
- `pylint_opts = ['--version'] # --rcfile for using the configuration file, see user guide. `
- `pylint.lint.Run(pylint_opts)`

It has the option to do parallel execution in order to speed up the execution of Pylint.

See the [user guide](http://pylint.pycqa.org/en/latest/user_guide/run.html) for more information. 

*Tip: To disable a warning for one single line (or block) you can type in the line or at the 
indentation level (e.g. a method or class) that you wish to disable the following 
comment: # pylint: disable=Warning-name-or-code.*

*Tip: When a warning is disabled by using `#pylint: disable=Warning-name-or-code.`, that particular type of checking
becomes disabled for the rest of the code starting from that line. Therefore, it is recommended to enable the same warning
after it is used for a specific part of code. This is explained in more detail in the following examples.*

### Exception Excluded

Overview
- invalid-name: In order to prevent invalid naming for file naming `# pylint: disable=invalid-name` 
`# pylint: enable=invalid-name` are added in the beginning of the file consecutively. This prevents pylint
to give an error because of file name but pylint still checks the rest of the file if it is 
added in the beginning of the file as above.
- too-many-arguments: If number of arguments are bigger than 5, then pylint gives an error. These type of
error is suppressed by `#pylint: disable=too-many-arguments` because sometimes it is necessary to use more 
than 5 arguments and it is a design choice.
-too-few-public-methods: If number of functions in a class is less than 2, then pylint gives an error.
This error is suppressed by using `#pylint: disable=too-few-public-methods` because it is a design choice.
- arguments-differ: Some abstract function's parameters are overridden in other classes while overriding 
the functions. When the number of parameters differ from inherited function, then pylint gives 
arguments-differ error. No solution was found for such an error, therefore errors are suppressed by
`# pylint: disable=arguments-differ` and enabled checking after function by `# pylint: enable=arguments-differ`.

**Note:** Lets use _...disable..._ at the beginning and _...enable..._ and the end. Both with minimal possible scope.

*IMPORTANT NOTE: duplicate-code: Pylint gives error for duplicate code. However, these code
can be written on purpose that way and they are sometimes design choice. Therefore, these errors can be
suppressed. However, disabling the duplicate-code error is not possible locally for pylint. 
Refer [here](https://github.com/PyCQA/pylint/issues/214) for the issue. This is solved by disabling 
duplicate-code error globally. It is needed to be careful for next time usages.*

## Pytest

*TODO* - adjust for new make commands.

It is framework that makes building simple and scalable tests easy.

To execute Pytest there are three ways:
- (PS) For all test files located in .\tests: 
    - `make pystest`
- (PS) For a specific test file:
    - `python -q pytest .\path\test_*.py`
- (PyCharm) Through Python Integrated Tools (PIT):
    - Go to File -> Settings -> Tools -> PIT and change default tester to pytest.
    - Select the configuration pytest and run. 
    
    
Lets use an existing example for showing how Pytest works. We have two files:
- .\sr\delete\leap_year.py -> function that 
determines if the input is a leap year or not.
- .\tests\test_leap_year.py -> functions that assert if the 
input is a leap year or not.

We then execute pytest (in the PS for example) and our output is:

`platform win32 -- Python 3.7.4, pytest-5.3.1, py-1.8.0, pluggy-0.13.1`<br/>
`rootdir: C:\MLTemplate, inifile: pytest.ini`<br/>
`collected 4 items`<br/>

`tests\test_leap_year.py ....`&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                              &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                              `[100%]`<br/>

`========================== 4 passed in 0.03s ==========================`

In this case, all four tests were passed.

###Pytest-cov
There are two possible easy to use coverage modules which are pytest-cov and coverage. There are 
 also some other tools to calculate similar metrics even with deeper analysis. For example,
 [sealights](https://www.sealights.io/agile-testing/test-metrics/python-code-coverage/) is a tool that 
 gives deeper analysis including MC/DC ([info](https://en.wikipedia.org/wiki/Modified_condition/decision_coverage)) 
 coverage. All calculated coverages in this project uses branch coverage which checks every line and
 all possibilities of conditional statements if they were tested.
 
 Pytest-cov is chosen for calculating test coverage because it already uses coverage module and 
 it can additionally calculate branch coverage.
 
 In order to calculate total test coverage or test coverages of different files, following 
 command from makefile is used on command line: 
 - `make coverage`: It runs pytest-cov with branch coverage option enable. It saves the files
  into folder coverage. If folder already exists then it is overwritten by module.
 - `make log_cov`: It first runs the coverage command to calculate all the coverage ratios. Then,
 it saves the total coverage ratio into file "Coverage_Log.csv" which is in Reports. This command
 can be used with an optional comment as follows:
  `make log_cov comment=MyCommentForLogging` then MyCommentForLogging will be added to the csv file's
  regarding comment column. If it is not passed as a parameter through command line then comment 
  section will be empty.    

## Benchmarking (a.k.a. Cronus)

We have different methods to benchmark modules, functions or code snippets:

- Snippet: Use either Timerer.py or the 3rd party module Timeit for calculating the running time.
- Functions (or Methods within a class): Two ways were found, only one was developed:
    - Decorator: The idea is to import a module with a benchmarking function (decorator) and target
    the desired method. Due to the time consuming task of adapting the decorator to include 
    arguments for the targeted function (see 
    [this thread](https://stackoverflow.com/questions/5929107/decorators-with-parameters) for 
    more information), this benchmarker has been discarded. See Appendix A for the decorator code.
    - Cronus: This method uses Pytest's plugin named benchmark 
    ([link](https://pypi.org/project/pytest-benchmark/)) to run a complete time analysis of 
    the target function (which takes into consideration warm ups, number of iterations, etc). To 
    run the benchmarks please modify test_Cronus (in t_Utils) as described in the file.
    The main advantages of this method are:
        - Adapted to the make file as make cronus. It is excluded from other make pytest runs. 
        - It can accept parametrized tests and provides individual results.
        - Possibility to change the default settings of the benchmark and its output. See the 
        [documentation](https://pytest-benchmark.readthedocs.io/en/stable/usage.html#commandline-options)
         for more information. (Possible to compare the tests one by one, it is also possible to
         plot a histogram for each test)
- Modules: The module ModuleBenchmarker.py (in Appendix B of this document) benchmarks the whole 
calculation time of one single module (file). To use it, import it into the module to be
tested, e.g.: `from src.Utils import ModuleBenchmarker`. When you will execute the target module, 
the running time will be printed at the end of the console. When tested it only worked with those 
files containing a loop process. Further research is needed to implement it to all files. In the 
meantime, use the Timerer.py module in the Utils folder.
         


 

# Makefile

## Installation for Windows

To make it work install cygwin based on this 
[description](https://www.howtogeek.com/howto/41382/how-to-use-linux-commands-in-windows-with-cygwin/).
- **Please include binutils and make because of venv during the installation process.**
- Cygwin terminal starts in C:\Cygwin\home\<user>.
- Move to C:\ use `cd /cygdrive/c `
- But it works in anaconda after this process.
- Try to run `make hello`

## How to Run Makes

To run command:
- In anaconda in the project repository folder run `make <command_name>` (example: `make hello`)
- To suppress errors and warning - for example for all_f run `make -i all_f`

## Updating Makes

**BEWATE OF TABS IN FRONT - PYCHARM CHANGE IT TO FOUR SPACES**  
**HAVE TO BE A TAB BEFORE, OTHERWISE AN ERROR**

## APPENDIX A. BENCHMARK DECORATOR

    """
    Benchmarker
    """
    
    import time
    
    # To run the decorator make sure that the function you want to benchmark has already predetermined
    # arguments since the decorator cannot take arguments (technically possible, but time consuming to
    # develop). To use it, import the function timedecorator into the module where the function that
    # you want to test is, and call it as a decorator on that function.
    # More information: https://stackoverflow.com/questions/5929107/decorators-with-parameters
    
    def timedecorator(func):
        """
        A timer decorator
        """
    
        def function_timer(*args, **kwargs):
            """
            A nested function for timing other functions
            """
            start = time.time()
            value = func(*args, **kwargs)
            end = time.time()
            runtime = end - start
            msg = "The runtime for {func} took {time} seconds to complete"
            print(msg.format(func=func.__name__, time=runtime))
            return value
    
        return function_timer
        
## APPENDIX B. MODULE BENCHMARKER
    """
    Benchmarker
    
    # To use this benchmark module, you only need to import it to the module that you wish to
    # benchmark. More information can be found in the comment of Nicojo:
    # https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution/
    # 12344609#12344609
    """
    
    import atexit
    from datetime import timedelta
    from time import strftime, localtime, process_time
    from typing import Optional, Union
    
    
    def seconds_to_str(elapsed: Optional[float] = None) -> str:
        """
        Transforms seconds to strings for the elapsed time input. If not, it gives back the local time.
        :param elapsed: Float or None. Time elapsed.
        :return: strftime or string. If elapsed is none, it will provide a strftime. If a float is
        giving for elapsed, it will return a string of the timedelta of that elapsed amount.
        """
        if elapsed is None:
            return strftime("%Y-%m-%d %H:%M:%S", localtime())
    
        return str(timedelta(seconds=elapsed))
    
    
    def start_log_benchmark(string: str, elapsed: Optional[Union[float, str]] = None) -> None:
        """
        To create a print out of the elapsed time.
        :param string: String. Text to print out with the elapsed time.
        :param elapsed: Float or None. Time elapsed.
        """
        line = "=" * 40
        print(line)
        print(seconds_to_str(), '-', string)
        if elapsed:
            print("Elapsed time:", elapsed)
        print(line)
        print()
    
    
    def end_log_benchmark() -> None:
        """
        To stop the running time count.
        """
        end = process_time()
        elapsed = end - START
        start_log_benchmark("End Program", seconds_to_str(elapsed))
    
    
    START = process_time()
    atexit.register(end_log_benchmark)
    start_log_benchmark("Start Program")