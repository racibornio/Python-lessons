def new_line_remover(text):
    
    strings_to_remove = ["\n", "\t"]

    for s in strings_to_remove:
        text = text.replace(s, "")
    return text


outcome = new_line_remover("""
Location: Wrocław (will not consider relocation or remote locations)

Are you ready to push the boundaries of what's possible with AI and shape the Future of AI-human interactions? Opera is seeking a driven Data Scientist to join our AI Development Hub and help us build the next generation of AI-powered browsers.

This is a unique opportunity to work on cutting-edge AI technologies while developing products used by millions of people worldwide. You'll be at the forefront of innovation, applying your expertise to create groundbreaking solutions that delight our users.

As part of our AI team, you'll play a key role in researching, building, and optimizing AI-powered features, integrating AI solutions into our products, and continuously improving the browsing experience.

Role & Responsibilities:

    Research and develop AI-driven products and features to create smarter, more intuitive browsing experiences.
    Enhance and optimize existing AI-based solutions, ensuring continuous improvement and scalability.
    Prototype and test AI systems, ensuring performance, reliability and robustness.
    Collaborate with cross-functional teams to integrate AI into Opera’s products and services.
    Stay up-to-date on the latest advancements in AI and explore new technologies to drive innovation.
    Contribute to a culture of knowledge sharing, creativity, and experimentation.

Job Requirements:

    Strong programming skills in Python
    Familiarity with data science libraries (e.g., Pandas, NumPy, scikit-learn).
    Hands-on experience with machine learning frameworks such as TensorFlow, PyTorch, or similar.
    Solid understanding of statistics and data modeling
    Familiarity with LLMs, and AI Agents

An Ideal Candidate’s Profile:

    Analytical mindset with strong problem-solving skills.
    Comfortable working cross-functionally with engineers, researchers,, and product managers.
    Curious, collaborative, and committed to delivering high-impact solutions.
    Passionate about new technology, especially AI agentic systems.

What’s on Offer:

    Work on AI-powered features used by tens of millions of users globally.
    Collaborate with a diverse and innovative AI team.
    Access to cutting-edge tools and infrastructure in data science and machine learning.
    Continuous learning and professional growth in a dynamic, forward-thinking environment.

""")


print(outcome)