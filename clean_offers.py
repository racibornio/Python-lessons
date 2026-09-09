import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """

Senior Business Analyst
Company: PRETIUS SOFTWARE SP. Z O.O.
from: 18 August 2026
to: 17 September 2026
110 - 140 złnet (+ VAT)/ hr.B2B contract (full-time)
level:senior
working mode:remote
Warszawa, Włochy
more
Requirements
Expected technologies
Busniness Analysis
Agile
Optional technologies
OneSource Tax
Corporate Tax
Partnership Compliance
Our requirements

    5+ years of experience as a Business Analyst, preferably in technology or business transformation projects.
    Strong experience in requirements gathering, process analysis, and documentation.
    Ability to work effectively across business and technical teams.
    Experience supporting system migrations, platform transformations, or technology modernization initiatives.
    Good understanding of system integrations, data flows, and complex enterprise application landscapes.
    Experience working in Agile delivery environments.
    Excellent communication, analytical, and stakeholder management skills.
    Ability to translate business needs into clear and actionable requirements.

Optional

    Experience with OneSource Tax, including implementation, migration, or support.
    Knowledge of Corporate Tax and/or Partnership Compliance processes.
    Experience with workflow management, workflow transformation, or process automation platforms.
    Background in tax, finance, compliance, or regulatory technology.
    Experience with large-scale enterprise system migrations and modernization programs.

Your responsibilities

    Gather, analyze, and document business and technical requirements.
    Facilitate workshops and collaborate with business and technology stakeholders.
    Analyze, map, and optimize business processes and workflows.
    Support solution design, impact assessments, and implementation activities.
    Analyze system integrations, data flows, and application dependencies.
    Create user stories and manage requirements throughout the delivery lifecycle.
    Support testing, UAT, migration activities, and business readiness.
    Contribute to technology transformation and enterprise system modernization initiatives.

Company
About the project
At Pretius, we are looking for a Senior Business Analyst to support strategic transformation initiatives within Compliance Services. The role requires a strong blend of technical analysis, business process expertise, and stakeholder management skills.
less
What we offer

    We focus on long-term relationships based on fair principles and reliability.
    Co-financing of the Multisport card and Medicover private healthcare.
    Modern office available.
    Team bonding activities, internal courses, conferences, certifications.

Benefits

    sharing the costs of professional training & courses
    flexible working time
    integration events
    video games at work
    parking space for employees
    leisure zone

PRETIUS SOFTWARE SP. Z O.O.
Pretius is a Polish software company founded in 2006 in Warsaw. That's right - we have 19 years of experience in developing dedicated software systems. From the very beginning we have been working with market leaders in need of enterprise solutions. We can boast that as many as 93% of our clients, after completing their first project, either continue working with us straight away or come back after time with new projects. With over 180 specialists on board, we are able to take care of the full range of services - from business analysis, design and development to long-term maintenance. In 2016, we founded our sister company IN Team, specialising in body leasing, and in 2021 the Pretius Low-Code brand was launched.

"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)