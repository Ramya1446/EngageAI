# modules/strategy.py

def generate_strategy(df):
    def get_best_channel(row):
        # Logic based on company size or tech
        if row["Employees"] > 100:
            return "Email"
        elif "AI" in row["Industry"]:
            return "LinkedIn"
        else:
            return "Twitter DM"

    def get_best_time(row):
        if row["Employees"] > 100:
            return "Tuesday 10 AM"
        elif row["Employees"] > 50:
            return "Wednesday 11 AM"
        else:
            return "Thursday 3 PM"

    def get_cta(row):
        if "AI" in row["Industry"]:
            return "Invite to webinar"
        elif row["Employees"] > 100:
            return "Book a demo"
        elif "Bootstrapped" in row["Funding"]:
            return "Download free guide"
        else:
            return "Try free trial"

    def get_hook(row):
        return f"Noticed you're in the {row['Industry']} space — looks like a great fit for what we offer!"

    def get_followup(row):
        return "Follow up after 3 days if no reply."

    df["Best Channel"] = df.apply(get_best_channel, axis=1)
    df["Best Time to Reach"] = df.apply(get_best_time, axis=1)
    df["Suggested CTA"] = df.apply(get_cta, axis=1)
    df["Hook Line"] = df.apply(get_hook, axis=1)
    df["Follow-Up Advice"] = df.apply(get_followup, axis=1)

    return df
