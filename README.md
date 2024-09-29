Methodology:
Going towards this project was very difficult for me because I have never used opencv or done any coding similar to this. However, this peaked my interest even further because I want to learn and actually get to do this outside of practice. I started out with checking out the opencv help documents but they were not really that helpful. Then I watched a few tutorials on youtube about the basics. I then used ChatGPT to really guide and show me how opencv works. Throughout all this I came accross many problems.

What did you try and why do you think it did not work:
Obviously feeding ChatGPT something so analytical was not going to work, and unsurprisingly it did exactly that. First it would draw lines on the wall, then it would just draw random lines. Eventually by "printing" the color mask of the image, I figured out the root cause was the GRB color detection. The range was completely off as it was detecting the walls, the chairs and it was also comparing two ranges and combining them. I got rid of the combining and trialed and errored the color range. Eventually I got a perfect mask and the rest of the code came together

Libraries used:
OpenCV, Numpy
