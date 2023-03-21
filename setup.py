import os
import pkg_resources
from setuptools import setup, find_packages
setup(
    name="getpic",
    version="1.0.3",
    license="Apache License Version 2.0",
    package_data={
        'conf': ['*.json']
    },
    author="lyq",
    author_email='liuyuqi.gov@msn.cn',
    url="https://github.com/jianboy/getpic",
    description='Crawl image from Google or Baidu search engine',
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__),
                 "requirements.txt"), encoding="utf-8")
        )
    ],
    include_package_data=True,
    extras_require={'dev': ['pytest']},
    classifiers=[
        "License :: OSI Approved :: Apache License Version 2.0",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
