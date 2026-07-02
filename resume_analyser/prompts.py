RESUME_PROMPT ="""
Act as a senior HR Recruiter .

Analyse the following candidate resume carefully. 

Tasks.
1. Extract candiate name
2. Extract Technical Skills
3. Identify Years of Experience
4. Compare with Job Description
5. Calculate Matching Percentage
6. Mention Strengths
7. Mention weakness
9. Provide hiring recomendation

Job Description:
{job_description}

Resume:
{resume_text}

output_format:

Candidate  Name

Skills:
Experience:
Technical Skills:
Years of Experience:
Matching Percentage:
Strength:
Weakness:
Recommendation:
"""