<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
![PyPI](https://img.shields.io/pypi/v/allsafe)

<!-- PROJECT LOGO -->
<br />
<div>
  <h1 align="center">AllSafe</h2>
  <p align="center">
    Modern Safe and Unique Password Generator. Do Not Worry About Passwords Anymore.
    <br />
    <br />
    <a href="https://github.com/emargi/AllSafe/issues/new?labels=bug">Report Bug</a>
    &middot;
    <a href="https://github.com/emargi/AllSafe/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
      <ul>
        <li><a href="#linux">Linux</a></li>
        <li><a href="#windows">Windows</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#credits">Credits</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
[![asciicast](https://asciinema.org/a/704458.svg)](https://asciinema.org/a/704458)


> [!NOTE]
> This tool will never store any of your data and does *NOT* need an internet connection. so you do not have to worry about your data-safety.

> AllSafe is a terminal tool to generate unique password for each application or website you want to sign up in.

AllSafe will give you a unique password for every app based on the given info, so everytime you pass the same info, you will get the same password

### Why do we need unique passwords?
with having a unique password for each website, you will not need to worry about other passwords in case one of the websites has a security breach or your password gets leaked somehow.

### How do we not forget the passwords?
You don't, you just have to memorize your secret codes (safe enough to use one for all passwords). with the same secret code and the same data, you will get the same password. so no need to worry about storing or memorizing your passwords.

### How does the algorithm work?
Your secret code will turn your data into some weird characters. the weird characters are encrypted into a hash. the algorithm gets rid of some keys in the hash. the incomplete hash is seperated into small parts based on the password length. each small part will be converted into a decimal number. each decimal number is divided by the length of the password characters, and a character will be chosen for the password based on the remainder.

### If my password gets exposed, will my secret code be revealed?
No, even if they find a way to guess the hash, they will have the incomplete hash. although the complete hash is based on some weird characters.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- INSTALLATION -->
## Installation
### Linux
1. **Install `pipx`:**
  Use the package manager of your wish on your OS (e.g. apt)
  ```sh
  sudo apt install pipx
  pipx ensurepath
  ```
2. **Install `AllSafe`:**
  - Trust PyPi's Build?
  ```sh
  pipx install allsafe
  ```
  - Not Trust PyPi's Build?
  ```sh
  pipx install git+https://github.com/emargi/allsafe
  ```

### Windows
First, make sure you have python and pip installed on your system.
- Trust PyPi's Build?
  ```sh
  pip install allsafe
  ```
- Not Trust PyPi's Build?
  ```sh
  pip install git+https://github.com/emargi/allsafe
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE -->
## Usage

### Interactive Mode
Run:
```sh
allsafe
```
or alternatively:
```sh
allsafe -i
```

### Commandline Arguments
required arguments:
```sh
allsafe -a APP -u USERNAME -s SECRET
```
see full help:
```sh
allsafe -h
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Note that we use <a href="https://semver.org">Semantic Versioning</a> in the project and you have to change the `__version__` variables in every file that contains it, before a commit.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
3. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Credits -->
## Credits
- This README file is based on [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
