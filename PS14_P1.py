class Employee:
  def __init__(self, name, salary):
      self.name = name
      self.salary = salary

  def calculate_bonus(self, bonus_rate):
      bonus = bonus_rate * self.salary
      return bonus

# Create an employee object
employee = Employee("Sam", 50000)

# Enter a bonus rate
bonus_rate = 0.1  # 10% bonus

# Calculate and display the bonus
bonus = employee.calculate_bonus(bonus_rate)
print(f"Bonus for {employee.name} at rate {bonus_rate*100}% is: ${bonus:.2f}")
