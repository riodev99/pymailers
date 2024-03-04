from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pymailers',
    version='1.2.4',
    description='An email sending library for Python with support for HTML content and attachments.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='riodev99',
    author_email='jgeniya1994@gmail.com',
    url='https://github.com/riodev99/pymailersexpanded',
    project_urls={
        'Source': 'https://github.com/riodev99/pymailersexpanded',  # The "Source" label URL pointing to GitHub repo
    },
    packages=['pymailers'],
    install_requires=[
        'jinja2>=2.11.3',  # Specify the minimum version of jinja2 required
    ],
    python_requires='>=3.6',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='email smtp attachments html mail jinja2',
)
