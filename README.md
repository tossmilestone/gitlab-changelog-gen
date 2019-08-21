# Gitlab Changelog Generator

A command line utility to generate CHANGELOG.md for a gitlab repository.

The merged merge requests tagged with a milestone will be collected to generate the changelog.

## Install

```bash
# pip install gitlab-changelog-gen
```

## Usage

```shell
# chg-gen init
Gitlab host: https://your-gitlab.com
Gitlab group: your-group
Gitlab project: your-project
Gitlab private token: your-token
# chg-gen output
Changelog is generated to './CHANGELOG.md' success.
```

## Configuration

Before generate the changelog file, you need to run `chg-gen init` to init the config first. The default config file
is `.chg-gen.config` under the working directory.

The config file is `YAML` format, and this is the instructions:
```yaml
// host address of your gitlab
host: https://gitlab.example
// group name of your repo
group: foo
// project name of your repo
project: bar
// private_token to access your gitlab API
private_token: yourtoken
```

## Generation Rules

The generation rules of a changelog consist of:

* Release: A `release` section contains `features` and `bug fixes`. The release name is the title of `milestone`
of the project.
* Features: Composed by the merged `merge requests` labeled with `feature` or `enhancement`.
* Bug Fixes: Composed by the merged `merge requests` labeled with `bug`.
* Change Items: Components of `Features` and `Bug Fixes`. The content is the title of the `merge request` with its
reference and the `author` reference.

An example of [CHANGELOG.md](https://github.com/tossmilestone/gitlab-changelog-gen/blob/master/example/CHANGELOG.md).
