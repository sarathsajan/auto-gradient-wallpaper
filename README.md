# AutomatedGradientWallpaperSystem CQ-23

* Generate 4K gradient coloured wallpapers
* Directly change the desktop wallpaper in a click
* Generated image is also saved in the directory, both Sharp and Gaussian Blurred
* <img src="https://www.youtube.com/s/desktop/e9a67dcd/img/favicon.ico" width = 16px> [Demo on youtube](https://www.youtube.com/watch?v=P3KJboXtU04)

---

### How It Works

* Generate a block (or tile) of solid color, now use a FOR loop to generate NxN blocks(or tiles) of random color
* Stich them all together to get a mosaic of NxN tiles.
* Now pass Gaussian Blur effect of desired strength to achieve the frosted glass effect.

---

### Samples

#### Auto-generated wallpaper sample 1
<img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%201/demo_picture_w1_1.jpg" width = 400px> <img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%201/demo_picture_w1_2.jpg" width = 400px>
<img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%201/w1_sharp.jpeg" width = 400px> <img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%201/w1_gradient.jpeg" width = 400px>


#### Auto-generated wallpaper sample 2
<img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%202/demo_picture_w2_1.jpg" width = 400px> <img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%202/demo_picture_w2_2.jpg" width = 400px>
<img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%202/w2_sharp.jpeg" width = 400px> <img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%202/w2_gradient.jpeg" width = 400px>


#### Auto-generated wallpaper sample 3
<img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%203/demo_picture_w3_1.jpg" width = 400px> <img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%203/demo_picture_w3_2.jpg" width = 400px>
<img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%203/w3_sharp.jpeg" width = 400px> <img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%203/w3_gradient.jpeg" width = 400px>


#### Auto-generated wallpaper sample 4
<img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%204/demo_picture_w4_1.jpg" width = 400px> <img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%204/demo_picture_w4_2.jpg" width = 400px>
<img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%204/w4_sharp.jpeg" width = 400px> <img src="https://github.com/sarathsajan/auto-gradient-wallpaper/blob/main/demo/wallpaper%204/w4_gradient.jpeg" width = 400px>

---

### How to use

_Project written in python 3.11, so I am assuming you have already python installed and is familiar with it. I will make the project more user-friendly at a later stage._

#### Step 1

Run the requirements.txt using the below command

```pip install -r requirements.txt```


#### Step 2

Run the python file named app.py using the below command

```python app.py```


#### Bonus Step

Right-click and edit the path inside the Windows Batch file named ```AutoGradientWallpaper.bat```

Here, first give the absolute path to your ```python.exe``` (if virtual environment is used then give the path to ```python.exe``` in virtual environment).

Then, give the absolute path to our ```app.py``` file.

That's it, now create a copy of the ```AutoGradientWallpaper.bat``` in to your desktop (home screen). Double-click and enjoy.
