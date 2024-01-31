<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/VVVICTORZHOU/pymeili_resource">
    <img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/logo_v1.png' width='500' alt='pymeili_logo_img'>

  </a>

  <h1 align="center">pymeili</h1>

  <p align="center">
    A Python package to beautify your matplotlib's plots simply!
    <br />
    <a href="https://github.com/VVVICTORZHOU/pymeili_resource"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/VVVICTORZHOU/pymeili_resource">View Demo</a>
    ·
    <a href="https://github.com/VVVICTORZHOU/pymeili_resource/issues">Report Bug</a>
    ·
    <a href="https://github.com/VVVICTORZHOU/pymeili_resource/issues">Request Feature</a>
  </p>
</div>

## What is it?
**pymeili** is a Python package that provides fast, flexible, and expressive; "meili(美丽/美麗)" literally means beautiful in Chinese.
This package aims to simplify cumbersome and redundant personalized settings, providing a convenient and fast syntax to accelerate code editing speed. Simultaneously, it enhances the visual aesthetics of image output, ensuring efficiency while breaking free from the monotonous default image style, creating a more ‘high-quality’ matplotlib visual feast.

## What does it have?
- Self-defined ***global*** parameters
- Multiple functional ***Axes*** supports
  - matplotlib's Figure
  - matplotlib's Subplot
  - Cartopy
  - Basemap
- High flexability for ***Mix and match*** functions between matplotlib and pymeili

## How to get started?
### Preparation
Before starting install pymeili, please make sure you have installed the following python pacakges at first
- matploblib
- numpy
- pathlib / pathlib2
- cartopy
- basemap
To install packages, use the following command in your terminal
```sh
pip install {pacakge_names}
```
Using `space` to seperate different packages' name.

### Installation
Then, we can start to install pymeili package by using following command
```sh
pip install pymeili
```
Binary installers for the latest released version are available at the Python Package Index (PyPI), you can also visit the PyPI library: [pymeili in PyPI](https://pypi.org/project/pymeili/) to download the package file manually.

### Important
Due to the font file and config file (source files as called) downloading requirement, you might encounter the errors raising if you have not deployed git environment yet. You have two choice to fix this problem
1. Deploy `git` environment in your PC, and using following command in you terminal
   - First, go to the location of installed pymeili at your PC
   ```sh
   cd C:/Username/path/to/your/pymeili/folder/
   ```
   - Next, clone the resource folder by using
   ```sh
   git clone https://github.com/VVVICTORZHOU/pymeili_resource.git
   ```
2. Manually download "source files" from github
   - Go to [pymeili in Github](https://github.com/VVVICTORZHOU/pymeili_resource) directly, download the *whole* respository to your PC; moving the `pymeili_resource` folder into installed pymeili package folder.
- Note that the pymeili package usually installed at `c:\users\Username\appdata\local\programs\python\python311\lib\site-packages\pymeili\`

### After Installation
To make sure you have successfully install pymeili, import the module in your python script such as
```python
from pymeili import beautifyplot as bp
```


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/VVVICTORZHOU/pymeili_resource.svg?style=for-the-badge
[contributors-url]: https://github.com/VVVICTORZHOU/pymeili_resource/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/VVVICTORZHOU/pymeili_resource.svg?style=for-the-badge
[forks-url]: https://github.com/VVVICTORZHOU/pymeili_resource/network/members
[stars-shield]: https://img.shields.io/github/stars/VVVICTORZHOU/pymeili_resource.svg?style=for-the-badge
[stars-url]: https://github.com/VVVICTORZHOU/pymeili_resource/stargazers
[issues-shield]: https://img.shields.io/github/issues/VVVICTORZHOU/pymeili_resource.svg?style=for-the-badge
[issues-url]: https://github.com/VVVICTORZHOU/pymeili_resource/issues
[license-shield]: https://img.shields.io/github/license/VVVICTORZHOU/pymeili_resource.svg?style=for-the-badge
[license-url]: https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
