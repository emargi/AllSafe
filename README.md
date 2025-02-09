<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

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
[![asciicast](https://asciinema.org/a/700512.svg)](https://asciinema.org/a/700512)

This tool will never store any of your data and does *NOT* need an internet connection. so you do not have to worry about your data-safety.

Before any sign in/up in a website/app, you can use this tool to generate a unique and safe password. each time you use this tool with the same given data, you'll get the same password so you don't need to remember the passwords. you just have to remember a secret code for your passwords. You can use a single secret code for all of your passwords (it is safe enough but not recommended).

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
