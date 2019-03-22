# TempPi
- A server room temperature sensor system.
- This program was create for a Raspberry Pi model 3 b+

## WorkFlow
1. When adding a feature Create a new branch for your feature using "git checkout -b <name of your new branch>"
2. When done use push up your branch using "git add <name(s) of added files>" "git commit -m 'MSG'" "git push"
3. Then create a pull request to merge your changes with the master branch. [click here](https://github.com/Cookie150CC/TempPi/pulls) 
  
## Python Programming Standards
- Please read the PEP 8 programming standard before submitting any python code to the repository.
- [PEP-8 programming standard](https://www.python.org/dev/peps/pep-0008/#maximum-line-length)
- Pyhton 3 will be used exclusively

## Install
- To ensure proper functionality please clone this directory into ~/Source on the Raspberry Pi file system.
- To use the Adafruit_Python_DHT sensor library. The directory can be found [here](https://github.com/adafruit/Adafruit_Python_DHT). Then run the setup.py script to install on the Raspberry Pi
- For used wiring please reference [here](https://github.com/Cookie150CC/TempPi/blob/master/Spikes/RaspberryPi_v01_WiringSchematic.pdf) in the Spikes directory
- For real time clock integration please reference [here](https://github.com/Cookie150CC/TempPi/blob/master/Spikes/Spike%20on%20RTC%20integration.md)
