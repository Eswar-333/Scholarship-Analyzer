def analyze_scholarship_eligibility(student_info):
    name = student_info.get("name", "The student")
    gpa = float(student_info.get("gpa", 0))
    income_lpa = float(student_info.get("income", 0))
    income = int(income_lpa * 100000)
    academic_level = student_info.get("academic_level", "").lower()
    gender = student_info.get("gender", "").lower()
    interests = student_info.get("interests", "").lower()

    def format_indian_currency(amount):
        lakh = amount // 100000
        thousand = (amount % 100000) // 1000
        return f"₹{lakh} Lakh {thousand} Thousand"

    scholarships = []

    if academic_level in ["10th", "11th"]:
        scholarships.append({
            "name": "Pre-Matric Scholarship for Minorities",
            "description": "For 10th and 11th grade minority students.\nCovers tuition and books."
        })
        if gender == "female":
            scholarships.append({
                "name": "Savitribai Phule Scholarship",
                "description": "For girl students in class 9th and 10th.\n₹100/month for 10 months."
            })

    if academic_level == "12th":
        if gpa >= 90 and income < 100000 and gender == "male":
            scholarships.append({
                "name": "Swami Vivekananda Merit-cum-Means Scholarship",
                "description": "For 12th grade boys with 90%+ and low income.\n₹1,000–₹5,000/month."
            })

    if 60 <= gpa < 75:
        scholarships.append({
            "name": "Medhavi National Scholarship",
            "description": "For students scoring 60–75%.\nMerit-cum-means based monthly support."
        })
        scholarships.append({
            "name": "IndusInd Foundation Scholarship",
            "description": "For UG students with modest scores and low income.\nCovers tuition fee."
        })

    if 75 <= gpa < 90:
        scholarships.append({
            "name": "Vidya Samunnathi Scholarship",
            "description": "For economically backward students with 75%+.\nFor UG and PG courses."
        })
        scholarships.append({
            "name": "CLP India Scholarship",
            "description": "For students scoring between 75–90%.\nCovers part of tuition expenses."
        })

    if gpa >= 90:
        scholarships.append({
            "name": "Kishore Vaigyanik Protsahan Yojana (KVPY)",
            "description": "For students with research potential in science.\nMonthly stipend and annual contingency grant."
        })
        scholarships.append({
            "name": "Indian Oil Academic Scholarship",
            "description": "For meritorious students from all streams.\n₹3,000/month."
        })
        if gender == "female" and academic_level in ["10th", "12th"]:
            scholarships.append({
                "name": "CBSE Merit Scholarship for Single Girl Child",
                "description": "For girls with 90%+ in CBSE 10th or 12th.\n₹500/month for two years."
            })

    if income < 400000:
        scholarships.append({
            "name": "Sitaram Jindal Foundation Scholarship",
            "description": "For students with family income < ₹4 LPA.\nUp to ₹2,000/month."
        })
        scholarships.append({
            "name": "ONGC Scholarship",
            "description": "₹48,000/year for SC/ST/OBC students in engineering, medical, MBA, or geology."
        })

    if income < 250000:
        scholarships.append({
            "name": "NSP – Post-Matric Scholarship for Minorities",
            "description": "Income < ₹2.5 LPA.\nCovers tuition, maintenance, allowances."
        })
        scholarships.append({
            "name": "Maulana Azad National Scholarship",
            "description": "For minority girls from low-income families.\n₹12,000/year."
        })

    if academic_level in ["11th", "12th", "undergraduate", "bachelor", "b.tech", "b.sc"] and gpa >= 85:
        scholarships.append({
            "name": "Inspire Scholarship (DST, Govt. of India)",
            "description": "For top-performing science stream students.\nOffers ₹80,000/year."
        })
        scholarships.append({
            "name": "NIIT Scholarship",
            "description": "For meritorious students pursuing technology or IT.\nCovers partial tuition."
        })

    if academic_level in ["undergraduate", "bachelor", "b.tech", "b.sc"] and "engineering" in interests:
        scholarships.append({
            "name": "LIC Golden Jubilee Scholarship",
            "description": "For economically weak UG students in engineering/medicine/arts.\nUp to ₹20,000/year."
        })
        scholarships.append({
            "name": "Foundation for Excellence Scholarship",
            "description": "For engineering and medical UG students with financial need.\nFull tuition support."
        })

    if academic_level in ["pg", "postgraduate", "master's", "m.tech", "m.sc"]:
        scholarships.append({
            "name": "Central Sector Scheme for College and University Students",
            "description": "For PG students with >80% in 12th.\n₹20,000/year."
        })
        scholarships.append({
            "name": "AICTE PG Scholarship",
            "description": "For GATE/GPAT qualified PG students.\n₹12,400/month."
        })

    if gender == "female":
        scholarships.append({
            "name": "Fair & Lovely Foundation Scholarship",
            "description": "For women pursuing UG/PG.\nBased on merit and income."
        })
        scholarships.append({
            "name": "Tata Housing Scholarship for Meritorious Girl Students",
            "description": "For girls in civil engineering and architecture.\nUp to ₹60,000/year."
        })
        if "technical" in interests or "stem" in interests:
            scholarships.append({
                "name": "Pragati Scholarship for Girl Students (AICTE)",
                "description": "For girls in technical education.\n₹50,000/year."
            })
            scholarships.append({
                "name": "Adobe Women-in-Tech Scholarship",
                "description": "For exceptional women in tech.\nCovers tuition and offers mentorship."
            })

    if gender == "male":
        scholarships.append({
            "name": "Sahu Jain Trust Loan Scholarship",
            "description": "For male UG/PG students.\nInterest-free loan scholarship for education."
        })
        scholarships.append({
            "name": "K.C. Mahindra Scholarship",
            "description": "For Indian men pursuing PG studies.\nUp to ₹4 lakh."
        })

    if "sports" in interests or "cricket" in interests:
        scholarships.append({
            "name": "Sports Authority of India (SAI) Scholarship",
            "description": "For students excelling in sports.\nIncludes training and financial aid."
        })
        scholarships.append({
            "name": "Amity University Sports Scholarship",
            "description": "For talented athletes.\nUp to 100% fee waiver based on performance."
        })

    assessment = (
        f"\nEntered Information:\n"
        f"Name: {name}\n"
        f"GPA: {gpa}\n"
        f"Family Income: {format_indian_currency(income)} ({income_lpa} LPA)\n"
        f"Academic Level: {academic_level}\n"
        f"Gender: {gender}\n"
        f"Interests: {interests}\n\n"
        f"Assessment: {name} has a GPA of {gpa}, academic level '{academic_level}', and a family income of {format_indian_currency(income)}.\n"
    )

    if scholarships:
        assessment += "Based on the provided information, the student may be eligible for the following scholarships:"
    else:
        assessment += "Unfortunately, no matching scholarships were found based on the current criteria."

    return {
        "assessment": assessment,
        "scholarships": scholarships,
        "guidance": "Visit https://scholarships.gov.in and other official portals. Prepare all required documents and apply early. Highlight achievements, leadership, and personal goals."
    }
