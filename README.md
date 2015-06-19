# README #

A very simple naive Bayes classifier.

### How to test and run ###

Run 
```
#!bash

python nbtest.py
```
to run the unit tests.

To run the classifier:

```
#!bash

python nb.py input.yml
```
where input.yml is a YAML-format input file. The format of this is:

```
#!yaml
categorisemodule: "/path/to/categorise.py" # Function to categorise training data
categories: ["list", "of", "pre-defined", "categories"]
trainingdata: "/path/to/folder/containing/training/data"
testfile: ["/list/of", "/paths/to/files", "/to/categorise"]
```

### Dependencies ###

* PyYAML (http://pyyaml.org/)