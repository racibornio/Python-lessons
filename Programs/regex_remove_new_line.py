def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""

About the job

Company Overview

At Motorola Solutions, we believe that everything starts with our people. We’re a global close-knit community, united by the relentless pursuit to help keep people safer everywhere. Our critical communications, video security and command center technologies support public safety agencies and enterprises alike, enabling the coordination that’s critical for safer communities, safer schools, safer hospitals and safer businesses. Connect with a career that matters, and help us build a safer future.

Department Overview

Motorola Solutions (MSI) is seeking a Senior Software Quality Engineer with expertise in data analytics and software development life cycles (SDLC) to drive quality improvements across Motorola video products, land mobile devices, and infrastructure systems. The ideal candidate will have a strong understanding of software quality processes, process, leading and lagging metrics, and the ability to support defect prediction initiatives. This role requires a proactive leader who excels at identifying critical data, ensuring data integrity, and communicating insights that enhance software quality and development processes.

Job Description

    Software Quality and Process Improvement:
        Collaborate with software engineering teams to integrate quality best practices throughout the SDLC. 
        Define and monitor leading and lagging metrics that measure software process performance and product quality. 
        Identify gaps in the software development process and drive initiatives to mitigate quality escapes. 
    Data Analytics and Defect Prediction:
        Develop data models and reports that provide insights into software defect trends, severity, and risk areas. 
        Support defect prediction efforts by identifying key historical and real-time data points to forecast potential quality risks. 
        Ensure quality data collection processes align with software development milestones and deliverables. 
    Data Integrity and Warehousing:
        Work with data warehousing teams to ensure seamless integration of software quality data from multiple sources. 
        Ensure that data pipelines are accurate, reliable, and aligned with business needs. 
        Build and maintain dashboards using tools such as Power BI, Tableau, SQL, Python, or Excel to support decision-making. 
    Leadership and Cross-Functional Collaboration:
        Lead root cause analysis (RCA) for software defects and quality issues, ensuring lessons learned are fed back into the SDLC. 
        Partner with cross-functional teams, including R&D, testing, and operations, to align quality goals with product roadmaps. 
        Mentor and support junior engineers to strengthen the organization's overall software quality capabilities. 

In return for your expertise, we’ll support you in this new challenge with coaching & development every step of the way. Also, to reward your work you’ll get the following:

    Contract of Employment (UoP)
    Private medical coverage, Multisport
    Life insurance (two annual incomes), 
    Employee Stock Purchase Plan – 15% discount for buying Motorola’s Stock units, 
    Employee Pension Plan – 3,5 % of the month’s salary gross, which goes to the retirement account
    Yearly salary increase (depends on individual performance)
    Yearly bonus (depends on company performance)
    Flexible working hours (usually day starts between 7-10), 
    8 hours working day (30 minutes lunch break included). 
    Hybrid work

Basic Requirements

    Bachelor’s degree in Software Engineering, Computer Science, or related field (Master's preferred). 
    Lean Six Sigma Green Belt or Black Belt certification (or equivalent experience). 
    8+ years of experience in software quality engineering or data analytics roles. 
    Proficiency in data analysis and visualization tools such as SQL, Python, Power BI, Tableau, or Excel. 
    Strong understanding of data warehousing, ETL processes, and data pipelines. 
    Expertise in software quality processes and metrics (e.g., defect density, MTTR, code coverage, and escape rates). 
    Experience with defect tracking and software lifecycle tools (e.g., JIRA, Azure DevOps, or Rally). 
    Experience with data analytics tools (e.g., powerBI, easyBI, Tableau). 

Travel Requirements

Under 10%

Relocation Provided

Domestic

Position Type

Experienced

Referral Payment Plan

Yes

Company

Motorola Solutions Systems Polska Sp.z.o.o

EEO Statement

Motorola Solutions is an Equal Opportunity Employer. All qualified applicants will receive consideration for employment without regard to race, color, religion or belief, sex, sexual orientation, gender identity, national origin, disability, veteran status or any other legally-protected characteristic.

We are proud of our people-first and community-focused culture, empowering every Motorolan to be their most authentic self and to do their best work to deliver on the promise of a safer world. If you’d like to join our team but feel that you don’t quite meet all of the preferred skills, we’d still love to hear why you think you’d be a great addition to our team.


""")


print(outcome)