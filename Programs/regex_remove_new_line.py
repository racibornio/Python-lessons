def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""
What are the key objectives and expectations from this role?  
We are looking for an experienced Business/Software Analyst that will be responsible for fleshing out mobile application requirements within the end-to-end vision and roadmap of Product Owner/Product Manager. This role main area of focus will be performing detailed requirement analysis, documenting requirements and business processes. The Business/Software Analyst will work closely primarily with the Global Product Owner/Product Manager. This position requires perfect communication skills as it involves multiple stakeholders. To succeed in this role, the candidate must also have solid technical background, vast experience in agile software development but also strong soft skills such as ability to clearly express ideas, critical-thinking and negotiation.

What is the direct impact of this role on the team or organization? 

End-to-end ownership of requirements traceability. Accountable over what should have been documented and where, ensuring proper control processes are in place and the requirements are always up to date. Lead the process of eliciting requirements which includes engaging with various departments regularly to get al inputs needed to complete the analysis.  


Reports to	Global Product Owner
Number of Direct Reports 	N/A
Core Relationships	Internal – Global consumer experience teams (eCommerce, CRM, loyalty), legal, IT security, marketing brand teams, key stakeholders in region and end-markets. 
External – Number of partners supplying delivery with focus on design and delivery leads, scrum master team, D2C DevOps teams
Geographic Scope  	Global 
Travel Required	Max 5% of the time in relevant project workshops

ACCOUNTABILITIES 
(please provide a list of typical accountabilities to be performed. Please avoid unfamiliar acronyms, project names or BAT jargon and ensure terminology is external market friendly. Please prioritise the most critical accountabilities and reflect them within the first 8 points)  
•	Elicit and document business requirements with stakeholders using a range of techniques, conducting feasibility studies, usability, requirements, risk, cost and value analysis
•	Identify and obtain agreement on the requirements / features which will be most beneficial to the business and to the end consumer
•	Responsible for translating business requirements into user stories with clear acceptance criteria, capturing these in the Product Backlog and own Backlog Refinement sessions. 
•	Provide ad-hoc business analysis and process mapping documentation when required to technical/non-technical stakeholders
•	Collaborate with all stakeholders and team members in the software development process and business units (e.g., R&D, Product Development, Legal, Marketing) to get all the inputs required to complete requirements analysis 
•	Identifying and raising issues, process or scope gaps and recommend solutions/mitigations 
•	Pro-actively optimize WoW and contribute to agile ceremonies – sprint daily, planning, retrospective and review 

EXPERIENCE, SKILLS, KNOWLEDGE
ESSENTIAL (please provide only criteria considered to be ‘must haves’)

Experience Required
(Please put the most critical information in the first 2 points
•	Proven experience in building complex solutions from scratch,
•	Proven experience in building Mobile Apps (Native/PWA) or at least customer-facing solutions,
•	Proven experience in system integration,
•	Proven experience in product delivery from inception to maintenance
•	Vast experience in requirements documentation, decomposition and backlog preparation
•	Extensive experience in planning business analysis works, activities and deliverables within complex projects
•	Experience in complex organization on a global scale

Technical / Functional / Leadership Skills Required
(Please put the most critical information and reflect it in the first 4 points) 
•	Mobile app delivery
•	Delivery of high quality specification
•	Familiarity with system integrations and architecture patterns
•	Understanding of XML and JSON structures, REST and SOAP
•	Senior stakeholders management (relationship and expectations)
•	Have experience in Data Privacy by design
Education / Qualifications / Certifications Required
(Please put the most critical information and reflect it in the first 2 points) 
•	University degree
•	5+ years of relevant professional experience


BENEFICIAL (please provide a maximum of 3 criteria that would be deemed ‘useful to have’ but not essential)
•	Any agile certification
•	Any business analysis certification
QUALIFYING QUESTIONS FOR APPLICANTS
(Helping the right candidates to apply is critical. Please provide up to 3 questions that a job seeker can use to self-assess their suitability. 
These questions should be answerable with ‘yes or no’ and will feature when the role is being advertised e.g. Do you have recent experience in…? Do you have knowledge of…? Are you familiar with…? Have you worked in…? Have you used…? Do you have...?)
•	Do you have experience in building complex solutions from scratch?
•	Do you have experience in system integration?
•	Do you have experience in complex backlog management?
•	Do you have experience in building Mobile Apps (Native/PWA) or at least customer-facing solutions?
•	Do you have specific consumer-facing platform development experience, where you had a significant contribution to the technology decisions and use case delivery?
•	Do you have experience in multiple stakeholders management? 
•	Do you have experience in working with development & UX/UI through multiple third-party suppliers?

""")


print(outcome)