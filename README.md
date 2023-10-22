# !!! Remove this section !!!
1. Create empty Git repository with your preferred name: example `django-my-new-pkg-name`
2. Checkout local copy of this new **empty** repository
3. Copy all the contents of this repository inside the **new cloned empty repository**
4. Delete the directory **src\django_pkg.egg-info**
5. Rename the directory inside **src** from `PACKAGE_NAME` to `my_new_pkg_src_location`
6. Massive **replace** with match case the string `PACKAGE_NAME` with your src location `my_new_pkg_src_location`
7. Massive **replace** the string `django-pkg` with your new package's name `django-my-new-pkg-name`
8. **Edit** the `setup.cfg` file for the needed  app's `description` attribute
9. **Edit** the `tests/settings.py` file for the needed configuration to test your app
10. **Rename and edit** the `tests/test_fake.py` file for the needed application's tests
11. Copy or create all source's files of the app inside the **src/my_new_pkg_src_location**
12. Install python's requirements `pip install -r requirements/dev.in`
13. Install python's requirements `pip install -r requirements/requirements.in`
14. Execute `black -t py39 .` to do the first lint analysis 
15. Install python's package `pip install .` to test the package's local version
16. Execute `python runtests.py` and validate all tests are passed (if any error is present, the automatic workflow on tag will fail)
17. Edit the file `README.md` removing these notes and change needed information
18. Edit docs ...
19. Install python requirements `pip install -r requirements/docs.in`
20. Add files as first commit `git add .github requirements/*`
21. Commit local files just added `git commit -m "Initial commit"`
22. Push to remote `git push` git the current repository's local initial's commit 
23. Inside Git repository's settings, section *General*, **enable** the `Allow auto-merge` and `Automatically delete head branches`
24. Inside Git repository's settings, section *Access*, **add access** to be able to execute workflows (as team member's or bot-user collaborator)
25. Inside Git repository's workflows, manually execute the first run of **Upgrade dependencies** workflow and wait the **Success** finish
26. Inside Git repository's workflows, wait the **Pull request** CI workflow's complete and its status is **Merged** 
27. Pull from remote `git pull` inside local git repository the workflow's generated requirements
28. Double-check the file `README.md` is as expect: without step-by-step templates and changed with needed app's info
29. Execute `pre-commit run --all-file` to do the pre-commit analysis 
30. Add all others local files as first commit `git add .`
31. Execute `bump-my-verion` to upgrade the initial 0.0.0 version
32. Execute `python setup.py sdist bdist_wheel` to build the project
33. Execute `twine upload dist/*` to upload the built files with `__token__` account's credential
34. Inside PyPi repository, section *Account Settings -> API tokens*, **generate** new API key with the only scope of project
35. Inside Git repository's settings, section *Security*, **add security repository secret** named `PYPI_API_TOKEN` to be able to upload packages inside PyPi's repository
36. Push to remote `git push --tags` git the current repository's local commits and tags


# django-static-base [![PyPi license](https://img.shields.io/pypi/l/django-static-base.svg)](https://pypi.python.org/pypi/django-static-base)

[![PyPi status](https://img.shields.io/pypi/status/django-static-base.svg)](https://pypi.python.org/pypi/django-static-base)
[![PyPi version](https://img.shields.io/pypi/v/django-static-base.svg)](https://pypi.python.org/pypi/django-static-base)
[![PyPi python version](https://img.shields.io/pypi/pyversions/django-static-base.svg)](https://pypi.python.org/pypi/django-static-base)
[![PyPi downloads](https://img.shields.io/pypi/dm/django-static-base.svg)](https://pypi.python.org/pypi/django-static-base)
[![PyPi downloads](https://img.shields.io/pypi/dw/django-static-base.svg)](https://pypi.python.org/pypi/django-static-base)
[![PyPi downloads](https://img.shields.io/pypi/dd/django-static-base.svg)](https://pypi.python.org/pypi/django-static-base)

## GitHub ![GitHub release](https://img.shields.io/github/tag/DLRSP/django-static-base.svg) ![GitHub release](https://img.shields.io/github/release/DLRSP/django-static-base.svg)

## Test [![codecov.io](https://codecov.io/github/DLRSP/django-static-base/coverage.svg?branch=main)](https://codecov.io/github/DLRSP/django-static-base?branch=main) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DLRSP/django-static-base/main.svg)](https://results.pre-commit.ci/latest/github/DLRSP/django-static-base/main) [![gitthub.com](https://github.com/DLRSP/django-static-base/actions/workflows/ci.yaml/badge.svg)](https://github.com/DLRSP/django-static-base/actions/workflows/ci.yaml)

## Check Demo Project
* Check the demo repo on [GitHub](https://github.com/DLRSP/example/tree/django-static-base)

## Requirements
-   Python 3.8+ supported.
-   Django 3.2+ supported.

## Setup
1. Install from **pip**:
    ```shell
    pip install django-static-base
    ```
2. Modify `settings.py` by adding the app to `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
        # ...
        "static_base",
        # ...
    ]
    ```
3. Finally, modify your project `urls.py` with handlers for all errors:
    ```python
    # ...other imports...
    
    urlpatterns = [
        # ...other urls...
    ]
    ```
4. Execute Django's command `migrate` inside your project's root:
    ```shell
    python manage.py migrate
    Running migrations:
      Applying static_base.0001_initial... OK
    ```

## Run Example Project

```shell
git clone --depth=50 --branch=django-static-base https://github.com/DLRSP/example.git DLRSP/example
cd DLRSP/example
python manage.py runserver
```

Now browser the app @ http://127.0.0.1:8000
