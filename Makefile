########################################################################################################################
# BEWATE OF TABS IN FRONT - PYCHARM CHANGE IT TO FOUR SPACES ###########################################################
# NEED TO REPLACE IT - FOR EXAMPLE NOTEPAD #############################################################################
########################################################################################################################

.PHONY: help messages ahoj mypy lint test venv test t lint_f mypy_f all_f clear_console

# CONSTANTS ------------------------------------------------------------------------------------------------------------

include make_config.mk

# UTILS ----------------------------------------------------------------------------------------------------------------

hello:
	@echo ""
	@echo "###################################################################################"
	@echo "############################### Hail to you, hero!! ###############################"
	@echo "############# Congratulations to you running your first make command! #############"
	@echo "###################################################################################"

.DEFAULT: clear_console
clear_console:
	@echo "";\
	clear;\

# FILE MAKES -----------------------------------------------------------------------------------------------------------

.DEFAULT: mypy_f
mypy_f:
	@echo "# MYPY SOURCE FILE ################################################################################";\
	echo "   - File Name: $(FILE_NAME)";\
	echo "   - File Folder: $(FILE_FOLDER)";\
	echo "###################################################################################################";\
	echo "";\
	echo "";\
	mypy --strict src/$(FILE_FOLDER)/$(FILE_NAME).py --config-file mypy.ini;\
	echo "";\
	echo "";\
	echo "# MYPY TEST FILE ###################################################################################";\
	echo "   - File Name: $(FILE_NAME)";\
	echo "   - File Folder: $(FILE_FOLDER)";\
	echo "###################################################################################################";\
	echo "";\
	echo "";\
	mypy --strict tests/t_$(FILE_FOLDER)/test_$(FILE_NAME).py --config-file mypy.ini;\
	echo "";\
	echo "";\

.DEFAULT: lint_f
lint_f:
	@echo "# LINT SOURCE FILE ################################################################################";\
	echo "   - File Name: $(FILE_NAME)";\
	echo "   - File Folder: $(FILE_FOLDER)";\
	echo "###################################################################################################";\
	echo "";\
	echo "";\
	pylint src/$(FILE_FOLDER)/$(FILE_NAME).py --rcfile .pylintrc;\
	echo "# LINT TEST FILE ###################################################################################";\
		echo "   - File Name: $(FILE_NAME)";\
	echo "   - File Folder: $(FILE_FOLDER)";\
	echo "###################################################################################################";\
	echo "";\
	echo "";\
	pylint tests/t_$(FILE_FOLDER)/test_$(FILE_NAME).py --rcfile .pylintrc;\
	echo "";\
	echo "";\

.DEFAULT: test_f
test_f:
	@echo "# PYTEST AND DOCTEST ##############################################################################";\
	echo "   - File Name: $(FILE_NAME)";\
	echo "   - File Folder: $(FILE_FOLDER)";\
	echo "###################################################################################################";\
	echo "";\
	echo "";\
	python -m pytest tests/t_$(FILE_FOLDER)/test_$(FILE_NAME).py;\
	python -m pytest tests/t_$(FILE_FOLDER)/test_$(FILE_NAME).txt;\

all_f_no_clear_console:  mypy_f lint_f test_f

.DEFAULT: all_f
all_f: clear_console all_f_no_clear_console

# GLOBAL CODE MAKES EXCEPT NOTEBOOKS -----------------------------------------------------------------------------------

mypy_no_clear_console:
	@echo "###################################################################################################";\
	echo "# TYPE CHECKING IN SRC PIPELINE AND TESTS FOLDER ##################################################";\
	echo "###################################################################################################";\
	echo "";\
	echo "Excluded from checking, for more information see documentation *.md file.";\
	echo "    - Untyped decorator makes function 'test_density' untyped : in test_* files.";\
	echo "    - Pytest fixture Class cannot subclass 'BaseTransformator' (has type 'Any') in child classes.";\
	echo "";\
	echo "";\
	mypy --strict src pipelines tests --config-file mypy.ini;\

.DEVAULT: mypy
mypy: clear_console mypy_no_clear_console

