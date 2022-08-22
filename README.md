# Prerequisites
* Unix-like operating system
* Python 3.8+

# Usage
``` shell
cd-data-converter [OPTIONS] INPUTFILE [OUTPUTFILE]
``` 
Try `cd-data-converter --help` for help.


# Run in Docker
To start an interactive session to try out the `cd-data-converter` without installing anything locally, navigate to the repository and run:
```shell
 docker run --rm -it $(docker build -q .)
```
The `cd_catalog.xml` example file is available in the default `/Demo`  directory.

# Local installation
Navigate to the repository and run:
```shell
python3 -m pip install -e .
```


# Running tests
Tests can be run using `tox` or `make test`.


# Reviewing the code
For reviewing the code, the Makefile offers the ability to quickly configure a virtual environment with all dependencies:

* `make setup`: Create a virtual environment and install dependencies
* `make test`: Run tests in the same virtual environment
* `make clean`: Remove venv, build and tempfiles

The application will also be installed in the virtual environment as `cd-data-converter`.


# Notes and tradeoffs
- Style is black + flake8 with 100 character line length limit
- Not much in terms of tests, they are mostly serving as placeholders to have something to run through tox/pytest
- I made the assumption that all incoming items should contain the complete data as indicated by the provided example, any items containing malformed or null values will be discarded with a note to the logs
- I deprioritized logging and designing "non tech" friendly log messages
- I grabbed an off-the-shelf bloom filter to save time, it has poor performance due to using cryptographic hashes
- The spec indicates that the JSON export should contain currency values represented as floats. In the processing, all currency operations are done using Decimal and the converted to floats to fit the spec before export. I would not export currency as floats in a business setting.
- There is also no particular handling of float precision in any currency data
