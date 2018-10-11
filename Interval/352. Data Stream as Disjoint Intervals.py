"""
thought process:
what's the best data structure to maintain this interval array, such that it has low cost to add numbers.
List will have addNum O(n) and getInterval O(1) --> good design for less write/add and heavy read/query
BST will have addNum O(lgn) and getInterval O(n) --> good design for heavy write and light query
"""
