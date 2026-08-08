import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """
Hi Patryk,
I hope you’re doing well.
We currently have an opportunity for a Senior Business Analyst with the following details:
Position Type: Contract
Location: Warsaw, Poland - Hybrid

If you’re interested, please share your updated CV at tushar.s@i-q.co

Position Summary
 We are seeking an experienced Senior Business Analyst to join our product development
 organization responsible for delivering enterprise software solutions hosted on Microsoft
 Azure This role serves as the critical bridge between business stakeholders product
 management architecture engineering and operations teams to ensure business needs are
 translated into high quality scalable and secure software solutions
 The Senior Business Analyst works closely with Product Managers Product Owners
 Engineering Leads Solution Architects UX Designers and development teams to define
 product capabilities document requirements improve business processes and drive
 successful delivery outcomes
 The ideal candidate combines strong business analysis expertise experience working within
 Agile software delivery teams a solid understanding of cloud based applications and working
 knowledge of Artificial Intelligence AI technologies and AIenabled business solutions

Tushar Sam
Technical Recruiter | Hiring Engineers & Product Talent | Scaling High-Impact Tech Teams FOR Poland - Europe AND UK
"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)