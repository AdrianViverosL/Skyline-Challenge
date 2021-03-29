# The Skyline Challenge 
This is my solution to the problem of a Skyline contour, where are given certain "buildings" described as coordinates [Li, Ri, Hi] being Li the left point of the ith building, Ri for the right side, and Hi as the height of the current building. 

This python script receives a list of buildings and draws the contour of it returning a list of coordinates of xi, yi, that represents each point of the skyline. 

The following image shows on the left side, the buildings present in a list, while on the right side is the output expected. 

![alt text](https://github.com/AdrianViverosL/Skyline-Challenge/blob/main/example.png?raw=true)

As you can see, the list that contains all the buildings in the above image is: 
```python
[[2,9,10],[3,6,15],[5,12,12],[13,16,10],[15,17,5]]
```
While the contour list should be: 
```python
[[2, 10], [3, 15], [6, 12], [12, 0], [13, 10], [16, 5], [17,0]]
```