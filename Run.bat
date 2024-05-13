pytest -vs -m "sanity or regression" --html=.//Reports/report.html  test_cases/ --browser chrome 
REM pytest -vs -n=3 -m "sanity or regression" --html=.//Reports/report.html  test_cases/ --browser chrome 
REM pytest -vs -m "sanity" --html=.//Reports/report.html test_cases/ --browser chrome 
REM pytest -vs -m "regression" --html=.//Reports/report.html test_cases/ --browser chrome 
REM pytest -vs -m "smoke" --html=.//Reports/report.html test_cases/ --browser chrome 

REM pytest -vs -m "smoke or sanity" --html=.//Reports/report.html  test_cases/ --browser firefox 
REM pytest -vs -m "sanity" --html=.//Reports/report.html test_cases/ --browser firefox 
REM pytest -vs -m "regression" --html=.//Reports/report.html test_cases/ --browser firefox 
REM pytest -vs -m "smoke" --html=.//Reports/report.html test_cases/ --browser firefox 

REM pytest -vs -m "smoke or sanity" --html=.//Reports/report.html  test_cases/ --browser edge 
REM pytest -vs -m "sanity" --html=.//Reports/report.html test_cases/ --browser edge 
REM pytest -vs -m "regression" --html=.//Reports/report.html test_cases/ --browser edge 
REM pytest -vs -m "smoke" --html=.//Reports/report.html test_cases/ --browser edge 