def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""
Who we looking for?

We are looking for an experienced Requirements Engineer to join our team. You will work for the customer from energy sector.

In this role, you will be responsible for gathering and management of the requirement, creating, maintaining, and improving documentation for our hybrid cloud platform services. Requirements engineers work closely with software developers, product managers, and other stakeholders to ensure that all specifications are accurate, and comprehensive.

 

Profile Requirements:

    Minimum 5 years of experience as a business / system analyst / requirements engineer in a software development environment;
    Excellent written and verbal communication skills in English (C1);
    Experience with business processes modelling, data model design;
    Experience in user stories, use cases analysis;
    Knowledge of UML and BPMN;
    Strong understanding of software development processes and methodologies, including Agile and DevOps;
    Ability to understand complex technical concepts and translate them into clear, concise specifications;
    Experience with documentation tools such as Confluence, Jira, and other documentation platforms;
    Ability to work independently and manage multiple tasks and projects simultaneously;
    Collaborative, with an ability to work in cross-functional teams;
    Strong soft and presentation skills.

 

Nice to have Competencies/Skills:

    Familiarity with cloud platforms, particularly hybrid cloud environments;
    Familiarity with containerization and container management with Kubernetes;
    Knowledge of API documentation standards and best practices;
    Experience with version control systems such as Git;

 

What’s in it for you?

    100% remote or hybrid working mode;
    Courses and certifications e.g. Google Cloud, AWS, ITIL;
    Wellbeing programs & work-life balance - integration and passion sharing events;
    Private medical and dental care;
    Benefits platform – shopping, cinema, sport etc.;
    Co-funding of sport activities, e.g. Multisport & OK system cards, b-active program;
    Conferences and Expert Communities;
    Gift packages for special occasions: Easter, Christmas, Children’s Day;
    Appreciation for seniority: additional days off, Atos Jubilee gifts;
    Charity and eco initiatives.

 

What happens next?

    Quick conversation with HR;
    Interview with a Manager/IT expert/project representative;
    Work like you want: remotely, in hybrid mode or at our office.

""")


print(outcome)