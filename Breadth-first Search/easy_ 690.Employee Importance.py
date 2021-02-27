"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        im_value = 0
        queue = [id]
        Map_idToEmployee = {e.id: e for e in employees}
        while queue:
            leader = queue.pop(0)
            im_value += Map_idToEmployee[leader].importance
            queue.extend(Map_idToEmployee[id].subordinates)
        return im_value


"""
【discription BFS solution】
im_value = 0
queue = [id]
use hash map to query the employ quicky : Map_idToEmployee = {employee.id -> employee}
while queue:
    leader = queue.pop
    im_value += employees[leader].important
    for employees in employees[id].subordinates:
        put the employees id in the queue
        add employees value to the im_value

return im_value
    
"""
