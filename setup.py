import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="task-dag-control",
    version="0.0.3",
    author="Shane",
    author_email="imu_xxd@163.com",
    description="framework for flow-control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ctccxxd/task-control",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
