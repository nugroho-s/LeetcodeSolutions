class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = {}
        for task in tasks:
            if task in task_map:
                task_map[task] = task_map[task] + 1
            else:
                task_map[task] = 1
        frequencies = list(task_map.values())
        max_frequency = frequencies.count(max(frequencies))
        return max((n + 1) * (max(frequencies) - 1) + max_frequency, len(tasks))
