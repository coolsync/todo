1 **Create Visual Balance Using the text-align Property**



`text-align: justify;` causes all lines of text except the last line to meet the left and right edges of the line box.

`text-align: center;` centers the text

`text-align: right;` right-aligns the text

`text-align: left;` (the default) left-aligns the text.



2 **Adjust the Width of an Element Using the width Property**



3 **Adjust the Height of an Element Using the height Property**



**Adjust the Height of an Element Using the height Property**



**Use the strong Tag to Make Text Bold**



With the `strong` tag, the browser applies the CSS of `font-weight: bold;` to the element.



**Use the u Tag to Underline Text**



This is often used to signify that a section of text is important,  or something to remember. 



With the `u` tag, the browser applies the CSS of `text-decoration: underline;` to the element.



**Use the em Tag to Italicize Text**



 as the browser applies the CSS of `font-style: italic;` to the element.



**Use the s Tag to Strikethrough Text**



With the `s` tag, the browser applies the CSS of `text-decoration: line-through;` to the element.



**Create a Horizontal Line Using the hr Element**



**Adjust the background-color Property of Text**



> rgba stands for:
>  r = red
>  g = green
>  b = blue
>  a = alpha/level of opacity



 `background-color: rgba(45, 45, 45, 0.1)` 



**Adjust the Size of a Header Versus a Paragraph Tag**

`font-size: 27px`



**Add a box-shadow to a Card-like Element**

The `box-shadow` property takes values for

- `offset-x` (how far to push the shadow horizontally from the element),
- `offset-y` (how far to push the shadow vertically from the element),
- `blur-radius`,
- `spread-radius` and
- `color`, in that order.

The `blur-radius` and `spread-radius` values are optional.

Multiple box-shadows can be created by using commas to separate properties of each `box-shadow` element.



```css
box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
```



**Decrease the Opacity of an Element**

.

> A value of 1 is opaque, which isn't transparent at all.
> A value of 0.5 is half see-through.
> A value of 0 is completely transparent.



**Use the text-transform Property to Make Text Uppercase**



|    Value     |                         Result                         |
| :----------: | :----------------------------------------------------: |
| `lowercase`  |                     "transform me"                     |
| `uppercase`  |                     "TRANSFORM ME"                     |
| `capitalize` |                     "Transform Me"                     |
|  `initial`   |                 Use the default value                  |
|  `inherit`   | Use the `text-transform` value from the parent element |
|    `none`    |           **Default:** Use the original text           |



**Set the font-size for Multiple Heading Elements**



**Set the font-weight for Multiple Heading Elements**



**Set the font-size of Paragraph Text**



**Set the line-height of Paragraphs**



**Adjust the Hover State of an Anchor Tag**



**Change an Element's Relative Position**

Block-level items automatically start on a new line (think headings, paragraphs, and divs) while inline items sit within surrounding content (like images or spans).



`relative`, move it *relative* to its current position in the normal flow of the page.



**Move a Relatively Positioned Element with CSS Offsets**



![img](https://cdn-media-1.freecodecamp.org/imgr/eWWi3gZ.gif)





**Lock an Element to its Parent with Absolute Positioning**



**Change the Position of Overlapping Elements with the z-index Property**

