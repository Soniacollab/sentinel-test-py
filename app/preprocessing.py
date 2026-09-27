def clean_user_input(data: dict) -> dict:
    cleaned_data = data.copy()
    cleaned_data["username"] = data.get("username", "").strip().lower()

    user_score = data.get("user_score", 0.0)
    value = user_score
    if value is None or value == "":
        cleaned_data["user_score"] = 0.0
    else:
        cleaned_data["user_score"] = float(value)

    return cleaned_data
    