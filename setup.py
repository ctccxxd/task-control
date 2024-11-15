import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="taskmanager",
    version="0.0.1",
    author="Shane",
    author_email="imu_xxd@vip.qq.com",
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
