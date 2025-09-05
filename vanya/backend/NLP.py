#story or report LLM
def make_story(detections):
    humans = sum(1 for d in detections if d["class"] == "person")
    vehicles = sum(1 for d in detections if "car" in d["class"] or "truck" in d["class"])
    animals = sum(1 for d in detections if d["class"] in ["elephant", "zebra", "rhino"])

    if humans or vehicles:
        return f"⚠️ {humans} humans and {vehicles} vehicles spotted in protected area. Possible poaching risk."
    elif animals:
        return f"🦓 {animals} animals observed. Wildlife activity normal."
    else:
        return "✅ No unusual activity detected."
