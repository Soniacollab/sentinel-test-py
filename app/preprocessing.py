def clean_user_input(data: dict) -> dict:
    cleaned_data = data.copy()
    cleaned_data["username"] = data.get("username", "").strip().lower()

    user_score = data.get("user_score", 0.0)
    cleaned_data["user_score"] = float(user_score)

    return cleaned_data
    