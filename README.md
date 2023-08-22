# Quantitative Ultrasound Tool

## Overview

This program supports spectral tissue characterization analysis on 2D radiofrequency (RF) and in-phase and quadrature phase (IQ) data.

Additionally, it supports 2D and 3D contrast-enhanced ultrasound (CEUS) analysis for bolus injections. The 2D software uses motion correction software developed by [Thodsawit Tiyarattanachai MD, PhD](https://pubmed.ncbi.nlm.nih.gov/35970658/). Currently, the 3D software does not have motion correction software, but enables users to manually edit their time intensity curve (TIC) as shown in the tutorial below.

## Requirements

* [Docker](docker.com/products/docker-desktop/) (only required for Philips RF parser)
* Any version of [Python3.9](https://www.python.org/downloads/)

## Building

### Mac/Linux

```shell
git clone https://github.com/davidspector67/QusTools.git
cd QusTools
python3.9 -m pip install virtualenv
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd Parsers
gcc -c -Wall -Wpedantic philips_rf_parser.c
gcc -o philips_rf_parser philips_rf_parser.o
cd ..
```

### Windows

```shell
git clone https://github.com/davidspector67/QusTools.git
cd QusTools
python3.9 -m pip install virtualenv
python3.9 -m venv venv
call \venv\scripts\activate.bat
pip install -r requirements.txt
deactivate
```

From here, compile Parsers\philips_rf_parser.c into Parsers\philips_rf_parser executable using Windows C compiler of choice.

## Running

### Mac/Linux

```shell
source venv/bin/activate
python main.py
deactivate
```

### Windows

```shell
call venv\scripts\activate.bat
python main.py
deactivate
```
