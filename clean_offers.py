import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """




Hello Patryk! 
Andersen is looking for a 𝐒𝐲𝐬𝐭𝐞𝐦 𝐀𝐧𝐚𝐥𝐲𝐬𝐭 with PO experience for a large insurance and fintech product ecosystem. If you enjoy combining system analysis, product ownership, stakeholder communication, and Agile delivery, this could be a great fit. Interested? 

Wednesday
View Yana’s profileYana Ivanova
Yana Ivanova   12:41 PM
Hi Patryk,

Thanks for connecting! I came across your profile and thought you might be a great fit for a 𝐒𝐲𝐬𝐭𝐞𝐦 𝐀𝐧𝐚𝐥𝐲𝐬𝐭 role we’re currently hiring for. 

𝐀𝐛𝐨𝐮𝐭 𝐭𝐡𝐞 𝐩𝐫𝐨𝐣𝐞𝐜𝐭 
You'll join a large product environment in the insurance and fintech domain. Several Agile teams are already delivering integration solutions, while new teams are building strategic products. The focus is on developing a central integration layer that connects multiple platforms, partner systems, and customer-facing services. 

𝐘𝐨𝐮𝐫 𝐫𝐨𝐥𝐞 
This role combines System Analysis and Product Ownership. You'll gather and document requirements, create user stories and acceptance criteria, model business processes with BPMN and UML, refine backlog items, and support solution design. You'll also align stakeholders, facilitate discussions, manage priorities, validate delivered functionality, monitor product goals, and help drive continuous improvement across Agile teams. 

Here’s a quick look at the role: https://people-andersenlab.com/vacancy/2509956?utm_source=SA&utm_campaign=recruiter
 
And this is a bit about us as a company: https://people.andersenlab.com/useful-links-andersen 

𝐖𝐡𝐲 𝐀𝐧𝐝𝐞𝐫𝐬𝐞𝐧 
At Andersen, you'll work on international products, collaborate with a strong analyst community, and gain access to mentoring, internal training, certification reimbursement, and clear career growth opportunities. We support both expert and leadership development while providing project stability and a comprehensive benefits package. 

Would you be open to discussing this opportunity further?

Today
View Yana’s profileYana Ivanova
Yana Ivanova   12:46 PM
👏
👍
😊



Hello Patryk! Are you interested in the proposed vacancy? 



"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)