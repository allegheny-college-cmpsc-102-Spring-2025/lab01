# File Searching

## Assigned and Due

- __Assigned__: Monday, 22 Jan 2024
- __Due__: Monday, 28 January 2024
- __Expiration__: 5 Feb 2024

---

![The Games's a foot!](graphics/sholmes_sm.png)

You are invited to complete a program to play the part of Sherlock Holmes to uncover words in a block of text.

## Project Goals

This lab assignment invites you to combine what you learned about the basics of Python programming to implement a useful program that can search for a word in a file. As you enhance your technical skills, you will program with tools such as VS Code and a terminal window and the Python programming language and the Poetry package manager.

## Project Access

You can access this assignment by clicking the link provided to you in Discord or in a course schedule. Once you click this link it will create a GitHub repository that you can clone to your computer by using the `git clone` command to download the project from GitHub to your computer. Now you are ready to add source code and documentation to the project!

## Installations

After cloning this repository to your computer, please complete the following installations, if not done previously, before starting the work on the assignment:

- Install Python. Please see:
  - [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
  - [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
  - [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)
- Install `gatorgrade`
  - First, [install `pipx`](https://pypa.github.io/pipx/installation/)
  - Then, install `gatorgrade` with `pipx install gatorgrade`
- [Install `poetry`](https://python-poetry.org/docs/)
- Install `VSCode` or another editor. See [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

## Programming task

When you have completed necessary installations, you can begin the programming effort by completing the following steps:

- In your terminal, use the `cd` command to change into the directory for this repository
- Change into the program directory by typing `cd search/`
- Install the dependencies for the project by typing `poetry install`
- You may need to wait for several minutes for the project's dependencies to install
- Run the program in its two different modes by typing:
  - `poetry run search --word speckled --dir input --file speckledBand.txt`
  - Please note that the program will not work unless you add the required
    source code at the designated `TODO` markers
- Confirm that the program is producing the expected output
- Use a `gatorgrade --config config/gatorgrade.yml` command to run GatorGrader
- You may also use the output from running GatorGrader in GitHub Actions
- Provide all of the required responses in the `writing/reflection.md` file

## Expected Output

This project invites you to implement a file searching program called `search`. The `search` program takes as input a word (e.g., "proactive") and determines whether or not it is in the text of a file provided on the input. For instance, if the file called `input/speckledBand.txt` contains inside of the text on the main page of this web site, then searching for the word `proactive` with the command `poetry run search --word speckled --dir input --file speckledBand.txt` yields:

```shell
😃 Searching through the file called input/speckledBand.txt!

Was the word "speckled" found in the file input/speckledBand.txt? Yes
```

When you search for a word that does not appear inside of the input file with a command like `poetry run search --word conundrum --dir input --file speckledBand.txt` then the program will produce the following output:

```shell
😃 Searching through the file called input/speckledBand.txt!

Was the word "elementary" found in the file input/speckledBand.txt? No
```

Once your program is working correctly, you should also try to use it when
specify a file that is not available on your computer! For instance, if you run it with the command `poetry run search --word python --dir input --file notfound.txt` then it will not perform a search and instead produce the following output:

```shell
😃 Searching through the file called input/notfound.txt!

🤷 input/notfound.txt was not a valid file
```

### Special note: Use Poetry

Don't forget that if you want to run the `search` program you must use your terminal window to first go into the GitHub working repository containing this project and then go into the `search` directory that contains the project's source code. Finally, remember that before running the program you must run `poetry install` to add the dependencies.

## Adding Functionality

If you study the file `search/search/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `search` will produce correct output. If you run the provided test suite with the command `poetry run task test` you will see that it produces output like the following:

```
================================== ERRORS ==================================
__________________ ERROR collecting tests/test_search.py ___________________
tests/test_search.py:5: in <module>
    from search import main
search/main.py:31: in <module>
    ???
E   NameError: name 'cli' is not defined
========================= short test summary info ==========================
ERROR tests/test_search.py - NameError: name 'cli' is not defined
!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!
============================= 1 error in 0.11s =============================
```

Alternatively, running the program with a command like `poetry run search --word speckled --dir input --file speckledBand.txt` will produce the following output:

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/gkapfham/.pyenv/versions/3.9.2/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 790, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  [...]
    @cli.command()
NameError: name 'cli' is not defined
```

This output suggests that the `cli` variable was not correctly declared! After declaring the `cli` variable in the appropriate fashion, following the relevant instructions in the description of the [technical skills](/proactive-skills/introduction-proactive-skills/), you should find the other `TODO` markers and correctly resolve them. For instance, you can add this function to the `main.py` file:

```python linenums="1"
def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    if file is not None:
        # the file is valid
        if file.is_file():
            return True
    # the file was either none or not valid
    return False
```

Line `1` of the above source code segment contains the signature for the
`confirm_valid_file` function, showing that it takes as input a `file` variable that is of type `Path` and returns a `bool` to indicate whether or not the file is valid. If the conditional logic on lines `4` and `6` confirms that the `file` variable is both not equal to `None` and is, in fact, a file, then the function returns `True`. Otherwise, line `9` of `confirm_valid_file` returns `False` to indicate that the provided `file` is not valid.

In addition to `confirm_valid_file`, you must completely implement these
functions:

- `def human_readable_boolean(answer: bool) -> str`
- `def word_search(text: str, word: str) -> bool`
- `def word(word: str = typer.Option(None), dir: Path = typer.Option(None), file: Path = typer.Option(None)) -> None`

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section:

```toml
[tool.taskipy.tasks]
black = { cmd = "black search tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 search tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy search", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle search tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint search tests", help = "Run the pylint checks for source code documentation" }
test = { cmd = "pytest -x -s", help = "Run the pytest test suite" }
test-silent = { cmd = "pytest -x --show-capture=no", help = "Run the pytest test suite without showing output" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy && task test"
lint = "task black && task flake8 && task pydocstyle && task pylint"
```

This section makes it easy to run commands like `poetry run task lint` to
automatically run all of the linters designed to check the Python source code in your program and its test suite. You can also use the command `poetry run task black` to confirm that your source code adheres to the industry-standard format defined by the `black` tool. If it does not adhere to the standard then you can run the command `poetry run black search tests` and it will automatically reformat the source code.

Along with running tasks like `poetry run task list`, you can run `gatorgrade --config config/gatorgrade.yml` to check your work. If `gatorgrade` command shows that all checks pass, you will know that you made progress towards correctly implementing and writing about `search`.

If your program has all of the anticipated functionality, you can run the
command `poetry run task test` and see that the test suite produces output like this:

```shell
collected 5 items

tests/test_search.py .....
```

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text editor to answer all of the questions in the `writing/reflection.md` file. For instance, you should provide the output of the Python program in a fenced code block, explain the meaning of the Python source code segments that you implemented, and answer all of the other questions about your experiences in completing this project.


## Submission 

As you are working on your lab, you are to commit and push regularly. The commands are the following.

 ``` bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 50%]:**: For the lab01 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is only checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

---

## GatorGrade

### Checks for GatorGrade

For immediate feedback on submissions, we will be using Gator Grade to inform the of missing components in the submission. As you submit, you will notice that there is a thick red X that will change to a green check mark when all components have been included in the submission. You are encouraged to click on the red X to find a listing of the components to address.

You can check the baseline writing and commit requirements for this lab assignment by running department's assignment checking `gatorgrade` tool. To use `gatorgrade`, you first need to make sure you have Python3 installed (type `python --version` to check). If you do not have Python installed, please see:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, if you have not done so already, you need to install `gatorgrade`:

- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`: `gatorgrade --config config/gatorgrade.yml`

## Seeking Assistance

* Extra resources for using markdown include;
  + [Markdown Tidbits](https://www.youtube.com/watch?v=cdJEUAy5IyA)
  + [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* Do not forget to use the above git commands to push your work to the cloud for the instructor to grade your assignment. You can go to your GitHub repository using your browser to verify that your files have been submitted. Please see the TL’s or the instructor if you have any questions about assignment submission.

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.
