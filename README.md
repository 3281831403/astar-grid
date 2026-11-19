# 网格 A*：堆、启发式与路径

寻路在拐角处绕远、堆序错乱：启发式用欧氏距离而不是曼哈顿，开放集没有用二叉堆，相同 f 值没有稳定 tie-break，已访问节点没有更新，路径没有回溯，墙判定漏掉边界，无路时返回空而不是 -1，批量寻路只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
gameplay/__init__.py
gameplay/astar.py
tests/test_astar.py
```

## 当前状态

`gameplay/astar.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_astar.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 曼哈顿启发式
2. 二叉堆 push/pop
3. 相同 f 稳定 tie-break
4. 更优代价更新节点
5. 路径回溯
6. 边界与墙判定
7. 无路返回 -1

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `gameplay/astar.py`
后 15 条用例应全部通过。
