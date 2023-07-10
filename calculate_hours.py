""" example of a function to calculate hours in Python """
""" provided by Bard Google AI 7/10/2023 - 12:26PM """

def calculate_hours(minutes):
  """ Calculates the number of hours in a given number of minutes
  Args:
    minutes: The number of minutes to calculate the hours for

  Returns:
    The number of hours in the given number of minues"""

hours = minutes // 60
minutes_remainder = minutes % 60

return hours, minutes_remainder

if __name__ == "__main__":
  minutes = 120
  hours, minutes_remainder = calculate_hours(minutes)
  print(f"There are {hours} hours and {minutes_remainder} minutes in {minutes} minutes.")


# doesn't run as created, though did provide decent functions to calculate hours and minutes_remainder
# 7/10 - still stuck on C, will take another crack soon
