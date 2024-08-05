# Matrices meme generator

There is a format which uses elements for matrices such that 

```
a b  *  e f  =  10a+e   10b+f
c d     g h     10c+g   10d+h
```

which is funny because this is not how matrix multiplication works.

Here:

- `mats.py` generates elements for matrices in this format with 0<a,b,c,d,e,f,g,h<10 with ones that look too symmetrical omitted and outputs this into `results.txt`.
- `build-worksheet.py` generates a LaTeX worksheet drawing 20 random items from `results.txt` and outputs `worksheet.tex`. 

At present, `results.txt` is 73 items that are output from `mats.py` as is, and `results-squares.txt` is a further set of 24 items where a=e, b=f, c=g and d=h, i.e. a matrix squared. 

Also `worksheet-sm.tex`, `worksheet-sm.pdf` and `worksheet-sm.png` are a version I reformatted a bit to post on social media 5/8/24. I posted this [on Mastodon here](https://mathstodon.xyz/@peterrowlett/112908839913498146).