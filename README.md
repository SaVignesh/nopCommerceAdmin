# Selenium Hybrid Framework

## NOPCOMMERCE

###	Prerequisite

1. Python 3 
1. Selenium: - Selenium libraries 
1. Pytest : - Python Unit Test Framework
1. pytest-html: - Pytest HTML reports
1. pytest-xdist : - Run tests parallel 
1. openpyxl: - Microsoft Excel support

### What framework offers 
* Command line execution (No IDE required)
*	Custom configurations
*	Custom logger
*	Cross browser support
*	Parallel test execution
*	HTML reports 
*	Single test case or group of test cases can be run

### Folder structure
* Package: - Consist Python file
* Folder: - Images, log files, etc.

**Project Name** <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PageObjects (Package) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Base (Package) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;testCases (Package) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br /> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Utilities (Package) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TestData (Folder) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Configurations (Folder) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Logs (Folder) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Screenshots (Folder) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reports (Folder) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run.bat (File) <br />
<br />

### Folder Description 

* PageObjects: - Page object scripts. Script use to perform action on target site<br />

* Base: - Common scripts to perform common actions like Explicit wait (to wait for a blocking element to go invisible) that will be used for all test cases<br />

*	testCases: - Test cases<br />
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;              conftest.py: - fixtures<br />

*	Utilities: - Scripts for utilities like reading configuration file, logger configuration <br />

*	TestData: - Excel files, text files having test data<br />

*	Configurations: - Configuration file<br />
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                   config.ini: - driver locations, log file location etc.<br />

*	Logs: - Log file of run<br />

*	Screenshots: - screenshots (mostly  ’.png’ format) to understand arbitrary failures<br />

*	Reports: - HTML reports of run<br />


### Commands to run

*	Execute run.bat file to execute the test cases. There are pre existing commands within the batch file <br />

*	To Run the single test case <br />
 &nbsp;&nbsp;&nbsp;`pytest -vs test_cases/test_001_login.py`<br />

 *	To Run the group of test cases with marked as 'smoke' test case <br />
 &nbsp;&nbsp;&nbsp;`pytest -vs -m "smoke" test_cases/test_001_login.py`<br />

* To Run on specific browser &nbsp;&nbsp; <br />
&nbsp;&nbsp;&nbsp;`pytest -vs test_cases/test_001_login.py –-browser chrome`  

* For parallel execution  &nbsp;&nbsp **(-n <num> runs the tests by using multiple workers)** <br />
 &nbsp;&nbsp;&nbsp;`pytest -vs -n=3 test_cases/test_001_login.py` 				
 
* To generate HTML report<br />
`pytest -vs --html .//Reports\report.html test_cases/test_001_login.py --browser chrome`

#### You can also directly run the code from Github Folder in Jenkins using the Run.bat file:
![jenkins nopCommerce pass](https://github.com/SaVignesh/nopCommerceAdmin/assets/47379614/83c3a795-ecec-4c18-ba5f-3dbe90b4f170)


