# ILCI-NotebookTemplates

## Overview

In this repository we expect to host a collection on Jupyter Notebook templates suitable for data access and analysis of breeding data.

The goal is to use these templates with the BrAPI helper JupyterLab extension, however these templates will be usable as standalone notebooks in `cookie cutter` fashion.

The repository is experimental, expect things to break.


## Templates

Templates are located in the [src/templates/](src/templates/) directory.
For each template write to a text file a brief one liner (just a few words) that describes what the template does, name this file with the following pattern `template_name.info`.
For example `template_rtassel_demo.ipynb` we create `template_rtassel_demo.info` with these contents:
```
Process data from BrAPI sources with rTASSEL
```
The metadata obtained from the info files will be used to generate a template [catalog](src/templates/catalog.json) in `JSON` format very similar to this:
```JSON
{
    "data": [
        {
            "name": "some_template.ipynb",
            "description": "brief description"
        },
        {
            "name": "template_rtassel_demo.ipynb",
            "description": "Process data from BrAPI sources with rTASSEL"
        },
        {
            "name": "sommer_evals.ipynb",
            "description": "mixed model analysis with Sommer"
        }
    ]
}

```

## BrAPI Helper

To intall the **experimental** BrAPI Helper extension open the command line and run:
``` bash
/opt/shared/test_dir/brapi_helper_installer.run
```
This extension is only avaiable for a subset of users for testing.

## Notes

We would also like to look at how templates are used and managed by the [jupytemplate](https://github.com/xtreamsrl/jupytemplate) and the [jupyterlab_templates](https://github.com/finos/jupyterlab_templates) extensions.
