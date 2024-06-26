# FPL

The FPL package is a Python package that provides a simple interface to the Fantasy Premier League API. It is designed to be easy to use and to provide a simple way to access the data for the Fantasy Premier League game. The package is designed to be used by anyone who wants to access the data for the Fantasy Premier League game, whether they are a beginner or an experienced user.

### Recommended developer setup
We want to use the `make` command to run the `Makefile` commands. To do this, we will need to install `make` on through Chocolatey. Chocolatey is a package manager for Windows that allows you to install software from the command line. To install Chocolatey, follow these instructions ([installation link](https://chocolatey.org/install)).

You can now install `make` by opening a new Command Prompt as administrator and executing `choco install make` in the terminal.

Configure PyCharm to use Command Prompt as the terminal instead of PowerShell. 
To do this, go to `File > Settings > Tools > Terminal` and select `cmd.exe` as the shell path.

### Build an image
To build the image, you can run `make build` in the terminal.

### Run the app
To run the app, you can run `make run` in the terminal.
Then, navigate to `http://localhost:8000/` in your web browser.

### Run JupyterLab
To run JupyterLab, you can run `make jupyter` in the terminal.
Then, navigate to `http://localhost:8889/` in your web browser (if prompted for a token, copy and paste the token from the terminal into the web page).

### Run the tests
To run the tests, you can run `make test` in the terminal.
