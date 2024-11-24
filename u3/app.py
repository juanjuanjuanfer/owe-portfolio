import streamlit as st
import pandas as pd

def main():
    # Page config
    st.set_page_config(
        page_title="Executive Documents Guide",
        page_icon="📄",
        layout="centered"
    )

    # Custom CSS for infographic-style layout
    st.markdown("""
        <style>
        /* Main background animation */
        .main {
            background: linear-gradient(45deg, #f3f4f6 25%, transparent 25%) -50px 0,
                        linear-gradient(-45deg, #f3f4f6 25%, transparent 25%) -50px 0,
                        linear-gradient(45deg, transparent 75%, #f3f4f6 75%),
                        linear-gradient(-45deg, transparent 75%, #f3f4f6 75%);
            background-size: 100px 100px;
            background-color: #ffffff;
            animation: gradient-animation 15s ease infinite;
            position: relative;
        }

        @keyframes gradient-animation {
            0% {
                background-position: 0% 50%, 0% 50%, 50px 0px, 50px 0px;
            }
            50% {
                background-position: 100% 50%, 100% 50%, -50px 0px, -50px 0px;
            }
            100% {
                background-position: 0% 50%, 0% 50%, 50px 0px, 50px 0px;
            }
        }

        /* Floating animation for sections */
        .doc-section {
            background-color: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin: 2rem 0;
            transition: transform 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .doc-section:hover {
            transform: translateY(-5px);
        }

        /* Animated accent border */
        .doc-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #1f4287, #4070f4, #1f4287);
            background-size: 200% 100%;
            animation: border-animation 3s linear infinite;
        }

        @keyframes border-animation {
            0% { background-position: 100% 0; }
            100% { background-position: -100% 0; }
        }

        /* Glowing effect for section titles */
        .section-title {
            color: #1f4287;
            text-align: center;
            padding: 1rem;
            font-size: 1.8rem;
            margin-bottom: 1rem;
            position: relative;
            text-shadow: 0 0 10px rgba(31,66,135,0.1);
        }

        /* Pulsing highlight boxes */
        .highlight-box {
            background-color: #e7eeff;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            animation: pulse 4s ease infinite;
            border: 1px solid rgba(31,66,135,0.1);
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(31,66,135,0.2); }
            70% { box-shadow: 0 0 0 10px rgba(31,66,135,0); }
            100% { box-shadow: 0 0 0 0 rgba(31,66,135,0); }
        }

        /* Floating icons */
        .floating-icon {
            animation: floating 3s ease infinite;
            display: inline-block;
        }

        @keyframes floating {
            0% { transform: translate(0, 0px); }
            50% { transform: translate(0, 15px); }
            100% { transform: translate(0, 0px); }
        }

        /* Custom styling for interactive elements */
        .stSelectbox, .stRadio > label {
            background-color: white;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        .stButton > button {
            background: linear-gradient(45deg, #1f4287, #4070f4);
            color: white;
            border: none;
            padding: 0.5rem 2rem;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(31,66,135,0.2);
        }

        /* Animated progress bars */
        .stProgress > div > div > div {
            background: linear-gradient(90deg, #1f4287, #4070f4);
            background-size: 200% 100%;
            animation: progress-animation 2s linear infinite;
        }

        @keyframes progress-animation {
            0% { background-position: 100% 0; }
            100% { background-position: -100% 0; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("Executive Documents Explorer")
    

    st.subheader("What Are Executive Documents?")
    st.write("Executive documents are formal business communications used to convey important information, proposals, or professional qualifications in a structured format. They are essential tools in business settings that require clear, concise, and professional presentation.")

    # Document Type Selector
    doc_type = st.selectbox(
        "Select Document Type",
        options=["Business Letters", "Memos", "Executive Summaries", "CV/Resume", "Proposals"]
    )

    # Dynamic Content Based on Selection
    show_document_content(doc_type)

def show_document_content(doc_type):
    # Document Overview Section
    with st.container():
        st.markdown(f"## Understanding {doc_type}")
        
        col1, col2, col3 = st.columns([1,4,1])
        with col2:
            st.markdown(f"""
            #### Key Characteristics
            - Purpose: {get_purpose(doc_type)}
            - Length: {get_length(doc_type)}
            - Formality: {get_formality(doc_type)}
            """)

    # Interactive Template Explorer
    st.markdown("### 📝 Template Explorer")
    with st.expander("View Template Structure", expanded=True):
        show_template(doc_type)

    # Interactive Elements Section
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### ✍️ Key Elements")
        show_elements(doc_type)
    
    with col2:
        st.markdown("### 🎯 Best Practices")
        show_best_practices(doc_type)

    # Interactive Practice Section
    st.markdown("### Example")
    example_data = st.text_area("Modify this.", get_sample_text(doc_type), height=500)

    st.download_button(
            label="Download Example",
            data=example_data,
            file_name=f"{doc_type.replace(' ', '_').lower()}_example.txt",
            mime="text/plain"
    )
    # Tips and Common Mistakes
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 💡 Pro Tips")
        for tip in get_tips(doc_type):
            st.info(tip)
    
    with col2:
        st.markdown("### ⚠️ Common Mistakes")
        for mistake in get_mistakes(doc_type):
            st.warning(mistake)

    # Quick Quiz
    st.markdown("### 🎯 Quick Check")
    with st.form("quiz"):
        st.write("Test your knowledge:")
        q1 = st.radio(
            get_quiz_question(doc_type),
            get_quiz_options(doc_type)
        )
        quiz_submitted = st.form_submit_button("Submit Answer")
        if quiz_submitted:
            check_quiz_answer(doc_type, q1)

def check_understanding(doc_type, answer):
    st.success("Great observation! Here's what you might have missed...")

def get_purpose(doc_type):
    purposes = {
        "Business Letters": "Professional written communication used for formal business matters such as job applications, complaints, inquiries, and official responses. They maintain professional relationships and document important business interactions.",
        "Memos": "Internal company communications used to inform staff about policies, procedures, or updates. They efficiently share information, announce changes, and document internal decisions within an organization.",
        "Executive Summaries": "Concise overview of longer documents or reports, highlighting key findings and recommendations. They allow busy executives to quickly grasp the main points and make informed decisions.",
        "CV/Resume": "Professional document showcasing an individual's qualifications, experience, and skills for employment opportunities. It presents career history and achievements in a structured format.",
        "Proposals": "Detailed documents that present solutions to problems or suggest new initiatives. They convince stakeholders to approve projects, allocate resources, or accept suggested changes."
    }
    return purposes.get(doc_type, "")

def get_length(doc_type):
    lengths = {
        "Business Letters": "1-2 pages (typically 3-5 paragraphs)",
        "Memos": "1 page (brief and focused on single topic)",
        "Executive Summaries": "1-2 pages (10% of original document length)",
        "CV/Resume": "1-2 pages for entry/mid-level; 2-3 pages for senior positions",
        "Proposals": "5-10 pages for small projects; 20-50 pages for complex proposals"
    }
    return lengths.get(doc_type, "")

def get_formality(doc_type):
    formality = {
        "Business Letters": "Highly Formal - Uses professional language, proper titles, and standard business format",
        "Memos": "Semi-Formal - Direct and clear language, less rigid formatting than letters",
        "Executive Summaries": "Formal - Professional and concise, focuses on key facts and data",
        "CV/Resume": "Formal - Professional terminology, action verbs, and industry-specific language",
        "Proposals": "Formal - Technical and professional language, detailed and precise information"
    }
    return formality.get(doc_type, "")

def show_template(doc_type):
    templates = {
        "Business Letters": """
        [Your Company Letterhead]
        [Your Address]
        [City, State ZIP]
        
        [Date]
        
        [Recipient's Name]
        [Title]
        [Company Name]
        [Street Address]
        [City, State ZIP]
        
        Dear [Mr./Ms. Last Name]:
        
        [Opening Paragraph: State the purpose of your letter]
        
        [Body Paragraph(s): Provide relevant details and supporting information]
        
        [Closing Paragraph: Include a call to action or next steps]
        
        Sincerely,
        [Your Full Name]
        [Your Title]
        [Contact Information]
        """,
        
        "Memos": """
        MEMORANDUM

        TO: [Recipient(s) Name and Title]
        FROM: [Your Name and Title]
        DATE: [Month Day, Year]
        SUBJECT: [Clear, Concise Topic Description]

        PURPOSE:
        [Brief statement of the memo's purpose]

        BACKGROUND:
        [Relevant context or history]

        DISCUSSION:
        [Key points and supporting information]

        ACTION ITEMS:
        [List of required actions, deadlines, and responsibilities]

        NEXT STEPS:
        [Follow-up procedures or expectations]
        """,
        
        "Executive Summaries": """
        EXECUTIVE SUMMARY

        Document Title: [Title of Full Document]
        Date: [Month Day, Year]
        Prepared By: [Your Name/Department]

        PURPOSE:
        [Brief overview of the document's purpose]

        KEY FINDINGS:
        • [Major Finding 1]
        • [Major Finding 2]
        • [Major Finding 3]

        RECOMMENDATIONS:
        1. [Primary Recommendation]
        2. [Secondary Recommendation]
        3. [Additional Recommendation]

        FINANCIAL IMPLICATIONS:
        [Cost/Benefit Summary]

        TIMELINE:
        [Implementation Schedule]

        CONCLUSION:
        [Final statement and call to action]
        """,
        
        "CV/Resume": """
        [Your Full Name]
        [Professional Title]
        [Address]
        [Phone] | [Email] | [LinkedIn]

        PROFESSIONAL SUMMARY
        [2-3 sentences highlighting key qualifications]

        PROFESSIONAL EXPERIENCE
        [Company Name] | [Location]
        [Job Title] | [Dates]
        • [Achievement/Responsibility]
        • [Achievement/Responsibility]
        • [Achievement/Responsibility]

        EDUCATION
        [Degree] | [Institution]
        [Major] | [Graduation Date]

        SKILLS
        • [Technical Skills]
        • [Soft Skills]
        • [Industry-Specific Skills]

        CERTIFICATIONS
        • [Certification Name]
        • [Certification Name]
        """,
        
        "Proposals": """
        [Project Title]
        [Proposal Submission Date]

        1. EXECUTIVE SUMMARY
        [Brief overview of the proposal]

        2. PROBLEM STATEMENT
        [Clear description of the issue to be addressed]

        3. PROPOSED SOLUTION
        [Detailed description of your solution]
        3.1 Methodology
        3.2 Implementation Plan
        3.3 Timeline

        4. BUDGET
        [Detailed cost breakdown]
        4.1 Direct Costs
        4.2 Indirect Costs
        4.3 ROI Analysis

        5. TEAM AND RESOURCES
        [Team structure and available resources]

        6. RISK ANALYSIS
        [Potential risks and mitigation strategies]

        7. CONCLUSION
        [Summary and call to action]

        APPENDICES
        [Supporting documentation]
        """
    }
    st.code(templates.get(doc_type, "Template coming soon..."))

def show_elements(doc_type):
    elements = {
        "Business Letters": [
            "Letterhead - Company logo and contact information",
            "Date - Current date in formal format (Month Day, Year)",
            "Inside Address - Recipient's complete information",
            "Salutation - Formal greeting using proper title",
            "Opening Paragraph - Clear purpose statement",
            "Body Paragraphs - Detailed information and context",
            "Closing Paragraph - Clear conclusion and call to action",
            "Complimentary Close - 'Sincerely' or similar formal closing",
            "Signature Block - Name, title, and contact details"
        ],
        
        "Memos": [
            "Header Block - To, From, Date, Subject",
            "Purpose Statement - Clear objective",
            "Background Information - Context if needed",
            "Key Points - Main message and details",
            "Action Items - Required steps or responses",
            "Timeline - Deadlines and schedule",
            "Contact Information - For follow-up questions"
        ],
        
        "Executive Summaries": [
            "Title - Document identification",
            "Overview - Brief introduction",
            "Key Findings - Major discoveries or points",
            "Recommendations - Suggested actions",
            "Financial Impact - Cost and benefit analysis",
            "Timeline - Implementation schedule",
            "Conclusion - Final thoughts and next steps"
        ],
        
        "CV/Resume": [
            "Header - Name and contact information",
            "Professional Summary - Career overview",
            "Work Experience - Employment history",
            "Education - Academic credentials",
            "Skills - Technical and soft skills",
            "Certifications - Professional qualifications",
            "Achievements - Quantifiable successes",
            "Optional Sections - Publications, volunteer work, etc."
        ],
        
        "Proposals": [
            "Executive Summary - Brief overview",
            "Problem Statement - Issue description",
            "Solution - Detailed approach",
            "Methodology - Implementation plan",
            "Budget - Cost breakdown",
            "Timeline - Project schedule",
            "Team - Resource allocation",
            "Risk Analysis - Potential issues and solutions",
            "Conclusion - Summary and recommendations"
        ]
    }
    for element in elements.get(doc_type, []):
        st.markdown(f"- {element}")

def show_best_practices(doc_type):
    practices = {
        "Business Letters": [
            "Use proper business letter format (block or modified block)",
            "Maintain professional tone throughout",
            "Be concise and focused on one main topic",
            "Proofread carefully for errors",
            "Include all necessary contact information",
            "Use appropriate spacing (single-spaced with double space between paragraphs)",
            "Keep paragraphs short and focused (3-5 sentences)",
            "Use professional font (Times New Roman, Arial, 11-12pt)"
        ],
        
        "Memos": [
            "Keep content brief and to the point",
            "Use clear headings and bullet points",
            "State purpose in first paragraph",
            "Use objective, professional tone",
            "Include specific action items",
            "Organize information logically",
            "Proofread for clarity and accuracy",
            "Use consistent formatting"
        ],
        
        "Executive Summaries": [
            "Keep it concise (10% of full document)",
            "Focus on key findings and recommendations",
            "Use clear, direct language",
            "Include specific data and metrics",
            "Organize with clear headings",
            "Write for your audience",
            "Avoid technical jargon",
            "Provide clear conclusions"
        ],
        
        "CV/Resume": [
            "Tailor content to specific job",
            "Use action verbs and metrics",
            "Keep format clean and consistent",
            "Update regularly",
            "Proofread thoroughly",
            "Include relevant keywords",
            "Focus on achievements over duties",
            "Maintain reverse chronological order"
        ],
        
        "Proposals": [
            "Research thoroughly before writing",
            "Focus on client benefits",
            "Include detailed methodology",
            "Provide clear budget breakdown",
            "Use professional formatting",
            "Include visual elements",
            "Address potential concerns",
            "Follow submission guidelines"
        ]
    }
    for practice in practices.get(doc_type, []):
        st.markdown(f"- {practice}")

def get_sample_text(doc_type):
    samples = {
        "Business Letters": """TechCore Solutions
123 Innovation Drive
Silicon Valley, CA 94025

October 15, 2024

Mr. Robert Chen
Hiring Manager
Future Tech Inc.
456 Enterprise Avenue
San Francisco, CA 94105

Dear Mr. Chen:

I am writing to apply for the Senior Developer position at Future Tech Inc., as advertised on your company website. With over five years of experience in software development and a strong background in AI technologies, I believe I would be a valuable addition to your team.

My current role at TechCore Solutions has given me extensive experience in leading development teams and implementing innovative solutions. I have successfully managed projects that increased company revenue by 30% and improved system efficiency by 45%.

I would welcome the opportunity to discuss how my skills and experience align with Future Tech Inc.'s needs. I can be reached at (555) 123-4567 or maria.smith@email.com.

Sincerely,
Maria Smith
Senior Software Developer
TechCore Solutions""",

        "Memos": """MEMORANDUM

TO: All Development Team Members
FROM: Sarah Johnson, Project Manager
DATE: November 15, 2024
SUBJECT: New Code Review Process Implementation

PURPOSE:
To outline the new code review process effective December 1, 2024.

BACKGROUND:
Our current code review process has led to delays in project delivery and inconsistent code quality.

KEY CHANGES:
• Implementation of automated code review tools
• Maximum 24-hour review turnaround time
• Mandatory peer reviews for all major features
• Weekly code quality metrics reporting

ACTION ITEMS:
1. Complete tool training by November 25
2. Update IDE configurations by November 28
3. Attend process overview meeting on November 30

Please direct any questions to sarah.j@techcore.com

Next team meeting: November 20, 2024 at 10:00 AM""",

        "Executive Summaries": """EXECUTIVE SUMMARY
Q4 2024 Performance Report

The fourth quarter of 2024 showed significant growth in key performance areas. Revenue increased by 28% compared to Q3, reaching $12.5M. Customer acquisition costs decreased by 15%, while customer retention improved to 92%.

Key Achievements:
• Launched three new product features
• Expanded into two new markets
• Reduced operating costs by 18%
• Achieved 99.9% system uptime

Recommendations:
1. Increase investment in AI capabilities
2. Expand sales team by 25%
3. Implement new customer feedback system

Financial Impact:
Projected ROI of 250% over 18 months with initial investment of $2.8M.

Implementation Timeline:
January 2025 - June 2025

Next Steps:
Board approval required for budget allocation by December 30, 2024.""",

        "CV/Resume": """JANE WILSON
Senior Software Engineer

CONTACT
email: jane.wilson@email.com
phone: (555) 234-5678
LinkedIn: linkedin.com/in/janewilson

PROFESSIONAL SUMMARY
Innovative Senior Software Engineer with 8+ years of experience in full-stack development. Specialized in cloud architecture and AI implementation. Led teams of 5-10 developers in delivering enterprise solutions.

EXPERIENCE
Senior Software Engineer | TechCorp Inc. | 2020-Present
• Led development of cloud-native application, reducing costs by 40%
• Implemented AI-driven features, increasing user engagement by 65%
• Mentored 12 junior developers, with 8 receiving promotions

EDUCATION
M.S. Computer Science | Stanford University | 2018
B.S. Software Engineering | MIT | 2016

SKILLS
• Languages: Python, Java, JavaScript
• Frameworks: React, Node.js, Django
• Tools: AWS, Docker, Kubernetes""",

        "Proposals": """CLOUD INFRASTRUCTURE MODERNIZATION PROPOSAL
Submitted to: GlobalTech Industries
Date: November 20, 2024

EXECUTIVE SUMMARY
This proposal outlines a comprehensive cloud migration strategy for GlobalTech's legacy systems, promising 40% cost reduction and 99.99% uptime.

PROBLEM STATEMENT
Current infrastructure faces scalability issues and high maintenance costs, with system downtime causing $50,000 in losses per hour.

SOLUTION
Proposed three-phase migration to AWS cloud infrastructure:
Phase 1: Assessment and Planning (2 months)
Phase 2: Migration and Testing (4 months)
Phase 3: Optimization and Training (2 months)

BUDGET
Total Investment: $1.2M
• Infrastructure: $600K
• Implementation: $400K
• Training: $200K

ROI PROJECTION
• Cost savings: $500K/year
• Performance improvement: 60%
• Break-even point: 18 months

Next steps require approval by December 15, 2024."""
    }
    return samples.get(doc_type, "Sample coming soon...")

def get_tips(doc_type):
    tips = {
        "Business Letters": [
            "Use a professional email address for contact information",
            "Research the recipient's correct name and title",
            "Keep the entire letter to one page when possible",
            "Save as PDF to maintain formatting",
            "Use active voice and positive language",
            "Include specific examples and metrics when relevant"
        ],
        
        "Memos": [
            "Start with the most important information",
            "Use clear and specific subject lines",
            "Include deadline dates in bold",
            "Break information into digestible chunks",
            "Use bullet points for action items",
            "Keep language neutral and objective"
        ],
        
        "Executive Summaries": [
            "Write the summary last, after completing the main document",
            "Focus on conclusions and recommendations",
            "Use data to support key points",
            "Keep it under two pages",
            "Use headers and bullet points effectively",
            "Avoid technical jargon unless necessary"
        ],
        
        "CV/Resume": [
            "Customize for each job application",
            "Use industry-specific keywords",
            "Quantify achievements with numbers",
            "Keep design clean and professional",
            "Update regularly with new accomplishments",
            "Place most relevant information first"
        ],
        
        "Proposals": [
            "Research the client's needs thoroughly",
            "Focus on benefits rather than features",
            "Include clear timelines and milestones",
            "Use visuals to illustrate key points",
            "Address potential objections",
            "Provide detailed but clear budget information"
        ]
    }
    return tips.get(doc_type, [])

def get_mistakes(doc_type):
    mistakes = {
        "Business Letters": [
            "Using informal language or slang",
            "Including personal or irrelevant information",
            "Forgetting to sign the letter",
            "Making spelling or grammar errors",
            "Using incorrect titles or recipient information",
            "Writing overly long paragraphs"
        ],
        
        "Memos": [
            "Being too verbose or unclear",
            "Forgetting to include action items",
            "Using emotional language",
            "Omitting crucial details",
            "Poor formatting or organization",
            "Not specifying deadlines"
        ],
        
        "Executive Summaries": [
            "Including too much detail",
            "Using technical jargon unnecessarily",
            "Failing to include recommendations",
            "Not highlighting key findings",
            "Making it too long",
            "Forgetting the target audience"
        ],
        
        "CV/Resume": [
            "Including irrelevant experience",
            "Using generic descriptions",
            "Making it too long or dense",
            "Including personal information",
            "Having unexplained gaps",
            "Using unprofessional email address"
        ],
        
        "Proposals": [
            "Focusing on features instead of benefits",
            "Unclear or unrealistic budgets",
            "Not addressing client needs",
            "Poor risk assessment",
            "Vague implementation plans",
            "Missing executive summary"
        ]
    }
    return mistakes.get(doc_type, [])

def get_quiz_question(doc_type):
    questions = {
        "Business Letters": "Which element is essential in a business letter's header?",
        "Memos": "What is the most important part of a memo's header?",
        "Executive Summaries": "What is the recommended length of an executive summary?",
        "CV/Resume": "Which formatting style is most appropriate for work experience?",
        "Proposals": "What should be included in the first section of a proposal?"
    }
    return questions.get(doc_type, "")

def get_quiz_options(doc_type):
    options = {
        "Business Letters": [
            "The sender's complete contact information",
            "A creative slogan",
            "The company's mission statement",
            "The current weather conditions"
        ],
        
        "Memos": [
            "The subject line",
            "A company logo",
            "A greeting line",
            "A signature block"
        ],
        
        "Executive Summaries": [
            "10% of the original document",
            "50% of the original document",
            "Same length as original document",
            "As long as needed"
        ],
        
        "CV/Resume": [
            "Reverse chronological order",
            "Alphabetical order",
            "Random order",
            "Order of importance"
        ],
        
        "Proposals": [
            "Executive Summary",
            "Team Biographies",
            "Company History",
            "Technical Specifications"
        ]
    }
    return options.get(doc_type, [])

def check_quiz_answer(doc_type, answer):
    correct_answers = {
        "Business Letters": "The sender's complete contact information",
        "Memos": "The subject line",
        "Executive Summaries": "10% of the original document",
        "CV/Resume": "Reverse chronological order",
        "Proposals": "Executive Summary"
    }
    
    explanations = {
        "Business Letters": "The sender's contact information is crucial for business correspondence and allows the recipient to respond.",
        "Memos": "A clear subject line immediately informs readers of the memo's purpose and helps with document organization.",
        "Executive Summaries": "An executive summary should be concise, typically about 10% of the original document's length.",
        "CV/Resume": "Reverse chronological order shows career progression and keeps recent, relevant experience most visible.",
        "Proposals": "The executive summary provides a crucial overview and captures the reader's interest in the proposal."
    }
    
    if answer == correct_answers.get(doc_type):
        st.success(f"Correct! {explanations.get(doc_type)}")
    else:
        st.error(f"Not quite. {explanations.get(doc_type)}")

if __name__ == "__main__":
    main()