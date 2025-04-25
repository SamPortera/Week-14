class Student:
  def __init__(self, first_name, last_name, district_code, enrolled_credits):
      self.first_name = first_name
      self.last_name = last_name
      self.district_code = district_code.upper()  # Ensures code is case-insensitive
      self.enrolled_credits = enrolled_credits

  def compute_tuition(self):
      if self.district_code == 'I':
          tuition_rate = 250.00
      else:
          tuition_rate = 500.00
      return self.enrolled_credits * tuition_rate

# Example test
student1 = Student("Dansby", "Swanson", "I", 12)
tuition1 = student1.compute_tuition()
print(f"{student1.first_name} {student1.last_name} owes ${tuition1:.2f} in tuition.")

student2 = Student("Kyle", "Tucker", "O", 12)
tuition2 = student2.compute_tuition()
print(f"{student2.first_name} {student2.last_name} owes ${tuition2:.2f} in tuition.")
