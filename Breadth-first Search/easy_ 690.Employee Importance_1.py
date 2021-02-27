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
        Map_idToEmployee = {e.id: e for e in employees}

        def dfs(e_id):
            im_value = Map_idToEmployee[e_id].importance
            if len(Map_idToEmployee[e_id].subordinates) == 0:
                return im_value
            else:
                for a in Map_idToEmployee[e_id].subordinates:
                    im_value += dfs(a)
                    return im_value
        return dfs(id)

        """
            im_value = Map_idToEmployee[id].importance
        if len(Map_idToEmployee[id].subordinates) == 0:
            return im_value
        for i in Map_idToEmployee[id].subordinates:
            im_value += self.getImportance(employees, i)
        return im_value

        """
