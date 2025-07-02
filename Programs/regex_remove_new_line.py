def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""
As IT Business Analyst, you will be part of the Global Custom Software Solutions team in Poland, building PPG’s backbone for Digital Commerce. You will be responsible in identifying, defining, and documenting business and stakeholder requirements. To successfully perform this role, the applicant must be able to communicate solutions to technical and non-technical stakeholders, analyze customer needs and created detailed user stories and requirements for their development team, and assist in driving adherence to agile and scrum standards.

Work model: Hybrid

Location: Wrocław


Key Responsibilities:

    Analyze product owner feedback to drive and create user stories and requirements for the development team to action.
    Build strong and detailed acceptance criteria ensuring understanding of expectations across all team members.
    Work closely with SQAs to review and approve test cases and validate test results.
    Adapt and develop effective working relationships across a diverse team of multiple functional, technical, and business partners.
    Work with the members of the development team following scrum and Agile principles to ensure consistent delivery.
    Explain and communicate technical solutions to technical and non-technical stakeholders
    Leverage AI Tools for Requirements Analysis and Documentation
    Utilize problem-solving skills for evaluating multiple approaches to find the most feasible solutions.
    Provide a high level of commitment to delivering high quality work in a dynamic and fast paced environment.
    Utilize Azure DevOps as the source for project and development documentation to ensure efficiency.
    Assess, document, and manage requirements changes, improvements and enhancements
    Proactively Participate in processes improvement, sharing best practices and proactively suggesting improvement points
    Promote AI-Driven Practices Within the BA Community
    Strong oral and written communication skills



Qualifications:

    Bachelor's Degree or higher in Computer Science, Management Information Systems or related field
    Minimum 6 years of experience in Business Analyst or similar role
    Previous experience in an environment using Agile development methodology
    Good Understanding of software development lifecycle
    Experience using AI-powered tools to support analysis, documentation, and decision-making tasks
    Ability to understand complex business problems and translate it to IT language
    Structured, process driven, pragmatic problem solver approach
    Good communication skills
    Creative approach to problem-solving
    Experience with working in a multicultural environment
    Ability to effectively present information in one-on-one and small group situations to customers, clients, and other employees of the organization.
    Fluent in English

PPG pay ranges and benefits can vary by location which allows us to compensate employees competitively in different geographic markets. PPG considers several factors in making compensation decisions including, but not limited to, skill sets, experience and training, qualifications and education, licensure and certifications, and other organizational needs. Other incentives may apply. 
 
Our employee benefits programs are designed to support the health and well-being of our employees. Any insurance coverages and benefits will be in accordance with the terms and conditions of the applicable plans and associated governing plan documents.
 
About us:

Here at PPG we make it happen, and we seek candidates of the highest integrity and professionalism who share our values, with the commitment and drive to strive today to do better than yesterday – everyday.

PPG: WE PROTECT AND BEAUTIFY THE WORLD™
Through leadership in innovation, sustainability and color, PPG helps customers in industrial, transportation, consumer products, and construction markets and aftermarkets to enhance more surfaces in more ways than does any other company.. To learn more, visit www.ppg.com and follow @ PPG on Twitter.

The PPG Way
Every single day at PPG:
We partner with customers to create mutual value.
We are “One PPG” to the world.
We trust our people every day, in every way.
We make it happen.
We run it like we own it.
We do better today than yesterday – everyday.

PPG provides equal opportunity to all candidates and employees. We offer an opportunity to grow and develop your career in an environment that provides a fulfilling workplace for employees, creates an environment for continuous learning, and embraces the ideas and diversity of others. All qualified applicants will receive consideration for employment without regard to sex, pregnancy, race, color, creed, religion, national origin, age, disability status, marital status, sexual orientation, gender identity or expression. If you need assistance to complete your application due to a disability, please email recruiting@ppg.com.

PPG values your feedback on our recruiting process. We encourage you to visit Glassdoor.com and provide feedback on the process, so that we can do better today than yesterday.
Benefits will be discussed with you by your recruiter during the hiring process.
""")


print(outcome)