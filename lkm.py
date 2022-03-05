from datetime import date, timedelta

MONDAY_REMINDER_STR = "Happy Monday @lingokilometrenos! Please fill in your results for this period ({period}) by end of day today. I'll announce results tomorrow morning. :slightly_smiling_face: Any questions, let me know!"


RESULTS_STR = """
And the results are in! :abacus:

For the period starting {period}, we got {num_full_achievements} goal achievements! :star2::star2::star2::star2::star2::star2::star2::star2::star2::star2::star2::star2:

Hats off to {full_achievers} for hitting your goals! :raised_hands:

Partial achievements from {partial_achievers}. :thumbsup:

Special mentions to {special_mentions}! :smile::raised_hands:
"""

SPECIAL_MENTION_STR = "{achiever} for {gendered_possessive} {ordinal} star"


def get_period(relative_weeks=0):
    today = date.today()
    period_start = today + timedelta(days=7*relative_weeks-today.weekday())
    return period_start.strftime('%d/%m')


def monday_reminder():
    period = get_period(relative_weeks=-1)
    print(MONDAY_REMINDER_STR.format(period=period))


monday_reminder()
