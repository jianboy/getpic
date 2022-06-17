import pkg_resources
import os
from setuptools import setup, find_packages
setup(
    name="getpic",
    version="1.0.2",
    package_data={
        'conf': ['*.json']
    },
    author="lyq",
    author_email='liuyuqi.gov@msn.cn',
    url="https://github.com/jianboy/getpic",
    description='Crawl image from Google or Baidu search engine',
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True,
    extras_require={'dev': ['pytest']},

)
