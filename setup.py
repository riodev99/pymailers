from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

des = 'An email sending library for Python with'
dess = 'support for HTML content and attachments'

setup(
    name='pymailers',
    version='1.5.1',
    description=des + ' ' + dess,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='riodev99',
    author_email='jgeniya1994@gmail.com',
    url='https://github.com/riodev99/pymailersexpanded', 
    project_urls={
        'Source': 'https://github.com/riodev99/pymailersexpanded',  # The "Source" label URL pointing to GitHub repo
    },
    packages=['pymailers'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',
    install_requires=[
      "requests",
      "bs4"
    ],
)
