def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""
Who we are looking for

We are looking for a passionate Junior Business System Analyst (BSA) with a technical background to join Deloitte's Cloud Integration practice, where you will contribute to delivering state-of-the-art integration solutions for our clients.

To be successful in the interview you must have at least: 

computer science studies or at least 1 year of experience on similar position
business requirements gathering
documentation preparation
test cases preparation (scenarios, data quality)
test plans and test cases execution
ETL/ELT reverse engineering, including SQL code
data structures and data analysis
at least basinc understanding of data modelling concepts and ETL/ELT processes
at least medium knowledge of SQL
analytical thinking, detail oriented, problem solving mindset
EU Work Permit

Your future role

Gathering and analyzing business and technical requirements 
Assisting in system design and writing technical documentation 
Collaborating with developers, QA engineers, DevOps, and product owners 
Supporting system logic validation and reviewing data/integration flows 
Creating diagrams (process, data flow, architecture) to visualize system behavior. 

What we offer

Flexible working hours,
Permanent employment or contract,
Medical and health insurance,
Multisport and other lifestyle benefits,
Language courses,
Friendly coworkers & team spirit,
Multiple geographies and clients,
Work for well-known brands,
Exposure to trailblazing business and technology projects,
A place in the first line of a digital transformation,
Everyday opportunities to influence how and where we do our business,
A development path to fit your needs.

Selection process

We kindly ask you to upload your CV in English.

Shortlisted candidates will be contacted for the interviewing process.

If your CV would be interesting for us there will be a few steps:

 Quick HR call or meeting;
 One or two HR and technical interviews with our colleagues from the respective team;
 Final decision.

About Deloitte

Deloitte is a variety of people, experience, industries and services we deliver in 150 countries of the world. It is an intellectual challenge, a good starting point for your career, and an excellent opportunity for continuous development and gaining valuable life experiences. What you only must do is to take the first step - press the apply button and send us your CV, go through all the stages of the recruitment process and sign a contract with us. Deloitte is simply your best choice.

About the team

Our Cloud Engineering teams design and deliver interesting cloud projects for clients in Poland and abroad in areas of cloud development, DevOps, integration, migration, data management, infrastructure and others. We help our clients to strategize, design and implement and migrate solutions with use of modern cloud technologies.
""")


print(outcome)