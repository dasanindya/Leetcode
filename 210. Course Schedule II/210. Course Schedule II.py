#
# Problem: 210. Course Schedule II
# Difficulty: Medium
# Link: https://leetcode.com/problems/course-schedule-ii/submissions/2188955816/
# Language: python3
# Date: 2026-11-03


from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        # Step 1: Build graph and in-degree array
        adj = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # Step 2: Initialize queue with courses requiring 0 prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        # Step 3: Process courses
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            # Unlock dependent courses
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Step 4: If order contains all courses, return it. Otherwise, cycle detected.
        return order if len(order) == numCourses else []
            
