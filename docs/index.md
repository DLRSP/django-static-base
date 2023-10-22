Django's application to serve up-to-date common static files (JQuery, Bootstrap, Plugins, ...) as "base" static directory

---

## Requirements

These packages are required:

* Python (3.8+)
* Django (3.2+)

We **highly recommend** and only officially support the latest patch release of each Python and Django series.


## Installation

1. Install using `pip`, including any optional packages you want...

    ``` shell
    pip install django-static-base
    ```

    ...or clone the project from github.

    ``` shell
    git clone https://github.com/DLRSP/django-static-base/
    ```

2. Add `'static_base'` to your `INSTALLED_APPS` setting.

    ``` python title="settings.py"
    INSTALLED_APPS = [
        # ...other apps
        "static_base"
    ]
    ```

3. Add the following pre-requisites to your `base.html` template

    ``` html title="base.html"
    <html>
    <head>
    ...
      <link rel="stylesheet" type="text/css" href="{% static 'base/css/bootstrap.css' %}">
    ...
    </head>
    <body>
    ...
      <script type="text/javascript" src="{% static 'base/js/jquery.min.js' %}"></script>
      <script type="text/javascript" src="{% static 'base/js/bootstrap.min.js' %}"></script>
      <script type="text/javascript" src="{% static 'base/js/plugins/lazysizes.min.js' %}" async></script>
    ...
      <script type="module" src="{% static 'base/js/plugins/instantpage.min.js' %}" defer></script>
    </body>
    </html>
    ```

4. Add all your needed plugins or customization to your `base.html` template or sub-templates used by your project

    ``` html title="base.html"
    <html>
    <head>
    ...
      <link rel="stylesheet" type="text/css" href="{% static 'base/css/plugins/jquery.smartmenus.bootstrap-4.css' %}">
    ...
      <link rel="stylesheet" type="text/css" href="{% static 'base/css/style-btn.css' %}">
      <link rel="stylesheet" type="text/css" href="{% static 'base/css/color/blue.css' %}">
    ...
      <link rel="stylesheet" type="text/css" href="{% static 'base/css/custom.css' %}">
    ...
    </head>
    <body>
    ...
      <script type="text/javascript" src="{% static 'base/js/jquery.min.js' %}"></script>
      <script type="text/javascript" src="{% static 'base/js/bootstrap.min.js' %}"></script>
    ...
      <script type="module" src="{% static 'base/js/plugins/instantpage.min.js' %}" defer></script>
    </body>
    </html>
    ```


## Example

Let's take a look at a quick example of using this project to build a simple App with **custom error pages**.

* Check the demo repo on [GitHub][github-demo]

## Quickstart

Can't wait to get started? The [quickstart guide][quickstart] is the fastest way to get up and running and building a **demo App**.

## Customize

Do you want custom solutions? The [customize][customize] section is an overview of which part are easy to design.
If you find how to personalize different scenarios or behaviors, a [pull request][pull-request] is welcome!

## Development

See the [Contribution guidelines][contributing] for information on how to clone  the repository, run the test suite and contribute changes back to django-errors.

## Security

If you believe you’ve found something in this project which has security implications, please **do not raise the issue in a public forum**.

Send a description of the issue via email to [dlrsp.issue@gmail.com][security-mail].  The project maintainers will then work with you to resolve any issues where required, prior to any public disclosure.

## License

MIT License

Copyright (c) 2010-present DLRSP (https://dlrsp.org) and other contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[index]: .
[github-demo]: https://github.com/DLRSP/example/tree/    

[quickstart]: tutorial/example.md
[customize]: tutorial/customize.md

[contributing]: community/contributing.md
[pull-request]: community/contributing.md#pull-requests

[security-mail]: mailto:dlrsp.issue@gmail.com
