def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""
About the job
Location: 100% remote or hybrid - you choose. You are always more than welcome to work from our offices located in Warsaw or Krakow
Salary: B2B, 14.000 - 24.000 PLN net + VAT
Expected start date: as soon as possible




Join our Team as Business System Analyst !
We are looking for a person who understands business needs very well and will cooperate closely with Business Users to define business requirements and with delivery team to design optimal solution and ensure that project will deliver business value.
Experience, partnership, and desire for continuous development - it's our DNA.



What makes you a great fit?

5+ years of experience in Business and System analysis in Data/AI
Experience with gathering and documenting requirements and designing & documenting final solution
Experience in Data Analysis & Data Modeling
Ability to cooperate effectively with Stakeholders from different levels of the organizational structure: from TOP management to operational level
Ability to understand different solution architecture models and diagrams
Can-do and problem-solving attitude to advise customer in the best possible way
Goal-oriented attitude and proactiveness
Customer focus approach to work
Fluent English


Nice to have

SQL
Power BI
Tools for designing business processes, mockups and data models
Awareness of business area specific such as: Finance & Controlling, Sales & Marketing, Supply chain, Production


What will you do?

--> Project Delivery Area

Analyzing data sources and designing optimal data models
Creating and proposing a final solution to the Client, e.g. in the form of ready-made Power BI report mockups
Identifying business needs and business goals to define project scope/product Roadmap
Preparing and conducting presentations targeted to the different groups of the audience
Collecting functional and non-functional requirements
Verifying existing business processes and identifying potential improvements and enhancements
Building Project Backlogs, especially defining Epics and User Stories
Preparing Tests Plans and testing developed solutions
Analytical documentation management
--> Business Development

Direct cooperation with the client in creating Business Intelligence solutions and business apps.
Close cooperation with the architects in the design phase
Close cooperation with the developers in the implementation of the project
Supporting Project Owner in project management or the possibility of project coordination in the SCRUM / AGILE method


Our benefits:

Knowledge Sharing: Collaborate with top industry professionals, exchange innovative ideas, and make your voice heard. Your insights matter here.
Development Budget: Invest in your growth with us. Choose the conferences, training sessions, or certifications that best suit your career path.
Hardware of Your Choice: Work with the best tools. Choose the equipment that helps you perform at your peak.
Flexible Hours: Whether you’re an early bird or a night owl, we offer flexible hours to fit your lifestyle and maximize your productivity.
Remote Work: Enjoy the freedom to work from home or any location that suits you, while maintaining a healthy work-life balance.
Leader’s Support: Our leaders are here to support you. Just ask for guidance or feedback whenever you need it.
Project Bonuses: Celebrate your successes with us. Receive bonuses for outstanding project achievements.
Social Events: Join in the fun! Participate in various social events and sports activities with your colleagues.
Health Insurance: Your well-being is our priority. Benefit from comprehensive health insurance coverage.
Comfy Office in a Great Locations: Work in a comfortable, ergonomic office located in the heart of the city, designed to inspire creativity and collaboration.
Relaxed Atmosphere: Experience a flat organizational structure with no dress code. Join a team of talented, down-to-earth professionals.
Up to 6000 PLN for Employee Recommendations: Help us grow our team and earn up to 6000 PLN for successful employee referrals.
""")


print(outcome)