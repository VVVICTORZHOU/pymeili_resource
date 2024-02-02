<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Facebook][facebook-shield]][facebook-url]
[![Weibo][Weibo-shield]][Weibo-url]

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
    <a href="https://github.com/VVVICTORZHOU/pymeili_resource/tree/main?tab=readme-ov-file#demonstration">View Demo</a>
    ·
    <a href="https://github.com/VVVICTORZHOU/pymeili_resource/issues">Report Bug</a>
    ·
    <a href="https://github.com/VVVICTORZHOU/pymeili_resource/issues">Request Feature</a>
    .
    <a href="https://github.com/VVVICTORZHOU/pymeili_resource/wiki">Wiki</a>
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
  - Windrose
- High flexability for ***Mix and match*** functions between matplotlib and pymeili

## How to getting started?
### Preparation
Before starting install pymeili, please make sure you have installed the following python pacakges at first
- matploblib
- numpy
- pathlib / pathlib2
- cartopy
- basemap
- windrose

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
   - Go to [pymeili in Github](https://github.com/VVVICTORZHOU/pymeili_resource) directly, download the *whole* respository to your PC; unziping and moving the `pymeili_resource-main` folder into installed pymeili package folder. Finally, **Rename** the folder into `pymeili_resource` (get rid of '-main').
- Note that the pymeili package usually located at `c:\users\Username\appdata\local\programs\python\python311\lib\site-packages\pymeili\`

3. Manually download full package version from github
   - Go to [pymeili releases in Github](https://github.com/VVVICTORZHOU/pymeili_resource/releases) directly, download the zipped folder (, whose filename includes "pymeili") in the assets of latest release. Move the `pymeili` folder in the unzipped folder into your root folder to import it hastily. Remind that this way is **strongly not recommended**.

### After Installation
To make sure you have successfully install pymeili, import the module in your python script such as
```python
from pymeili import beautifyplot as bp
```

## How to use?
### Basic instruction
Learning basic concepts about how pymeili works is good for beginners; for instance, how `initplot()` works and how to transfer different types of axes to pymeili axes. Read [pymeili wiki: Basic Instruction](https://github.com/VVVICTORZHOU/pymeili_resource/wiki/Basic-Instruction) for further guidances.

### Functions Instruction
Please visit [pymeili wiki](https://github.com/VVVICTORZHOU/pymeili_resource/wiki). There are still many pymeili's functions have not been composed into wiki, we will try to keep catch up and update frequently.

### Demonstration
For further demo about using pymeili package, please check out following script link:
1. **Get start!** Plot the basic figure in pymeili: [Demo 1](https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/script/demo1_BasicPlot.py)
  <div align="center"><img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/demo/demo1_BasicPloy.png' width='300' alt='pymeili_demo1_img'></div>

2. **Change theme!** Plot figure in dark mode: [Demo 2](https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/script/demo2_BasicPlotDarkMode.py)
  <div align="center"><img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/demo/demo2_BasicPloyDarkMode.png' width='400' alt='pymeili_demo2_img'></div>

3. **Give me donut!** Contour plot in pymeili: [Demo 3](https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/script/demo3_ContourPlot.py)
  <div align="center"><img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/demo/demo3_ContourPlot.png' width='500' alt='pymeili_demo3_img'></div>

4. **World map!?** Using cartopy under pymeili: [Demo 4](https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/script/demo4_Cartopy.py)
  <div align="center"><img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/demo/demo4_Cartopy.png' width='500' alt='pymeili_demo4_img'></div>

5. **Need more plots at the same time?** Basic intro of subplot in pymeili: [Demo 5](https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/script/demo5_BasicSubplot.py)
  <div align="center"><img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/demo/demo5_BasicSubplot.png' width='500' alt='pymeili_demo5_img'></div>

6. **Many colorful world map!** Subplot with basemap in pymeili: [Demo 6](https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/script/demo6_BasemapContourf.py)
  <div align="center"><img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/demo/demo6_Basemap.png' width='500' alt='pymeili_demo6_img'></div>

7. **Cartopy vs. Basemap!** Comparison between two ways to plot map: [Demo 7](https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/script/demo7_BasemapVSCartopy.py)
  <div align="center"><img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/demo/demo7_BasemapVSCartopy.png' width='750' alt='pymeili_demo7_img'></div>

8. **Image Processing!** Image Processing in pymeili: [Demo 8](https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/script/demo8_ImshowPlot.py)
  <div align="center"><img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/demo/demo8_ImshowPlot.png' width='500' alt='pymeili_demo8_img'></div>

9. **What a beautifyful rose!?** Plotting simple windrose in pymeili: [Demo 9](https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/script/demo9_Windrose.py)
  <div align="center"><img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/demo/demo9_Windrose.png' width='500' alt='pymeili_demo9_img'></div>

## How to getting help?
For more usage questions, go to [pymeili in stackflow](https://stackoverflow.com/questions/tagged/pymeili) is recommended. By the way, you can also contact the developer, but we cannot promise to response you immidiately.

## What Next?
### Community Request
We will be committed to continuously maintaining this package and optimizing and developing it based on reported bugs and requested features. All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome; you can report bugs for this project through the following ways, and you can also submit requests for wanted new features.
- Access [Bugs Report & Features Request](https://github.com/VVVICTORZHOU/pymeili_resource/issues)

### Development Roadmap
We will issue the roadmap regularly to response the community requests, including bugs and wishlist.
<img src='https://github.com/VVVICTORZHOU/pymeili_resource/blob/main/img/roadmap_v1.png' width='1200' alt='pymeili_roadmap_img'>
For changelog information, please visit [pymeili in PyPI](https://pypi.org/project/pymeili/).

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
[linkedin-url]: https://www.linkedin.com/in/%E5%91%A8%E5%BD%A5%E5%BB%B7-z-v-829a232b1

[facebook-shield]: https://img.shields.io/badge/FB-brightgreen?style=for-the-badge&logo=flat&logoColor=0866ff&label=Facebook&color=0866ff
[facebook-url]: https://www.facebook.com/profile.php?id=100067467153966

[Weibo-shield]: https://img.shields.io/badge/WB-brightgreen?style=for-the-badge&logo=flat&logoColor=d52c2b&label=WEIBO&color=d52c2b
[Weibo-url]: https://weibo.com/u/7564787149?tabtype=feed

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
