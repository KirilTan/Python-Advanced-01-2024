def gather_credits(credits_needed: int, *course_credits: tuple) -> str:
    credits_gathered = 0
    courses_taken = []

    all_courses = {course_name: course_credits for course_name, course_credits in course_credits}

    for course_name, course_credits in all_courses.items():
        if credits_gathered < credits_needed:
            courses_taken.append(course_name)
            credits_gathered += course_credits

        if credits_gathered >= credits_needed:
            break

    if credits_gathered >= credits_needed:
        courses_taken.sort()
        return (f'Enrollment finished! Maximum credits: {credits_gathered}.\n'
                f'Courses: {", ".join(courses_taken)}')
    else:
        credits_shortage = credits_needed - credits_gathered
        return f'You need to enroll in more courses! You have to gather {credits_shortage} credits more.'


print(gather_credits(80, ("Basics", 27)))
print()
print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27)))
print()
print(gather_credits(60, ("Basics", 27), ("Fundamentals", 27), ("Advanced", 30), ("Web", 30)))
print()