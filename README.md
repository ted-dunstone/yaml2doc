# yaml2doc (YAML to document)

## Introduction

Convert YAML to documentation. 

Particularly useful for documenting specifications or examples.

## Requirements

Relies on the amazing [pandoc](pandoc.org) for the document conversion. It will however run as a pure python yaml to markdown converter without pandoc (as it converts to md and then to pandoc)

## How to use

This script takes all lines beginning with # as text-lines. All other lines are treated as “yaml”. 

For each text the # is removed and the “code” will get spaces prepended.

## Setup

pip3 install .

# Usage

Once installed the package can be used from the commandline

```
usage: yamltodoc <infile.yaml> <outfile.[md|pdf|docx|pptx]>

```

The following will build an example report with the files in the "test" directory and the title as "a major report"

eg:
```sh
yamltodoc test/blueprint.yaml blueprint.pdf 
```

# Acknowledgement

Derived from [yaml2rst 0.3](https://pypi.org/project/yaml2rst/) which was a yaml to RST converter
