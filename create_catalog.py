import json
import glob
import os

# This script creates a catalog of Jupyter notebooks and their descriptions, 
# which are stored in .info files. The catalog is then written to a JSON file.

TEMPLATE_DIR = 'src/templates'
INDENT = 2
out_file = 'catalog.json'

catalog = {'data':[]}
print(f"Reading {TEMPLATE_DIR=}")
info_files = glob.glob(os.path.join(TEMPLATE_DIR, "*.info"))
print(f"The following files were found: {info_files} ")

print("Reading data...")
for info_file in glob.glob(os.path.join(TEMPLATE_DIR, "*.info")):
    # Get the common name of the .info and .ipynb files
    common_name, ext = os.path.splitext(info_file)
    nb_path = common_name + ".ipynb"
    nb_file = os.path.basename(nb_path)
    description = open(info_file).read().rstrip()
    catalog['data'].append({'name':nb_file, 'description':description})


print(f"Catalog created.\n======== Catalog contents: ==========\n {json.dumps(catalog, indent=INDENT)}\n========        END       ==========\n")

print(f"Saving to: {out_file}")
# Write the catalog to a JSON file
out_fp = open(out_file, "w")
json.dump(catalog, out_fp, indent=INDENT)
