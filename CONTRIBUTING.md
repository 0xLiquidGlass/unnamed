# Contributing To Unnamed

Thank you for contributing to Unnamed. Your contribution means a lot to this project

## 1. About Unnamed Wallet

Unnamed Wallet is an Algorand wallet that grants users of the wallet privacy and security, and it is built on Python Algorand SDK

## 2. How To Contribute? 

You can contribute to the development of Unnamed in many ways:

- Report bugs,
- Write or improving on documentation,
- Write new code or improve on existing code,
- Coming up with new features and submit it as a proposal and
- Help to answer questions in the community

## 3. Unnamed's Code Style

### a. Unix Philosophy

- "Do one thing and do it well"
- One file, one purpose
- All programs should work without the need of converting text to binary
- To ease development and maintenance of code

More can be found here: [https://en.wikipedia.org/wiki/Unix_philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)

### b. Self-Documenting Code

- Make use of meaningful names to write code variables, functions, classes, etc
- Reduce friction for other developers and maintainers to understand the code
- Reduce need for comments

More can be found here: [https://en.wikipedia.org/wiki/Self-documenting_code](https://en.wikipedia.org/wiki/Self-documenting_code)

### c. Current naming conventions:

- File names --> PascalCase

- Variables --> camelCase

- Functions --> lower_case_with_underscores

Note that all of thse naming conventions are only applicable to programs in Unnamed Wallet

## 4. Pull Request

Any pull requests are welcomed as long as they have a good reason to be implemented. They can be new features, bug fixes, vulnerability fixes, and many more

For your pull requests to be merged to the "main" branch, remember to:

a. Clone the repo using "git clone https://github.com/0xLiquidGlass/unnamed.git"from the original repo. No fork is needed.

b. Do a "git remote add origin https://github.com/0xLiquidGlass/unnamed.git" to add the repo

c. Do a "git checkout" with the option "-b" with the name of your new branch to create the new branch

d. Go to the directory where you want to commit your changes or additions and do a "git add <files or directory>"

e. Do a "git commit" with your PGP key signature using "-S" (capital S) and add a brief message containing using "-m" what the merge is about and if possible, state briefly what are the changes or additions

f. "git push origin -u <branch name>" your new branch to the original repo

g. Go to the repo's branch that you pushed to and click "Create pull request" when you are ready to do a pull request

[Here](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key) is how you can tell Github about your PGP signing key

Please make sure that the pull requests are working before doing the pull request
