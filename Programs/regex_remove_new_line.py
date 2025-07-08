def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""
Hi! We're Bee Talents, an IT recruitment agency that has been helping clients from all around the world in building their technical teams since 2015. Today, we would like to invite you to participate in the recruitment process for Reef Technologies.
A few words from Reef Technologies:

We’re a fully-remote, senior-only team of Python backend engineers with 5+ years of experience.

We build complex distributed systems with low latency, fault tolerance, high scalability and self-healing. We also make APIs, databases, and libraries, and we’re not afraid to dig into custom algorithm design when we have to.

Right now, most of us are working on an internal product that runs parts of a large distributed AI ecosystem. If you join us, you’ll help us build a decentralized supercluster managed by advanced consensus algorithms that surpass traditional ones like PAXOS and RAFT.

On a larger timescale, we work with startups from all over the world. Our projects range from one-off tasks to multi-year collaborations. Some notable examples include a financial data warehouse for a London fintech, a graph search system for Norwegian auditors, and a scalable WAF for a client in Chicago.

When we’re not building cutting-edge backend systems, we shape Reef Technologies into where we really want to work. We co-create all company policies using Sociocracy 3.0, a framework that ensures every voice is heard and rules are never forced on people.

Our main goal at Reef Technologies is to get things done and do them well. We offer high rates and a high degree of flexibility, and in return, we expect everyone to take responsibility for their contributions and deliver them fast. No lurking allowed.

We do our best to make sure everyone gets to work on the most suitable project. You'll have as much say as possible in choosing your path within the company.

We typically work 30–40 hours per week, with plenty of flexibility to set our schedules. We’re also distributed all around the world – some of us work from Poland, others in Hong Kong or Romania, while some enjoy semi-permanent workations in Spain or even Bali.

Our sister company is a team of high-end executive assistants. They’re regularly available to help our engineers save time and focus on what counts – building more Python backends!
What Reef Technologies can offer:

    🎯 Role: Senior Python Backend Engineer
    💰 Salary and type of contract: 45-75 USD or 190-315 PLN per hour, or 7560-12990 USD or 31920-54495 PLN a month assuming 40 hours per week (but tbh, most of us chose fewer hours). ~ Rates are automatically adjusted for inflation. ~
    🌴 Holiday: Flexible vacation scheduling
    ⏱ Working hours: Flexible working hours
    🏢 Working mode: 100% remote
    🇬🇧 Speaking language: Fluency in English required

What you’ll need:

    We’re looking for developers with 5+ years of programming experience, including 1 year with Python. You should be good at solving complex problems with Python and producing functional, efficient, and well-designed code.
    Responsibility is important to us. You’ll be taking ownership of problems and guide solutions to their intended impact.
    Independence is equally important. You should manage your workload, make decisions, and find solutions. Do this without needing constant guidance.

Full offer for you:

    45-75 USD or 190-315 PLN per hour, or 7560-12990 USD or 31920-54495 PLN a month assuming 40 hours per week.
    Flexible hours (tracked via a time management tool).
    Cover reasonable coworking space expenses.
    Assign a dedicated private assistant to help save time on personal obligations.
    Provide financial support for purchasing necessary hardware.
    Take advantage of a flexible leave policy.

Sounds interesting? Let’s talk! :)


BEE TALENTS INFORMATION CLAUSE ⬇️

The Administrator of your personal data is Bee Talents PSA, ul. Garbary 35/12, 61-868 Poznan, NIP: 7792463296. The purposes of processing your personal data are: conducting the initial stage of recruitment, based on your consents, participation in future recruitment processes conducted for our clients, based on the consent, defense against potential claims of our Clients for whom we conduct recruitment, in particular regarding the non-compliance of the Candidate’s profile with the requirements specified by the Client – which is a legitimate interest of the Data Administrator pursuant to art. 6 section 1 pt. f) GDPR. Due to data processing you have the right to access your personal data, request a copy of it, retrificate it, delete or limit it and withdraw of consents at any time, make an objection to the processing of personal data and lodge a complaint to the President of the Personal Data Protection Office if it violate the GDPR rights. You can read the full content of the information clause here: https://beetalents.com/eng-gdpr.
""")


print(outcome)