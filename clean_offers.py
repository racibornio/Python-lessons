import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """
 Hi, I hope you’re doing well! I wanted to check whether the following opportunity for a Senior Product Manager / Senior Product Owner might be interesting for you.

Offer details:
 Rate: 130–150 PLN/h B2B
 Project for a UK-based client from the Media & Advertising industry

Role description:
 We are looking for an experienced Product Manager / Product Owner to join an existing project and support product development in an Agile environment. The role involves close cooperation with business and technical teams, process analysis and translating business needs into clear product requirements.

Responsibilities:
 • Ownership of product-related topics in an existing project
 • Working closely with stakeholders, business and engineering teams
 • Analyzing business processes and translating needs into product requirements
 • Managing and prioritizing product backlog
 • Supporting Agile delivery and Scrum ceremonies
 • Ensuring clear communication between business and technical teams
 • Supporting decision-making with structured analysis and product insight

Requirements:
 • Experience as a Product Manager / Product Owner
 • Strong knowledge of Agile / Scrum
 • Experience with business process analysis
 • Ability to work closely with technical and business stakeholders
 • Strong communication skills
 • Ownership, proactivity and ability to drive topics forward

Interested?
 Please send your CV using the application link:
https://hrk.traffit.com/public/form/a/926f69f7ae1cfe85fdf71620585ef8745338736a3745413d

If the role is not a perfect fit for you, feel free to share it with someone from your network — I’ll be happy to connect.

Best regards,
Aleksandra Jaczyńska

"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)