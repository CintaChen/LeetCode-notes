# LeetCode 3. 无重复字符的最长子串

## 题目描述

给定一个字符串 `s`，请你找出其中不含有重复字符的最长子串的长度。

示例：

```python
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以长度为 3。
```

------

## 解题思路：滑动窗口 + 哈希表

这道题可以使用滑动窗口来解决。

我们维护一个窗口 `[left, right]`，保证窗口中的字符始终没有重复。

- `left` 表示窗口左边界
- `right` 表示窗口右边界
- `char_indexMap` 用来记录当前窗口中出现过的字符
- `max_length` 用来记录目前找到的最长无重复子串长度

当右指针 `right` 遍历字符串时：

1. 如果 `s[right]` 不在当前窗口中，说明没有重复，可以直接加入窗口。
2. 如果 `s[right]` 已经在窗口中，说明出现重复字符。
3. 此时不断删除窗口左边的字符，并移动 `left`，直到当前字符不再重复。
4. 每次更新窗口后，计算当前窗口长度：`right - left + 1`。
5. 用它更新最大长度。

------

## 代码实现

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_indexMap = {}
        max_length = 0

        for right in range(len(s)):
            # 如果当前字符已经在窗口中，说明出现重复
            # 不断删除窗口左侧字符，直到当前字符不重复
            while s[right] in char_indexMap:
                del char_indexMap[s[left]]
                left += 1

            # 将当前字符加入窗口
            char_indexMap[s[right]] = right

            # 更新最大长度
            max_length = max(max_length, right - left + 1)

        return max_length
```

------

## 示例分析

以字符串 `"abba"` 为例：

```text
初始:
left = 0
window = {}
max_length = 0
```

遍历过程：

```text
right = 0, s[right] = 'a'
window = {'a': 0}
当前长度 = 1
max_length = 1
right = 1, s[right] = 'b'
window = {'a': 0, 'b': 1}
当前长度 = 2
max_length = 2
right = 2, s[right] = 'b'
'b' 已经在 window 中，出现重复

删除 s[left]，也就是 'a'
left 向右移动

'b' 仍然在 window 中
继续删除 s[left]，也就是旧的 'b'
left 继续向右移动

然后加入新的 'b'
window = {'b': 2}
max_length = 2
right = 3, s[right] = 'a'
window = {'b': 2, 'a': 3}
当前长度 = 2
max_length = 2
```

最终结果：

```python
return 2
```

最长无重复子串可以是 `"ab"` 或 `"ba"`。

------

## 关键点总结

这段代码的核心在于：

```python
while s[right] in char_indexMap:
    del char_indexMap[s[left]]
    left += 1
```

它的含义是：

> 如果当前字符已经在窗口中，就从窗口左边开始删除字符，直到当前字符不再重复。

这里使用 `while` 而不是 `if`，是因为重复字符不一定刚好在窗口最左边，可能需要连续删除多个字符。

------

## 复杂度分析

时间复杂度：`O(n)`

虽然代码里有 `while` 循环，但是每个字符最多被加入一次、删除一次，所以整体仍然是线性时间复杂度。

空间复杂度：`O(k)`

其中 `k` 是字符集大小。字典中最多存储当前窗口中的所有不重复字符。