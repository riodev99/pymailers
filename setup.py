import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymailers",
    version="2.0.2",  # Update the version number
    author="riodev99",
    description="The classic email sending library for Python was expanded to include more useful features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='jgeniya1994@gmail.com',
    url='https://github.com/riodev99/pymailers', 
    project_urls={
        'Source': 'https://github.com/riodev99/pymailers',  # The "Source" label URL pointing to GitHub repo
    },
    package_dir={"": "pymailers"},
    packages=setuptools.find_packages(where="pymailers"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "jinja2>=2.11.3",
        'pymailers>=1.0.1',
        'pyscraping>=1.0.1',
    ],
)
