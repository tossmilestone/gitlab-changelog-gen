import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitlab_changelog_gen",
    version="0.0.3",
    author="tossmilestone",
    author_email="tossmilestone@gmail.com",
    url="https://github.com/tossmilestone/gitlab-changelog-gen",
    description="A command line utility to generate CHANGELOG.md with Gitlab merge requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="gitlab changelog python",
    entry_points={
        "console_scripts": ["chg-gen=gitlab_changelog_gen.cmd:main"]
    },
    packages=setuptools.find_packages(),
    install_requires=[
        "python-gitlab>=1.10.0",
        "pyyaml>=5.1",
    ],
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)