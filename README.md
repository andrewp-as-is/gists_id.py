<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/gists_id.svg?maxAge=3600)](https://pypi.org/project/gists_id/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/gists_id.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/gists_id.py/actions)

### Installation
```bash
$ [sudo] pip install gists_id
```

#### Config
```bash
$ export GITHUB_TOKEN="<GITHUB_TOKEN>"
```

#### Examples
```bash
$ python -m gists_id
```

delete orphaned gists

```bash
$ pip install gist-delete gist-id
$ python -m gists_id | grep -v "$(find ~/git/gists -maxdepth 1 -exec gist-id {} \; 2> /dev/null)" | xargs gist-delete;:
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>