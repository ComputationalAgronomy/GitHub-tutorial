def get_grade_label(score):
    if score < 0 or score > 100:
        return "Invalid"

    # TODO: complete if/elif/else blocks
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "TODO"
