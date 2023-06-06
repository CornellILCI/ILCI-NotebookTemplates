# ILCI-NotebookTemplates

## Overview

In this repository we expect to host a collection on Jupyter Notebook templates suitable for data access and analysis of breeding data.

The goal is to use these templates with the BrAPI helper JupyterLab extension, however these templates will be usable as standalone notebooks in `cookie cutter` fashion.

The repository is experimental, expect things to break.


## Templates

The templates are located in the `src/templates/` directory.
A catalog with the template and a brief one liner (just a few words) can be added with the `template_name.info`.
For example `template_rtassel_demo.ipynb` we create `template_rtassel_demo.info` with these contents:
```
process data from BrAPI sources with RTassel
```

## BrAPI Helper

To intall the **experimental** BrAPI Helper extension open the command line and run:
``` bash
/opt/shared/test_dir/brapi_helper_installer.run
```
This extension is only avaiable for a subset of users for testing.

## Notes

We would also like to look at how templates are used and managed by the [jupytemplate](https://github.com/xtreamsrl/jupytemplate) and the [jupyterlab_templates](https://github.com/finos/jupyterlab_templates) extensions.
