import re

def new_line_remover(text):
    text = re.sub(r'[\n\r\t\u2028\u2029]', '', text)
    text = re.sub(r'[ ]{2,}', ' ', text)
    return text.strip()


input_text = """
 Job Description

With us you will:

    Work on visualizing product and process related KPI for modern products (Software Cloud and Virtualization market)
    Use Power BI and SQL database
    Develop and verify dashboards and graphs
    UX reviews of dashboards and graphs for alignment and look & feel
    Support the organization with a true visualization of the status of the operation
    Work in multicultural teams and friendful atmosphere

Requirements

    Experience in designing and delivering BI and reporting tools.
    Metrics repository is an SQL database, back-end processing is done with SQL scripts (MS SQL)
    Proficiency in using Power BI
    Experience with ETL
    Knowledge of Python programming language (OOP, Rest API)
    Being thorough and reliable
    Openness to learn new tools and technology
    Good communication skills (written and spoken English)

Nice To Have

    Understand and apply best practices related to reporting, dashboards, and data visualization
    Knowledge of Python libraries: Pandas, NumPy, SQLAlchemy
    Web design experience (HTML, CSS)

We Offer You

    Competitive salary
    Career development possibilities 
    Private medical coverage 
    Group life insurance 
    Investment fund 
    Holiday allowance
    Lunch & home office allowance
    & other benefits

Additional Information

At Tietoevry, we believe in the power of diversity, equity, and inclusion. We encourage applicants of all backgrounds, genders (m/f/d), and walks of life to join our team, as we believe that this fosters an inspiring workplace and fuels innovation. Our commitment to openness, trust, and diversity is at the heart of our mission to create digital futures that benefit businesses, societies, and humanity.

"""

outcome = new_line_remover(input_text)

print(outcome)