lint_no_clear_console:
	@echo "###################################################################################################";\
	echo "# LINTING ALL FILES IN SRC PIPELINE AND TESTS FOLDER ##############################################";\
	echo "###################################################################################################";\
	echo "";\
	echo "Excluded from checking, for more information see documentation *.md file.";\
	echo "    - Module and file names starting with t_, test_, tests name.";\
	echo "    - Duplicate code - for that is the separate make.";\
	echo "    - Parameters differ from overridden methods fit, fit_predict, predict.";\
	echo "      Because of problem in Base classes.";\
	echo "";\
	echo "";\
	pylint src pipelines tests --rcfile .pylintrc;\

.DEFAULT: lint
lint: clear_console lint_no_clear_console

lint_dup_no_clear_console:
	@echo "###################################################################################################";\
	echo "# LINTING ALL FILES IN SRC PIPELINE AND TESTS FOLDER, CHECK DUPLICITIES ###########################";\
	echo "###################################################################################################";\
	echo "";\
	echo "Excluded from checking, for more information see documentation *.md file.";\
	echo "    - Module and file names starting with t_, test_, tests name.";\
	echo "    - Duplicate code - for that is the separate make.";\
	echo "    - Parameters differ from overridden methods fit, fit_predict, predict.";\
	echo "      Because of problem in Base classes.";\
	echo "";\
	echo "";\
	pylint src pipelines tests --rcfile .pylintrc_dup;\

lint_dup: clear_console lint_dup_no_clear_console

test_no_clear_console:
	@echo "###################################################################################################";\
	echo "# PYTEST AND DOCTEST FOR ALL FILES ################################################################";\
	echo "###################################################################################################";\
	echo "";\
	echo "";\
	python -m pytest --ignore=tests/t_Utils/test_Cronus.py;\

.DEFAULT: test
test: clear_console test_no_clear_console

# SAMPLE CODE FOR TEST COVERAGE -----------------------------------------------------------------------------------

cover:
	@echo "##################################################################################################";\
	echo "# PYTEST COVERAGE STATISTICS FOR ALL TEST FILES & REPORT GENERATION IN HTML FORMAT#################";\
	echo "# FIND YOUR REPORT IN HTML FORMAT IN YOUR DIRECTORY INSIDE THE FOLDER coverage#####################";\
	echo "###################################################################################################";\
	echo "";\
	echo "";\
	pytest --cov-report html:coverage --cov-branch --cov=tests

.DEFAULT: coverage
coverage: clear_console cover

log_coverage:
	@echo "###################################################################################################";\
	echo "# TOTAL COVERAGE RATIO WILL BE BACKLOGGED INTO coverage_log.csv FILE###############################";\
	echo "###################################################################################################"
ifdef comment
	@python ./src/Utils/CoverageLogger.py $(comment)
else
	python ./src/Utils/CoverageLogger.py
endif
	@echo "# TOTAL COVERAGE RATIO IS BACKLOGGED INTO coverage_log.csv FILE####################################"

.DEFAULT: log_cov
log_cov: clear_console log_coverage

all: clear_console mypy_no_clear_console lint_no_clear_console test_no_clear_console

# FOR BENCHMARKING -----------------------------------------------------------------------------------------------------

cronus_test:
	@echo "###################################################################################################";\
	echo "# BENCHMARK #######################################################################################";\
	echo "###################################################################################################";\
	echo "";\
	echo "Default benchmarking parameters:";\
	echo "    - Minimum running time per test = 0.000005";\
    echo "    - Maximum running time per test = 1.0";\
    echo "    - Minimum number of rounds per test = 10";\
    echo "    - Warm up run to calibrate the benchmarker = True";\
    echo "    - Number of warm up iterations = 10000";\
	echo "";\
	echo "";\
	python -m pytest tests/t_Utils/test_Cronus.py;\

.DEFAULT: cronus
cronus: clear_console cronus_test

# FOR FIXING -----------------------------------------------------------------------------------------------------------

.DEFAULT: venv
venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d .venv || virtualenv .venv
	. .venv/Scripts/activate; pip install -r requirements.txt
	. .venv/Scripts/activate

.DEFAULT: t
t:
	touch .venv/Scripts/activate
	activate

# TESTS --------------------------------------------------------------------------------------

messages:
	$(info Info message)
	# $(warning Warning message)
	# $(error Error message)
	$(info Info message)

.DEFAULT: help
help:
	$(info ******HELP*******)
	$(info     Please fill in help)
	