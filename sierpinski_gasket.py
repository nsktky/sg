import matplotlib.pyplot as plt
import matplotlib.patches as pat
import math
import streamlit as st

st.title('シェルピンスキーのギャスケット')
'''
## 説明
シェルピンスキーのギャスケットはフラクタル図形の1種であり、自己相似的な無数の三角形からなる図形です。

## 作成方法
シェルピンスキーのギャスケットは以下のように作成できます。
- 正三角形を用意する
- 正三角形の各辺の中点を互いに結んでできた中央の正三角形を切り取る
- 残った正三角形に対して上記の手順を無限に繰り返す

## 操作方法
サイドバーから深さを調節できます。初期値は0で、最大7まで設定できます。
'''
depth = st.sidebar.slider("Level of depth", 0, 7, 0, 1)

def return_triangle(triangle):
    x1 = (triangle[0][0] + triangle[1][0]) / 2
    y1 = (triangle[0][1] + triangle[1][1]) / 2
    x2 = (triangle[1][0] + triangle[2][0]) / 2
    y2 = (triangle[1][1] + triangle[2][1]) / 2
    x3 = (triangle[2][0] + triangle[0][0]) / 2
    y3 = (triangle[2][1] + triangle[0][1]) / 2
    new_triangle = [(x1, y1), (x2, y2), (x3, y3)]
    return new_triangle

def distance(p1,p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def select_neighbor_points(p, triangle):
    distance1 = distance(p, triangle[0])
    distance2 = distance(p, triangle[1])
    distance3 = distance(p, triangle[2])
    if distance1 > distance2:
        if distance1 > distance3:
            return [p, triangle[1], triangle[2]]
        else:
            return [p, triangle[0], triangle[1]]
    else:
        if distance2 > distance3:
            return(p, triangle[0], triangle[2])
        else:
            return(p, triangle[0], triangle[1])

def produce_fractal1(triangle, iteration):
    if iteration == 0: return 0
    p1 = triangle[0]
    p2 = triangle[1]
    p3 = triangle[2]
    new_triangle = return_triangle(triangle)
    p = pat.Polygon(xy = new_triangle,fc = "black", ec = "black")
    ax.add_patch(p)
    produce_fractal1(select_neighbor_points(p1, new_triangle), iteration - 1)
    produce_fractal1(select_neighbor_points(p2, new_triangle), iteration - 1)
    produce_fractal1(select_neighbor_points(p3, new_triangle), iteration - 1)

triangle = [(0.2, 0.2), (0.8, 0.2), (0.5, 0.8)]
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1, 1, 1)
ax.axis('off')
p = pat.Polygon(xy = triangle, fc = "yellow", ec = "black")
ax.add_patch(p)

produce_fractal1(triangle, depth)
fig


st.write('参考文献1：https://qiita.com/okakatsuo/items/f2e79fc501ed9f799734')
st.write('参考文献2：https://ja.wikipedia.org/wiki/%E3%82%B7%E3%82%A7%E3%83%AB%E3%83%94%E3%83%B3%E3%82%B9%E3%82%AD%E3%83%BC%E3%81%AE%E3%82%AE%E3%83%A3%E3%82%B9%E3%82%B1%E3%83%83%E3%83%88')