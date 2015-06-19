# README #

A very simple naive Bayes classifier based on http://blog.yhathq.com/posts/naive-bayes-in-python.html.

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