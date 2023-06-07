# ILCI-NotebookTemplates

## Overview

In this repository we expect to host a collection on Jupyter Notebook templates suitable for data access and analysis of breeding data.

The goal is to use these templates with the BrAPI helper JupyterLab extension, however these templates will be usable as standalone notebooks in `cookie cutter` fashion.

The repository is experimental, expect things to break.


## Templates

Templates are located in the [src/templates/](src/templates/) directory.
For each template write to a text file a brief one liner (just a few words) that describes what the template does, name this file with the following pattern `template_name.info`.
For example, to describe what `template_rtassel_demo.ipynb` does  we would create `template_rtassel_demo.info` with these contents in a single line:
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

### Using templates (not imeplemented yet!!)

The BrAPI extension reads templates from the `$HOME/templates` directory (not implemented yet).
If you wish to use the templates from this repo with the extension directly you could create a symlink to the this repo's contents. For instance lets assume you clone this repo from your `$HOME` directory, this will create `$HOME/ILCI-NotebookTemplates`
``` bash
ln -s $HOME/ILCI-NotebookTemplates/src/templates $HOME
```


## Notes

We would also like to look at how templates are used and managed by the [jupytemplate](https://github.com/xtreamsrl/jupytemplate) and the [jupyterlab_templates](https://github.com/finos/jupyterlab_templates) extensions.
