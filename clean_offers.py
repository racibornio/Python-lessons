import re

# Wklej tutaj wieloliniowy tekst ogłoszenia w potrójnym cudzysłowie:
raw_job_description = """
 Location: Wrocław/Warsaw (Hybrid)


We are looking for an AI Product Builder who will help shape the future of AI-powered developer tools. You will own product direction across multiple projects, working closely with engineers and designers to define what we build, for whom, and why. This role goes beyond traditional product management, you will prototype with AI tools, validate ideas with real users, and help design agentic products where AI systems can reason, act, and collaborate with humans. You will join a fast-moving environment where product decisions turn into shipped experiences within days, not months.

Role & Responsibilities:

    Design AI-native products and workflows - define how AI agents perceive, decide, act, and collaborate with users, including human-in-the-loop patterns, failure handling, and validation mechanisms.

    Own product direction across multiple projects - drive decisions around user needs, product strategy, priorities, and success criteria while working closely with engineering and design teams.

    Build and experiment with AI technologies - use LLM APIs, coding agents, prototypes, and evaluation methods to test ideas quickly and turn concepts into working solutions.

    Validate problems before building solutions - talk to users, analyze feedback and usage signals, run experiments, and ensure we solve meaningful problems rather than simply shipping features.

    Operate in AI-native development loops - write clear product specs, define measurable outcomes, prioritize effectively, and continuously adjust direction based on learnings.

Job Requirements:

    Hands-on experience building with modern AI technologies, including LLM APIs, AI coding tools, prompting, or evaluation frameworks. You understand AI capabilities and limitations through practical experience.

    Experience building products for developers or technical users, such as developer tools, SDKs, APIs, infrastructure, platforms, or similar products.

    4+ years of product management experience, ideally in a startup or fast-paced environment where you owned outcomes and product decisions.

    Strong product discovery and problem-solving skills, you can identify user needs, form hypotheses, validate assumptions, and make data-informed decisions.

    Technical fluency that allows you to collaborate effectively with engineers and understand software development trade-offs. Coding experience is a plus, but not required.

What’s On Offer:

At Opera, you’ll join a diverse and inclusive team of experienced, supportive professionals who value creativity and collaboration. We work in a flat structure with short decision-making paths, use smart technology, and support your ongoing skill development in a friendly and empowering environment.

Interested?

We’d love to hear from you! Applications are reviewed on a rolling basis, so we encourage you to apply soon. Please submit your CV in English. Have questions about our recruitment process, remote work, or benefits? Check out our FAQ page for more details.
"""


def clean_text(text: str) -> str:
    # Zamienia nowe linie i tabulacje na spacje oraz usuwa podwójne spacje
    text_no_newlines = re.sub(r"[\r\n\t]+", " ", text)
    clean_single_spaces = re.sub(r"\s+", " ", text_no_newlines)
    return clean_single_spaces.strip()


cleaned = clean_text(raw_job_description)

print("Gotowy tekst do Excela:\n")
print(cleaned)