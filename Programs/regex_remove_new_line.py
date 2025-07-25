def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""
The client is an American multinational association that is involved in the design, development, manufacturing, worldwide marketing, and sales of apparel, footwear, accessories, equipment, and services. The company is a proven leader in its industry and is constantly working to create innovative products and services.

The project is about using a full price sales performance to predict value marketplace behaviour. There is a team of Data and Machine Learning engineers who develop the product using different ML models and data from different sources for tranings.

Requirements

You are an experienced Product / Data Analyst. You enjoy working at the intersection of data and business, gathering and refining requirements from stakeholders, and collaborating with engineering teams to ensure successful project delivery. You have a proven ability to translate business needs into actionable data solutions and to ensure these solutions have real business impact. You thrive in dynamic environments, are curious, and enjoy working in cross-functional teams.


5+ years of experience in data analysis, business analysis, or a related role.
A bachelor’s or master’s degree in a relevant field such as Computer Science, Data Science, Engineering, or Business Analytics.
Strong SQL skills (must have).
Proficiency in Python for data analysis (must have) to explore, prepare, and analyze data.
Understanding of AI/ML concepts and ability to collaborate with ML teams on data requirements.
Understanding of data quality, data integrity, and data governance principles.
Excellent verbal and written English communication skills.
Experience with project management methodologies and tools.
Ability to interpret business requirements and translate them into clear data needs and actionable insights.
Strong problem-solving skills and the ability to work through data-related challenges.
Collaboration and communication skills to work effectively with data scientists, ML engineers, and other stakeholders.
Ability to create clear documentation and deliver engaging presentations for both technical and non-technical audiences.


Job responsibilities


Work closely with business stakeholders to understand their needs, pain points, and goals, and translate these into clear data requirements.
Collaborate with data engineers and ML teams to identify and secure the required data for analysis and model development.
Conduct data exploration, profiling, and preparation to ensure data quality and relevance.
Document data flows, requirements, and data-related business processes.
Translate business requirements into clear technical specifications and ensure alignment with project goals.
Help identify potential challenges and limitations in the proposed data solutions and collaborate to resolve them.
Act as a bridge between business and technical teams by clearly explaining how data can be used to support business decisions.
Provide insights and recommendations based on data analysis to improve business outcomes.
Create user guides or documentation to help non-technical stakeholders understand data usage and AI/ML outputs.
Present findings and insights in a clear and accessible manner.


What we offer

Culture of caring. At GlobalLogic, we prioritize a culture of caring. Across every region and department, at every level, we consistently put people first. From day one, you’ll experience an inclusive culture of acceptance and belonging, where you’ll have the chance to build meaningful connections with collaborative teammates, supportive managers, and compassionate leaders.

Learning and development. We are committed to your continuous learning and development. You’ll learn and grow daily in an environment with many opportunities to try new things, sharpen your skills, and advance your career at GlobalLogic. With our Career Navigator tool as just one example, GlobalLogic offers a rich array of programs, training curricula, and hands-on opportunities to grow personally and professionally.

Interesting & meaningful work. GlobalLogic is known for engineering impact for and with clients around the world. As part of our team, you’ll have the chance to work on projects that matter. Each is a unique opportunity to engage your curiosity and creative problem-solving skills as you help clients reimagine what’s possible and bring new solutions to market. In the process, you’ll have the privilege of working on some of the most cutting-edge and impactful solutions shaping the world today.

Balance and flexibility. We believe in the importance of balance and flexibility. With many functional career areas, roles, and work arrangements, you can explore ways of achieving the perfect balance between your work and life. Your life extends beyond the office, and we always do our best to help you integrate and balance the best of work and life, having fun along the way!

High-trust organization. We are a high-trust organization where integrity is key. By joining GlobalLogic, you’re placing your trust in a safe, reliable, and ethical global company. Integrity and trust are a cornerstone of our value proposition to our employees and clients. You will find truthfulness, candor, and integrity in everything we do.

About GlobalLogic

GlobalLogic, a Hitachi Group Company, is a trusted digital engineering partner to the world’s largest and most forward-thinking companies. Since 2000, we’ve been at the forefront of the digital revolution – helping create some of the most innovative and widely used digital products and experiences. Today we continue to collaborate with clients in transforming businesses and redefining industries through intelligent products, platforms, and services.
""")


print(outcome)