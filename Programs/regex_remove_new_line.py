def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""


We are a part of ASTEK Group, which has been gathering experience in the global consulting and engineering services market since 1988. ASTEK Group is a global player in engineering and technology consulting, present on 5 continents. 

What do we learn from other Group entities in our daily work? First and foremost: inspiration, objectives, good practices, innovative activities and values. In 2020, 2021, 2022 and 2023 we received the Great Place to Work certificate, and found ourselves among the 15 Best Workplaces in Poland in the category: large companies. 


Our Client is is the world’s largest biotech company, with truly differentiated medicines in oncology, immunology, infectious diseases, ophthalmology and diseases of the central nervous system. The Client is also the world leader in vitro diagnostics and tissue-based cancer diagnostics, and a frontrunner in diabetes management.


How about joining ASTEK Polska’s community of BI Reporting Specialist?


Salary: 

    up to 525 PLN net + VAT/MD (B2B) depending on your professional experience (0,5 FTE)
    up to 9,250 PLN gross/month (contract of employment; 0,5 FTE)


Work model: 

    Remote FROM POLAND
    0,5 FTE


About the project: 

PDG Analytics Platform project, under DASOS Disease Area & Study Operational Strategy Product. The PDG Analytics Platform combines internal and external data sources into a data management cloud that can be accessed through a number of analytical applications.


Your day-to-day responsibilities include: 

    Conducting data analysis using tools such as SQL, DBT, Airflow or Talend to support data-driven initiatives and integration projects.
    Creating and maintaining high-quality technical documentation to ensure clarity and alignment across global, cross-functional teams.
    Collaborating with stakeholders from both technical and non-technical backgrounds, ensuring effective communication of complex data concepts.
    Participating in agile ceremonies and contributing to the continuous improvement of team workflows and deliverables.
    Ensuring adherence to data and requirements engineering standards (e.g. IREB) while working independently in a fast-paced, multicultural environment.


You’re ideal for this role if you have: 

    At least 5 years of experience with Business Objects XI (Web Intelligence, Desktop Intelligence, Crystal Reports,
    Designer, Information design Tool, Xcelcius, etc) or Tableau Software (Tableau Desktop)
    Experience in data analysis e.g. DBT/Airflow, Talend
    Wide knowledge of data warehousing concept
    Very good knowledge of data modeling and data warehouse modeling
    Knowledge of ETL tool
    Good knowledge of SQL
    Ability to communicate effectively
    Fluent English in writing and speech
    5+ years of experience in at least one of the following reporting tools: Tableau, Tibco Spotfire SSRS, SAP BO
    At least 2- years of experience in design and usability in BI
    Ability to design and prototype BI solutions based on business requirements
    Be able to give realistic estimates, possibly with collaboration with other BI developers
    Know what is the best testing strategy for the given BI solution
    Ability to negotiate and discuss possible BI solutions with the stakeholders based on available toolset and knowledge
    Be open to customization of the standard BI tools, know how to approach this topic, be able to say all the pros and cons of standard versus custom BI solution for a given case, give the reasoning to the stakeholders
    Be ready to defend the designed solution architecture to the architects board
    Be aware of how the Infrastructure Team works, especially when it comes to BI solutions, what are the main environments that can be used, how to request them, etc.


Your personality: 

    You are a team player 
    You are focused on long-term cooperation 
    You easily adopt to changes 


Added value for you: 

    Long-term cooperation and long-term projects
    Possibility to choose preferred type of cooperation (regular job contract with all benefits or flexible B2B contract) 
    Technical trainings, certificates and upskilling 
    Competence Center mentoring - you will be a member of CC community from the first day of your work. You’ll have a chance to develop your skills, participate in various conferences and share your knowledge and experience with people who face the same challenges in their daily work 
    Clear career path 
    Employee benefits package 
    Friendly work atmosphere, social events and team-building meetings 


Need more information? Contact me: olga.lefelbajn@astek.net 

It’s not about you? Recommend us your friend and get a bonus up to 7,000 PLN Link: https://astek.pl/system-rekomendacji/ 


No ref: AO194576


""")


print(outcome)