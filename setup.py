"""referenced = https://qiita.com/shonansurvivors/items/0fbcbfde129f2d26301c
"""
from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cjeReportingTool',
    packages=['cjeReportingTool'],
    version='2.0.1',
    license='MIT',
    author='kami; Takahito Murakami',
    author_email='takahito@klis.tsukuba.ac.jp',
    url='https://github.com/murataka9/cjeReportingTool',
    description=('This Tool made for CJE(Chishiki Joho Enshu 3) class at Univ. of Tsukuba, KLIS. '
                 'This package converts source code comment to markdown text using split words.'),
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='cjeReportingTool comment converter CJE University of Tsukuba KLIS',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        "console_scripts": [
            "cjerep=cjeReportingTool.main:main",
        ]
    },
)
