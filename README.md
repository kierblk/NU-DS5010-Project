# CleanLockHolmes

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
![GitHub repo size](https://img.shields.io/github/repo-size/kierblk/NU-DS5010-Project)
![GitHub contributors](https://img.shields.io/github/contributors/kierblk/NU-DS5010-Project)
![GitHub stars](https://img.shields.io/github/stars/kierblk/NU-DS5010-Project?style=social)
![GitHub forks](https://img.shields.io/github/forks/kierblk/NU-DS5010-Project?style=social)

CleanLockHolmes is a Python library that allows you to clean and prepare 
tabular data for accurate analysis and modeling. This is a collaborative 
project for Northeastern University, DS 
5010 - 
Spring 2023. 

For full project requirements: [Project Requirements](project-requirements.md)

## Contributors

* [@sezzagore91](https://github.com/sezzagore91) 
* [@rebeccabronfeld](https://github.com/rebeccabronfeld) 
* [@kierblk](https://github.com/kierblk)

## Package Structure

```text
NU-DS5010-Project
├── LICENSE.md
├── cleanlockholmes
│   ├── data
│   │   ├── xxxx.py
│   │   └── xxxx.py
│   ├── __init__.py
│   ├── __main__.py
│   └── tests
│       ├── xxxx.py
│       └── xxxx.py
├── README.md
└── .gitignore
```


## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed the latest version of `Python`
* You have a `<Windows/Linux/Mac>` machine. State which OS is supported/which is not.
* You have read `<guide/link/documentation_related_to_project>`.

## Installing TO

To install CleanLockHolmes, follow these steps:

macOS:
```
<install_command>
```


Add run commands and examples you think users will find useful. Provide an options reference for bonus points!

## Contributing
To contribute, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.
6. Request the review of at least two exisiting contributors.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [<license_name>](<link>).

--------
Notes area for combining README format with our project notes:

Usage Example 1: Import CleanlockHolmes, read .csv file of tabular data, identify column types by user input, remove rows containing specificed invalid value, reading new file.

Usage Example 2: Import CleanlockHolmes, read .csv file, utilize prompt option to determine invalid values and remove rows containing them.

Resources:

https://docs.python-guide.org/writing/structure/
https://shields.io/
https://github.com/scottydocs/README-template.md/blob/master/README.md
https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6