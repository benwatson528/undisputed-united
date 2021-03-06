from datetime import datetime
from string import Template

from pandas import Series


def update_readme(match: Series):
    substitutions = {'champion': match.home if match.result == 'H' else match.away,
                     'loser': match.away if match.result == 'H' else match.home,
                     'score': match.score,
                     'render_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                     'match_date': datetime.fromisoformat(match.date).strftime('%A %d %B %Y')}

    with open('data/README.template') as f:
        template = Template(f.read())
        replaced = template.substitute(substitutions)
        with open("../README.md", "w") as output:
            output.write(replaced)
