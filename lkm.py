from sheets import load_sheet

from datetime import date, timedelta

FULL = '🌟'
PARTIAL = '🌗'
NONE = '🌑'

MONDAY_REMINDER_STR = "Happy Monday @lingokilometrenos! Please fill in your results for this period ({period}) by end of day today. I'll announce results tomorrow morning. :slightly_smiling_face: Any questions, let me know!"


RESULTS_STR = """
And the results are in! :abacus:

For the period starting {period}, we got {num_full_achievements} goal achievements! :star2::star2::star2::star2::star2::star2::star2::star2::star2::star2::star2::star2:

Hats off to {full_achievers_str} for hitting your goals! :raised_hands:

Partial achievements from {partial_achievers_str}. :thumbsup:

Special mentions to {special_mentions_str}! :smile::raised_hands:
"""

SPECIAL_MENTION_STR = "{achiever} for {gendered_possessive} {ordinal} star"


def get_period(relative_weeks=0):
    today = date.today()
    period_start = today + timedelta(days=7*relative_weeks-today.weekday())
    return period_start.strftime('%d/%m')


def get_special_mentions_str(special_mentions):
    return ', '.join(
        SPECIAL_MENTION_STR.format(special_mention)
        for special_mention in special_mentions
    )


def print_monday_reminder():
    period = get_period(relative_weeks=-1)
    print(MONDAY_REMINDER_STR.format(period=period))


def get_period_results(period):
    sheet_rows = load_sheet()

    first_row = next(sheet_rows)
    period_index = first_row.index(period)

    next(sheet_rows)

    full_achievers = []
    partial_achievers = []

    while True:
        name = next(sheet_rows)[0]
        if not name:
            break

        next(sheet_rows)
        next(sheet_rows)
        char = next(sheet_rows)[period_index]

        if char == FULL:
            full_achievers.append(name)
        if char == PARTIAL:
            partial_achievers.append(name)


    special_mentions = []

    return full_achievers, partial_achievers, special_mentions


def print_results():
    period = get_period(relative_weeks=-1)

    num_full_achievements = 0
    full_achievers, partial_achievers, special_mentions = \
        get_period_results(period)
    special_mentions_str = get_special_mentions_str(special_mentions)

    print(RESULTS_STR.format(
        period=period,
        num_full_achievements=num_full_achievements,
        full_achievers_str=', '.join(full_achievers),
        partial_achievers_str=', '.join(partial_achievers),
        special_mentions_str=special_mentions_str
    ))


print_monday_reminder()
print_results()
