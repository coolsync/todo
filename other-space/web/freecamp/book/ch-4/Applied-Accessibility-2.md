## Use tabindex to Specify the Order of Keyboard Focus for Several Elements

使用 tabindex 指定多个元素的键盘焦点顺序

```powershell

Inspirational Quotes     励志名言


```




## Create a Media Query

```powershell

viewport        (屏幕的) 视点, 视图


```

Here's an example of a media query that returns the content when the device's width is less than or equal to 100px:
```css
@media (max-width: 100px) { /* CSS Rules */ }
```

and the following media query returns the content when the device's height is more than or equal to 350px:
```css
@media (min-height: 350px) { /* CSS Rules */ }
```


## Make an Image Responsive

使图像具有响应性


aspect ratio    纵横比


```css
img {
  max-width: 100%;
  height: auto;
}
```
The max-width of 100% will make sure the image is never wider than the container it is in, and the height of auto will make the image keep its original aspect ratio.


## Use a Retina Image for Higher Resolution Displays

使用 Retina 图像进行更高分辨率的显示


像素密度就是区分不同显示设备的一个指标，
它一般会以 PPI（Pixel Per Inch，即每英寸像素）或 DPI（每英寸点数）为计量单位。

```html
<style>
  img {
    height: 100px;
    width: 100px;
  }
</style>

<img src="https://s3.amazonaws.com/freecodecamp/FCCStickers-CamperBot200x200.jpg" alt="freeCodeCamp sticker that says 'Because CamperBot Cares'">
```


## Make Typography Responsive

使排版具有响应性

The four different viewport units are:

vw (viewport width): 10vw would be 10% of the viewport's width.
vh (viewport height): 3vh would be 3% of the viewport's height.
vmin (viewport minimum): 70vmin would be 70% of the viewport's smaller dimension (height or width).
vmax (viewport maximum): 100vmax would be 100% of the viewport's bigger dimension (height or width).

vmin： 如 70vmin 的意思是视窗的高度和宽度中较小一个的 70%。
vmax： 如 100vmax 的意思是视窗的高度和宽度中较大一个的 100%

```html
<style>
  h2 {
    width: 80vw;
  }
  p {
    width: 75vmin;
  }
</style>

<h2>Importantus Ipsum</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus quis tempus massa. Aenean erat nisl, gravida vel vestibulum cursus, interdum sit amet lectus. Sed sit amet quam nibh. Suspendisse quis tincidunt nulla. In hac habitasse platea dictumst. Ut sit amet pretium nisl. Vivamus vel mi sem. Aenean sit amet consectetur sem. Suspendisse pretium, purus et gravida consequat, nunc ligula ultricies diam, at aliquet velit libero a dui.</p>
```



