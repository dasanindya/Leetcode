#
# Problem: 207. Course Schedule
# Difficulty: Medium
# Link: https://leetcode.com/problems/course-schedule/submissions/2188955615/
# Language: python3
# Date: 2026-11-03


from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Kahn's Algorithm (BFS with In-Degrees)
        # Step 1: Build adjacency list and in-degree array
        # Build Adjacency List & In-Degree Array: Track outgoing edges from each course and count how many incoming prerequisites (in_degree) each course has.
        adj = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # Step 2: Initialize queue with courses having 0 in-degree
        # Initialize Queue: Enqueue all courses with an in-degree of 0 (courses with no prerequisites that can be taken immediately).
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0
        
        # Step 3: Process the queue (BFS)
        # Process Queue: Pop a course, increment your count of completed courses, and for each of its dependent courses, decrement their in-degree. If a dependent course's in-degree reaches 0, push it to the queue.
        while queue:
            curr = queue.popleft()
            completed += 1
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Step 4: Check if all courses were completed
        # Result: If the total number of processed courses equals numCourses, all courses can be completed (True). Otherwise, a cycle exists (False).
        return completed == numCourses
            
