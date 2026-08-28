import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """
Opportunity for Product Owner in Krakow, Poland (Hybrid) - 3 Days WFO mandatory
Hi Patryk ,
Hope you are doing well.

I recently came across your profile and was impressed by your expertise. We are currently seeking Product Owner to join our team in Krakow, Poland (Hybrid)- 3 Days WFO mandatory and it's a Contract role. 

We are seeking a highly experienced and strategic Product Owner to lead product development initiatives across multiple teams and functions. The ideal candidate will bring deep expertise in Artificial Intelligence, Financial Products, and Agile methodologies, with a strong focus on user-centric design, innovation, and continuous improvement & STAKEHOLDER MANAGEMENT

Key Responsibilities: 
Own the full product lifecycle: discovery, idea evaluation, roadmap creation, implementation, and feedback gathering. 
Collaborate across cross-functional teams to ensure alignment and delivery of product goals. 
Define long-term product vision and translate it into actionable roadmaps. 
Prioritize features and functionalities based on user needs, business value, and technical feasibility. 
Manage and refine product backlogs, ensuring clarity and alignment with business objectives. 
Interpret business requirements and translate them into detailed technical specifications. 
Identify commonalities across platform tenants and define appropriate customizations. 
Engage with stakeholders at all levels to gather feedback and drive product decisions. 

Required Skills & Qualifications:
10+ years of experience in product ownership or product management. 
Proven experience managing complex project backlogs. 
Deep understanding of Agile methodology and software development lifecycle. 
Proficiency in Microsoft Office tools and Copilot. 
Working knowledge of GitLab and SQL. 
Experience with AI technologies and financial product development (preferred). 

If you're interested please share me a copy of your updated resume.

Thanks and Regards,
Deeksha
Engineering Recruiter
📞 +44 2080 950 384
✉️ deeksha@ixceed-solutions.com
🌐 www.ixceed-solutions.com
"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)