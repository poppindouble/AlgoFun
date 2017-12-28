class Employee:
	def __init__(self, id, importance, subordinates):
		self.id = id
		self.importance = importance
		self.subordinates = subordinates

	def __repr__(self):
		return "id: {0}, importance: {1}, subordinates: {2}".format(self.id, self.importance, self.subordinates)

	def __str__(self):
		return "id: {0}, importance: {1}, subordinates: {2}".format(self.id, self.importance, self.subordinates)		

class Solution:
	def getImportance(self, employees, id):
		leader = self.__findEmployees__(employees, id)
		if not leader.subordinates:
			return leader.importance
		result = leader.importance
		for subordinate in leader.subordinates:
			result += self.getImportance(employees, subordinate)
		return result

	def __findEmployees__(self, employees, id):
		for employee in employees:
			if employee.id == id:
				return employee

def main():
	employee1 = Employee(1, 15, [2])
	employee2 = Employee(2, 10, [3])
	employee3 = Employee(3, 4, [6, 10])
	employee6 = Employee(6, 2, [])
	employee10 = Employee(10, 1, [])
	employees = [employee1, employee2, employee3, employee6, employee10]
	print(Solution().getImportance(employees, 1))

if __name__ == "__main__":
	main()
