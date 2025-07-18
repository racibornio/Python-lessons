def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""
Intro:



Make retail great again through the power of technology! Intellias helps retailers provide consistent and customer-centric shopping experiences across all channels with disruptive retail tech solutions. Get on board and make your own contribution to the industry!


Project Overview:



A global quick-service restaurant (QSR) brand with a franchise-based operational model is embarking on a digital transformation journey to streamline and unify its data and operational landscape across multiple franchisees. The brand operates in highly competitive and fast-paced retail and food service markets, requiring consistent, real-time insights and operational efficiency.
This project focuses on designing and implementing a centralised data integration and reporting platform to address key systemic challenges across the organisation’s franchise network.


Requirements:



Fluent English and outstanding communication skills, both verbal and written 
5–7 years of experience in a Product Owner or Business Analyst role, with a focus on data platforms 
5+ years of hands-on experience with data warehousing (data modeling, ETL, integration flows) 
Strong knowledge of data warehouse tools such as Snowflake, Redshift, or BigQuery 
Familiarity with ETL tools such as Talend, Informatica, or Apache NiFi 
Excellent SQL skills for data analysis, issue investigation, and logic validation 
Proven ability to manage stakeholders, gather and prioritize requirements, and lead solution scoping 
Hands-on mentality and experience operating in fast-paced, Agile environments 
Prior experience in QSR, retail, or franchise-based operating models is highly desirable 




Responsibilities:



Own the end-to-end translation of business requirements into clear data platform specifications 
Serve as the key contact for business stakeholders, source system vendors, and the data engineering team 
Design, document, and validate functional and non-functional data requirements 
Collaborate on the development of logical and physical data models (e.g., star and snowflake schemas) 
Support ETL development by shaping transformation logic and defining integration requirements 
Ensure high-quality, reliable data outputs through validation rules and quality checks 
Analyze data issues, identify root causes, and guide resolution strategies 
Contribute to roadmap planning, backlog prioritization, and delivery tracking within an Agile setup
""")


print(outcome)