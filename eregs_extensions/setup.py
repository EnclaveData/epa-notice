from setuptools import setup, find_packages

ns = "eregs_ns.parser"  # The namespace for regulations-parser extensions.
fs = "epa_regparser"  # The directory name for the package.
entry_points = {
    "%s.term_definitions" % ns: [
        "epa_terms = %s.term_defs:term_defs" % fs
    ]
}

setup(
    name=fs,
    version="1.0.0",
    packages=find_packages(),
    classifiers=[
        'License :: Public Domain',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication'
    ],
    entry_points=entry_points
)
