def get_average_grade(grades_tuple):
    """Return the average of a tuple of grades, or None if empty."""
    try:
        if len(grades_tuple) == 0:
            raise ValueError("Empty grade list")
        return sum(grades_tuple) / len(grades_tuple)
    except Exception as e:
        print(f"Warning: Could not compute average ({e})")
        return None


course_grades = {
    "Math": (90, 85, 88, 92),
    "Science": (78, 81, 74),
    "History": (95, 89),
    "Art": ()  
}

for course, grades in course_grades.items():
    avg = get_average_grade(grades)
    if avg is None:
        print(f"The average grade for {course} cannot be calculated.")
    else:
        print(f"The average grade for {course} is {avg:.2f}")
