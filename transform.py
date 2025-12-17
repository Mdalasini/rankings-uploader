from selectolax.parser import HTMLParser

from models import Team


def transform(html_content: str) -> list[Team]:
    """
    Parse HTML content to extract team rankings data.

    Args:
        html_content: HTML string containing the rankings table

    Returns:
        List of dictionaries with team_name, off_rank, and def_rank
    """
    tree = HTMLParser(html_content)

    # Get the rankings table
    rankings_table = tree.css_first("table#rankings-table")
    if not rankings_table:
        return []

    # Get the tbody
    tbody = rankings_table.css_first("tbody")
    if not tbody:
        return []

    results: list[Team] = []

    # Go through all rows (trs) in tbody
    for row in tbody.css("tr"):
        # Get team_name: Second td -> span.team.fw-bold -> text
        second_td = row.css("td")[1] if len(row.css("td")) > 1 else None
        if not second_td:
            continue

        team_span = second_td.css_first("span.team.fw-bold")
        if not team_span:
            continue
        team_name = team_span.text(strip=True)

        # Get off_rank: Second to last td -> text
        tds = row.css("td")
        if len(tds) < 2:
            continue
        off_rank = tds[-2].text(strip=True)

        # Get def_rank: Last td -> text
        def_rank = tds[-1].text(strip=True)

        results.append(
            Team(team_name=team_name, off_rank=int(off_rank), def_rank=int(def_rank))
        )

    return results
