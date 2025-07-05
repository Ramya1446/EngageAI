# modules/scorer.py

def score_leads(df):
    def get_score(row):
        score = 0
        if "Series A" in row["Funding"]:
            score += 40
        elif "Series B" in row["Funding"]:
            score += 30
        elif "Seed" in row["Funding"]:
            score += 20
        elif "Bootstrapped" in row["Funding"]:
            score += 10

        if row["Employees"] > 100:
            score += 30
        elif row["Employees"] > 50:
            score += 20
        else:
            score += 10

        if "AI" in row["Industry"]:
            score += 20
        elif "Fintech" in row["Industry"]:
            score += 15
        elif "Healthcare" in row["Industry"]:
            score += 10

        return min(score, 100)

    def get_lead_temp(score):
        if score >= 80:
            return "🔥 Hot Lead"
        elif score >= 50:
            return "🌤️ Warm Lead"
        else:
            return "❄️ Cold Lead"

    df["Priority Score"] = df.apply(get_score, axis=1)
    df["Lead Temperature"] = df["Priority Score"].apply(get_lead_temp)

    return df
