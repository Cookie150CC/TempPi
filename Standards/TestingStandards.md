# Testing Standards

## Unit tests for python
- Pythons native unittest library will be used for testing of individual functions
- Documentation for pythons unittest library can be found [here](https://docs.python.org/3/library/unittest.html)
- To automate test set up the following cron job 0 0 * * * python /home/pi/Source/tests.py >> /home/pi/Source/TempPi/Source/test_logs.txt 2>&1

